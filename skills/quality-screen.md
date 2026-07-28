# Quality Screen: 7 Metrics to Quickly Rule Out Non-First-Class Companies

Run the elimination-metric screen on $ARGUMENTS to quickly rule out names that fail first-class-company standards.

**Supported input formats**:

| Input type | Example | Notes |
|------------|---------|-------|
| Single stock | `PETR4, VALE3, ITUB4` | Screen each company one by one |
| Industry | `Brazilian brewers` `Global cloud computing` `B3 retail names` | First search the industry's main listed companies (10–20), then screen each |
| Market / index | `Ibovespa constituents` `IBrX-100` `Nasdaq 100` | Pull the constituent list, then screen each |
| Theme | `Brazilian high-dividend leaders` `Global AI compute chain` | First search theme-related companies, then screen each |

In industry/market/theme mode, the output additionally includes: pass-rate statistics, in-industry ranking, and a sector comparison summary.

## Design Principles

- **Goal**: never kill a genuinely first-class company by mistake, but reliably eliminate companies that are clearly not first-class
- **Logic**: 7 hard metrics + 2 exemption rules, biased toward letting borderline cases through rather than false rejection
- **Scope**: all listed companies (banks/insurers are exempt from metric #3, interest coverage)

---

## The 7 Elimination Metrics

| # | Metric | Exclusion condition | What it measures |
|---|--------|---------------------|------------------|
| 1 | 10-year average ROE | < 8% | Capital efficiency — can shareholders' money beat the opportunity cost |
| 2 | 5-year cumulative free cash flow | Negative | Hard cash — is the profit real or "paper wealth" |
| 3 | Interest coverage (EBIT / interest) | < 2x | Solvency safety — ability to service interest |
| 4 | Long-run gross margin | < 15% | Pricing power — is the product/service differentiated |
| 5 | Operating cash flow / net income (5-yr avg) | < 0.7 | Earnings quality — do reported profits convert to cash |
| 6 | Long-run net margin | < 5% | Resilience — does profit go to zero when revenue wobbles |
| 7 | 5-year share-count inflation | > 20% (non-M&A) | Shareholder interest — is management diluting your stake |

## The 3 Exemption Rules

### Exemption A: Strategic-investment-phase exemption (applies to metric #1)

If all three conditions below hold, metric #1 (ROE shortfall) can be exempted:
1. Listed for less than 10 years
2. Gross margin > 30% (proves the business model itself has pricing power)
3. Operating cash flow positive in the last 2 years (proves the cash-generating engine is in place)

**Logic**: high gross margin + turning cash-flow-positive shows the business model is sound; low ROE is only because the company is still in the investment phase.

### Exemption B: Deliberate low-margin exemption (applies to metric #6)

If both conditions below hold, metric #6 (net-margin shortfall) can be exempted:
1. Gross margin > 30% (able to earn but choosing not to)
2. Net margin has recovered above 5% in the last 2 years, or shows a clear upward trend

**Logic**: high gross margin means pricing power exists; low net margin is a strategic choice (reinvestment) rather than a capability gap. Classic example: Amazon.

### Exemption C: High-turnover, thin-margin model exemption (applies to metrics #4 and #6)

If all three conditions below hold, metric #4 (gross margin) and metric #6 (net margin) shortfalls can be exempted:
1. ROE > 20% (proves that despite low margins, return on capital is extremely high)
2. Operating cash flow / net income > 1.0 (earnings quality is not an issue)
3. The business model is of the "membership / platform commission / high-turnover thin-margin" type (profit is not embedded in product markups)

**Logic**: for some first-class companies the profit is not hidden in gross margin but in membership fees, turnover efficiency, or platform take-rates. Their gross and net margins are naturally very low, but an extremely high ROE shows first-class capital efficiency. Classic example: Costco (gross margin 12%, net margin 2.5%, yet ROE 25%+ and membership renewal 90%+).

---

## Execution Flow

### Step 1: Parse the input and define the screening universe

**Mode determination**:
- If the input is a specific company name/ticker → **single-stock mode**, go straight to Step 2
- If the input is an industry/market/theme → **batch mode**, first do the following:
  1. Use WebSearch to find the main listed companies in that industry/market/theme
  2. Industry mode: cover the top 15–20 listed companies by market cap in that industry
  3. Index mode: pull the full constituent list
  4. Theme mode: search related companies, cover 15–30
  5. List the full company roster for confirmation (if company count > 30, process in parallel batches)

For each company, determine the full name, ticker, and exchange.

### Step 2: Parallel data collection

Launch an independent background Agent for each company, using WebSearch and the available MCP market-data tools (market-data server and finnhub) to gather the following:

1. **ROE**: year-by-year ROE for the past 10 years (or since listing), compute the average
2. **Free cash flow**: operating cash flow and capex for the past 5 years, compute 5-year cumulative FCF
3. **Interest coverage**: latest-year EBIT and interest expense, compute the ratio
4. **Gross margin**: 5-year gross-margin trend
5. **Operating cash flow / net income**: the ratio over 5 years, compute the average
6. **Net margin**: 10-year net-margin trend, compute the average
7. **Share-count change**: total shares 5 years ago vs current, compute the inflation ratio

Data-source priority: company filings (CVM ITR/DFP, SEC 20-F for ADRs) > sell-side research > financial data platforms. Cross-verify key figures per `skills/financial-data.md`.

### Step 3: Check each metric

For each company, check all 7 metrics one by one:
- ✅ Pass
- ❌ Fail
- ⚠️ Borderline (with a numeric note)

If a metric is violated, check whether the corresponding exemption condition is met.

### Step 4: Output the result

#### Output format

```markdown
# Quality Screen Results

**Screen date**: {today's date}
**Number of companies**: {N}

## Summary Table

| Company | ①ROE | ②FCF | ③Int. cov. | ④Gross margin | ⑤OCF/NI | ⑥Net margin | ⑦Dilution | Result |
|---------|------|------|-----------|---------------|---------|-------------|-----------|--------|
| xxx | ✅ 24% | ✅ | ✅ | ✅ 56% | ✅ | ✅ 30% | ✅ | **Pass** |
| yyy | ❌ 3% | ❌ | ❌ | ✅ 20% | ✅ | ❌ 2% | ✅ | **Excluded** |
| zzz | ⚠️→✅ | ✅ | ✅ | ✅ 35% | ✅ | ⚠️→✅ | ✅ | **Pass (exempted)** |

## Companies That Passed (N)
[list]

## Companies Excluded (N)
| Company | Metric violated | Specific data | Reason for exclusion |
|---------|-----------------|---------------|----------------------|

## Companies Passed via Exemption (N)
| Company | Exemption clause | Specific data | Exemption rationale |
|---------|------------------|---------------|---------------------|

## Borderline / Disputed (if any)
[additional notes on companies near a threshold]

## Sector Summary (industry/market mode only)

**Pass rate**: {passed}/{total} = {percentage}
**Industry quality assessment**: [assess overall industry quality based on the pass rate]

| Quality tier | Companies | Common traits |
|--------------|-----------|---------------|
| First-class (all pass + high ROE) | xxx, yyy | ... |
| Acceptable (all pass but mediocre metrics) | aaa, bbb | ... |
| Eliminated | ccc, ddd | ... |

**Industry stock-picking conclusion**: [one-sentence take on whether this industry is worth deeper work, and which 2–3 names most warrant attention]
```

---

## Cautions

1. **Banks/insurers**: metric #3 (interest coverage) does not apply — their business model is fundamentally spread-based
2. **REITs**: ROE can swing widely due to property revaluation; use "core operating profit ROE" instead
3. **Insufficient data**: if a metric cannot be obtained, mark it "insufficient data" rather than defaulting to pass/fail
4. **Cyclical industries**: use averages over a full cycle (covering at least one peak and one trough), not a single year
5. **Short listing history**: for companies with less than 5 years of history, use all available data but flag "insufficient data window" in the result

## Limitations Statement

This metric set can eliminate companies that are "definitely not good," but passing the screen does not mean a company is "definitely good." Companies that pass still require further research:
- Is the business model sustainable
- Is management trustworthy
- Is the current valuation reasonable
- Is the competitive landscape deteriorating

Elimination is the first step, not the last.
