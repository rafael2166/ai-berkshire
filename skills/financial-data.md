# Financial Data Sourcing and Cross-Verification Standard

This standard applies to all research involving corporate financial data. **Every key data point must come from two independent sources; any discrepancy >1% must be flagged.**

---

## Data Source Priority

### Brazil / B3 (primary market — e.g., PETR4, VALE3, ITUB4, BBAS3, WEGE3, ABEV3)

| Priority | Source | URL | How to access |
|----------|--------|-----|---------------|
| 1 (primary) | **MCP market-data tools** | market-data server + finnhub (available in this environment) | Prefer these for live prices, fundamentals, and market data |
| 2 (secondary) | **statusinvest / Fundamentus** | statusinvest.com.br/acoes/{ticker} · fundamentus.com.br | Direct access, no registration |
| Primary-source filings | **CVM (RAD portal)** | www.rad.cvm.gov.br | ITR (quarterly) / DFP (annual) / release financials |
| Company IR | **RI (Relações com Investidores) sites** | Each issuer's investor-relations site | Earnings releases, presentations, reference forms |
| Market data | **B3** | www.b3.com.br | Prices, share counts, indices |

Notes for Brazil:

1. **Currency is the Brazilian Real (BRL, R$)** — always label it explicitly. When mixing with USD/EUR figures, state the FX date and convert to one currency before cross-market comparison.
2. **Filings via CVM**: Brazilian issuers file the ITR (quarterly information) and DFP (standardized annual financial statements) through the CVM RAD portal. These are the primary-source documents; company earnings releases (divulgação de resultados) on the RI site are useful but always reconcile to the CVM filing.
3. **Statutory vs adjusted / "recorrente"**: Brazilian companies frequently report both statutory (IFRS) and adjusted "recurring" EBITDA/earnings. Discrepancies between data providers are often due to this. Always note which basis a figure uses (see discrepancy rules below).
4. **Preferred vs ordinary shares**: Many B3 tickers exist as ON (ordinary, e.g., PETR3) and PN (preferred, e.g., PETR4), plus Units (e.g., SANB11). Be explicit about which class you are using, and remember market cap must sum across all classes, not just one ticker.

### US-listed ADRs (e.g., PBR/PBR.A for Petrobras, VALE for Vale, ITUB for Itaú, ABEV for Ambev)

| Priority | Source | URL | How to access |
|----------|--------|-----|---------------|
| 1 (primary) | **MCP market-data tools** | market-data server + finnhub | Live ADR quotes and fundamentals |
| 2 (secondary) | **macrotrends / stockanalysis** | macrotrends.net/stocks/charts/{ticker} · stockanalysis.com/stocks/{ticker}/financials | Direct access, no registration |
| Primary-source filings | **SEC EDGAR** | sec.gov/cgi-bin/browse-edgar | 20-F (annual) / 6-K (interim) originals |

Notes for ADRs:

1. Cross-check ADR figures against the local B3 shares. Mind the **ADR ratio** (e.g., 1 PBR ADR = 1 PETR4 share for Petrobras; confirm the ratio per issuer as it varies) and the **BRL/USD FX rate** applied.
2. ADR fundamentals reported to the SEC (20-F) are in USD; local CVM filings are in BRL. Reconcile currency before comparing.
3. For live financial and market data, the analyst has **MCP market-data tools available (a market-data server and finnhub), plus WebSearch/WebFetch** — prefer those over any scraper.

---

## Execution Standard

### Step 1: Obtain the data

For each financial metric (revenue, net income, gross margin, operating cash flow, leverage ratio, etc.), pull the figure separately from **Source 1** and **Source 2**.

### Step 2: Discrepancy calculation and flagging

```
discrepancy % = |Source 1 value − Source 2 value| / Source 1 value × 100%
```

| Discrepancy | Handling |
|-------------|----------|
| ≤ 1% | ✅ Consistent — use the Source 1 value, cite both sources |
| 1% – 5% | ⚠️ Flag "data discrepancy" — state both values and explain the likely cause (FX / accounting basis) |
| > 5% | ❌ Flag "material discrepancy" — must verify against the primary filing, do not use the figure directly |

### Step 3: Data presentation format

Every key data point must be annotated in the following format:

```
Revenue: R$ 123.9 bn ✅
  - statusinvest: R$ 124.1 bn
  - finnhub: R$ 123.7 bn
  - discrepancy: 0.3%
```

Discrepancy example:

```
Net income: R$ 24.5 bn ⚠️ data discrepancy
  - CVM filing (IFRS statutory): R$ 24.5 bn
  - provider (adjusted/recurring): R$ 27.8 bn
  - discrepancy: 13.5% — cause: different basis (statutory vs recurring)
```

---

## Common Causes of Discrepancy (not necessarily errors)

| Cause | Explanation |
|-------|-------------|
| Statutory (IFRS) vs adjusted/recurring | Most common, especially for profit and EBITDA figures |
| FX conversion | BRL/USD converted at different points in time |
| Fiscal-year definition | Calendar year vs fiscal year |
| Consolidation basis | Whether minority interest is included |
| Data update lag | A platform has not yet updated the latest reporting period |

---

## Special Rules

1. **Private / unlisted companies**: when only one primary source exists, prefix the figure with `[estimate]` and do not run cross-verification.
2. **Quarterly vs annual data**: prefer annual data for cross-verification; some providers lag on quarterly figures.
3. **Primary filing wins**: if both sources disagree with the primary filing (20-F / DFP / annual report PDF), the primary filing prevails — flag the sources as erroneous.

---

## Price and Adjustment (mandatory for historical series)

Prices come in three bases; mixing them distorts historical price levels, long-run returns, and historical valuation percentiles:

| Basis | Meaning | Use |
|-------|---------|-----|
| Unadjusted | Actual traded price, gaps down on ex-dividend/ex-rights dates | "Current point-in-time" snapshot only |
| Back-adjusted (forward) | Historical prices adjusted to the latest price as the reference | Historical price comparison, N-year return, historical PE bands — always use this |
| Forward-adjusted | Adjusted forward from the first listing day as reference | Computing historical total return / annualized return |

Rules:

1. Any analysis involving historical prices uses **back-adjusted** prices consistently, and must **never mix** adjusted and unadjusted sources within the same analysis.
2. Current market cap / current PE use **current actual price × current total share count** — unrelated to adjustment; adjustment only affects the historical series.
3. Per-share metrics that span splits or large stock dividends/bonus issues (historical EPS, historical price) must be adjustment-restated before year-over-year comparison.
4. Total return / annualized return must include dividends (forward-adjusted already accounts for them); looking at price appreciation alone understates it.
5. Post-issuance/buyback market-cap checks use the latest total share count (`financial_rigor.py verify-market-cap` flags a deviation >5% for review).

---

## Quick Index

| Scenario | Primary source | Backup source |
|----------|----------------|---------------|
| Petrobras (PETR4 / PETR3) | MCP market-data tools | statusinvest.com.br/acoes/petr4 · CVM RAD |
| Petrobras ADR | macrotrends.net/stocks/charts/PBR | stockanalysis.com/stocks/pbr · SEC 20-F |
| Vale (VALE3) | MCP market-data tools | statusinvest.com.br/acoes/vale3 · CVM RAD |
| Vale ADR | macrotrends.net/stocks/charts/VALE | stockanalysis.com/stocks/vale · SEC 20-F |
| Itaú Unibanco (ITUB4) | MCP market-data tools | statusinvest.com.br/acoes/itub4 · CVM RAD |
| Banco do Brasil (BBAS3) | MCP market-data tools | fundamentus.com.br · CVM RAD |
| WEG (WEGE3) | MCP market-data tools | statusinvest.com.br/acoes/wege3 · CVM RAD |
| Ambev (ABEV3) | MCP market-data tools | statusinvest.com.br/acoes/abev3 · CVM RAD |
| Ambev ADR | macrotrends.net/stocks/charts/ABEV | stockanalysis.com/stocks/abev · SEC 20-F |
