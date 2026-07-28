# Industry Investment Research: Value-Chain Panorama + Four-Masters Stock Analysis Framework

Conduct systematic value-chain investment research on the $ARGUMENTS industry.

## Research Objectives

Starting from an investment theme / logic chain, complete the following:
1. Validate every link in the investment logic chain
2. Map the complete value-chain panorama
3. Scan all listed companies globally (B3 / Brazil, US, and other international markets)
4. Run the four-masters framework analysis on the leading companies in each sub-segment
5. Deliver industry-level portfolio allocation recommendations

---

## Step 1: Building and Validating the Investment Logic Chain

### 1.1 Draw the Logic Chain
Use an arrow chain to express the causal relationship from "underlying trend" to "beneficiary target", for example:
```
Underlying trend A
    → drives demand B
        → creates bottleneck / hard demand C
            → benefits value chain D
```

### 1.2 Validate Link by Link
Challenge every arrow in the logic chain and look for evidence:

| Link | Core Assumption | Validation Method | Data Source |
|------|-----------------|-------------------|-------------|
| A→B | | Search industry data / forecasts | |
| B→C | | Search supply-demand analysis | |
| C→D | | Search real cases / signed contracts | |

### 1.3 Look for "Validation Events That Have Already Happened"
List the **real, already-signed / already-executed business events** that support the logic chain (not forecasts), for example large-company procurement agreements, policy documents, industry reports, etc.

---

## Step 2: Mapping the Value-Chain Panorama

### 2.1 Draw the Value-Chain Structure
Break the industry into upstream → midstream → downstream → supporting segments, for example:
```
Upstream: raw materials / resource extraction → material processing / refining
Midstream: core equipment manufacturing → systems integration / engineering & construction → new-technology R&D
Downstream: operations / services → end customers
Supporting: testing / certification → maintenance services → financial instruments (ETFs / trusts)
```

### 2.2 Identify the "Business Characteristics" of Each Segment
Annotate every segment:

| Segment | Business Model | Gross-Margin Range | Competitive Landscape | Barrier Type | Cyclicality |
|---------|----------------|--------------------|-----------------------|--------------|-------------|
| | sell resources / sell equipment / sell services / collect rent | | monopoly / oligopoly / fully competitive | resources / license / technology / scale | strong / medium / weak |

### 2.3 Flag the "Chokepoint Segments"
Identify the segments in the value chain where supply is tightest, substitution is hardest, and margins are highest — these are often where the best investment targets sit.

---

## AI Research-Bias Awareness: Special Traps in Industry Research

In industry research, AI data bias amplifies in distinctive ways:

**Industry-level biases**:
| Bias Type | Manifestation | Countermeasure |
|-----------|---------------|----------------|
| Mature-industry preference | Traditional industries (banking / energy / consumer) have abundant material, so AI analysis looks "more certain" | Certainty comes from the business model, not the volume of research reports |
| New-industry underestimation | New industries (AI applications / synthetic biology, etc.) have little material, so AI analysis skews conservative | Judge industry value using "endgame thinking", not "current data" |
| Leader preference | Large companies have far more material than small ones, so AI naturally tends to recommend leaders | Small companies may have a better risk-reward ratio; do not ignore them just because AI's analysis is shorter |
| Listed-company preference | Scanning only listed companies misses key private players in the value chain | You must search for private companies and flag "future IPO candidates" |
| English-language preference | AI processes English material more capably and may underestimate Brazilian / Latin American players | You must search both Portuguese and English sources |

**Anti-bias measures in value-chain scanning**:
1. For each segment, not only list "companies AI easily finds", but also actively search for "obscure but potentially high-quality targets"
2. For small-cap companies with scarce information, do not lower the recommendation just because the analysis is short — judge on core questions (business essence, moat, management) rather than report length
3. In the final report, flag each company's "information sufficiency" (grade A/B/C) so the reader knows how reliable the AI analysis is

## Step 3: Global Listed-Company Scan

Use the Task tool to launch background agents and comprehensively search for all listed companies in the industry.

### Search Checklist
- B3 (Brazil, e.g. Novo Mercado / traditional segments) related companies
- US-listed companies (NYSE / NASDAQ / NYSE American), including Brazilian ADRs
- Other international markets (Europe / Japan / Latin America / Australia, etc.)
- Industry ETFs
- Key private companies (potential future IPOs)

Prefer the analyst's MCP market-data tools (market-data server + finnhub) plus WebSearch / WebFetch to gather this information.

### For Each Company, Collect
- Company name (and ticker in the local language if relevant)
- Ticker and exchange
- Market cap (approximate; state currency — BRL R$ for B3, USD for US listings)
- One-line description (its position and role in the value chain)
- Whether it is a pure-play target (pure exposure vs. a diversified company with some exposure)
- Which value-chain segment it belongs to

### Output Format
Group by value-chain segment, one table per segment, including every company scanned.
Then stratify by investment certainty:
- **Tier 1**: large-cap, pure-play, industry leader
- **Tier 2**: mid-cap, pure-play or high-exposure, sub-segment leader
- **Tier 3**: small-cap, development stage, high risk / high beta
- **Tier 4**: large diversified companies with relevant business lines

---

## Step 4: Four-Masters Analysis of the Leading Companies in Each Segment

For the **Tier 1 and Tier 2 companies** in each value-chain segment, run the following analysis (a brief note is enough for Tier 3/4 companies):

### 4.1 Business Essence (Duan Yongping)
- Define in one sentence what this company does in the value chain
- Revenue structure and growth rate
- Gross-margin / net-margin level and trend
- Cash-flow characteristics
- **Follow-up question**: Is this a good business? Why?

### 4.2 Moat (Warren Buffett)
Score using the five moat types (★1-5):

| Moat | Strength | Evidence |
|------|----------|----------|
| Brand / pricing power | | |
| Switching costs | | |
| Network effects | | |
| Economies of scale | | |
| Technology / license barriers | | |

**Follow-up question**: Will the moat still be there in 10 years?

### 4.3 Risk (Charlie Munger)
- How is this company most likely to fail?
- What is it worth in the worst-case scenario?
- Why don't smart people buy it?

### 4.4 Management (Duan Yongping + Warren Buffett)
- Who is the CEO / founder? Record of key decisions
- Ownership stake and interest alignment
- Brief rating (grade A/B/C)

### 4.5 Valuation Snapshot
- Current P/E / P/S / EV/EBITDA
- Comparison with competitors in the same segment
- Brief verdict: expensive / fair / cheap

### 4.6 Recommendation Level
Mark with ★1-5:
- ★★★★★ = core position candidate
- ★★★★☆ = satellite position candidate
- ★★★☆☆ = watchlist
- ★★☆☆☆ = high-risk option
- ★☆☆☆☆ = not recommended

---

## Step 5: Industry-Level Risk Assessment (Munger's "Checklist")

### 5.1 Systemic-Risk Checklist

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| A link in the investment logic chain is falsified | | | |
| A substitute technology emerges | | | |
| Policy / regulatory black swan | | | |
| Cyclical demand pullback | | | |
| Valuation bubble bursts | | | |

### 5.2 Historical Analogy
Find a historically similar value-chain investment theme and analyze how it ultimately ended:
- What was the analogous industry?
- Who were the eventual winners? (upstream / midstream / downstream?)
- Did most investors make or lose money?
- What is the lesson for the current industry?

### 5.3 Bias Self-Check
- Narrative bias: Is the story too perfect?
- Anchoring: Are you anchored on recent price gains?
- Herding: Are you buying because "everyone is buying"?

---

## Step 6: Civilizational-Trend Judgment (Li Lu Framework)

- Is the underlying trend this industry rests on a "civilization-level paradigm shift" or a "temporary fad"?
- What is the closest historical analogy of a technology revolution?
- What is the endgame for this industry in 10-20 years?
- Within the value chain, which segment is most likely to become "winner-take-all"?
- Which segment is most likely to be disrupted?

---

## Step 7: Portfolio Allocation Recommendation

### 7.1 Recommended Portfolio
Output using the following structure:

| Tier | Position Weight | Target | Segment | Core Logic |
|------|-----------------|--------|---------|------------|
| **Core position** | 50-60% of theme allocation | | | Most certain, widest moat |
| **Satellite position** | 25-35% of theme allocation | | | Higher beta, slightly lower certainty |
| **Option position** | 5-15% of theme allocation | | | High risk / high reward, can go to zero |
| **ETF alternative** | Can replace all of the above | | | The "lazy" option for those who don't want to pick stocks |

### 7.2 Buy / Sell Signals

| Signal Type | Specific Condition |
|-------------|--------------------|
| Add signal | |
| Trim signal | |
| Exit signal | |

### 7.3 Recommended Theme-Position Cap
Based on the certainty and risk of the investment logic chain, recommend a cap on this theme's share of the total portfolio.

---

## Step 8: Integrated Decision Memo

### Industry Summary Table

| Dimension | Conclusion | Confidence |
|-----------|------------|------------|
| Investment logic chain (degree of validation) | | |
| Best segment (Duan Yongping's "right business") | | |
| Widest moat (Buffett) | | |
| Biggest risk (Munger) | | |
| Civilizational-trend positioning (Li Lu) | | |
| Overall valuation level | | |

### Simulated Commentary from the Four Masters
Using quotation format, simulate how the four masters would comment on this industry's investment opportunity.

---

## Output Requirements

1. Every analysis must be backed by data, with sources cited
2. Present key data in Markdown tables
3. Represent the value-chain panorama as a text diagram in a code block
4. Analyze at least 2-3 leading companies per segment
5. The global company scan must be as complete as possible (B3 / Brazil, US, international)
6. Write the complete report in English to `reports/{Industry}-industry-{YYYYMMDD}.md` (industry reports go in the reports/ root; use English / Latin names)
7. Conclusions must be explicit, with specific targets, position sizes, and price-range recommendations
8. Each analysis module ends with the corresponding master's "follow-up question"

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
