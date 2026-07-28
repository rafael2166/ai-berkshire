# AI Berkshire (Brazil Edition) — Project Instructions

## Overview

A collection of value-investing research Skills for Claude Code, adapted for the **Brazilian stock market (B3)**. Built on a four-master framework: **Warren Buffett, Charlie Munger, Duan Yongping, Li Lu**.

Primary market: **Brazil / B3** (BRL). US-listed companies and ADRs are supported as a secondary case (SEC filings).

## Project Structure

```
skills/    — investment-research Skill definitions (.md); copy to ~/.claude/commands/ to use
tools/     — helper scripts (financial_rigor.py for precise math, report_audit.py for QA, etc.)
reports/   — research report output (organized by company)
```

## Data Sources (Brazil primary)

- **Filings & disclosures:** CVM (Comissão de Valores Mobiliários) via the RAD portal (www.rad.cvm.gov.br); company IR ("Relações com Investidores") sites; B3 (www.b3.com.br).
- **Market data:** the connected MCP market-data tools (a market-data server and finnhub) are the preferred source for prices, quotes, and fundamentals — do NOT use web scraping for market data. Supplement with WebSearch / WebFetch for news and primary documents.
- **US-listed / ADRs (secondary):** SEC EDGAR for filings.
- **Regulators to watch (for news/regulatory analysis):** CVM (securities), CADE (antitrust), BACEN (banking/monetary), sector agencies (ANP oil & gas, ANEEL electricity, ANATEL telecom, ANS health).

## Report Directory Structure

All reports live under a per-**company** folder (English/latin folder names):

```
reports/
├── Petrobras/                 — all Petrobras reports
│   ├── Petrobras-research-20260728.md
│   ├── Petrobras-earnings-2026Q2.md
│   ├── Petrobras-management-20260728.md
│   └── Petrobras-thesis.md
├── Vale/                      — all Vale reports
├── Itau/                      — all Itaú reports
├── {Industry}-industry-{YYYYMMDD}.md    — industry reports at root
├── {Industry}-funnel-{YYYYMMDD}.md      — funnel-screen reports at root
├── portfolio-latest.md                  — portfolio report at root (continuously updated)
└── {Company}-comparison-checklist-{YYYYMMDD}.md — multi-company reports at root
```

## Report Naming Conventions

| Skill | Filename format | Example |
|------|---------|------|
| /investment-team | `{Company}/` folder with 4 perspectives + final report | `reports/Petrobras/final-report.md` |
| /investment-research | `{Company}-research-{YYYYMMDD}.md` | `reports/Vale/Vale-research-20260728.md` |
| /investment-checklist | `{Company}-checklist-{YYYYMMDD}.md` | `reports/Vale/Vale-checklist-20260728.md` |
| /industry-research | `{Industry}-industry-{YYYYMMDD}.md` (root) | `reports/mining-industry-20260728.md` |
| /industry-funnel | `{Industry}-funnel-{YYYYMMDD}.md` (root) | `reports/banking-funnel-20260728.md` |
| /private-company-research | `{Company}-private-{YYYYMMDD}.md` | `reports/Nubank/Nubank-private-20260728.md` |
| /earnings-review | `{Company}-earnings-{period}.md` | `reports/Vale/Vale-earnings-2026Q2.md` |
| /earnings-team | `{Company}/` folder: 4 master perspectives + research draft + final report | `reports/Vale/Vale-earnings-2026Q2.md` |
| /thesis-tracker | `{Company}-thesis.md` (long-lived) | `reports/Vale/Vale-thesis.md` |
| /portfolio-review | `portfolio-latest.md` (root, continuously updated) | `reports/portfolio-latest.md` |
| /management-deep-dive | `{Company}-management-{YYYYMMDD}.md` | `reports/Vale/Vale-management-20260728.md` |
| /news-pulse | `{Company}-news-{YYYYMMDD}.md` | `reports/Vale/Vale-news-20260728.md` |

## /investment-team File Structure

```
reports/{Company}/
├── README.md                              — research-framework overview + core conclusions
├── 01-business-model-duan-yongping.md
├── 02-financials-valuation-buffett.md
├── 03-industry-competition-munger.md
├── 04-risk-management-li-lu.md
└── final-report.md                        — Team Lead synthesized report
```

## Core Analytical Principles (Highest Priority)

- **Objectivity above all** — every judgment must rest on facts and data; no unsupported assertions.
- Strictly separate **fact** from **opinion**: back facts with data; explicitly label opinions as "opinion" or "speculation."
- **No preset stance**: don't start bullish or bearish. Lay out the data, then the logic, then the conclusion. Conclusions must follow naturally from the data.
- Avoid subjective phrasing ("I think", "obviously"). Use "the data shows", "the evidence indicates", "according to {source}".
- **Present both sides**: every core judgment must carry a counter-argument ("but on the other hand…") so the reader can weigh it.
- Be honest about uncertainty — say "uncertain" or "insufficient data" rather than filling gaps with speculation.
- Every Skill must follow these principles when it runs.

## Report Language & Style

- **All output is in English** — reports, section headers, commit messages, filenames. This overrides any Chinese scaffolding that may remain in a skill template; the output language is always English.
- Style: direct, sharp, no filler.
- Cite a source for every data point; cross-verify key figures with ≥2 independent sources.
- Label estimates as "estimate".
- Ratings use ★ (1–5, no half-stars).
- Weave in Buffett / Munger / Duan Yongping / Li Lu commentary where it adds insight.

## Data-Integrity Notes

- Verify market cap by hand: share price × shares outstanding, then compare to the reported figure.
- State the currency explicitly (BRL / USD) to avoid mix-ups, especially for companies with both B3 shares and US ADRs.
- Compute PE / ROE and similar ratios precisely with `tools/financial_rigor.py`.
- Prefer the connected MCP market-data tools over any scraping for prices/fundamentals.
- After writing a report, ask whether to push it to GitHub.

## GitHub Workflow

- Remote `origin` → this fork: `https://github.com/rafael2166/ai-berkshire.git`
- Remote `upstream` → original project: `https://github.com/xbtlin/ai-berkshire.git` (pull updates with `git pull upstream main` if desired)
- **Commit messages in English**, clearly describing what changed.
- Don't push intermediate working files — push only the final report.

```bash
# push a report to your fork
cd ~/Documents/Projects/Research/ai-berkshire
git add reports/{Company}/{report}.md
git commit -m "Add {Company} {report-type} report"
git push origin main
```
