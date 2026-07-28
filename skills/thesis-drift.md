# Thesis Drift Detection: Separating Fact Changes from Wording Changes

Run thesis-drift detection on $ARGUMENTS.

**Supported input formats**:
- `CompanyName old-report-path new-report-path` — compare two specified research reports or thesis snapshots
- `CompanyName reports/{CompanyName}/thesis-{old-date}.md reports/{CompanyName}/thesis-{new-date}.md` — compare two dated thesis snapshots
- `CompanyName` — automatically locate `reports/{CompanyName}/thesis.md` and historical snapshots in the same directory; if no baseline exists, fall through to missing-baseline handling

> "When the facts change, I change my mind. What do you do, sir?" — John Maynard Keynes
>
> "A share-price swing is not thesis drift; a change in the facts is." — AI Berkshire

## Design Philosophy

The hardest part of holding for the long term is not reading the news every day but distinguishing three things:
- **Fact change**: revenue, margins, competitive landscape, management behavior, or capital allocation undergo a verifiable change
- **Price change**: market sentiment or the valuation multiple changes, but the business itself has not
- **Wording change**: two reports phrase things differently, but the underlying evidence and judgment are unchanged

The goal of thesis-drift detection is: **acknowledge a thesis change only when the evidence changes.** Do not manufacture drift because a report was rewritten, and do not misjudge fundamentals because the share price moved.

This Skill depends on the structured dimensions produced by `/thesis-tracker`: the core-assumption list, red-line list, valuation anchor, and tracking-record table. When those structures are absent, first build the baseline, then run drift detection.

## Execution Flow

### Step 1: Determine the operating mode

Parse `$ARGUMENTS`:
- If two report paths are provided → enter **specified-report comparison** mode
- If only a company name is provided → locate `reports/{CompanyName}/thesis.md` and historical snapshots, enter **automatic-snapshot comparison** mode
- If only one report is found or there is no historical baseline → enter **missing-baseline handling** mode
- If the two reports are not for the same company → stop and ask the user to confirm; do not make a cross-company drift judgment

---

## Mode A: Specified-Report Comparison

### A1: Read and validate both reports

Read the old and new reports and extract:
- Report date, company name, ticker
- Core thesis (5 sentences)
- Core-assumption list
- Red-line list
- Valuation anchor
- Tracking-record table
- Management-quality judgment
- Competitive-moat judgment
- Current recommended action (Buy / Hold / Watch / Reduce / Exit)

If a report lacks a key structure, first flag "structure missing" but still try to extract evidence from the body text; mark dimensions that cannot be extracted as "cannot determine" — do not fabricate conclusions.

### A2: Evidence normalization

Organize the factual evidence from both reports into one shared table:

| Dimension | Old-report evidence | New-report evidence | Data source | Verifiable? |
|-----------|---------------------|---------------------|-------------|-------------|
| Valuation anchor | | | | |
| Core assumptions | | | | |
| Red lines | | | | |
| Management quality | | | | |
| Competitive moat | | | | |

**Compare only evidence, not prose style.** If the new vs old report is merely a paraphrase, reordering, or tone change, but the factual data and judgment thresholds are unchanged, rule it Unchanged.

### A3: Numeric and valuation verification

All numeric changes must be computed precisely with `tools/financial_rigor.py`; LLM mental arithmetic is prohibited:

```bash
python3 tools/financial_rigor.py verify-valuation \
  --price {current price} \
  --eps {EPS} \
  --bvps {book value per share} \
  --fcf-per-share {free cash flow per share}
```

To compute market cap, percentage changes, target-price differences, or scenario valuations, use:

```bash
python3 tools/financial_rigor.py verify-market-cap --price {price} --shares {shares} --reported {reported market cap} --currency {currency}
python3 tools/financial_rigor.py cross-validate --field {field} --values '{JSON}' --unit {unit}
python3 tools/financial_rigor.py three-scenario --price {price} --eps {EPS} --shares {shares in 100M} --growth {bull} {base} {bear} --pe {bull PE} {base PE} {bear PE}
python3 tools/financial_rigor.py calc --expr '{exact expression}'
```

Key financial data must be cross-verified against at least two independent sources. Figures with insufficient sourcing, inconsistent basis, or that cannot be reconciled must be flagged as "low confidence / to be verified."

### A4: Judge drift per dimension

Use the following fixed dimensions; do not add or drop them ad hoc:

| Dimension | Judgment focus | Improved | Unchanged | Weakened |
|-----------|----------------|----------|-----------|----------|
| Valuation anchor | Intrinsic value, PE/PB/FCF Yield, margin of safety, target-price range | Margin of safety widens or intrinsic value revised up, tool-verified | Valuation range and margin of safety materially unchanged | Margin of safety narrows, intrinsic value revised down, or valuation assumptions invalidated |
| Core-assumption list | Revenue growth, margins, cash flow, users/orders/capacity and other verifiable assumptions | More assumptions reinforced by new evidence | Assumption status broadly consistent with evidence | Assumptions marginally weakened, impaired, or broken |
| Red-line list | Integrity, regulation, business decline, competitive breakthrough, abnormal management action | Existing red-line risk removed or materially reduced | Not triggered and risk level unchanged | A red line is triggered or its probability rises |
| Management quality | Integrity, capital allocation, buybacks/dividends, execution, shareholder friendliness | New behavior raises trust | Behavior continues the prior judgment | Behavior harms trust or capital allocation worsens |
| Competitive moat | Market share, pricing power, network effects, cost advantage, substitution threat | Moat widens or competitive advantage is validated | Landscape materially unchanged | Moat weakened or a competitor breaks through |

Each dimension may yield only three conclusions: **Improved / Unchanged / Weakened**.

### A5: Evidence-driven rule

Every non-Unchanged conclusion must cite the specific new evidence that caused the change:
- Financial-statement line items: e.g., revenue growth, gross margin, operating cash flow, buyback amount, net cash
- Regulatory disclosures: e.g., DFP/ITR (CVM filings), 20-F for US-listed ADRs, annual/interim reports, CVM material-fact notices (fato relevante), SEC filings
- News events: e.g., management change, regulatory penalty, loss of a major customer, competitor breakthrough
- Price and valuation: must state whether this is a "valuation change" or a "fundamental change" — do not conflate them

If no evidence can be found to explain a change, it must be ruled **Unchanged** or **cannot determine**; drift cannot be inferred from wording differences.

### A6: Output the drift report

#### Report structure

```
1. Comparison subjects and time span
2. Overall conclusion: has the thesis drifted
3. Dimension drift table
4. Evidence-difference detail
5. Valuation and numeric verification
6. Recommended-action migration
7. Uncertain items and sources still needed
8. Focus points for the next review
```

#### Dimension drift table

| Dimension | Old judgment | New judgment | Drift direction | Trigger evidence | Confidence |
|-----------|--------------|--------------|:---------------:|------------------|:----------:|
| Valuation anchor | | | Improved / Unchanged / Weakened | | High/Med/Low |
| Core-assumption list | | | Improved / Unchanged / Weakened | | High/Med/Low |
| Red-line list | | | Improved / Unchanged / Weakened | | High/Med/Low |
| Management quality | | | Improved / Unchanged / Weakened | | High/Med/Low |
| Competitive moat | | | Improved / Unchanged / Weakened | | High/Med/Low |

**For Unchanged rows, write `—` for trigger evidence; do not fabricate evidence to fill the table.**

#### The overall conclusion must answer

1. **Has the thesis drifted?** Not drifted / positive drift / negative drift / insufficient evidence to determine
2. **Where does the drift come from?** Valuation / fundamentals / management / competitive landscape / red-line event
3. **Is it a fact change or a price change?** Separate them explicitly
4. **How should the recommended action migrate?** e.g., Watch → Buy, Buy → Hold, Hold → Reduce, Reduce → Exit
5. **What evidence is needed next?** Next earnings report / regulatory disclosure / management explanation / competitor data

---

## Mode B: Automatic-Snapshot Comparison

### B1: Locate snapshots

Search under `reports/`:
- `reports/{CompanyName}/thesis.md`
- `reports/{CompanyName}/thesis-*.md`
- Reports under `reports/{CompanyName}/` containing `thesis` or `tracking` in the name

Choose the earliest structurally complete file as the old report, and the most recent file as the new report. If the user specifies dates, the user's specification prevails.

### B2: Prevent mismatched pairing

Before comparing, confirm:
- Company name or ticker matches
- Report dates differ
- Both reports contain an extractable thesis structure or research conclusion

If the same company cannot be confirmed, stop and ask the user to provide explicit paths.

### B3: Run Mode A

Once two valid snapshots are found, run Mode A in full.

---

## Mode C: Missing-Baseline Handling

If only one report is found or no old snapshot is found:

1. State clearly: **no comparable historical baseline exists, so drift detection cannot run**
2. Do not reconstruct an old thesis from memory or market impression
3. Guide the user to first run `/thesis-tracker {CompanyName} build thesis` to establish a structured baseline
4. If the current report is already sufficiently complete, suggest saving it as `reports/{CompanyName}/thesis.md` as the baseline for future drift detection

Output format:

```
Cannot run thesis-drift detection: no historical baseline.

Found:
- Current report: {path / not found}
- Historical baseline: not found

Suggested:
1. First run /thesis-tracker {CompanyName} to build the thesis
2. After the next earnings report or a major event, run /thesis-drift {CompanyName} old-report new-report
```

---

## Key Principles

- **Evidence over wording** — a paraphrase is not drift; only a change in factual evidence is drift
- **Fundamentals over share price** — price moves only affect the valuation anchor, they do not automatically change business quality
- **Numbers must be verified** — all percentages, valuation multiples, and target-price differences must use `tools/financial_rigor.py`
- **When uncertain, say uncertain** — when sources are missing, bases are inconsistent, or figures cannot be reconciled, do not force a judgment
- **Red lines handled separately** — a red-line trigger outranks cheap valuation and cannot be masked by a low PE
- **Output must be auditable** — every Improved / Weakened conclusion must be traceable to specific evidence
