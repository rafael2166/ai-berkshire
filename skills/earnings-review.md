# Earnings Review: Deep Reading of Primary Sources

Perform a deep earnings review of `$ARGUMENTS`.

**Supported input formats**: `Company Quarter`, e.g. `Petrobras 2025Q4`, `Vale 2025 Annual Report`, `Itau latest` (defaults to the most recent period).

> "I never read sell-side research; I only read the original filings." — Li Lu
>
> "I read 500 pages a day. That's how knowledge builds up, like compound interest." — Warren Buffett

## Design Philosophy

Most AI investment-research tools rely on secondhand information (news, research-note summaries, data websites). But the core skill of Buffett and Li Lu is **reading primary sources** — annual reports, quarterly reports, and earnings-call transcripts.

Problems with secondhand information:
- It has been filtered — analysts selectively present the data that supports their view.
- It lags — by the time others have digested it, the alpha is gone.
- It lacks context — "revenue grew 15%" is stripped of management's discussion of the quality of that growth.

This Skill reads primary sources directly, focusing on what Buffett and Li Lu actually look at.

Default market is Brazil / B3. Default tickers are B3 (e.g. PETR4, VALE3, ITUB4, BBAS3, WEGE3, ABEV3). Currency is BRL (R$); state it explicitly and note USD ADRs where relevant.

## Execution Flow

### Prerequisite: Source Availability Rating

| Grade | Characteristics | Impact |
|-------|-----------------|--------|
| A | Complete original filing obtained (annual/interim report, earnings-call transcript) | Execute all steps normally |
| B | Only partial original text or a third-party summary obtained | Flag as "not a primary source"; reduce the weight of footnote analysis |
| C | Only news reports and data-website summaries available | Focus on core financial-data changes, skip footnote mining, flag as "insufficient primary sources" |

### Step 1: Obtain Primary Sources

Use the Task tool to launch multiple background Agents **in parallel** to obtain the following raw materials:

1. **Original filing**: from the company's Investor Relations (RI) site, CVM via the RAD portal (www.rad.cvm.gov.br) for Brazilian issuers, and the SEC (EDGAR) for US-listed ADRs. Market data via B3.
2. **Earnings-call transcript / recording**: from the company's RI site, earnings-call providers, and reputable financial-news sources.
3. **Management letter to shareholders** (if an annual report): read in full.
4. **Investor Day / analyst-day materials** (if recently held).

The analyst also has MCP market-data tools available (a market-data server plus finnhub) as well as WebSearch/WebFetch; prefer those for pricing, fundamentals, and filings discovery.

If the complete original filing cannot be obtained, follow the `skills/financial-data.md` conventions and assemble the data from standard sources (Brazilian equities: company RI + B3 + CVM disclosures, complemented by reputable financial-data providers; US ADRs: SEC filings + market-data providers). Always flag "not the original filing; assembled from third-party summaries", and mark any key figure whose two sources disagree by more than 1%.

### Step 2: Extract and Verify Core Financial Data

#### 2.1 Income Statement

| Metric | Current | Prior | YoY Change | Management Guidance | On Target? |
|--------|---------|-------|-----------|---------------------|-----------|

Must cover:
- Total revenue plus a breakdown by segment/geography.
- Gross profit and change in gross margin.
- Operating profit and change in operating margin (distinguish GAAP/IFRS from non-GAAP/adjusted).
- Net income (watch for the impact of non-recurring items).
- EPS (basic vs. diluted).

#### 2.2 Cash Flow Statement (Buffett's Top Priority)

| Metric | Current | Prior | Change | Watch For |
|--------|---------|-------|--------|-----------|

Must cover:
- Operating cash flow vs. net income ratio (>100% is good, <80% warrants caution).
- Capital expenditure and its composition (maintenance vs. expansion).
- Free cash flow = operating cash flow − capex.
- Buybacks and dividends paid.
- Ending cash and equivalents balance.

#### 2.3 Balance-Sheet Health

Must cover:
- Cash + short-term investments vs. interest-bearing debt.
- Trend in net cash / net debt.
- Change in days sales outstanding (is the company loosening credit terms to pump revenue?).
- Change in days inventory outstanding (is inventory piling up?).
- Goodwill and intangibles as a share of assets (any impairment risk?).

**Data verification**: use `tools/financial_rigor.py` to check key figures.

```bash
# Cross-validate revenue and net income (at least 2 sources)
python3 tools/financial_rigor.py cross-validate \
  --metric "revenue" --values 108.3e9 107.9e9 --sources "Company filing" "Market-data provider"

# Market-cap check
python3 tools/financial_rigor.py verify-market-cap \
  --price 38.5 --shares 12.9e9 --reported 4.97e11 --currency BRL

# Valuation-metric check
python3 tools/financial_rigor.py verify-valuation \
  --price 38.5 --eps 6.2 --bvps 22.4 --fcf-per-share 5.1
```

### Step 3: Deep Reading of the Management Discussion (MD&A)

This is where Buffett and Li Lu spend the most time. It is not about the numbers — it is about **listening to how management talks**.

#### 3.1 Management-Tone Analysis

Read the management discussion / earnings-call remarks paragraph by paragraph, flagging the following signals:

| Signal Type | Manifestation | Example |
|-------------|---------------|---------|
| 🟢 **Candor signal** | Proactively admits problems, gives specific reasons | "Margins fell this quarter mainly because our investment in X exceeded plan" |
| 🟢 **Clarity signal** | Concrete strategy statements with quantified targets | "We plan to raise X's market share from 15% to 20% over the next 12 months" |
| 🔴 **Vagueness signal** | Heavy use of "we believe", "over the long term", and other content-free phrases | "We are confident about the future" |
| 🔴 **Deflection signal** | Dodges the direct question, changes the subject | Asked about margins, pivots to revenue growth |
| 🔴 **Externalizing blame** | Blames everything on macro/industry/competitors | "Owing to the macro environment..." |

#### 3.2 Promise Tracking

Extract management's specific commitments from the prior earnings report / call and compare them against actual results this period:

| Prior Commitment | Actual This Period | Assessment |
|------------------|--------------------|------------|
| "Margins will recover to X% in H2" | Actual Y% | ✅ Met / ❌ Missed / ⚠️ Partially met |

**Duan Yongping**: "The simplest way to judge whether a management team is reliable is to check whether they did what they said they would."

#### 3.3 Key-Question Identification

Extract the sharpest analyst questions from the Q&A and rate the quality of management's answers:

| Analyst Question | Management Answer | Answer Quality (1-5) | Evasive? |
|------------------|-------------------|:--------------------:|:--------:|

### Step 4: Mining Footnotes and Hidden Information

The footnotes hide information management would rather you not find easily:

#### 4.1 Mandatory Footnote Checks

- [ ] **Related-party transactions**: are the terms with major shareholders / affiliates fair?
- [ ] **Share-based compensation**: how large is the dilution from options/RSUs? What is the strike price?
- [ ] **Contingent liabilities**: litigation, guarantees, commitments, and other off-balance-sheet risks.
- [ ] **Accounting-policy changes**: any change to revenue recognition, depreciation lives, etc.?
- [ ] **Segment information**: margin differences across segments — is a "good business subsidizing a bad one"?
- [ ] **Customer/supplier concentration**: share of the top five customers/suppliers.

#### 4.2 Anomaly Detection

- [ ] Receivables growth > revenue growth (possible channel stuffing).
- [ ] Inventory growth > revenue growth (possible pile-up).
- [ ] Operating cash flow < net income with a widening gap (earnings quality in doubt).
- [ ] Sudden increase in capitalized expenditure (possible earnings dressing).
- [ ] Sudden rise in the share of non-recurring gains.

### Step 5: Comparison Against Historical Data

#### 5.1 Trend Analysis

Place this period's key metrics into a time series of at least 4 quarters (or 3 years of annual reports):

| Metric | Q-4 | Q-3 | Q-2 | Q-1 | Current | Trend |
|--------|-----|-----|-----|-----|---------|-------|

Key focus:
- Are margins improving or deteriorating?
- Is revenue growth accelerating or decelerating?
- Is cash-flow quality rising or falling?
- Is capex intensity increasing or decreasing?

#### 5.2 Comparison Against Management Guidance

| Metric | Prior Management Guidance | Actual Result | Deviation | Interpretation |
|--------|---------------------------|---------------|-----------|----------------|

### Step 6: Produce the Earnings-Review Report

#### Report Structure

```
1. Core data at a glance (one-page table)
2. The 3 most important changes this period (under 500 words)
3. Management tone and promise tracking
4. Hidden information in the footnotes
5. Key questions (selected earnings-call Q&A)
6. Relationship to the investment thesis (if held)
7. Conclusion: what did this report change?
```

#### The Conclusion Must Clearly Answer

1. **Was this report a beat, in line, or a miss?** (No hedging "broadly in line" followed by a list of both-sides talking points.)
2. **Impact on the investment thesis**: reinforces / no impact / weakens / breaks it.
3. **What is the next catalyst to watch?**
4. **If you already hold, should you add / hold / trim?**

### Step 7: Save the Report

Write the report to `reports/{Company}/{Company}-earnings-{Period}.md`, e.g. `reports/Petrobras/Petrobras-earnings-2025Q4.md`. Use English/latin folder names.

### Step 8: Data Spot-Check (Release Gate)

After writing the report, run the data spot-check; it must pass before release:

```bash
# Step 1 — extract the spot-check list
python3 tools/report_audit.py extract \
  --report reports/{Company}/{Company}-earnings-{Period}.md

# Step 2 — for each item, pull the figure from a reliable source (see skills/financial-data.md)

# Step 3 — output the pass/return verdict
python3 tools/report_audit.py verdict \
  --results '<completed JSON>' \
  --report {report filename}
```

**[PASS]** all items pass → release; **[RETURN]** any item fails → fix and re-audit.

## Key Principles

- **Read the original, not the summary**: obtain primary sources by every means possible.
- **Watch changes, not absolute levels**: the trend matters more than the number itself.
- **Listen to the tone, not just the content**: how management says it matters as much as what they say.
- **Check the footnotes, not just the body**: the devil is in the details.
- **Deliver a conclusion, not a recap**: the point of a deep read is to form a judgment, not to restate the filing.
- **Objectivity**: base everything on facts and data; separate fact from opinion; present both sides; cite sources (at least 2 for key data); be honest about uncertainty. All output reports are written in English.
