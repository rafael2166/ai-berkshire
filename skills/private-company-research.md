# Private Company Research: A Multi-Agent Parallel Deep-Research Framework

Run a team-based deep-research analysis on $ARGUMENTS. Designed for private (non-listed) companies such as Brazilian startups and scale-ups (e.g., Nubank pre-IPO, QuintoAndar, Loft, Wildlife Studios, C6 Bank, Gympass/Wellhub), and global privates like SpaceX or Stripe.

**Ultimate goal**: under conditions of naturally scarce information, reconstruct this company's **true value** as faithfully as possible — not the valuation the market assigns, but what the business itself is worth.

## Framework Characteristics

The core differences between researching private vs. listed companies:
- **No standardized filings**: you must piece together and cross-verify multiple sources
- **Few valuation anchors**: you rely on funding rounds, comparable-company analysis, and scenario modeling
- **Large information asymmetry**: you need more "jigsaw-style" research methods
- **Uncertain exit path**: IPO / acquisition / secondary transfer are all possible

## Self-Awareness of AI Research Bias (the core premise of this framework)

Private companies are the domain where AI research bias is most severe. You must constantly guard against the following traps:

**Core tension**: AI excels at structuring existing information, but private-company information is naturally scarce. This leads to:
1. **False conservatism**: because there is little material, AI tends to give conservative/vague conclusions — but little material ≠ a bad company
2. **False precision**: to fill out a report template, AI may dress up "reasonable guesses" as "evidence-based analysis"
3. **Benchmarking trap**: forcibly benchmarking against listed companies inherits their valuation logic and ignores the private company's unique value
4. **Survivorship bias**: the information findable online tends to be positively biased (companies actively broadcast good news)

**Governing principles**:
- Prefer leaving a blank and saying "unknown" over filling tables with speculation to fake certainty
- Every data point must carry a confidence tag (🟢 high / 🟡 medium / 🔴 low), letting the reader judge for themselves
- Distinguish "verifiable facts" from "AI reasoning" using different formatting
- For companies with extremely scarce information, switch to "first-principles mode" — don't chase report completeness, just answer a few core questions:
  1. What real problem does this business solve? Is the demand real or manufactured?
  2. Why this team? What unique advantage do they have?
  3. If it succeeds, how high is the ceiling? If it fails, where is it most likely to die?
  4. What is the key validation milestone at the current stage?

**Turning information asymmetry to your advantage**: the market has little information on private companies → pricing efficiency is low → this is precisely where excess returns may come from. The goal of AI research is not to eliminate information asymmetry (impossible), but to extract the most critical judgment basis from limited information.

---

## Execution Flow

### Step 1: Present the Team Framework

Show the user the following team structure, confirm, then launch:

| Role | Responsibility | Core Perspective |
|------|----------------|------------------|
| **team-lead** (yourself) | Coordination, information jigsaw, cross-verification, final report | Integrating the investment decision |
| **business-decoder** | Business-model teardown & product/user analysis | "What is the essence of this business" |
| **financial-detective** | Financial-data reconstruction & valuation modeling | "Reconstruct the true financial picture as far as possible under missing information" |
| **competitive-mapper** | Industry structure & competitive dynamics & substitution threats | "Who competes with it, and who might disrupt it" |
| **risk-governance-analyst** | Risk panorama & management/governance/investor assessment | "What could go wrong, and who is at the helm" |
| **tech-ip-analyst** | Tech stack / patents / R&D capability / technical moat | "Is the technical barrier real, and how long can it last" |
| **signal-miner** | Alternative-data mining: hiring / patents / litigation / app data / supply chain | "Beyond conventional information, what other traces exist" |

### Step 2: Create the Team

Use TeamCreate to create the team:
- team_name: `{Company}-private-research` (lowercase English, e.g., `nubank-private-research`)
- agent_type: `team-lead`

### Step 3: Create 6 Tasks

Use TaskCreate to create the following 6 tasks (each with a subject, description, and activeForm):

---

#### Task 1: Deep Analysis of Business Model and Product/Users
- subject: `Deconstruct {Company}'s business model, product matrix, and user ecosystem`
- activeForm: `Analyzing {Company}'s business model and user ecosystem`
- description contains:

```
## Deep Business-Model Teardown

### 1. Core Business Definition
- Define the essence of this business in one sentence (Duan Yongping style: in the plainest language, explain this business to someone smart but not familiar with the industry)
- What problem does the company solve? For whom does it create value?
- Value proposition and differentiation vs. peers
- If the company didn't exist, how would users solve this problem? How costly is the alternative?
- "Stickiness" of demand: in a downturn, will users cut this spending?

### 2. Revenue Model Teardown
- Revenue composition: advertising / commission / subscription / transaction take / financial services / SaaS / hardware / licensing, etc.
- Share and growth trend of each revenue line (if data available)
- Monetization-efficiency metrics: ARPU, take rate, ad load, conversion rate, etc.
- Revenue-quality assessment:
  - Share of recurring vs. one-off revenue
  - Revenue concentration: share of top 5 customers/channels
  - Revenue predictability (contract/subscription vs. transactional)
  - Whether revenue recognition is reasonable (any signs of early recognition)
- Benchmark monetization efficiency against listed peers

### 3. Unit Economics (UE) Estimation
- CAC (customer acquisition cost) estimate:
  - Share of paid acquisition vs. organic growth
  - CAC by channel (if available)
  - CAC trend: rising or falling as scale grows?
- LTV (lifetime value) estimate:
  - ARPU × expected lifetime
  - Consider cross-sell and upsell
- LTV/CAC ratio, payback period
- Marginal cost structure: marginal cost trend of an incremental user/transaction
- Scale-economics inflection: when/whether it has passed break-even

### 4. Product Matrix and Flywheel Effect
- Core product + extension products + incubating products
- How the flywheel spins: network effects / data flywheel / scale effects
- Synergies and cross-traffic among products
- Product lifecycle: which stage each product is in
- Iteration speed: app/product update frequency, major feature updates in the last 12 months

### 5. Business Model Canvas (BMC)
Describe the business model fully with the 9 building blocks:
| Building Block | Content |
|----------------|---------|
| Value Propositions | |
| Customer Segments | |
| Channels | |
| Customer Relationships | |
| Revenue Streams | |
| Key Resources | |
| Key Activities | |
| Key Partners | |
| Cost Structure | |

### 6. Deep User Analysis
- User scale: MAU/DAU (estimated from app-intelligence sources such as Sensor Tower, data.ai, SimilarWeb, and finnhub alternative data)
- User growth curve: which stage of the S-curve (argue with specific data)
- Stickiness metrics:
  - DAU/MAU ratio
  - Average session length, open frequency
  - Day-1 / 7-day / 30-day retention (if available)
  - User growth vs. retention trend (spot fake growth)
- User profile: age / region / spending power / occupation distribution
- User sentiment:
  - App Store / Google Play rating trend (last 12 months)
  - Social-media sentiment analysis
  - Real user feedback on Reclame Aqui, Google Reviews, Reddit, X/Twitter, and local forums
  - Main clusters of negative reviews
- Acquisition efficiency:
  - Ratio of paid acquisition vs. organic vs. word-of-mouth
  - Reliance on a single acquisition channel

### 7. Pricing Power Assessment
- Any price increases in the past 3 years? User churn after increases?
- Price comparison vs. competitors: price leader or follower?
- User price sensitivity assessment
- Reasonableness of commission/take rate within the value chain

### 8. Moat Assessment
Verify and score each of the following 6 dimensions (★1-5):

| Moat Type | Score | Evidence | Trend | Durability Assessment |
|-----------|-------|----------|-------|-----------------------|
| Network effects | | More users, more value? One-sided or two/multi-sided? | Widening/stable/narrowing | |
| Switching costs | | Cost of migrating to a competitor? Data/relationship/habit migration cost? | | |
| Brand mindshare | | Category = brand? NPS estimate? | | |
| Data barrier | | Is a data flywheel formed? Proprietary data assets? Data scale? | | |
| Regulatory license | | Entry barriers? Difficulty of obtaining a license? | | |
| Scale economics | | Are scale-driven cost advantages significant? | | |

Overall moat rating: Wide / Medium / Narrow / None

### 9. Internationalization Analysis (if applicable)
- Overseas-market expansion status
- Share of international revenue
- Localization strategy and challenges
- Differences in the overseas competitive landscape
```

---

#### Task 2: Financial-Data Reconstruction and Valuation Modeling
- subject: `Reconstruct {Company}'s financial data and run a valuation analysis`
- activeForm: `Reconstructing {Company}'s financials and valuation`
- description contains:

```
## Financial-Data Reconstruction (detective-style research)

Private companies have no standardized filings; you must piece together and cross-verify multiple sources. Every figure must be traced to a specific source, with time and confidence noted.

### 1. Data Source Matrix
**Search the following sources in priority order**:

| Priority | Source Type | Specific Sources | Credibility | Search Method |
|----------|-------------|------------------|-------------|---------------|
| 1 | Prospectus / regulatory filings | CVM (via the RAD portal) or SEC (for US-listed ADRs) prospectus / IPO filing drafts | 🟢 High | Search "company name + prospectus / prospecto / IPO filing" |
| 2 | Parent / affiliated listed-company filings | e.g., a listed parent's annual report disclosing the subsidiary's data | 🟢 High | Search related-party disclosures in the parent's annual report |
| 3 | Regulatory penalties / compliance disclosures | CVM, CADE, BACEN, sector-agency penalty documents | 🟢 High | Search "company name + penalty / fine / autuação / multa" |
| 4 | Bond / securitization (FIDC/CRI/CRA) offering documents | Underlying data in a securitization prospectus | 🟢 High | Search "company name + debênture / bond / FIDC / securitização" |
| 5 | Corporate registry information | Junta Comercial / Receita Federal (CNPJ) records, paid-in capital | 🟡 Medium-high | |
| 6 | Funding news | Valuation, funding amount, investors | 🟡 Medium | Search "company name + funding / rodada / valuation / aporte" |
| 7 | Third-party research | Brokerage, consulting-firm, industry-association reports | 🟡 Medium | Search "company name + report / relatório" |
| 8 | In-depth media coverage | Brazil Journal, NeoFeed, Pipeline Valor, The Information, Bloomberg, Reuters | 🟡 Medium | Search these outlets + company name directly |
| 9 | Industry-data back-out | Back out from industry total × market share | 🔴 Low-medium | |
| 10 | Ex-employee / insider leaks | Glassdoor, LinkedIn, forums | 🔴 Low | Reference only, not a primary basis |

### 2. Key Financial-Metric Estimation
Estimate the following as far as possible; **each data point must note**: source, time, confidence, estimation method.

**Revenue side**:
- Total revenue scale and growth (last 3 years, annual/quarterly granularity)
- Revenue-mix breakdown (by business line / product line)
- Decompose revenue growth: volume (users/transactions) × price (ARPU/ticket)
- Seasonal patterns in revenue

**Cost side**:
- Gross margin estimate (benchmark to listed peers; explain the selection logic)
- R&D expense ratio estimate (via headcount × average pay, or share of R&D staff)
- Sales expense ratio estimate (via acquisition channels and ad-spend data)
- G&A expense ratio estimate

**Profit side**:
- Operating profit / EBITDA estimate
- Net profit / adjusted net profit estimate
- Profitability timeline: when profitable? If not yet, projected when?

**Cash-flow side**:
- Operating cash flow judgment (positive/negative, self-funding or not)
- Capex level and trend
- Free cash flow estimate
- Cash on hand / burn rate (estimated from funding amounts, funding intervals, headcount)
- Cash runway: at the current burn rate, how long can it last?

**Efficiency metrics**:
- Headcount and productivity (revenue per employee, profit per employee)
- Capital efficiency: revenue generated per R$1 raised
- Benchmark efficiency metrics against listed peers

### 3. Financial-Data Cross-Verification
- If a metric has multiple sources, list them all and explain the differences
- Estimate the same metric via different methods; check whether results converge
- Flag "single-source" data that cannot be verified

| Metric | Source A (data/time) | Source B (data/time) | Difference | Adopted Judgment |
|--------|----------------------|----------------------|------------|------------------|

### 4. Funding History and Valuation Evolution
Assemble a complete funding timeline:

| Round | Date | Amount | Pre-money | Post-money | Lead Investor | Co-investors | Valuation Step-up | Notes |
|-------|------|--------|-----------|------------|---------------|--------------|-------------------|-------|

Analysis:
- Is the valuation-growth curve healthy (are per-round step-ups reasonable)?
- Are funding intervals reasonable (too frequent = fast burn? too sparse = trouble raising?)
- Any down rounds?
- Are existing shareholders continuing to double down (a confidence signal)?
- Inferred terms of the latest round:
  - Liquidation preference (1x / 2x / participating)
  - Anti-dilution (full ratchet / weighted average)
  - Milestone/ratchet clauses (performance / IPO timing)
  - Impact of these terms on common-share value

### 5. Valuation Analysis (multi-method cross-check)

**Method 1: Latest-round valuation**
- Latest round's valuation and date
- After preferences etc., the "common-share equivalent valuation" (usually a 20-40% discount)
- Adjustment for the time elapsed since
- Motivation analysis of that round's investors (financial vs. strategic; strategic investors may pay a premium)

**Method 2: Comparable listed companies**
- Choose 3-5 comparable listed companies; state the selection rationale (prefer B3-listed peers; use US/global peers where relevant)
- Key-multiple comparison:

| Comparable | P/S | P/E | EV/EBITDA | EV/Revenue | Growth | Margin |
|------------|-----|-----|-----------|------------|--------|--------|

- Applied adjustments:
  - Illiquidity discount: 20-30% (note the specific value and reason)
  - Growth premium/discount
  - Scale discount
  - Regulatory/policy risk discount

**Method 3: DCF scenario analysis**
Three scenarios, each listing key assumptions:

| Assumption | Bear | Base | Bull |
|------------|------|------|------|
| Revenue CAGR (next 5 years) | | | |
| Terminal operating margin | | | |
| Terminal growth rate | | | |
| WACC | | | |
| Terminal multiple (EV/EBITDA) | | | |

Each assumption needs support; don't assume out of thin air.

**Method 4: End-state market-cap back-out**
- Assume this business's market position at its terminal state in 5/10 years
- Terminal revenue and margin assumptions
- Terminal reasonable multiple (reference mature peers in the industry)
- Back out a reasonable current valuation range
- Implied annualized return

**Method 5: Transaction comparables**
- M&A / funding transactions in the industry over the last 2 years
- Transaction multiples (P/S, P/E)
- Transaction context and premium/discount factors

### 6. Synthesized Valuation Judgment

| Method | Valuation Range | Confidence | Weight | Weighted Valuation |
|--------|-----------------|------------|--------|--------------------|

- Do the methods converge? If they differ widely, analyze why
- The final valuation range should distinguish "reasonable valuation" from "conservative valuation" (margin-of-safety valuation)
```

---

#### Task 3: Industry Structure and Competitive-Dynamics Analysis
- subject: `Analyze the competitive landscape and substitution threats in {Company}'s industry`
- activeForm: `Analyzing {Company}'s industry structure and competitive dynamics`
- description contains:

```
## Industry Structure and Competitive Dynamics

### 1. Industry Positioning and Market Size
- Define the company's core arena (note: the company's own definition may be flattering; judge independently)
- TAM/SAM/SOM three-layer market sizing:
  - TAM (total addressable market): the whole large industry
  - SAM (serviceable addressable market): what the company's tech/model can cover
  - SOM (serviceable obtainable market): what it can actually capture now
- Compare market-size sources (different research firms can forecast very differently)
- Market penetration: current vs. ceiling
- Industry stage: nascent / growth / mature / decline (with evidence)
- Growth drivers: which forces are pushing/hindering industry growth

### 2. Full Value-Chain Map
Draw the complete value-chain structure (text diagram):

```
Upstream suppliers (who? bargaining power?)
    ↓
The company's link (which position in the value chain? share of the profit pool?)
    ↓
Downstream customers/users (concentration? substitute choices?)
    ↕
Competitors / substitutes / potential entrants
```

- Profit-pool analysis: profit distribution across value-chain links
- The company's bargaining power in the chain (upstream/downstream)
- Up/downstream dependence: any single-supplier/single-customer dependence?
- Structural changes underway in the value chain

### 3. Porter's Five Forces (quantified scoring)

| Force | Intensity (★1-5) | Key Factors | Impact on Company |
|-------|------------------|-------------|-------------------|
| Rivalry among competitors | | Concentration, differentiation, exit barriers | |
| Threat of new entrants | | Capital / tech / regulatory / brand barriers | |
| Threat of substitutes | | Substitute price-performance, switching cost | |
| Supplier bargaining power | | Supplier concentration, switching cost | |
| Buyer bargaining power | | Customer concentration, information transparency | |

Overall industry attractiveness score: ★1-5

### 4. Deep Scan of the Competitive Landscape

| Competitor | Type | Market Share (est.) | Revenue Scale | Funding/Mkt Cap | Core Strength | Main Weakness | Threat Level |
|------------|------|---------------------|---------------|-----------------|---------------|---------------|--------------|
| Direct competitor 1 | Direct | | | | | | |
| Direct competitor 2 | Direct | | | | | | |
| Indirect competitor 1 | Cross-sector | | | | | | |
| Potential entrant 1 | Incumbent giant | | | | | | |

Key analysis:
- **Direct competitors**: head-to-head rivals in the same arena; analyze each one's strategic intent and resource commitment
- **Indirect competitors**: cross-sector potential rivals, especially large incumbents' adjacent businesses
- **Substitute threats**: different tech paths/models, especially AI-driven disruption
- **Potential entrants**: probability and mode of a giant entering (build / acquire / invest)

### 5. Deep Competitor Comparison
Select 2-3 of the most direct competitors (listed and private), compare across dimensions:

| Dimension | {Company} | Competitor A | Competitor B | Competitor C |
|-----------|-----------|--------------|--------------|--------------|
| Founding year | | | | |
| User scale (MAU) | | | | |
| Revenue scale | | | | |
| Revenue growth | | | | |
| Total funding / mkt cap | | | | |
| Valuation / revenue multiple | | | | |
| Monetization efficiency (ARPU) | | | | |
| Gross margin | | | | |
| Profitability status | | | | |
| Headcount | | | | |
| Technical capability | | | | |
| Differentiated positioning | | | | |
| Internationalization | | | | |

### 6. Competitive Dynamics and Trends
- Key changes in the competitive landscape over the last 12 months (funding, M&A, product launches, personnel changes)
- Inferred strategic direction of competitors (from hiring, patents, product updates)
- Structural shifts underway in the industry
- Impact of technological change on the landscape (especially AI / large models)
- Impact of regulatory policy on the landscape
- Is this a "winner-take-all" industry, or will it settle into a stable oligopoly?

### 7. Competitive Scenario Modeling
- Scenario A: the company wins — what conditions are needed? probability?
- Scenario B: stalemate/coexistence — what is each player's survival space?
- Scenario C: disrupted — the most likely disruptor and path?

### 8. Global Benchmarking
Find overseas/domestic (listed) benchmark companies and analyze:

| Dimension | Benchmark A | Benchmark B | Implications for {Company} |
|-----------|-------------|-------------|----------------------------|
| Development path | | | |
| Current valuation level | | | |
| Time from a similar stage to IPO | | | |
| Post-IPO share performance | | | |
| Key success/failure factors | | | |

- Note the limits of benchmarking (Brazilian-market specifics, regulatory differences, user-habit differences)
```

---

#### Task 4: Risk Panorama and Governance Assessment
- subject: `Assess {Company}'s full-spectrum risk and management/governance structure`
- activeForm: `Assessing {Company}'s risk and governance structure`
- description contains:

```
## Risk Panorama and Governance Assessment

### 1. Deep Assessment of the Founder/CEO

> "Buying a stock is buying the people." — Duan Yongping

- **Background and track record**: education, career, entrepreneurial experience
  - Any serial-founder experience? Result of the last venture?
  - Years of relevant industry experience
  - Largest team/business previously managed
- **Strategic vision**: search the CEO's public statements over the past 3 years (talks, interviews, internal letters, social media)
  | Date | CEO's judgment/prediction | Actual result | Accuracy |
  |------|---------------------------|---------------|----------|
  - Any correct calls ahead of the market?
  - Any staying calm while everyone else was bullish?
- **Execution**: were key milestones hit on time?
  | Commitment | Committed date | Setting | Delivery | Assessment |
  |------------|----------------|---------|----------|------------|
- **Character and values**:
  - Attitude toward users/employees/society (judge from concrete events, not slogans)
  - Choices under difficulty (how layoffs were handled, crisis handling, trade-offs in conflicts of interest)
  - Trade-off between short-term profit and long-term value
- **Controversies**: any negative record (search "CEO name + controversy / scandal / problem")
- **Rating**: ★1-5 (with detailed reasoning)

### 2. Core-Team Assessment
- Roster and backgrounds of the core executive team (CTO/CFO/COO/VP, etc.)
  | Name | Title | Background | Tenure | Prior Experience |
  |------|-------|------------|--------|------------------|
- Key-talent flow analysis:
  - Important executive departures in the last 2 years (who left? where to? why?)
  - Important executive additions in the last 2 years (poached from where? what does it signal?)
  - Net talent inflow or outflow?
- Team complementarity: are the founding team's skills complementary? Any obvious gaps?
- Team-culture signals:
  - Glassdoor / LinkedIn ratings and trend (the 12-month direction of change matters more than the absolute value)
  - Willingness to recommend to a friend
  - CEO approval rating
  - Sentiment on overtime culture and organizational atmosphere
- Key-person dependence: what happens if the CEO/CTO leaves?

### 3. Ownership Structure and Governance

**Equity structure**:
| Shareholder | Ownership % | Voting % | Type | Notes |
|-------------|-------------|----------|------|-------|

- Founder-control structure: dual-class shares / voting agreements / holding-company structure
- Trend of the founder's ownership (dilution across rounds)
- Employee stock ownership plan: coverage, vesting conditions, IPO-linked terms

**Governance**:
- Board composition (share of independent directors, investor seats)
- Major-decision mechanisms
- Potential conflicts of interest:
  - Related-party transactions (deals between the founder's other companies and this one)
  - Non-compete conflicts
  - Points of conflict between large and small shareholders

### 4. Deep Analysis of the Investor Roster

| Investor | Round | Amount | Estimated Stake | Type | Strategic Value | Exit Pressure |
|----------|-------|--------|-----------------|------|-----------------|---------------|

Analysis:
- Signaling value of the lead investor (top-tier VC vs. unknown fund)
- Strategic synergy of corporate capital (does it bring resources/channels?)
- Investor exit-pressure assessment:
  - How much of the fund's life remains?
  - Have they already sold secondary shares?
  - Are ratchet/milestone clauses nearing their deadline?
- Red-flag signals in the investor roster:
  - Any investors with poor reputations?
  - Have early investors fully exited?
  - Follow-on in the latest round (existing shareholders not following = lack of confidence?)

### 5. Full-Spectrum Risk Checklist

| Risk Type | Specific Risk | Probability (H/M/L) | Impact (H/M/L) | Severity | Hedgeable? | Monitoring Metric |
|-----------|---------------|---------------------|----------------|----------|------------|-------------------|
| Regulatory risk | Antitrust (CADE), data protection (LGPD/ANPD), sector cleanup, license risk | | | | | |
| Competitive risk | Giant entry, new-model disruption, price war | | | | | |
| Technology risk | Platform migration, AI disruption, failed tech path | | | | | |
| Talent risk | Loss of founder/core team | | | | | |
| Financing risk | Funding-chain break, down round, hard to raise | | | | | |
| IPO risk | IPO window, regulatory approval, market conditions | | | | | |
| Geopolitical risk | Cross-border data, sanctions, FX volatility | | | | | |
| Commercialization risk | Monetization below expectations, user backlash | | | | | |
| Governance risk | Related-party transactions, opacity, investor conflict | | | | | |
| Compliance risk | Data privacy (LGPD/GDPR), content compliance | | | | | |
| Macro risk | Economic cycle, interest-rate environment (Selic), capital-market appetite | | | | | |
| ESG risk | Environmental / social / governance risks | | | | | |

### 6. Exit-Path Analysis

| Exit Route | Likelihood (★1-5) | Estimated Window | Expected Valuation Range | Key Preconditions | Main Obstacles |
|------------|-------------------|------------------|--------------------------|-------------------|----------------|
| B3 IPO | | | | | |
| US IPO (NYSE/Nasdaq) | | | | | |
| Acquisition | | Who are potential buyers? | | | |
| Secondary-market transfer | | Liquidity? | | | |
| SPAC | | | | | |
| Long-term no exit | | | | | |

- Most likely exit path and rationale
- Exit-timeline modeling
- Expected-return analysis under each exit path

### 7. Worst-Case Analysis (Munger-style inversion)

> "Invert, always invert." — Munger

- How is this company most likely to **fail**? List 3 specific failure paths
- Probability and trigger conditions for each failure path
- In the worst case, how much can investors recover? (liquidation-value analysis)
- Why would smart people **not** invest in this company? (list at least 5 reasons)
- Historically, which companies with similar positioning/stage failed? Why?
- What signals mean "the thesis is broken" and it's time to cut losses?
```

---

#### Task 5: Technical Capability and Intellectual Property Analysis
- subject: `Analyze {Company}'s tech stack, patent portfolio, and R&D capability`
- activeForm: `Analyzing {Company}'s technical capability and IP`
- description contains:

```
## Deep Analysis of Technical Capability and Intellectual Property

> For a tech company, the reality and durability of technical barriers directly determine whether the valuation is reasonable.

### 1. Tech-Stack Analysis
- Infer the core technical architecture (from hiring posts, tech blogs, open-source projects, conference talks)
- Whether the tech-stack choices are reasonable (right tools for the right problems)
- Technical-debt signals:
  - Are they hiring many "refactor/migration" roles?
  - Are they doing a large-scale tech-stack switch?
  - Frequent bug/outage complaints on the user side?

### 2. Patent-Portfolio Analysis
Search patent databases (Google Patents, INPI [Brazil], USPTO):

| Patent Metric | Data | Source |
|---------------|------|--------|
| Total granted patents | | |
| Applications pending | | |
| New patents in the last 2 years | | |
| Core tech-area distribution | | |
| Citations of key patents | | |
| International patent footprint | | |

- Patent-quality assessment (not just count):
  - Any core/foundational patents?
  - Do the patents cover tech areas consistent with the main business?
  - Any patent litigation (as defendant or plaintiff)?
- Patent trend: filing pace accelerating or slowing? Any shift in tech direction?
- Patent comparison vs. competitors

### 3. R&D Capability Assessment
- **R&D investment**:
  - Number/share of R&D staff (estimated from hiring platforms, LinkedIn)
  - R&D expense estimate (headcount × average pay + infrastructure)
  - R&D expense ratio (vs. peers)
  - R&D-investment trend: increasing or shrinking?
- **R&D output**:
  - Academic publications (search Google Scholar, arXiv)
  - Conference talks (search KDD, NeurIPS, SIGIR and other top venues)
  - Open-source contributions (search GitHub org accounts)
  - Tech-blog output
- **R&D efficiency**:
  - Speed from R&D to product delivery
  - Commercialization rate of technical results

### 4. Technical-Talent Assessment
- **Core technical leaders**: background and capability of the CTO / VP Eng / Chief Scientist
  | Name | Title | Education | Prior Company | Technical Influence |
  |------|-------|-----------|---------------|---------------------|
- **Technical-talent density**:
  - From which companies/labs? (share from top institutions — Google/Meta/Microsoft Research/leading local universities, etc.)
  - Compensation competitiveness of technical roles (estimated from hiring posts)
  - Attrition signals in the technical team (departure activity on LinkedIn)
- **Hiring signals**:
  - What technical roles are open now? (reflects tech-strategy direction)
  - Difficulty and fill speed of technical roles
  - Are they building a new technical team/lab?

### 5. Technical-Moat Assessment

| Technical-Barrier Dimension | Score (★1-5) | Evidence | Durability |
|-----------------------------|--------------|----------|------------|
| Algorithm / model barrier | | Any original algorithms? Reproducible? | |
| Data barrier | | Data scale, proprietary data, flywheel speed | |
| Engineering barrier | | System complexity, long-accumulated engineering capability | |
| Talent barrier | | Are core technical people hard to replace? | |
| Ecosystem barrier | | Developer ecosystem, API/SDK coverage, technical standards | |

- Overall technical-moat rating: Strong / Medium / Weak
- Assessment of technical-moat decay speed (in the AI era, the half-life of technical barriers may be very short)

### 6. AI / New-Technology Impact Assessment
- The company's AI capability and positioning
- AI's impact on the core business (augmenting vs. threatening vs. neutral)
- Is the company a beneficiary of the AI shift or a disruptee?
- Impact assessment of other emerging technologies (Web3 / AR/VR / quantum, etc.)

### 7. Technical-Risk Checklist
| Risk | Description | Probability | Impact |
|------|-------------|-------------|--------|
| Failed tech path | The bet-on tech direction is falsified | | |
| Open-source substitution | Core tech replaced by an open-source solution | | |
| Platform dependence | Dependence on a specific cloud/chip/OS | | |
| Security vulnerability | Data breach / system attack | | |
| Talent loss | Core technical people leave | | |
```

---

#### Task 6: Alternative-Data Signal Mining
- subject: `Mine {Company}'s unconventional data signals and hidden clues`
- activeForm: `Mining {Company}'s alternative-data signals`
- description contains:

```
## Alternative-Data Signal Mining

> Conventional information on private companies is limited; alternative data often provides more truthful operating signals than news coverage.
> The goal of this task: beyond conventional sources, mine every potentially useful trace.

### 1. Hiring-Signal Analysis
Search hiring information on LinkedIn, Gupy, Glassdoor, Indeed, and company career pages:

**Hiring scale and trend**:
- Total open roles now
- Hiring trend over the last 6 months (accelerating / flat / shrinking)
- Hiring scale vs. competitors

**Hiring-structure analysis**:
| Role Category | Count | Share | Signal Interpretation |
|---------------|-------|-------|-----------------------|
| R&D / engineering | | | Tech direction |
| Product | | | Product strategy |
| Sales / BD | | | Commercialization stage |
| Marketing / operations | | | Growth strategy |
| Data / AI | | | AI positioning |
| Internationalization | | | Overseas plans |
| Compliance / legal | | | Regulatory response / IPO prep |
| Finance / IR | | | IPO-prep signal |

**Key signals to capture**:
- Hiring for IR (investor relations) = IPO signal
- Hiring for compliance / data security = regulatory pressure or IPO prep
- Hiring for overseas roles = internationalization
- Compensation ranges for senior roles = financial strength and talent competitiveness
- Tech stacks / business directions mentioned in JDs = strategic direction

### 2. App / Product-Data Analysis
Search App Store, Google Play, Sensor Tower, data.ai, SimilarWeb (and finnhub alternative data):

| Metric | Data | Source | Trend |
|--------|------|--------|-------|
| App Store ranking | | | Last-6-month trend |
| User rating | | | Direction of change |
| Number of ratings | | | Growth rate |
| Estimated downloads | | | |
| App update frequency | | | |
| Main features of latest update | | | |

- High-frequency keywords and sentiment in App Store reviews
- Main clusters of recent negative reviews (bug? pricing? worse experience?)
- Web-traffic data (SimilarWeb): UV, PV, session length, bounce rate

### 3. Social-Media and Sentiment Signals
Search X/Twitter, Reddit, Instagram, LinkedIn, YouTube, and local forums:

- Interaction data on the company's official accounts (followers/shares/comments trend)
- Heat and sentiment of organic user discussion (positive/negative/neutral)
- Assessments of the company by industry KOLs / influencers
- Sentiment hot-spots in the last 3 months
- List of negative sentiment events and the company's response
- Any insider (ex/current-employee) leaks?

### 4. Corporate-Registry and Legal Signals
Search Brazilian corporate/legal sources (Junta Comercial, Receita Federal CNPJ, JusBrasil, court dockets):

**Corporate-registry information**:
- Registered capital and change history
- Paid-in capital
- Shareholder / equity change records
- Subsidiary / affiliate list (new entity = new business? dissolution = business contraction?)
- Changes to the scope of business (new scope = new business direction)

**Legal information**:
| Type | Count | Summary of Important Cases |
|------|-------|----------------------------|
| Lawsuits as plaintiff | | |
| Lawsuits as defendant | | |
| IP disputes | | |
| Labor claims | | |
| Administrative penalties | | |
| Enforcement records | | |

- Details and potential financial impact of major litigation/arbitration
- Administrative-penalty records (environmental / tax / labor / data-security, etc.)

### 5. Supply-Chain and Partner Signals
- List of known core suppliers/partners
- Are suppliers listed? Do their filings mention collaboration data with this company?
- Tender/procurement information (government procurement portals, corporate tender platforms)
- Partner assessments and depth of collaboration

### 6. Domain and Digital Footprint
Search domain/subdomain information:
- List of domains the company registered (newly registered domains may hint at new business/products)
- Subdomain analysis (api.xx.com, pay.xx.com, etc. hint at business architecture)
- SSL-certificate information
- Trademark registrations at INPI (new trademarks = new brand/product line)

### 7. Industry-Conference and Exposure Signals
- Executive talks/attendance over the last 12 months
- Industry awards / media lists (did it enter "unicorn" or "most innovative" lists?)
- Interaction with government/industry associations (policy consultation, standard-setting participation)
- Trend in media-exposure frequency and quality

### 8. Secondary-Market Trading Signals (if any)
- Is there a secondary market for old shares (Forge, EquityZen, informal groups)?
- Implied valuation of secondary trades vs. the latest funding-round valuation
- Supply/demand between buyers and sellers
- Are many employees selling options/RSUs?

### 9. Signal Synthesis Scoring

| Signal Category | Direction (Pos/Neg/Neutral) | Strength (Strong/Med/Weak) | Confidence | Core Finding |
|-----------------|-----------------------------|----------------------------|------------|--------------|
| Hiring signals | | | | |
| Product data | | | | |
| Sentiment signals | | | | |
| Legal signals | | | | |
| Supply-chain signals | | | | |
| Digital footprint | | | | |
| Industry exposure | | | | |
| Secondary trading | | | | |

**Combined-signal judgment**: do the signals point in the same direction? Any contradictory signals?

### 10. Anomalous-Signal Checklist (most important)
List all "unusual" findings — these are often the most valuable information:
- Signals inconsistent with the company's public narrative
- Data that defies industry common sense
- Sudden changes (abrupt hiring freeze/expansion, dense executive departures, etc.)
- Unexplained phenomena
```

---

### Step 4: Launch 6 Parallel Agents

Use the Agent tool to launch 6 Agents at once (**they must be invoked in parallel within a single message**):

Each Agent's config:
- `subagent_type`: `general-purpose`
- `run_in_background`: `true`

Prompt template for each Agent:

```
You are the "{role name}" on the {Company} private-company research team.

You are researching a **private (non-listed) company**, which means:
- There are no standardized public filings; you must piece together information from multiple sources
- Data may be incomplete or contradictory; you must tag confidence
- More reasoning and reasonable estimation is required, but show the estimation process transparently
- Not finding information ≠ the information not existing; the information you do find may be biased

Complete the following research task: {task subject}

Specific requirements:
{contents of the task description}

**Research method**:
1. Prefer the analyst's MCP market-data tools (market-data server + finnhub) for market data and fundamentals; use WebSearch for the latest public information, searching at least 3-5 times per dimension with different keyword combinations
2. Search-keyword strategy:
   - Portuguese: company name + receita/valuation/rodada/usuários/MAU/IPO/prospecto/demissões
   - English: Company Name + revenue/valuation/funding/users/IPO/filing
   - Specific person's name + company name (management-related information)
   - Company name + specific competitor name (competitive dynamics)
3. Priority information sources:
   - High confidence: prospectus, CVM/regulatory filings, related-party disclosures in listed-company filings
   - Medium confidence: Brazil Journal, NeoFeed, Pipeline Valor, The Information, Bloomberg, Reuters, TechCrunch
   - Supplementary verification: LinkedIn, Glassdoor, Reclame Aqui, JusBrasil, Receita Federal (CNPJ)
4. Use WebFetch to retrieve the full text of key articles (don't rely on search snippets alone)
5. For important data, cross-verify with at least 2 different sources

**Data-annotation standard (strictly enforced)**:
- Tag every key data point with its source (down to the outlet name and article title)
- Tag the data's time (to the year and month)
- Tag confidence: 🟢 high (prospectus/official disclosure) / 🟡 medium (credible media/research) / 🔴 low (estimate/rumor)
- When sources conflict, **list them all** and explain the difference and your judgment
- Distinguish "fact" from "reasoning": facts in normal font, reasoning/estimates in *italics* with the estimation method noted
- Explicitly mark unavailable information as "data missing"; do not fabricate

**Output requirements**:
- The report must be thorough, using Markdown tables to present key data
- Each analysis dimension needs a clear conclusion and score
- The estimation process must be fully transparent (show the calculation logic and every assumption)
- At the end of the report, provide:
  1. This dimension's overall score (★1-5) and core judgment
  2. Self-assessment of information completeness for this dimension (sufficient / adequate / insufficient / severely insufficient)
  3. The 3 most important findings
  4. The biggest information blind spot (which missing information most affects the judgment)
```

### Step 5: Receive Reports and Track Progress

- Show the user a live progress table (which Agents are done, which are still researching)
- As each report arrives, update progress and show that report's core takeaways (3-5 points)
- Wait for all 6 reports to arrive

### Step 6: Cross-Verification and Information Jigsaw

**This is the most critical new step in the enhanced framework.** Before synthesis, the team-lead must:

1. **Data-conflict arbitration**:
   - Extract key data from each Agent's report
   - Identify whether the same data cited by different Agents is consistent
   - Arbitrate conflicting data: list all sources, state which is adopted and why

2. **Signal-consistency check**:
   - Business-growth signals (business-decoder) vs. hiring signals (signal-miner) — consistent? (if business is growing fast but hiring is shrinking, explain it)
   - Tech-leadership narrative (tech-ip) vs. patent/talent data (signal-miner) — supported?
   - Valuation level (financial-detective) vs. competitive position (competitive-mapper) — matched?
   - Management's public narrative (risk-governance) vs. actual action signals (signal-miner) — consistent?

3. **Information-jigsaw reconstruction**:
   - Combine the information fragments from the 6 reports; see whether a more complete picture emerges
   - Mark information "white zones" (confirmed known), "gray zones" (some clues but uncertain), "black zones" (entirely unknown)

4. **Anti-bias check**:
   - Check whether the report has a "detailed positives, brief negatives" bias
   - Confirm every positive judgment has a corresponding negative test

### Step 7: Synthesize the Final Report

Combine the 6 analysis reports into a final report with the following structure:

---

#### 1. One-Sentence Conclusion
> In one paragraph (50-100 words), summarize the **true-value judgment** of this private company: what the business is worth, and why.

#### 2. Company Snapshot
| Item | Content | Confidence |
|------|---------|------------|
| Company name | | |
| Founding year | | |
| Headquarters | | |
| Founder/CEO | | |
| Core business | | |
| Headcount | | |
| Latest valuation | | |
| Latest funding round | | |
| Estimated revenue scale | | |
| Estimated profitability status | | |
| Estimated user scale | | |
| Main investors | | |
| Corporate structure (holding co / dual-class) | | |

#### 3. Six-Dimension Scorecard
| Dimension | Analyst | Score (★1-5) | Core Judgment | Confidence | Info Completeness |
|-----------|---------|--------------|---------------|------------|-------------------|
| Business model & users | business-decoder | | | | |
| Financials & valuation | financial-detective | | | | |
| Industry & competition | competitive-mapper | | | | |
| Risk & governance | risk-governance-analyst | | | | |
| Technology & IP | tech-ip-analyst | | | | |
| Alternative-data signals | signal-miner | | | | |

Overall score: ★X / 5

#### 4. Key-Data Jigsaw (after cross-verification)
Integrate the data pieced together by each analyst; **keep only cross-verified data**:

| Metric | Data | # Sources | Source Detail | Confidence | Notes |
|--------|------|-----------|---------------|------------|-------|

#### 5. Signal-Consistency Matrix
| Check Item | Signal A | Signal B | Consistency | Interpretation |
|------------|----------|----------|-------------|----------------|
| Growth narrative vs. hiring trend | | | ✅/⚠️/❌ | |
| Tech-leadership narrative vs. patent data | | | | |
| Valuation level vs. competitive position | | | | |
| Management narrative vs. actual action | | | | |

#### 6. Per-Dimension Analysis Summary
For each dimension, extract the 3-5 most important findings (with source and confidence)

#### 7. True-Value Assessment

**Business-essence judgment**:
- What kind of business is this? (one sentence)
- How high is the "certainty" of this business?
- Duan Yongping-style judgment: is this a "right business"?

**Moat scorecard**:
| Moat Type | Score (★1-5) | Core Evidence | Trend | Durability |
|-----------|--------------|---------------|-------|------------|
| Network effects | | | Widening/stable/narrowing | |
| Switching costs | | | | |
| Brand mindshare | | | | |
| Data barrier | | | | |
| Regulatory license | | | | |
| Scale economics | | | | |
| Technical barrier | | | | |

**Valuation judgment**:
| Valuation Method | Valuation Range | Confidence | Notes |
|------------------|-----------------|------------|-------|
| Latest-round valuation (adjusted) | | | |
| Comparable companies | | | |
| DCF scenario analysis | | | |
| End-state market-cap back-out | | | |
| Transaction comparables | | | |

**Synthesized true-value range** (state currency explicitly; use R$ for BRL, note US$ for any USD figure):
- Conservative valuation (margin-of-safety): R$XX bn
- Reasonable valuation (base case): R$XX bn
- Optimistic valuation (best case): R$XX bn
- Current market valuation: R$XX bn
- **Margin of safety**: current valuation vs. conservative valuation = XX%

#### 8. Investment Thesis (Bull vs. Bear)
- 🟢 Bull logic (5-7 points, each with an evidence source)
- 🔴 Bear logic (5-7 points, each with an evidence source)
- ⚖️ Which side's argument is more persuasive? Why?

#### 9. Risk Matrix
| Risk | Probability | Impact | Overall Severity | Hedgeable? | Monitoring Metric |
|------|-------------|--------|------------------|------------|-------------------|

Top 3 core risks and mitigation strategies

#### 10. Exit-Path Assessment
Most likely exit route, time window, expected return

#### 11. Investment-Decision Table

**One-page decision table**:
```
┌──────────────────────────────────────────────┐
│  Company: XXX    Latest valuation: R$XXbn     │
│  Stage: [Seed/Growth/Mature/Pre-IPO]         │
│  Info completeness: [Sufficient/Adequate/      │
│                      Insufficient/Severe]      │
├──────────────────────────────────────────────┤
│  Core investment logic (3 sentences max):     │
│  1. ________________________________________  │
│  2. ________________________________________  │
│  3. ________________________________________  │
├──────────────────────────────────────────────┤
│  True-value judgment:                         │
│  Reasonable valuation range: R$XXbn - R$XXbn  │
│  Current vs. reasonable: expensive/fair/cheap │
│  Margin of safety: ____%                      │
├──────────────────────────────────────────────┤
│  Key assumptions & verification:              │
│  Assumption1 → metric → milestone → date      │
│  Assumption2 → metric → milestone → date      │
│  Assumption3 → metric → milestone → date      │
├──────────────────────────────────────────────┤
│  Fatal risks & "thesis broken" signals:       │
│  Risk1 → if X happens, conclusion flips → stop│
│  Risk2 → if Y happens, conclusion flips → stop│
├──────────────────────────────────────────────┤
│  Conclusion: Invest / Watch / Avoid           │
│  If watching: what triggers a re-evaluation?  │
│  Expected exit: IPO / M&A / secondary transfer│
│  Expected return multiple: X - Y ×            │
│  Expected time frame: X - Y years             │
│  Annualized return: X% - Y%                   │
└──────────────────────────────────────────────┘
```

**Tiered recommendations**:
| Investor Type | Recommendation | Rationale |
|---------------|----------------|-----------|
| PE/VC (lead) | | |
| PE/VC (follow-on) | | |
| Secondary-market transfer | | |
| Buy post-IPO | | |
| Not recommended | | |

**Key catalysts**:
| Bull Catalyst | Est. Timing | Bear Catalyst | Est. Timing |
|---------------|-------------|---------------|-------------|
| | | | |

#### 12. Information Blind-Spot Map
| Dimension | Known Information | Missing Information | Impact of Gap | Suggested Way to Obtain |
|-----------|-------------------|---------------------|---------------|-------------------------|

Do these blind spots affect the reliability of the core conclusion? If so, state explicitly: "with X information missing, the confidence of the above conclusion is Y."

#### 13. Ongoing-Tracking Checklist
| Tracking Item | Frequency | Information Source | Metric to Watch | Warning Threshold |
|---------------|-----------|--------------------|-----------------|-------------------|

#### 14. Concluding Paragraph
A 150-250 word final summary, including:
- The essence of this business
- The true-value judgment
- The reasonableness of the current valuation
- The greatest certainty and uncertainty
- The final recommendation and its core rationale

---

### Step 8: Save the Report

Write the complete final report to `reports/{Company}/{Company}-private-{YYYYMMDD}.md` (English/latin company name).

### Step 9: Clean Up the Team

Use TeamDelete to clean up team resources.

---

## Important Notes

1. **The 6 Agents must be launched in parallel** — invoke the Agent tool 6 times in a single message
2. **Confidence tagging** — private-company data sources vary in quality; every key data point must be tagged with source and confidence
3. **Estimates must be transparent** — show the calculation logic for every estimate; never conjure numbers
4. **Cross-verification** — key data with at least 2 sources; when sources conflict, list them all
5. **Signal-consistency check** — the synthesis stage must run a cross-dimension signal-consistency check
6. **Conclusions must be clear** — don't dodge the invest/watch/avoid recommendation, but state the confidence of the conclusion
7. **Be patient** — 6 Agents take several minutes; update the user on progress in real time
8. **Bilingual search** — private-company information may be spread across Portuguese and English media; search in both languages
9. **Core anti-bias principle** — little material ≠ a bad company; a short AI analysis ≠ low investment certainty. For companies with extremely scarce information, switch to "first-principles mode" focused on core questions rather than chasing a formally complete report
10. **Honest blanks** — clearly distinguish "evidence-based analysis" from "speculative filler"; it is acceptable to write "this dimension has insufficient data to give a meaningful conclusion"
11. **Alternative data is not noise** — hiring, patents, litigation, app data, and other alternative data may be closer to true operating conditions than news coverage
12. **True-value orientation** — the ultimate goal is to judge what this business is worth, not to output a good-looking report. If information is insufficient for a reliable valuation, say directly "insufficient information, cannot give a reliable valuation"
