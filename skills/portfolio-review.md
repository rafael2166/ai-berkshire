# Portfolio Management: From "Researching Companies" to "Managing a Portfolio"

Perform a portfolio review and optimization for $ARGUMENTS.

**Supported input formats**:
- Holdings list, e.g.: `PETR4 30%, VALE3 20%, ITUB4 20%, WEGE3 15%, cash 15%`
- Or: `PETR4 500 shares @ R$38, VALE3 1000 shares @ R$62, ...`
- Or: `my holdings` (if a saved portfolio file `reports/portfolio-latest.md` already exists)

> "Diversification is protection against ignorance. It makes little sense if you know what you are doing." — Warren Buffett
>
> "In my whole life, the truly great investment opportunities I've seen can be counted on ten fingers." — Li Lu

## Design Philosophy

Researching companies is only half of investing. The other half is **portfolio-level decisions**:
- How much to buy? (position size)
- With what money? (funding source — new money or a switch)
- Does it conflict with existing holdings? (correlation)
- What does the optimal portfolio look like? (opportunity cost)

Buffett never looks at a stock in isolation — he is always asking, "Is this the best thing I can do?"

## Execution Flow

### Step 1: Parse Holdings

Parse the current holdings from the input and standardize into the following format:

| Name | Ticker | Quantity | Cost | Current price | Market value | Weight | P&L |
|------|------|--------|-------|------|------|------|------|

If the input only has percentages and no amounts, analyze by percentage.

Also check whether an existing portfolio file (`reports/portfolio-latest.md`) exists; if so, read and update it.

### Step 2: Get the Latest Data

Use the Task tool to launch background agents to fetch the following in parallel for each holding — prefer the connected MCP market-data tools (market-data server + finnhub); supplement with WebSearch/WebFetch:
1. Current price and valuation metrics (P/E, P/B, dividend yield). State currency explicitly (BRL for B3 shares, USD for ADRs)
2. Key financial changes in the most recent quarter
3. Recent major events
4. Analyst consensus (forward P/E, target price)

For each holding, use `tools/financial_rigor.py verify-valuation` to check valuation data. Tag each holding's information richness (A/B/C); mark C-grade holdings' conclusions as low confidence.

### Step 3: Single-Position Health Check

Do a quick health check on each holding:

| Name | Current P/E | Has the buy thesis changed? | Thesis health | Position advice |
|------|:------:|:--------------:|:---------:|---------|
| ITUB4 | 8x | Unchanged | 8/10 | Reasonable |
| WEGE3 | 32x | Competition intensifying | 6/10 | High, consider trimming |

For each holding, answer:
- [ ] **If you didn't already own it, would you buy at the current price today?**
- [ ] **If you couldn't trade for 5 years, would you be comfortable holding it?**
- [ ] **Is the buy thesis still intact?**

**Duan Yongping**: "If you don't want to hold a stock for 10 years, don't hold it for even one day."

### Step 4: Portfolio-Level Analysis

#### 4.1 Concentration Analysis

| Metric | Current value | Suggested range | Assessment |
|------|-------|---------|------|
| Largest holding weight | | <40% | |
| Top three holdings weight | | 50-80% | |
| Total number of holdings | | 5-15 | |
| Cash weight | | 10-30% (depending on market conditions) | |

**Li Lu's standard**: 3-5 core holdings, top 3 make up 80%+. **But this requires that each one be thoroughly researched.**

**Buffett's standard**: no more than 10 core holdings, but more satellite positions are allowed.

#### 4.2 Correlation Check

Identify hidden linkages between holdings:

| Holding A | Holding B | Correlation type | Risk |
|-------|-------|---------|------|
| PETR4 | PRIO3 | Both Brazilian oil & gas | Oil-price and ANP/fuel-policy resonance |
| VALE3 | CSNA3 | Iron-ore up/downstream | China demand and iron-ore price swings |
| ITUB4 | BBAS3 | Both Brazilian banks | Selic/credit-cycle and regulatory resonance |

**Checklist**:
- [ ] Is more than 50% of the portfolio exposed to a single theme/industry?
- [ ] Is more than 50% of the portfolio exposed to a single country/currency?
- [ ] If the BRL weakens sharply, how much does the portfolio lose (or gain via commodity/ADR exposure)?
- [ ] If there is a global recession, how much does the portfolio lose?

#### 4.3 Opportunity-Cost Analysis

This is Buffett's most central way of thinking — **every dollar should sit where its return is highest.**

Rank all holdings by "expected annualized return":

| Rank | Name | Current weight | Expected annualized return | Certainty | Expected return × certainty |
|:----:|------|:-------:|:----------:|:------:|:--------------:|
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |

Expected-return estimation method (compute with `tools/financial_rigor.py three-scenario`):
- **Simplified formula**: expected annualized ≈ FCF yield + expected growth (primary method)
- **Value-style check**: reversion of margin of safety + earnings growth + dividend yield
- **Growth-style check**: earnings growth × change in a reasonable P/E

**Key question**: For the lowest-ranked holding, is the expected return higher than cash? Note the Brazilian context: the risk-free rate is the Selic rate (currently well above US rates — check the current level), so the cash hurdle is high. If a holding can't beat it, consider selling into cash.

#### 4.4 Stress Test

| Scenario | Assumption | Estimated portfolio impact | Max drawdown |
|------|------|-----------|---------|
| Global recession | Corporate earnings down 20-30% | | |
| Commodity crash | Iron ore / oil down 30-40% | | |
| Selic spike / fiscal stress | Brazilian 10-year yield surges, BRL sells off | | |
| Domestic-demand slump | Consumption and credit contract | | |

For each scenario, do a qualitative + rough quantitative assessment (based on each holding's sector attributes and historical valuation-swing range):
- Which holdings are hit hardest? Approximate direction and magnitude range
- Can the portfolio as a whole withstand it?
- Is any hedge needed?

### Step 5: Optimization Recommendations

#### 5.1 Rebalancing Recommendations

Based on the analysis above, give specific rebalancing recommendations:

| Action | Name | Current weight | Suggested weight | Rationale |
|------|------|:-------:|:-------:|------|
| Add | | | | |
| Trim | | | | |
| Exit | | | | |
| New position | | | | |
| Hold | | | | |

#### 5.2 Finding Alternative Candidates

If the portfolio has a position that is "worse than cash," or the cash weight is too high, use `/industry-research` or `/investment-checklist` to systematically screen industries/companies of interest, rather than directly recommending individual stocks within this skill.

#### 5.3 Cash Management

| Current cash weight | Suggested cash weight | Rationale |
|:----------:|:----------:|------|

**Buffett**: when he cannot find good opportunities, cash is the best position — he has repeatedly let cash build to a large share of assets rather than force a bad buy. In Brazil, cash held at the Selic rate earns a meaningful real yield, which raises the bar every holding must clear.

### Step 6: Output the Portfolio Report

#### Report Structure

```
1. Portfolio Overview (holdings table + pie-chart description)
2. Single-Position Health Check (health status of each holding)
3. Portfolio Analysis
   - Concentration: over-diversified or over-concentrated?
   - Correlation: hidden linkages and risk resonance
   - Opportunity cost: is the lowest-ranked position worth holding?
   - Stress test: estimated drawdown under extreme scenarios
4. Rebalancing Recommendations (specific actions + rationale)
5. Next review date and focus areas
```

#### The Conclusion Must Clearly Answer

1. **Overall portfolio health**: Excellent / Good / Needs adjustment / Serious problems
2. **What is the single most important thing to do?** (Add X / Trim Y / Hold)
3. **What is the biggest current risk?**

### Step 7: Save the Portfolio File

Write the portfolio information to `reports/portfolio-latest.md`, including:
- Latest holdings table
- This review's date and conclusions
- Rebalancing log (append)
- Next-review reminder

---

## Key Principles

- **Every dollar has an opportunity cost** — the cost of holding a mediocre stock is missing an excellent one
- **Concentration isn't the risk; ignorance is** — holding 3 stocks you deeply understand is safer than 30 you barely know
- **Cash is a position** — there's no shame in holding cash when you can't find good opportunities
- **Portfolio level > single-stock level** — a good stock in the wrong position size will still drag you down
- **Review regularly, but don't over-trade** — reviewing once a quarter is enough; don't watch the screen and rebalance daily
