#!/usr/bin/env python3
"""Report Audit Tool for AI Berkshire.

Data spot-check tool: samples 15% of the financial data points in a research
report, compares them against reliable sources, and either passes (allow release)
or rejects (send back) the report with an explanation.

Zero external dependencies — uses only Python stdlib.
Requires Python >= 3.7.

Workflow (three steps):
  Step 1 — Extract data points, randomly sample 15%:
    python3 tools/report_audit.py extract --report reports/xxx.md

  Step 2 — For each data point in the spot-check list, Claude pulls the value from
            a reliable source (CVM/B3/company IR, or the connected market-data MCP)
            and fills in fetched_value

  Step 3 — Feed in the verification results, output the pass/reject verdict:
    python3 tools/report_audit.py verdict --results '[...]'

  One-step (extract + print the spot-check list only, no network verification):
    python3 tools/report_audit.py extract --report reports/xxx.md --dry-run
"""

import argparse
import json
import math
import os
import re
import sys
from decimal import Decimal, Context, ROUND_HALF_EVEN
from random import Random

_CTX = Context(prec=28, rounding=ROUND_HALF_EVEN)

# ---------------------------------------------------------------------------
# Data-point extraction: identify financial numbers in a Markdown report
# ---------------------------------------------------------------------------

# Match pattern: number + unit, preceded by a context label
# e.g. Revenue: R$ 512.3 bn, PE 8.5x, gross margin 42%, market cap ~US$ 90 B
#
# Note: every number capture group must include the optional sign position _SIGN,
# otherwise "-1.72%" would be captured as "1.72", making the reported value and the
# source value have opposite signs, a 200% deviation, and a false rejection.
# The sign position covers ASCII +/-, the Unicode minus (U+2212), the en-dash
# (U+2013), and the full-width plus/minus signs.
_SIGN = r'[+\-−–－＋]?'

# Magnitude tokens accepted after a number: M / B / T plus common long forms
# (mn/million, bn/billion, tn/trillion). Case-insensitive in every regex below.
_MAG = r'(?:mn|million|bn|billion|tn|trillion|[MBT])'
# Optional currency prefix on a value: R$ (BRL), US$ / $ (USD).
_CUR = r'(?:R\$|US\$|\$)?'

_PATTERNS = [
    # Percentage
    (r'(' + _SIGN + r'[\d,\.]+)\s*%',                                   '%',   'percent'),
    # Currency magnitude, e.g. R$ 512.3 bn / US$ 90 B
    (r'(?i:' + _CUR + r')\s*(' + _SIGN + r'[\d,\.]+)\s*(?i:' + _MAG + r')', 'B', 'magnitude'),
    # Multiple PE/PB/PS
    (r'(' + _SIGN + r'[\d,\.]+)\s*[xX]',                                'x',   'multiple'),
    # Plain integer (e.g. market cap, revenue, user counts; appears inside a table |)
    (r'\|\s*[~]?(?i:' + _CUR + r')\s*(' + _SIGN + r'[\d,\.]+)\s*\|',    '',    'table_num'),
]

_LABEL_RE = re.compile(
    r'(?P<label>[^\|\n:]{2,25}):\s+[~]?' + _CUR + r'\s*(?P<num>' + _SIGN + r'[\d,\.]+)'
    r'\s*(?P<unit>' + _MAG + r'|[xX]|%)?',
    re.IGNORECASE,
)

_TABLE_ROW_RE = re.compile(
    r'\|\s*(?P<label>[^|]{1,40})\s*\|\s*[~]?' + _CUR + r'\s*(?P<num>' + _SIGN + r'[\d,\.]+)'
    r'\s*(?P<unit>' + _MAG + r'|[xX]|%)?\s*\|',
    re.IGNORECASE,
)


def _clean_num(s: str) -> float:
    """Convert a number string with thousands separators and various signs to float.

    Supports ASCII '-'/'+', the Unicode minus '−'(U+2212), the en-dash '–'(U+2013),
    and the full-width '－'(U+FF0D)/'＋'(U+FF0B) — any of these may be used as a sign
    in a report.
    """
    s = s.replace(',', '').strip()
    # Normalize the various sign characters to ASCII
    for ch in ('−', '–', '－'):
        s = s.replace(ch, '-')
    s = s.replace('＋', '+')
    try:
        return float(s)
    except ValueError:
        return None


def _is_valid_label(label: str) -> bool:
    """Decide whether a label is a meaningful financial field name; filter out noise."""
    label = label.strip()
    # Too short
    if len(label) < 2:
        return False
    # Pure number or pure year/quarter (e.g. "2025", "Q3", "2025 Q3")
    if re.fullmatch(r'[\d\sQ]+', label, re.IGNORECASE):
        return False
    # Starts with a symbol / markdown marker
    if re.match(r'^[+\-\*#\|~\$>_`]', label):
        return False
    # Contains markdown bold/code markers
    if '**' in label or '`' in label or '__' in label:
        return False
    # Label is a bare growth figure (e.g. +56%, -13% standing alone as a label)
    if re.fullmatch(r'[+\-]?\d+(\.\d+)?%', label):
        return False
    # Common meaningless labels (English + Portuguese)
    _SKIP = {'source', 'sources', 'note', 'notes', 'total', 'subtotal',
             'unit', 'units', 'trend', 'n/a', '—', '-', '/',
             'fonte', 'fontes', 'nota', 'observação', 'observacao'}
    if label.lower() in _SKIP:
        return False
    return True


# Two-column table row: | label | value unit | (designed for financial-report KV tables)
_KV_TABLE_RE = re.compile(
    r'^\|\s*(?P<label>[^|*\n]{2,40}?)\s*\|\s*[~]?' + _CUR + r'\s*(?P<num>' + _SIGN + r'[\d,\.]+)\s*'
    r'(?P<unit>' + _MAG + r'|[xX]|%)?\s*[\|\(]',
    re.IGNORECASE,
)

# Labeled KV row: label: value unit (Latin / accented-Latin labels for Portuguese)
_KV_LABEL_RE = re.compile(
    r'(?P<label>[A-Za-zÀ-ÿ][^\|\n:*]{1,30}):\s*[~]?' + _CUR + r'\s*'
    r'(?P<num>' + _SIGN + r'[\d,\.]+)\s*(?P<unit>' + _MAG + r'|[xX]|%)?',
    re.IGNORECASE,
)


def _parse_md_tables(lines: list) -> list:
    """Parse all tables in the Markdown; return a list of (row_label, col_header, value, unit, lineno, raw)."""
    results = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Detect a header row (contains | and is not a separator row)
        if '|' in line and not re.match(r'^\|[\-\s\|:]+\|$', line):
            headers_raw = [h.strip().strip('*_').strip() for h in line.split('|')]
            headers_raw = [h for h in headers_raw if h]
            # The next line should be a separator row
            if i + 1 < len(lines) and re.match(r'^\|[\-\s\|:]+\|$', lines[i+1].strip()):
                i += 2  # Skip the separator row
                # Read data rows
                while i < len(lines):
                    dline = lines[i].strip()
                    if not dline or not dline.startswith('|'):
                        break
                    cells = [c.strip().strip('*_~').strip() for c in dline.split('|')]
                    cells = [c for c in cells if c != '']
                    if len(cells) < 2:
                        i += 1
                        continue
                    row_label = cells[0]
                    for col_idx, cell in enumerate(cells[1:], start=1):
                        col_header = headers_raw[col_idx] if col_idx < len(headers_raw) else f'col{col_idx}'
                        # Extract number + unit from the cell
                        m = re.search(
                            r'[~]?' + _CUR + r'\s*(' + _SIGN + r'[\d,\.]+)\s*'
                            r'(' + _MAG + r'|[xX]|%)?',
                            cell, re.IGNORECASE
                        )
                        if m:
                            val = _clean_num(m.group(1))
                            unit = (m.group(2) or '').strip()
                            if val is not None and val != 0 and abs(val) < 1e15:
                                results.append((row_label, col_header, val, unit, i + 1, dline))
                    i += 1
                continue
        i += 1
    return results


def extract_data_points(md_text: str) -> list:
    """Extract all recognizable financial data points from a Markdown report.

    Covers three structures:
      1. Multi-column Markdown tables (the primary source): (row label + column header) → value
      2. Colon-separated KV rows: label: value unit
      3. Bold number rows: **value** unit

    Returns a list of dict:
      {id, label, reported_value, unit, raw_text, line_number}
    """
    points = []
    seen = set()

    def _add(label, val, unit, lineno, raw):
        label = re.sub(r'[\*_`]+', '', label).strip()
        if not _is_valid_label(label):
            return
        if val is None or val == 0 or abs(val) > 1e15:
            return
        # Filter out pure year / quarter
        if re.fullmatch(r'(20\d{2}|Q[1-4]|\d{4}\s*Q[1-4])', label.strip()):
            return
        key = f"{label}|{round(val,4)}|{unit}"
        if key in seen:
            return
        seen.add(key)
        points.append({
            'id': len(points) + 1,
            'label': label,
            'reported_value': val,
            'unit': unit,
            'raw_text': raw[:120],
            'line_number': lineno,
        })

    lines = md_text.split('\n')
    in_code = False

    # --- 1. Multi-column tables ---
    for row_label, col_header, val, unit, lineno, raw in _parse_md_tables(lines):
        # Skip meaningless row labels
        if not _is_valid_label(row_label):
            continue
        # Skip meaningless column headers (a standalone YoY-growth column is not data to verify)
        if col_header.upper() in ('YOY', 'YOY GROWTH', 'GROWTH', 'CHANGE', 'TREND',
                                  'NOTE', 'VAR', 'VARIAÇÃO', 'VARIACAO'):
            continue
        # label = "row label · column header" (when the column header supplements the row label)
        if col_header and col_header != row_label:
            label = f"{row_label} · {col_header}"
        else:
            label = row_label
        _add(label, val, unit, lineno, raw)

    # --- 2. KV colon rows ---
    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        if in_code or stripped.startswith('> ') or re.match(r'^#{1,6}\s', stripped):
            continue
        if '|' in stripped:
            continue  # Tables are already handled above

        for m in _KV_LABEL_RE.finditer(stripped):
            label = m.group('label')
            val = _clean_num(m.group('num'))
            unit = (m.group('unit') or '').strip()
            _add(label, val, unit, lineno, stripped)

    return points


def sample_points(points: list, ratio: float = 0.15, seed: int = None) -> list:
    """Randomly sample a `ratio` fraction of the data points, minimum 3, maximum 30."""
    n = max(3, min(30, math.ceil(len(points) * ratio)))
    n = min(n, len(points))
    rng = Random(seed)
    sampled = rng.sample(points, n)
    # Sort by line number to make manual comparison easier
    return sorted(sampled, key=lambda p: p['line_number'])


# ---------------------------------------------------------------------------
# Pass / reject verdict
# ---------------------------------------------------------------------------

_TOLERANCE = 0.01   # 1% tolerance


def _pct_diff(reported: float, fetched: float) -> float:
    """Relative deviation (absolute)."""
    if reported == 0:
        return 0.0 if fetched == 0 else float('inf')
    return abs(reported - fetched) / abs(reported)


def render_verdict(results: list, report_name: str = "") -> dict:
    """
    Output a pass/reject verdict based on the verification results.

    results: list of dict, each containing:
      - id, label, reported_value, unit, fetched_value, fetched_source
      - (optional) fetched_value2, fetched_source2   ← second source

    Returns:
      {
        'verdict': 'PASS' | 'FAIL',
        'pass_count': int,
        'fail_count': int,
        'total': int,
        'fail_items': [...],
        'summary': str,
      }
    """
    BOLD = '\033[1m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

    print('=' * 70)
    print(f'{BOLD}Report Data Spot-Check — Pass/Reject Verdict{RESET}')
    if report_name:
        print(f'Report: {report_name}')
    print('=' * 70)
    print()

    fail_items = []
    warn_items = []

    for item in results:
        label = item.get('label', '?')
        reported = float(item.get('reported_value', 0))
        unit = item.get('unit', '')
        fetched = item.get('fetched_value')
        source = item.get('fetched_source', '?')
        fetched2 = item.get('fetched_value2')
        source2 = item.get('fetched_source2', '')

        # --- Compare against primary source ---
        if fetched is None:
            # No verification value provided → skip (not counted as pass/fail)
            print(f'  ⬜ [{item["id"]:>2}] {label[:35]:35s} {reported:>12.2f} {unit}  →  [no verification value provided, skipped]')
            continue

        fetched = float(fetched)
        diff1 = _pct_diff(reported, fetched)

        # --- Compare against second source (if any) ---
        diff2 = None
        if fetched2 is not None:
            fetched2 = float(fetched2)
            diff2 = _pct_diff(reported, fetched2)

        # Decide
        pass1 = diff1 <= _TOLERANCE
        pass2 = (diff2 is None) or (diff2 <= _TOLERANCE)

        if pass1 and pass2:
            status = f'{GREEN}✅ Pass{RESET}'
            detail = f'{source}: {fetched:.2f} (deviation {diff1*100:.2f}%)'
            if diff2 is not None:
                detail += f'  |  {source2}: {fetched2:.2f} (deviation {diff2*100:.2f}%)'
        elif not pass1 and not pass2:
            status = f'{RED}❌ Fail{RESET}'
            detail = f'{source}: {fetched:.2f} (deviation {diff1*100:.2f}%)'
            if diff2 is not None:
                detail += f'  |  {source2}: {fetched2:.2f} (deviation {diff2*100:.2f}%)'
            fail_items.append({
                'id': item['id'],
                'label': label,
                'reported': reported,
                'unit': unit,
                'fetched': fetched,
                'source': source,
                'fetched2': fetched2,
                'source2': source2,
                'diff1_pct': round(diff1 * 100, 2),
                'diff2_pct': round(diff2 * 100, 2) if diff2 is not None else None,
                'raw_text': item.get('raw_text', ''),
                'line_number': item.get('line_number', 0),
            })
        else:
            # One source passes, the other fails → warning, not counted as a failure
            status = f'{YELLOW}⚠️  Warning{RESET}'
            detail = f'{source}: {fetched:.2f} (deviation {diff1*100:.2f}%)'
            if diff2 is not None:
                detail += f'  |  {source2}: {fetched2:.2f} (deviation {diff2*100:.2f}%)'
            warn_items.append({
                'id': item['id'], 'label': label,
                'reported': reported, 'unit': unit,
                'diff1_pct': round(diff1 * 100, 2),
                'diff2_pct': round(diff2 * 100, 2) if diff2 is not None else None,
            })

        print(f'  {status} [{item["id"]:>2}] {label[:35]:35s}  Reported: {reported:>12.2f} {unit}')
        print(f'              {" " * 38}{detail}')

    print()
    print('-' * 70)

    total = len([r for r in results if r.get('fetched_value') is not None])
    fail_count = len(fail_items)
    warn_count = len(warn_items)
    pass_count = total - fail_count - warn_count

    print(f'  Total checked: {total}  |  Pass: {GREEN}{pass_count}{RESET}  |  Warning: {YELLOW}{warn_count}{RESET}  |  Fail: {RED}{fail_count}{RESET}')
    print()

    if fail_count == 0:
        print(f'{BOLD}{GREEN}[PASS] All spot-checked data passed, the report may be published.{RESET}')
        verdict = 'PASS'
    else:
        print(f'{BOLD}{RED}[REJECT] {fail_count} data point(s) failed verification, the report must be corrected and re-reviewed.{RESET}')
        print()
        print(f'{BOLD}Reasons for rejection:{RESET}')
        for fi in fail_items:
            print(f'  ❌ Line {fi["line_number"]} | {fi["label"]}')
            print(f'     Reported value: {fi["reported"]} {fi["unit"]}')
            print(f'     {fi["source"]}: {fi["fetched"]}  (deviation {fi["diff1_pct"]}%)')
            if fi.get('fetched2') is not None:
                print(f'     {fi["source2"]}: {fi["fetched2"]}  (deviation {fi["diff2_pct"]}%)')
            print(f'     Source text: {fi["raw_text"][:80]}')
            print()
        verdict = 'FAIL'

    if warn_count > 0:
        print(f'{YELLOW}Note: {warn_count} data point(s) have inconsistent results across the two sources (over 1%), possibly a definition difference (GAAP/Non-GAAP or FX); please review manually.{RESET}')
        for wi in warn_items:
            print(f'  ⚠️  {wi["label"]}  Reported: {wi["reported"]} {wi["unit"]}  deviation: {wi["diff1_pct"]}% / {wi["diff2_pct"]}%')

    print('=' * 70)

    return {
        'verdict': verdict,
        'pass_count': pass_count,
        'warn_count': warn_count,
        'fail_count': fail_count,
        'total': total,
        'fail_items': fail_items,
        'warn_items': warn_items,
    }


# ---------------------------------------------------------------------------
# CLI Entry Point
# ---------------------------------------------------------------------------

def _force_utf8_stdio():
    """Force stdout/stderr to UTF-8.

    The Windows console defaults to GBK, so characters like €, →, ★ in a report make
    print(json.dumps(...)) raise UnicodeEncodeError and crash. errors='replace' ensures
    even extreme characters do not interrupt the flow.
    """
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8', errors='replace')
        except Exception:
            pass  # Ignore when not a TextIOWrapper (e.g. redirected to a pipe object)


def main():
    _force_utf8_stdio()
    parser = argparse.ArgumentParser(
        description='Report Audit Tool — research-report data spot-check tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Workflow:

  Step 1 — Extract data points and randomly sample 15%, output the spot-check list:
    python3 tools/report_audit.py extract --report reports/Petrobras/Petrobras-research-20260728.md

  Step 2 — For each data point in the list, Claude pulls the value from a reliable source,
            filling in fetched_value / fetched_source / fetched_value2 / fetched_source2

  Step 3 — Feed in the verification results, output the pass/reject verdict:
    python3 tools/report_audit.py verdict --results '[
      {"id":1,"label":"Revenue","reported_value":512.3,"unit":"B","fetched_value":512.3,"fetched_source":"CVM","fetched_value2":511.0,"fetched_source2":"marketdata-mcp"},
      ...
    ]'

  One-step preview (print the spot-check list only, no verification):
    python3 tools/report_audit.py extract --report reports/xxx.md --dry-run

  Specify the sampling ratio (default 0.15):
    python3 tools/report_audit.py extract --report reports/xxx.md --ratio 0.20

  Fix the random seed (reproduce the same batch of samples):
    python3 tools/report_audit.py extract --report reports/xxx.md --seed 42
        """)

    sub = parser.add_subparsers(dest='command')

    # extract
    ext = sub.add_parser('extract', help='Extract data points from a report and randomly sample')
    ext.add_argument('--report', required=True, help='Report file path (Markdown)')
    ext.add_argument('--ratio', type=float, default=0.15, help='Sampling ratio, default 0.15')
    ext.add_argument('--seed', type=int, default=None, help='Random seed (optional, for reproduction)')
    ext.add_argument('--dry-run', action='store_true', help='Print only, do not output JSON')

    # verdict
    vrd = sub.add_parser('verdict', help='Output pass/reject verdict from verification results')
    vrd.add_argument('--results', required=True, help='JSON array with fields like fetched_value')
    vrd.add_argument('--report', default='', help='Report name (optional, for display)')
    vrd.add_argument('--output-json', action='store_true', help='Output the verdict result as JSON to stdout')

    args = parser.parse_args()

    if args.command == 'extract':
        if not os.path.exists(args.report):
            print(f'❌ File does not exist: {args.report}', file=sys.stderr)
            sys.exit(1)

        with open(args.report, 'r', encoding='utf-8') as f:
            text = f.read()

        all_points = extract_data_points(text)
        sampled = sample_points(all_points, ratio=args.ratio, seed=args.seed)

        print('=' * 70)
        print(f'Report Data Spot-Check List')
        print(f'File: {args.report}')
        print(f'Total data points extracted: {len(all_points)}  |  Sampling ratio: {args.ratio:.0%}  |  Sampled count: {len(sampled)}')
        if args.seed is not None:
            print(f'Random seed: {args.seed} (can be used to reproduce the same batch of samples)')
        print('=' * 70)
        print()
        print(f'{"ID":>3}  {"Line":>5}  {"Data label":<35}  {"Reported":>12}  {"Unit"}')
        print(f'{"─"*3}  {"─"*5}  {"─"*35}  {"─"*12}  {"─"*6}')
        for p in sampled:
            print(f'{p["id"]:>3}  {p["line_number"]:>5}  {p["label"][:35]:<35}  {p["reported_value"]:>12.2f}  {p["unit"]}')
        print()
        print('↑ For each data point above, pull the value from the sources below and fill in fetched_value:')
        print('  Brazil / B3: CVM (rad.cvm.gov.br) + B3 (b3.com.br) + company IR (primary)')
        print('               connected market-data MCP (prices/fundamentals, secondary)')
        print('  US-listed / ADRs: SEC EDGAR (primary) + stockanalysis.com (secondary)')
        print()

        if not args.dry_run:
            # Output a fillable JSON template
            template = []
            for p in sampled:
                template.append({
                    'id': p['id'],
                    'label': p['label'],
                    'reported_value': p['reported_value'],
                    'unit': p['unit'],
                    'line_number': p['line_number'],
                    'raw_text': p['raw_text'],
                    'fetched_value': None,       # ← fill in the primary-source verification value
                    'fetched_source': '',        # ← fill in the primary-source name
                    'fetched_value2': None,      # ← fill in the secondary-source verification value (optional)
                    'fetched_source2': '',       # ← fill in the secondary-source name (optional)
                })
            print('Spot-check list JSON (after filling in fetched_value, pass it to the verdict command):')
            print()
            print(json.dumps(template, ensure_ascii=False, indent=2))

    elif args.command == 'verdict':
        try:
            results = json.loads(args.results)
        except json.JSONDecodeError as e:
            print(f'❌ JSON parse failed: {e}', file=sys.stderr)
            sys.exit(1)

        report_name = args.report or ''
        outcome = render_verdict(results, report_name=report_name)

        if args.output_json:
            print(json.dumps(outcome, ensure_ascii=False, indent=2))

        # A non-zero exit code signals rejection, convenient for CI/scripts to check
        sys.exit(0 if outcome['verdict'] == 'PASS' else 1)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
