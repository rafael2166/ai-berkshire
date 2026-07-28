# Supply-Chain Bottleneck Hunter: AI-Driven Global Value-Chain Bottleneck Arbitrage

Run a supply-chain bottleneck scan and arbitrage-opportunity search on the $ARGUMENTS super-trend.

## Core Idea

Don't ask "what stock does AI recommend"; ask "if this trend keeps expanding, which link runs short first?"

Traditional research fixates on leaders and known arenas. This system reverses that: **start from the physical chokepoints of the supply chain and find the companies nobody watches but that, the moment they run out of stock, force the entire industry to stop and wait.**

Source of excess return: the first-layer bottlenecks (GPUs, HBM, power) are already fully priced. The real alpha is in the **second and third layers** — optical modules, lasers, InP substrates, SOI wafers, epitaxy equipment, wafer-level test, IC substrates, specialty glass fiber, and so on.

---

## Step 1: Super-Trend Confirmation

### 1.1 Trend Screening Criteria

Don't chase hallucinations inside minor fads; pursue only super-trends that meet all of the following:

| Criterion | Requirement | Validation Method |
|-----------|-------------|-------------------|
| Durability | At least 3-5 years of near-certain growth | Search industry forecasts and capex plans |
| Physicality | Requires building real hardware / materials / equipment | Distinguish "software upgrade" from "physical build-out" |
| Scale | Global capex > US$50bn / year | Search leading players' capex guidance |
| Acceleration | Demand growth > supply expansion speed | Compare demand growth rate vs. capacity expansion plans |

### 1.2 Currently Tracked Super-Trend List

Update on each run; initial list:

1. **AI infrastructure build-out** — data centers, GPU clusters, network interconnect, power
2. **Energy transition** — nuclear restart, grid upgrades, energy storage
3. **Defense modernization** — Western defense-spending upcycle, supply-chain reconfiguration
4. **Semiconductor reindustrialization** — US/EU/Japan subsidized fab construction, equipment/material bottlenecks
5. **Space economy** — satellite internet, surging launch cadence

If the user specifies a concrete trend (e.g., "AI infrastructure"), focus only on that trend.

### 1.3 Trend-Validation Output

```
Trend name:
Core driver: (one sentence)
Validation events that have already happened (at least 3):
  1. [date] [event] [source]
  2.
  3.
Capex scale: global ~US$XXbn / year, growth YY%
Supply-demand gap judgment: demand growth > supply expansion speed? Yes / No / Uncertain
Trend confirmation: ✅ trackable / ❌ insufficient evidence, do not track for now
```

---

## Step 2: Physical Decomposition of the Supply Chain

### 2.1 Layered Decomposition Framework

**Don't stop at the concept layer; decompose to physical entities.**

```
Layer 0 (end): final product / service
    │
Layer 1 (core components): core hardware already fully in market focus
    │                 ⬆ fully priced, limited alpha
    │─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
    │                 ⬇ low attention, alpha-concentrated zone
    │
Layer 2 (sub-components / materials): the parts and materials that support the core components
    │
Layer 3 (upstream equipment / raw materials): the equipment and raw materials needed to make the sub-components
    │
Layer 4 (infrastructure): power, cooling, land, talent, certification
```

### 2.2 Decomposition Template, Using AI Infrastructure as an Example

```
Layer 0: AI model training / inference services
Layer 1: GPU / accelerators, HBM memory, servers, data centers
Layer 2 (priority scan zone):
  ├─ Network interconnect: optical modules, optical fiber, switch chips, copper cables
  ├─ Optical-comms core: lasers (EML/VCSEL/CW), modulators, photodetectors
  ├─ Semiconductor materials: InP substrates, GaAs substrates, SOI wafers, SiC substrates
  ├─ Advanced packaging: CoWoS interposers, HBM TSV, ABF substrate film
  ├─ PCB / substrates: high-frequency high-speed PCB, IC substrates, specialty glass-fiber cloth
  ├─ Test: wafer-level test (probe cards), burn-in test, ATE
  ├─ Thermal / cooling: liquid-cooling systems, CDU, immersion coolant
  └─ Power connection: busways, UPS, distribution cabinets, transformers
Layer 3:
  ├─ Epitaxy equipment: MOCVD, MBE
  ├─ Litho / etch: specialty-wavelength lithography, InP etch
  ├─ Raw materials: high-purity metals (indium, gallium, germanium), specialty gases, sputtering targets
  └─ Certification / standards: MSA standards, Telcordia certification
Layer 4:
  ├─ Power: nuclear, natural-gas generation, transmission & distribution
  ├─ Cooling water / thermal infrastructure
  └─ Data-center land / permits
```

### 2.3 Decomposition of Other Trends

Run a similar decomposition for each confirmed super-trend. Use WebSearch to search:
- "{trend} supply chain bottleneck 2026"
- "{trend} shortage critical component"
- "{trend} capacity constraint"
- "{trend} sole source supplier"

---

## Step 3: Bottleneck Identification — Finding the "Chokepoint"

### 3.1 Six Bottleneck Criteria

For each link in Layers 2-3, evaluate one by one:

| # | Criterion | Question | Score |
|---|-----------|----------|-------|
| 1 | **Supply concentration** | Are there ≤ 3 suppliers globally? | 🔴 ≤ 2 / 🟡 3-5 / 🟢 > 5 |
| 2 | **Expansion cycle** | How long to add new capacity? | 🔴 > 2 yrs / 🟡 1-2 yrs / 🟢 < 1 yr |
| 3 | **Substitution difficulty** | Can another technology / material substitute? | 🔴 not substitutable / 🟡 partly / 🟢 easily |
| 4 | **Capacity utilization** | Current utilization? | 🔴 > 90% / 🟡 70-90% / 🟢 < 70% |
| 5 | **Demand growth** | Downstream demand growth? | 🔴 > 50%/yr / 🟡 20-50% / 🟢 < 20% |
| 6 | **Customer qualification cycle** | How long to qualify a new supplier? | 🔴 > 1 yr / 🟡 6-12 mo / 🟢 < 6 mo |

**Bottleneck rating**:
- 🔴🔴🔴 ≥ 4 → **S-class bottleneck** (single-point-of-failure level, highest priority)
- 🔴🔴 3 → **A-class bottleneck** (severely constrained)
- 🔴 1-2 → **B-class bottleneck** (under pressure but manageable)
- No 🔴 → not a bottleneck, skip

### 3.2 Bottleneck-Map Output

```
Supply-chain bottleneck map — {trend name}
Update date: YYYY-MM-DD

S-class bottlenecks (single point of failure):
  1. [link name] — [one-line reason] — suppliers: [company list]
  2.

A-class bottlenecks (severely constrained):
  1.
  2.

B-class bottlenecks (under pressure):
  1.
  2.

Recent changes (vs. last scan):
  - [added / upgraded / downgraded / resolved] [link name] — [reason]
```

---

## Step 4: Company Screening — From Bottleneck to Target

### 4.1 For Each S-Class and A-Class Bottleneck, Find All Relevant Listed Companies

Search approach:
- WebSearch "{bottleneck link} supplier listed company"
- WebSearch "{bottleneck link} manufacturer stock"
- WebSearch "{bottleneck product} market share company"

Prefer the analyst's MCP market-data tools (market-data server + finnhub) for prices, market cap, and fundamentals; use WebSearch / WebFetch for the qualitative search above.

### 4.2 Initial Screen (quick filter)

| Criterion | Requirement | Rationale |
|-----------|-------------|-----------|
| Listing status | Listed (B3 / Brazil, US, or other international market) | Tradable |
| Bottleneck-business share | > 30% of revenue from the bottleneck link | Purity |
| Market cap | Prefer < US$10bn | Large caps already fully priced |
| Liquidity | Average daily turnover > US$1m | Can enter and exit |

### 4.2.1 Valuation Check (mandatory, do not skip)

**A real bottleneck ≠ an investment opportunity.** You must compute P/S and P/E for every company and note them in the report. Use a combination of conditions to judge whether valuation is overextended:

#### Valuation Red Light (any one met → signal strength capped at ★★, flag "⚠️ valuation overextended")

1. **Market cap > 20% of TAM**: the company's market cap already exceeds 20% of its addressable market, meaning growth expectations are over-internalized
2. **P/S > 30x and revenue growth < 100%**: high valuation but growth insufficient to support it. Companies with growth > 100% are exempt from the P/S red line but still get flagged "⚠️ high valuation requires sustained high growth to validate"
3. **Market cap > 10x a 5-year optimistic revenue forecast**: even if the most optimistic assumptions all come true, the current pricing is still too high
4. **Share price doubles within 60 days of a secondary offering**: clearly sentiment-driven, downgrade signal strength by one level

#### Valuation Yellow Light (needs extra explanation, otherwise downgrade)

1. **Loss-making + P/S > 15x**: may enter ★★★ but must explain the path and timeline to profitability
2. **P/S ≥ 5x that of a profitable peer**: must explain the source of the premium (market share, growth differential, barrier differential)
3. **P/E > 80x**: compute PEG and explain whether growth supports it

#### Valuation Green Light (bonus)

- P/S < 10x and revenue growing → signal strength may add one level
- P/E < 30x and has a moat → flag "valuation has a margin of safety"

#### Valuation-Reasonableness Test (mandatory)

For each target, answer: "Buying at the current market cap, assuming the most optimistic scenario fully plays out and I exit at 25x P/E in 10 years, what is my annualized return?" Annualized return < 10% → flag "current price offers no margin of safety".

**Note**: the purpose of the valuation check is to prevent obvious mistakes like recommending "a loss-making company at 100x P/S", not to exclude every high-valuation early-stage company. The key is whether growth, TAM, and competitive structure can support the current valuation — this requires specific analysis, not a blanket rule.

**Getting data for individual tickers**: a supply-chain scan often lands on international names in multiple currencies. Pull price / P/E / market cap / revenue via the analyst's MCP market-data tools (market-data server + finnhub) or WebFetch of the company's IR page, and cross-verify per skills/financial-data.md. For B3-listed names, verify market cap by hand (share price × shares outstanding) and state the currency in BRL (R$); note the USD ADR line where one exists. For monthly-revenue disclosures, year-over-year monthly revenue is the fastest public signal that a bottleneck is producing "rising volume and price" together.

### 4.3 Deep-Screening Dimensions

For companies that pass the initial screen, evaluate each:

```
## {Company} ({Ticker})

**Bottleneck positioning**:
- Specific position in the supply chain
- Market share: #X globally, XX% share
- Customer list (known)

**Capacity and expansion**:
- Current capacity / utilization
- Expansion plan / timeline
- Capital needed for expansion vs. cash on hand

**Financial snapshot**:
- Market cap / revenue / profit / growth
- Bottleneck-business revenue share
- Gross-margin trend (the tighter the bottleneck, the more gross margin should rise)

**Risk checklist**:
- [ ] Substitution risk: can it be bypassed?
- [ ] Dilution risk: any large secondary offerings / convertibles?
- [ ] Geopolitical risk: located in a sensitive region / under export controls?
- [ ] Management risk: any bad track record?
- [ ] Customer-concentration risk: overly dependent on a single customer?
- [ ] Valuation overextension: does the current valuation already price in 3 years of growth?

**Bottleneck-durability judgment**:
- When will this bottleneck be resolved?
- After it is resolved, what does this company still have?
- Is it one-off or persistent?
```

---

## Step 5: Cross-Verification — Don't Listen to Just One Story

### 5.1 Positive Verification

| Verification Item | Question | Search Method |
|-------------------|----------|---------------|
| Customer verification | Have leading customers signed / designed in? | Search company announcements, mentions in customer filings |
| Revenue verification | Is the bottleneck already reflected in revenue growth? | Search the last 2-3 quarters of filings |
| Price verification | Are product prices rising? | Search industry quotes, analyst reports |
| Capacity verification | Is capacity genuinely tight? | Search lead-time data, customer complaints |
| Capital verification | Is there expansion capex? | Search company capex guidance |

### 5.2 Reverse Verification (Munger-style negation)

| Reverse Question | Meaning |
|------------------|---------|
| Why don't smart people buy this stock? | Find the known bearish arguments |
| Can this bottleneck be bypassed? Any alternative route? | Technology-route risk |
| Can competitors replicate the capacity quickly? | Supply-shock risk |
| If end demand slows 50%, what happens to this company? | Downside sensitivity |
| Has management diluted via offerings at highs in the past? | Management trustworthiness |
| What growth assumptions does the current valuation imply? | Valuation reasonableness |

### 5.3 Signal Cross-Verification

- Are multiple companies in the same bottleneck all rising? (industry verification)
- Are downstream customers mentioning supply tightness in their filings? (customer verification)
- Do industry associations / research firms have relevant data? (third-party verification)

---

## Step 6: Output — Bottleneck-Opportunity Board

### 6.1 Bottleneck-Opportunity Ranking Table

| Rank | Company | Ticker | Market Cap | Annual Revenue | P/S | P/E | Bottleneck Link | Bottleneck Rating | Market Share | Revenue Growth | Signal Strength | Valuation Verdict |
|------|---------|--------|------------|----------------|-----|-----|-----------------|-------------------|--------------|----------------|-----------------|-------------------|
| 1 | | | | | x | x | | S/A | | | ★1-5 | fair / high / overextended |

**Required fields**: market cap, annual revenue, P/S, P/E are mandatory and may not be skipped with "to be verified". If financial data cannot be obtained, signal strength may not exceed ★★.

Signal-strength rating (the valuation-check result directly affects the rating):
- ★★★★★ multiple cross-verifications, customer designed in, revenue already reflected, valuation green light (reasonable P/S + profitable or near-profitable)
- ★★★★ most verifications pass, valuation green or yellow light (needs explanation)
- ★★★ logic holds but partly unverified, valuation yellow light acceptable (e.g., high-growth early-stage company)
- ★★ early signal, or bottleneck logic holds but valuation red light (market cap > 20% of TAM, P/S > 30x with insufficient growth, market cap far exceeds 5-year forecast, etc.)
- ★ pure concept, unverified

### 6.2 One-Pager per Opportunity

```
🎯 {Company} ({Ticker}) — {one-line bottleneck positioning}

Why it's a bottleneck:
(2-3 sentences explaining why this link is a chokepoint)

Why this company:
(2-3 sentences explaining why this one and not another)

Catalyst timeline:
- Near term (1-3 mo): [specific event, e.g., earnings, capacity ramp, customer qualification]
- Medium term (3-12 mo): [industry trend, expansion milestone]

Main risks:
1.
2.

Key data: market cap $XX / annual revenue $XX / P/S Xx / P/E Xx / revenue growth XX% / bottleneck-business share XX%

Valuation margin-of-safety test: buy at current market cap, exit at 25x P/E in 10 years — requires net income of $XX, corresponding to annual revenue of $XX (X times today's), annualized return XX%. Conclusion: has / lacks margin of safety.

Cross-verification status: ✅ customer verified / ✅ revenue verified / ✅ valuation reasonable / ⚠️ valuation overextended / ❌ unverified items

Conclusion: worth deep research / add to watchlist / do not track for now
```

### 6.3 Action Recommendations

| Target | Recommended Action | Rationale |
|--------|--------------------|-----------|
| A | Run `/investment-team` for deep research | S-class bottleneck + multiple verifications |
| B | Add to watchlist, wait for next-quarter earnings | Logic holds but revenue not yet reflected |
| C | Do not track for now | Substitution-technology risk too high |

---

## Step 7: Incremental Update — Dynamic Maintenance of the Bottleneck Map

### 7.1 Incremental Update on Each Run

1. Check whether identified bottlenecks still hold
   - Have new suppliers entered?
   - Has capacity expanded enough to resolve the bottleneck?
   - Has substitution technology broken through?

2. Scan for newly emerging bottlenecks
   - Search the last 7 days of supply chain / shortage / bottleneck news
   - Check supply-chain-related disclosures during earnings season

3. Update bottleneck ratings (upgrade / downgrade / resolve)

### 7.2 State Files

Maintain in the `reports/bottleneck-map/` directory:
- `master-map.md` — master bottleneck map (continuously updated)
- `watchlist.md` — watchlist (continuously updated)
- `YYYY-MM-DD/` — one folder per day, containing all scan reports for that day
- `deep-dive/` — separate files for companies analyzed in depth

---

## Hourly Scan Mode (for scheduled tasks)

Run once per hour, using a "only issue a report when there's something" mode:

### Scan Flow (hourly)

1. **News scan**: search the last 1-2 hours of supply-chain-related news
   - Keywords: supply chain bottleneck, shortage, capacity constraint, allocation, lead time, sole source, gargalo (Portuguese: bottleneck), desabastecimento, capacidade, reajuste de preço
   - Coverage: English + Portuguese sources
2. **Market signals**: check tracked companies' price changes (watch abnormal moves > 5% in particular)
3. **Earnings / announcements**: check whether any bottleneck-related company has released earnings or a major announcement
4. **Valuation opportunities**: check whether any watchlist company has entered a buy range due to a broad-market selloff or similar
5. **Decide whether to issue a report**:
   - New bottleneck signal, a clear target opportunity, or a major status change → **issue a report**
   - No new findings → **no report**, only log "no new signals this round"

### Report Output Rules

**One folder per day**: `reports/bottleneck-map/YYYY-MM-DD/`

**File-naming rules** (so you can tell at a glance from the filename whether there's a target):

| Situation | Filename Format | Example |
|-----------|-----------------|---------|
| A clear target found | `HH-MM-ticker1-ticker2.md` | `09-00-WEGE3-ITUB4.md` |
| Bottleneck signal but no clear target | `HH-MM-signal-scan.md` | `14-00-signal-scan.md` |
| No new findings | No file generated | — |

**A ticker in the filename = a company that passed the valuation check and is worth deep research.** Companies that appeared only in the signal-scan stage but failed the valuation check are not put in the filename.

### Report Template (with a target)

```markdown
# Bottleneck Hunter — YYYY-MM-DD HH:MM

## Clear Targets

### {Company} ({Ticker}) — {one-line bottleneck positioning}

**Why it's worth attention now**: (the specific event / data change that triggered this attention)

**Bottleneck positioning**: Layer X, {link name}, bottleneck rating S/A/B
**Financial snapshot**: market cap $XX / annual revenue $XX / P/S Xx / P/E Xx / revenue growth XX%
**Valuation check**: red / yellow / green light (with specifics)
**Valuation margin of safety**: 10-year 25x-P/E exit method, annualized return XX%

**Bull case** (2-3 points):
1.
2.

**Bear case** (2-3 points):
1.
2.

**Recommendation**: run deep research / add to watch / wait for a better price

---

## Other Signals (no clear target)

| Link | Signal | Source | Preliminary Judgment |
|------|--------|--------|----------------------|

## Watchlist Status Changes

(upgrade / downgrade / add / remove; write "no change" if none)
```

### Report Template (signal scan only)

```markdown
# Bottleneck Hunter Signal Scan — YYYY-MM-DD HH:MM

## New Signals

| Link | Signal Description | Source | Investable Target? | Next Step |
|------|--------------------|--------|--------------------|-----------|

## Watchlist Status

No change / changed (list)
```

---

## AI Research-Bias Awareness

| Bias | Manifestation | Countermeasure |
|------|---------------|----------------|
| Leader preference | Search results dominated by large-caps | Deliberately search small-cap suppliers, add "small cap" keyword |
| English-language preference | Miss non-US suppliers | Must also search Brazilian / Latin American and other regional markets' suppliers |
| Narrative preference | Drawn to the "AI concept" label | Look only at the actual supply-chain position, not the market label |
| Confirmation bias | After finding a bottleneck, look only for supporting evidence | Force reverse verification (Step 5) |
| Recency / staleness bias | Rely on outdated information | Prioritize data from the last 30 days |

---

## Core Principles (Highest Priority)

1. **Don't let AI recommend stocks; let AI decompose supply chains** — the question matters more than the answer
2. **Physical first** — focus only on links that require real physical products / materials / equipment
3. **Second and third layers** — don't chase already-fully-priced leaders
4. **Cross-verify** — at least 2 independent sources per conclusion
5. **Be honest about uncertainty** — if you can't find data, write "insufficient data"; don't fill with speculation
6. **Bottlenecks are time-limited** — every bottleneck gets resolved; the key is judging the time window
7. **Small-cap ≠ good opportunity** — a small-cap can also be a bad company; it must pass the financial-quality gate
8. **A real bottleneck ≠ an investment opportunity** — a company can sit on the tightest bottleneck, but if P/S > 30x or it's still loss-making, the current price is not a buy point. **Valuation is a hard gate that cannot be overridden by bottleneck purity, signal strength, or narrative appeal.** Better to miss a bottleneck stock that has already run than to buy a loss-making company at 100x P/S
9. **Follow the CLAUDE.md objectivity principles** — no preset bullishness; data first, then conclusion

---

## Output Requirements

1. **Report location**:
   - Full scan: `reports/bottleneck-map/{Trend}-bottleneck-{YYYYMMDD}.md`
   - Daily scan: `reports/bottleneck-map/daily/{YYYY-MM-DD}-{am/pm}.md`
   - Master bottleneck map: `reports/bottleneck-map/master-map.md`
   - Watchlist: `reports/bottleneck-map/watchlist.md`
2. **Language**: English — write the report in English
3. **Style**: direct, sharp, no filler
4. **Data**: cite the source of all data; label estimates "estimate"
5. **No preset stance**: first present data → derive logic → reach conclusion
6. **Both sides**: attach counter-evidence to every core judgment
