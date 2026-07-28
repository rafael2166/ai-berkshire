# Management Deep Dive: Buying a Stock Means Buying People

Conduct an in-depth management study of $ARGUMENTS.

**Supported input formats**: `CompanyName` or `PersonName CompanyName`, e.g., `WEG`, `Roberto Campos WEG`, `Rubens Menin MRV`.

> "Buying a stock means buying people. Find people you trust, then hold for the long term." — Duan Yongping
>
> "When evaluating management, watch what they do when no one is looking." — Warren Buffett

## Design Philosophy

Most investment analysis stops at the surface when evaluating management: résumés, ownership stakes, compensation. But Buffett spends enormous amounts of time **having meals and talking with management**, Li Lu says **his investing is essentially investing in people**, and Duan Yongping says **buying a stock means buying people**.

This skill is the **deepened version** of the management-evaluation step in `/investment-research`. Use it for a deep-dive study when management scored uncertain (★★★ or below) in standard investment research, or when management is central to the investment thesis.

AI cannot share a meal with management, but it can achieve the following through public information:
- **Track whether what management says matches what they do** (promises vs. delivery)
- **Analyze the return on every major capital-allocation decision**
- **Infer character from decisions made in difficult times**
- **Cross-verify through feedback from employees / partners / customers**

## Execution Flow

### Step 1: Identify Key Management and Launch Parallel Data Collection

Use WebSearch to confirm the following key people:

| Role | Name | Tenure | Background | Ownership/Options |
|------|------|------|------|----------|
| CEO/Chairman | | | | |
| CFO | | | | |
| Founder (if not in office) | | | | |
| Controlling shareholder (if different from CEO) | | | | |
| Other key executives | | | | |

**Note**: Distinguish between "who makes the decisions" and "whose name is on the title." At some companies the founder has stepped down but remains the guiding force (for example, a founding family or controlling group that retains influence through a holding company even after leaving the executive role).

After confirming the key people, use the Task tool to launch multiple background agents to collect the following data **in parallel**:
1. Agent 1: CEO public statements and predictions record (shareholder letters, earnings calls, interviews, social media)
2. Agent 2: Capital-allocation decision record (M&A, buybacks, dividends, new-business investment)
3. Agent 3: Governance structure and compensation (ownership structure, related-party transactions, executive pay)
4. Agent 4: Cross-verification information (employee reviews, customer feedback, industry reputation)

### Step 2: CEO Circle-of-Competence Assessment

#### 2.1 Strategic Vision

Search the CEO's public statements over the past 5 years (shareholder letters, earnings calls, interviews, social media) and extract their judgment on the following:

| Date | CEO's judgment/prediction | Actual outcome | Accuracy |
|------|--------------|---------|:------:|
| | "We believe market X will..." | Market X actually... | ✅/❌ |
| | "Our focus for the next 3 years is..." | Actual execution... | ✅/❌ |

**Key questions**:
- Has the CEO made correct judgments ahead of the market?
- Has the CEO stayed calm when everyone else was bullish?
- Does the CEO understand industry trends by following the market or through independent thinking?

#### 2.2 Execution Ability

| Dimension | Assessment | Evidence |
|------|------|------|
| Strategy to execution | Did they deliver on what they said? | |
| Organizational capability | Can they attract and retain talent? | |
| Crisis handling | How do they respond to difficulty? | |
| Iteration speed | How fast do they correct after mistakes? | |

### Step 3: Integrity Assessment (Most Important)

**Buffett**: "We look for three qualities: integrity, intelligence, and energy. And if you don't have the first, the other two will kill you."

#### 3.1 Promises vs. Delivery Tracking

From the past 3 years of earnings calls, shareholder letters, and public interviews, extract **specific commitments** made by management:

| # | Date | Commitment | Setting | Delivery | Assessment |
|---|------|---------|---------|---------|------|
| 1 | | "We will make business X profitable in 2025" | 2024 annual results call | | ✅/⚠️/❌ |
| 2 | | "We plan to buy back R$X billion" | 2024 shareholder letter | | ✅/⚠️/❌ |

**Delivery-rate summary**:

| Commitment delivery rate | Assessment |
|:---------:|------|
| >80% | Excellent — they do what they say |
| 60-80% | Acceptable — right direction but execution slips |
| 40-60% | Concerning — over-promises and under-delivers |
| <40% | Serious problem — not trustworthy |

#### 3.2 Behavior in Difficult Times

Search for major crises/hardships in the company's history (share-price crashes, earnings misses, regulatory shocks, intensifying competition) and analyze management's response:

| Crisis event | Date | Management response | Assessment in hindsight |
|---------|------|-----------|-------------|

**Watch for**:
- Do they communicate proactively or avoid?
- Do they attribute the cause internally or shift blame externally?
- Do they use the moment to do the hard but right thing, or choose to placate the market short-term?

#### 3.3 Attitude Toward Stakeholders

| Stakeholder | Management attitude | Evidence | Assessment |
|-----------|-----------|------|------|
| Shareholders | Respect / ignore / exploit | | |
| Employees | Treat well / squeeze / neglect | | |
| Customers/users | Customer-centric / short-term extraction | | |
| Partners/suppliers | Fair cooperation / extreme price pressure | | |
| Regulators/society | Compliant / skirting the rules | | |

**Li Lu**: "The attitude toward stakeholders determines a company's long-term vitality. Short-term squeezing can boost efficiency, but over the long run it damages the ecosystem."

### Step 4: Capital-Allocation Ability

This is the management quality Buffett prizes most — **for every dollar earned, how much can management turn it into?**

#### 4.1 Capital-Allocation Decision Record

Search the company's major capital-allocation decisions over the past 5 years and assess each one:

**M&A record**:

| Date | Target | Amount | Strategic rationale | Return in hindsight | Score (1-5) |
|------|---------|------|---------|---------|:---------:|

**Buyback record**:

Use `tools/financial_rigor.py verify-valuation` to check valuation metrics such as P/E at the time of the buyback and currently.

| Date | Buyback amount | Average buyback price | P/E at the time | In hindsight | Score (1-5) |
|------|---------|-----------|:------:|---------|:---------:|

**Dividend record**:

| Year | Dividend amount | Payout ratio | FCF for the period | Sustainable? |
|------|---------|:------:|---------|:---------:|

**New-business investment**:

| Date | Investment area | Cumulative outlay | Current status | Return assessment | Score (1-5) |
|------|---------|---------|---------|---------|:---------:|

#### 4.2 Capital-Allocation Score

| Dimension | Score (1-5) | Notes |
|------|:---------:|------|
| M&A discipline | | Acquiring at reasonable prices? Integration afterward? |
| Buyback timing | | Buying back when undervalued, stopping when overvalued? |
| Dividend reasonableness | | Does the payout ratio match FCF? |
| New-business investment | | Success rate? Stop-loss discipline? |
| Cash management | | Are cash reserves reasonable? Hoarding too much? |
| **Overall score** | | |

**Buffett's standard**: Ideal management invests decisively when good opportunities exist, actively buys back / pays dividends when they don't, and never overpays for acquisitions.

### Step 5: Governance Structure Assessment

#### 5.1 Ownership Structure

| Item | Details | Risk assessment |
|------|------|---------|
| Dual-class / super-voting shares? | | |
| Founder/controlling-shareholder stake? | | |
| Cross-holding or holding-company structure? | | |
| Are independent directors truly independent? | | |
| Recent insider buying/selling by large shareholders? | | |

Note: on B3, many companies list under Novo Mercado (single class, one-share-one-vote), while others retain preferred (PN) shares with limited voting rights. Flag the governance segment and share-class structure explicitly.

#### 5.2 Compensation Reasonableness

| Executive | Annual total compensation | As % of net income | Vs. peers | Reasonable? |
|------|-----------|:------------:|:---------:|:-------:|

**Watch for**: Is the incentive structure aligned with long-term shareholder interests, or does it encourage short-term behavior?

#### 5.3 Related-Party Transactions

| Related party | Transaction | Amount | Arm's length? | Risk assessment |
|--------|---------|------|:-------:|---------|

### Step 6: Cross-Verification

AI cannot meet management face to face, but it can verify through public-channel indirect signals. **Note**: The following depends on what is publicly searchable and may be incomplete; annotate information sources and availability.

#### 6.1 Employee Perspective

Search **publicly searchable** employee reviews such as Glassdoor rating summaries and local platforms like Love Mondays / Reclame Aqui employer pages (for platforms that require login, mark as "users may supplement"):

| Dimension | Rating trend | Key feedback |
|------|---------|---------|
| Company culture | | |
| Management rating | | |
| Work intensity | | |
| Compensation satisfaction | | |
| Growth prospects | | |

#### 6.2 Customer/Partner Perspective

Search app-store ratings, consumer complaints (e.g., Reclame Aqui), and partner/merchant forums:

| Dimension | Rating/trend | Key feedback |
|------|----------|---------|
| Product satisfaction | | |
| Customer service | | |
| Partner/supplier relations | | |

#### 6.3 Industry Reputation

Search industry forums and social media to understand how peers and industry insiders view this management team.

### Step 7: Scenario Analysis for After the CEO Leaves

**Buffett**: "A good business is one that any fool can run — because sooner or later, one will."

| Question | Answer |
|------|------|
| If the CEO left tomorrow, would the company still run normally? | |
| How deep is the existing management team? Is there a clear successor? | |
| Does the company's competitive advantage depend on the CEO personally, or on the organization/system? | |
| Have past management transitions gone smoothly? | |

### Step 8: Output the Management Assessment Report

#### Report Structure

```
1. Key People at a Glance (table)
2. Integrity Assessment
   - Commitment delivery rate
   - Behavior in difficult times
   - Attitude toward stakeholders
3. Ability Assessment
   - Strategic vision (prediction accuracy)
   - Execution ability
   - Capital-allocation record
4. Governance Structure
   - Ownership-structure risk
   - Compensation reasonableness
   - Related-party transactions
5. Cross-Verification
   - Employee perspective
   - Customer/partner perspective
6. Overall Score and Conclusion
```

#### Overall Score

| Dimension | Weight | Score (1-5) | Weighted |
|------|:----:|:---------:|:----:|
| Integrity | 35% | | |
| Strategy and execution | 25% | | |
| Capital allocation | 25% | | |
| Governance structure | 15% | | |
| **Overall score** | 100% | | |

#### Duan Yongping's "Buying People" Test

> Answer the following three questions:
> 1. **Is this person honest?** (truthful, doesn't take advantage of shareholders)
> 2. **Is this person capable?** (strategic vision + execution + capital allocation)
> 3. **Would you hand this person your money to manage for 10 years?**
>
> All three "yes" = ★★★★★ (5)
> First two "yes" = ★★★★ (4)
> Only the first "yes" = ★★★ (3)
> First not "yes" = ★ (1, do not invest)

### Step 9: Save the Report

Write the report to `reports/{CompanyName}/{CompanyName}-management-{YYYYMMDD}.md`, e.g., `reports/WEG/WEG-management-20260409.md`.

---

## Key Principles

- **Integrity is a veto item** — lack of ability can be learned; a flawed character cannot be fixed
- **Watch behavior, not words** — what management says doesn't matter; what they did does
- **The truth shows in difficulty** — anyone is a good CEO with the wind at their back; only headwinds reveal the real skill
- **Capital allocation is the ultimate exam** — making money is easy; allocating the money you made is hard
- **Don't fall in love with management** — stay objective; even people you admire can make big mistakes
