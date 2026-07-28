# Thesis Tracker: The Post-Purchase Discipline System

Run an investment thesis tracking check on $ARGUMENTS.

**Supported input formats**:
- `CompanyName` — on first use, build the investment thesis; on later uses, run a tracking check
- `CompanyName build thesis` — force a rebuild of the investment thesis
- `CompanyName quarterly check` — run a thesis check based on the latest earnings

> "Buying is only the beginning. The real work is continuous tracking during the holding period." — Li Lu
>
> "When the facts change, I change my mind. What do you do?" — Keynes

## Design Philosophy

Most investors follow this process: research → buy → pray. They lack systematic post-purchase tracking, which leads to:
- Not selling when you should ("just wait a bit longer, it'll come back")
- Panic-selling when you shouldn't ("it dropped 20%, was I wrong?")
- Forgetting why you bought in the first place ("why did I buy this again?")

Buffett's and Li Lu's approach: **write down the sell conditions before you buy**. Then check every quarter whether the thesis still holds.

## Execution Flow

### Step 1: Determine the operating mode

Check whether an investment thesis file already exists for this company (`reports/{Company}/{Company}-thesis.md`):
- If it does not exist → enter **Build Thesis** mode
- If it exists → enter **Tracking Check** mode
- If it can't be found but the user says one exists → ask for the file path

---

## Mode A: Build the Investment Thesis

### A0: Data Collection

Prefer the analyst's MCP market-data tools (market-data server + finnhub) and WebSearch/WebFetch to gather the current share price, valuation metrics (P/E, P/B, dividend yield), and the latest core earnings figures, to populate the valuation anchors. Default tickers are B3-listed (e.g., PETR4, VALE3, ITUB4, BBAS3, WEGE3, ABEV3); state currency explicitly as BRL (R$), and note the USD figure for any US-listed ADR. Filings come from CVM via the RAD portal (www.rad.cvm.gov.br) and company investor-relations (RI) sites; market data via B3 (and SEC for US-listed ADRs). If a `/investment-research` or `/investment-team` report already exists for this company, read from it first.

Use `tools/financial_rigor.py verify-valuation` to validate the valuation data.

### A1: Core Thesis (must fit within 200 words)

The investment thesis must answer the following 5 questions, one sentence each:

```
I bought ___ (company) at R$___, because:
1. The essence of this business is ___, and I understand how it makes money
2. Its moat is ___, and it is widening / stable
3. Management is ___, and the reason they can be trusted is ___
4. The current price is a ___ discount to intrinsic value; the margin of safety comes from ___
5. Even if I'm wrong, the downside is limited, because ___
```

**If you can't write these 5 sentences completely, the thesis itself has a problem — it means the buy decision wasn't clear enough.**

### A2: Core Assumptions List

Break the thesis into specific, verifiable assumptions:

| # | Core Assumption | Verification Method | Frequency | Current Status |
|---|-----------------|---------------------|-----------|----------------|
| 1 | e.g., Revenue growth stays 15%+ | Quarterly revenue growth | Quarterly | 🟢 Holds |
| 2 | e.g., Gross margin stable at 60%+ | Quarterly gross margin | Quarterly | 🟢 Holds |
| 3 | e.g., Management keeps buying back stock | Buyback announcements / cash flow statement | Quarterly | 🟢 Holds |
| 4 | e.g., Competitors make no breakthrough | Industry data / competitor earnings | Semi-annually | 🟢 Holds |
| 5 | ... | ... | ... | ... |

Usually 3-7 assumptions. Too few means the thinking isn't deep enough; too many means the thesis isn't focused enough.

### A3: Red Lines List (triggering any one = mandatory reassessment)

| # | Red Line Condition | Severity | Action if Triggered |
|---|--------------------|----------|---------------------|
| 1 | e.g., Management integrity failure (accounting fraud, self-dealing) | Fatal | Liquidate immediately |
| 2 | e.g., Core business revenue declines for 2 consecutive quarters | Severe | Cut position 50%, reassess |
| 3 | e.g., Moat clearly breached (competitor gains equal capability) | Severe | Launch deep research, consider exit |
| 4 | e.g., Regulation fundamentally changes the business model | Severe | Reassess intrinsic value |
| 5 | e.g., Large-scale insider selling (unplanned) | Warning | Investigate the reason thoroughly |

**Duan Yongping**: "There are only three reasons to sell: 1. you realize you bought wrong; 2. the company's fundamentals have changed; 3. you found something better."

### A4: Valuation Anchors

| Metric | At Purchase | Optimistic Target | Base Target | Pessimistic Scenario |
|--------|-------------|-------------------|-------------|----------------------|
| Share price (R$) | | | | |
| P/E | | | | |
| Market cap (R$) | | | | |
| Intrinsic value estimate (R$) | | | | |
| Margin of safety | | | | |

### A5: Save the Thesis

Write the investment thesis to `reports/{Company}/{Company}-thesis.md`, including:
- Date established
- Purchase price and position size
- Core thesis (5 sentences)
- Core assumptions list
- Red lines list
- Valuation anchors
- Tracking record table (initially empty)

---

## Mode B: Tracking Check

### B1: Read the Existing Thesis

Read `reports/{Company}/{Company}-thesis.md` and load:
- Core thesis
- Core assumptions list
- Red lines list
- Last check record

### B2: Collect the Latest Data

Using the analyst's MCP market-data tools (market-data server + finnhub) and WebSearch/WebFetch, collect:
1. Latest earnings data (if there is a new quarterly/annual report — from CVM via the RAD portal and the company's RI site)
2. Recent major events (management changes, regulatory policy, competitive dynamics)
3. Current share price and valuation metrics (via B3; and SEC for any US-listed ADR)
4. Insider transaction records (controlling-shareholder buys/sells)

### B3: Check Each Core Assumption

For each core assumption, verify against the latest data:

| # | Core Assumption | Last Status | Latest Evidence | Current Status | Change |
|---|-----------------|-------------|-----------------|----------------|--------|
| 1 | Revenue growth 15%+ | 🟢 Holds | Q4 revenue growth 12% | 🟡 Marginal weakening | ⚠️ |
| 2 | Gross margin 60%+ | 🟢 Holds | Gross margin 61.2% | 🟢 Holds | — |
| 3 | ... | ... | ... | ... | ... |

Status definitions:
- 🟢 **Holds** — the latest data supports the assumption
- 🟡 **Marginal weakening** — data is still within an acceptable range, but the trend is unfavorable
- 🔴 **Impaired** — the data clearly does not support the assumption
- ⚫ **Broken** — the assumption has been overturned

### B4: Red Line Check

Check each red line in turn:

| # | Red Line Condition | Triggered? | Evidence |
|---|--------------------|:----------:|----------|
| 1 | Management integrity problem | ❌ Not triggered | — |
| 2 | Core business declines 2 consecutive quarters | ❌ Not triggered | — |

**If any red line is triggered → flag it prominently in the report and give a clear action recommendation.**

### B5: Valuation Update

| Metric | At Purchase | Last Check | Current | Change |
|--------|-------------|------------|---------|--------|
| Share price (R$) | | | | |
| P/E (TTM) | | | | |
| Intrinsic value estimate (R$) | | | | |
| Margin of safety | | | | |

### B6: Output the Tracking Report

#### Report Structure

```
1. Thesis health score (out of 10)
2. Core assumption check results (table)
3. Red line check results (table)
4. Key changes this period (under 500 words)
5. Valuation update
6. Conclusion and action recommendation
7. Key items to watch at the next check
```

#### Thesis Health Score Standard

**Formula**: Health = 10 − (⚫ broken assumptions × 3) − (🔴 impaired assumptions × 2) − (🟡 weakened assumptions × 1) − (red lines triggered × 5), floored at 1 and capped at 10.

| Score | Meaning | Recommended Action |
|:-----:|---------|--------------------|
| 9-10 | All assumptions hold; thesis stronger than at purchase | Consider adding |
| 7-8 | Core assumptions hold; a few marginally weakened | Continue holding |
| 5-6 | 1-2 assumptions impaired, but core logic unchanged | Hold, but raise vigilance |
| 3-4 | Multiple assumptions impaired; thesis foundation shaken | Consider trimming |
| 1-2 | Red line triggered or core assumption broken | Strongly recommend selling |

#### The Conclusion Must Clearly Answer

1. **Is the thesis still intact?** Intact / marginally weakened / impaired / broken
2. **What should you do?** Add / hold / trim / liquidate
3. **Next check timing**: after the next earnings release / after a specific event

### B7: Update the Thesis File

Append this check to the tracking record table in `reports/{Company}/{Company}-thesis.md`:

| Check Date | Health | Key Changes | Action Recommendation |
|------------|:------:|-------------|-----------------------|
| 2026-04-09 | 7/10 | Revenue growth slowed to 12%, but margins improved | Hold |

---

## Key Principles

- **Write the sell conditions before you buy** — decisions made when calm beat decisions made in panic
- **The thesis must be specific enough to verify** — "the company is great" is not a thesis; "ROE > 25% with a stable trend" is
- **Act the moment a red line triggers** — the deadliest habit is "let's wait and see," which is where big losses begin
- **A broken thesis ≠ a falling share price** — a 30% price drop doesn't necessarily mean sell; a broken thesis does
- **Face mistakes honestly** — if the thesis was built wrong, admit it; don't cling to it to save face
