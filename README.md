# AI Berkshire — Brazil Edition

A collection of value-investing research **Skills for [Claude Code](https://claude.com/claude-code)**, adapted for the **Brazilian stock market (B3)**. Every skill runs a disciplined, source-cited research workflow built on a four-master framework: **Warren Buffett, Charlie Munger, Duan Yongping, and Li Lu**.

> Fork of [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire), translated to English and retargeted from Chinese equities to Brazil / B3. All output — reports, commit messages, filenames — is in English.

## What's inside

**Primary market:** Brazil / B3 (BRL). US-listed companies and ADRs are supported as a secondary case.

**Data sources:** CVM filings (RAD portal) and company IR sites for disclosures; B3 and the connected MCP market-data tools (a market-data server + finnhub) for prices and fundamentals; SEC EDGAR for US/ADR filings.

## Skills

| Skill | What it does |
|------|------|
| `/investment-research` | Full four-master research on one company |
| `/investment-team` | Four parallel agents (one per master) → synthesized report |
| `/investment-checklist` | Buffett-style pre-buy checklist |
| `/quality-screen` | 7-metric fast screen to rule out non-first-class companies |
| `/industry-research` | Value-chain panorama + per-company analysis |
| `/industry-funnel` | Funnel screen from full market down to a few names |
| `/news-pulse` | Fast attribution of a stock's news / price move (4 parallel scouts) |
| `/earnings-review` | Deep read of a single earnings report |
| `/earnings-team` | Four-master parallel earnings deep-read |
| `/management-deep-dive` | "Buying a stock is buying the people" — management review |
| `/thesis-tracker` | Post-buy discipline system; long-lived thesis file |
| `/thesis-drift` | Detect thesis drift (fact change vs. wording change) |
| `/portfolio-review` | Manage the portfolio, not just individual companies |
| `/income-investment` | Durable + opportunistic distribution/income analysis |
| `/private-company-research` | Multi-agent research on unlisted companies |
| `/deep-company-series` | 3–8 long-form articles dissecting one company |
| `/bottleneck-hunter` | Global supply-chain bottleneck arbitrage |
| `/financial-data` | Financial-data sourcing & cross-verification standard |

## Usage

Copy the skill files into your Claude Code commands directory:

```bash
cp skills/*.md ~/.claude/commands/
```

Then invoke a skill in Claude Code, e.g. `/news-pulse Vale` or `/investment-research Petrobras`. Reports are written under `reports/{Company}/`.

## Layout

```
skills/    — skill definitions (.md)
tools/     — helper scripts (financial_rigor.py, report_audit.py, stock_screener.py, ...)
reports/   — research output, organized by company
```

See [CLAUDE.md](CLAUDE.md) for the full conventions (report naming, objectivity principles, data sources, GitHub workflow).

## License

See [LICENSE](LICENSE). This is a personal research toolkit; nothing here is investment advice.
