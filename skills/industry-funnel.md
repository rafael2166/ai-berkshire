# Industry Funnel Screening: A Value-Investing Selection Process from the Whole Market to 3 Names

Run a funnel-style value-investing screen on the $ARGUMENTS industry / theme, narrowing from a whole-market scan down to 3 final names, layer by layer.

## When to Use

When you name an industry or investment theme (e.g., "AI compute", "innovative drugs", "robotics") and want to:
1. Miss no important target (including B3 / Brazil, US-listed, and private IPO candidates)
2. Use a uniform standard to filter out "story stocks" and companies of insufficient quality
3. Focus your energy on the 3 leaders truly worth deep research
4. Have clear keep/discard criteria at each layer, so the process is reviewable and traceable

Difference from `industry-research`:
- `industry-research` emphasizes value-chain structure and panorama, slicing by segment
- `industry-funnel` emphasizes the stock-selection funnel, narrowing from the whole market to 3 names layer by layer

The two are complementary: first use `industry-research` to understand the value-chain landscape, then use `industry-funnel` to select targets.

---

## Funnel Structure Overview

```
Layer 1: whole-market scan     30-60 names   (union of activity + gainers + top 30 by market cap)
        ↓ 5 hard value-investing metrics
Layer 2: coarse screen         ≤ 10 names    (all 5 metrics pass + moat ★★★ or above)
        ↓ detailed analysis
Layer 3: detailed analysis     ≤ 10 names    (300-500 words of structured analysis each)
        ↓ final selection
Layer 4: four-masters deep dive  3 names      (800-1200 words each, Buffett-Munger-Duan-Li views)
        ↓
Output: investment recommendation + trade signals + position sizing
```

Every "filtered-out target" at each layer must have a documented reason for elimination — no black box.

---

## Step 1: Whole-Market Scan Entry

### 1.1 Active-Stock Definition (union of three categories)

**Category A - Trading Activity**:
- Top-ranked by 30-day average daily turnover within the industry (take the top 30 each for B3 / Brazil and US markets)

**Category B - Gainers List**:
- Top 20 by 30-day price gain
- Top 20 by 90-day price gain
- The union of the two

**Category C - Market-Cap Anchor**:
- Top 30 by market cap within the industry (regardless of price move)

Final scan pool = A ∪ B ∪ C, expected 30-60 names.

### 1.2 Markets That Must Be Searched

| Market | Suggested Sources |
|--------|-------------------|
| B3 (Brazil) | B3 sector indices / listings, company RI (Investor Relations) sites |
| US-listed | NYSE / NASDAQ sector ETF holdings, including Brazilian ADRs |
| International markets | Do not miss relevant companies in Europe, Japan, and the rest of Latin America (especially in mining, oil & gas, and agribusiness supply chains) |
| Private companies | List a separate "future IPO candidates" subsection, noting latest valuation and potential IPO timing |

Prefer the analyst's MCP market-data tools (market-data server + finnhub) plus WebSearch / WebFetch for this data.

### 1.3 Output Format

| Company | Ticker | Market | Market Cap | One-Line Core Business | Industry Exposure % | Selection Category (A/B/C) |
|---------|--------|--------|------------|------------------------|---------------------|----------------------------|

**Key self-check**:
- Be cautious with "tangential" names whose industry exposure is < 30%; flag them "not a pure play"
- Don't miss Brazilian / Latin American names just because there is less English-language material
- Don't miss small-caps just because AI prefers leaders

---

## Step 2: 5 Hard Value-Investing Metrics — Coarse Screen → ≤ 10 Names

Apply the 5 hard metrics to each of the 30-60 companies from Step 1.

### 2.1 The 5 Hard Metrics

| # | Metric | Pass Threshold | Relaxation Condition | Data Source |
|---|--------|----------------|----------------------|-------------|
| 1 | P/E valuation | Reasonable (vs. historical range and peers) | High growth may relax to PEG < 1.5 | Filings + market data |
| 2 | ROE | > 15% or improving 3-year trend | Capital-intensive industries may relax | Filings |
| 3 | Operating cash flow | Positive and > 70% of net income | — | Filings |
| 4 | Debt-to-assets | < 60% | Utilities / power may relax to 70% | Filings |
| 5 | Quick moat read | ★★★ or above | — | Qualitative judgment |

Filings are sourced from CVM via the RAD portal (www.rad.cvm.gov.br) and company RI sites (and SEC for US-listed ADRs). Market data via B3.

**The 5 moat types**:
- Brand / pricing power
- Switching costs / user stickiness
- Network effects
- Economies of scale
- Technology / license / resource barriers

### 2.2 Output Format

| Company | P/E | ROE | Cash Flow / Net Income | Debt Ratio | Moat | Overall | Keep/Discard | Elimination Reason |
|---------|-----|-----|------------------------|------------|------|---------|--------------|--------------------|

**Retention rules**:
- All 5 metrics pass → keep directly
- 4 pass + 1 close → keep but flag yellow
- Fewer than 4 pass → eliminate, note the reason

**Target**: keep ≤ 10 names. If too many are kept (> 12), raise the moat standard to ★★★★ and screen once more.

---

## Step 3: Detailed Analysis (≤ 10 names, 300-500 words each)

For the companies kept after the coarse screen, do a structured analysis of each.

### 3.1 Per-Company Analysis Template

```
## {Company} ({Ticker})

**One-line business model**:
(what it sells, to whom, how it makes money)

**Financial quality**:
- Revenue growth / profit growth / gross margin / ROE / cash flow
- Key change (the most important financial turning point of the last 1-2 years)

**Moat depth**:
- Primary moat type + specific evidence
- Brief judgment on whether the moat will still exist in 5 years

**Main risks (top 3)**:
1.
2.
3.

**Valuation quick take**:
- Current P/E / P/S / EV/EBITDA + position within historical range
- Peer comparison
- One-line verdict: expensive / fair / cheap

**Advance to the final 3?**: Yes / No (reason)
```

### 3.2 Selection Criteria for the Final 3

Do not simply rank by score and take the top 3; select by "portfolio complementarity":
- At least 1 "high-certainty, low-beta" name (Buffett type)
- At least 1 "medium-certainty, medium-beta" name (growth type)
- Optionally 1 "high-beta, high-risk" name (option type)

If a given sub-theme cannot yield 3 sufficiently good names, prefer to write "final 2 + 1 on watch" rather than pad the list.

---

## Step 4: Four-Masters Deep Dive (3 names, 800-1200 words each)

Run a four-masters deep-dive analysis on the final 3.

### 4.1 Duan Yongping View: Business Essence

- Define in one sentence what business this company is in
- Is it a good business? Why?
- What is its "honest core" (benfen)? Has management drifted from it?
- Where is the "durability" of the business model?

### 4.2 Buffett View: Moat Depth

- Score using the five moat types (★1-5), with specific evidence
- Will the moat still be there in 10 years?
- Where is the "margin of safety" for buying now?

| Moat | Strength | Specific Evidence |
|------|----------|-------------------|
| Brand / pricing power | | |
| Switching costs | | |
| Network effects | | |
| Economies of scale | | |
| Technology / license barriers | | |

### 4.3 Munger View: Risk and Failure Modes

- How is this company most likely to fail? (list the top 3 failure paths)
- What is it worth in the worst case? (minimalist valuation)
- Why don't smart people buy it? (inversion)
- Are there ethical / compliance / management risks?

### 4.4 Li Lu View: Civilizational-Trend Positioning

- Is this company's arena a "civilization-level paradigm shift" or a "temporary fad"?
- The closest historical analogy of a technology revolution?
- What is this company's endgame in 10-20 years?
- Is it a winner-take-all structure?

### 4.5 Overall Recommendation Level

```
Recommendation: ★★★★☆
Position type: core / satellite / option / watch
Suggested buy range: current price / pullback of N% / wait patiently
Suggested position size: X% of this theme's allocation
Key monitoring metric: (what signal would flip this company's thesis)
```

---

## Step 5: Integrated Output

Consolidate at the end of the report:

### 5.1 Final 3 Portfolio Table

| Company | Type | Recommendation | Suggested Position | Core Logic | Key Risk |
|---------|------|----------------|--------------------|------------|----------|
| A | Core | ★★★★★ | 50-60% | | |
| B | Satellite | ★★★★☆ | 25-35% | | |
| C | Option | ★★★☆☆ | 5-15% | | |

### 5.2 Industry-Level ETF Alternative

For those who don't want to pick stocks, list 1-3 relevant ETFs (B3 / Brazil, US).

### 5.3 Overall Industry Positioning Judgment

- Industry P/E / P/B historical percentile
- Fund flows (foreign flows, ETF creations/redemptions, sell-side coverage density)
- Whether the industry as a whole is in "early / expansion / mature / decline" stage

### 5.4 Information-Sufficiency Self-Assessment (required)

| Dimension | Grade | Notes |
|-----------|-------|-------|
| Completeness of company financials | A/B/C | |
| Timeliness of valuation data | A/B/C | |
| Judgment of industry landscape | A/B/C | |
| Management information | A/B/C | |

A = data sufficient and reliable; B = partially missing but does not affect the main conclusion; C = substantially missing, conclusion requires caution.

### 5.5 Data Points to Update

Explicitly list: which data are estimates, which data need later verification, and which quarter's filings should be tracked closely.

### 5.6 Source List

The source link for each data point / conclusion, listed by category (filings, research reports, news, industry reports).

---

## AI Research-Bias Awareness (Important)

Traps AI easily falls into during funnel screening:

| Bias | Manifestation | Countermeasure |
|------|---------------|----------------|
| Leader preference | Large-caps have more material and longer analysis, so they look "better" | Score by hard metrics and moat, not by report length |
| English-language preference | US material is abundant, so Brazilian / B3 names are easily underestimated | Search both Portuguese and English; don't miss B3 / ADR names |
| Story preference | High price gains + media buzz = a better-looking "AI concept stock" | Distinguish "AI revenue share" vs. "AI story share"; look at the real business |
| Present-bias | Companies with good current financials are easily selected, possibly missing turnaround dark horses | The Layer-2 coarse screen allows "improving trend" as a relaxation condition |
| Listed-company preference | Looking only at listed companies may miss the best players in the arena | You must list "future IPO candidates" and flag valuation and timing window |

---

## Output Requirements

1. **Report location**: `reports/{Industry}-funnel-{YYYYMMDD}.md` (industry reports go in the reports/ root; use English / Latin names)
2. **Language**: English — write the report in English
3. **Style**: direct, sharp, no filler
4. **Data**: cite the source of all data; label estimates "estimate"
5. **No preset stance**: first present data → derive logic → reach conclusion
6. **Both sides**: attach counter-evidence to every core judgment
7. **Keep elimination records at each layer**: eliminated companies keep their name + reason

---

## Data Spot-Check (Release Gate)

After the report is written, run a data spot-check; only a pass allows publication:

```bash
# Step 1 — Extract the spot-check list (15% random sample)
python3 tools/report_audit.py extract \
  --report <report file path>

# Step 2 — For each item on the list, pull data from a reliable source (see skills/financial-data.md)

# Step 3 — Output the pass / reject verdict
python3 tools/report_audit.py verdict \
  --results '<filled-in JSON>' \
  --report <report file name>
```

**[PASS]** All items pass → the report may be published; **[REJECT]** Any item fails → fix and re-review.

---

## Follow-Up Actions

After the funnel selects the final 3, you can run the following individually on each:
- `/investment-team` — full parallel four-masters deep research (independent subdirectory + 5 documents)
- `/investment-checklist` — run the Buffett pre-buy checklist end to end
- `/management-deep-dive` — in-depth management research

`industry-funnel` is the entry point; the follow-up skills are the deep dig.
