# Earnings Review Team: Four Masters Reading in Parallel

Run a team-based deep earnings review of $ARGUMENTS. Four masters read the filing in parallel, and the Team Lead synthesizes their work into a single research report.

**Supported input formats**: `Company Quarter`, e.g. `Petrobras 2025Q4`, `Vale 2025 Annual Report`, `Itau latest`

Default market is Brazil / B3. Default tickers are B3 (e.g. PETR4, VALE3, ITUB4, BBAS3, WEGE3, ABEV3). Currency is BRL (R$); state it explicitly and note USD ADRs where relevant.

## Design Philosophy

A good earnings analysis has to solve one core problem: **understanding the future for yourself** — which requires deep research from several different perspectives.

This Skill runs in two stages:
- **Stage 1 · Research**: the four masters read the filing in parallel (Duan Yongping reads the nature of the business, Buffett audits earnings quality, Munger reads the shift in competition, Li Lu hunts for risk signals).
- **Stage 2 · Synthesis**: the Team Lead integrates the four perspectives into a single research report.

---

## Stage 1: Four Masters Researching in Parallel

### Step 1: Obtain Primary Sources

Use the Agent tool to launch background Agents **in parallel** to obtain the following raw materials:

| Material Type | Source | Priority |
|---------------|--------|----------|
| Original filing | Company RI site; CVM via the RAD portal (www.rad.cvm.gov.br) for Brazilian issuers; SEC (EDGAR) for US-listed ADRs; market data via B3 | Highest |
| Earnings-call transcript | Company RI site; earnings-call providers; reputable financial-news sources | Highest |
| Management letter to shareholders | Extracted from the annual report | High (annual reports only) |
| Prior-period filing / call | Same as above | High (used for promise tracking) |

The analyst also has MCP market-data tools available (a market-data server plus finnhub) as well as WebSearch/WebFetch; prefer those for pricing, fundamentals, and filings discovery.

**Source-availability rating**:

| Grade | Characteristics | Impact |
|-------|-----------------|--------|
| A | Complete original filing obtained | Execute all steps normally |
| B | Only partial original text or a third-party summary | Flag as "not a primary source"; reduce the weight of footnote analysis |
| C | Only news reports and data-website summaries | Focus on core data changes, skip footnote mining, flag as "insufficient primary sources" |

Communicate the source-availability rating to each Agent; it affects the depth of their analysis.

### Step 2: Present the Team Framework to the User

| Stage | Role | Master / Positioning | Core Task |
|-------|------|----------------------|-----------|
| Research | **Team Lead** (yourself) | Overall coordination | Coordinate, synthesize, finalize |
| Research | Business-nature reader | Duan Yongping | Did the business get better or worse? |
| Research | Financial-quality auditor | Warren Buffett | Is it earning real money or fake money? |
| Research | Competition-shift reader | Charlie Munger | How is the competitive landscape changing? |
| Research | Risk-signal hunter | Li Lu | What is management hiding? |

### Step 3: Launch the 4 Parallel Research Agents

Use the Agent tool to launch 4 background Agents in a **single message**.

---

#### Agent 1: Reading the Nature of the Business (Duan Yongping's Lens)

**Core question: Did the business reflected in this filing get better or worse?**

> Duan Yongping: "Investing is buying a business. Reading a filing isn't about reading numbers — it's about whether the business has changed."

Analysis content:

1. **Revenue-mix breakdown and interpretation**
   - Revenue by segment/geography — which parts are accelerating, which are slowing.
   - Don't just list numbers — what business logic does each segment reflect?
   - Is revenue growth coming from "volume" or "price"? Which is healthier?

2. **Change in user/customer value**
   - Changes in operating metrics such as DAU/MAU/paying users.
   - Quality metrics such as time spent, ARPU, and retention.
   - Is the value of the platform/product to users strengthening or weakening?

3. **Moat check**
   - Does the change in gross margin reflect stable pricing power?
   - Does the change in market share reflect an effective competitive barrier?
   - Any sign that switching costs / network effects are being eroded?

4. **"Good business" test**
   - Duan Yongping's three conditions: differentiation, pricing power, sustainable competitive advantage — how did they change this period?
   - Is the business getting "heavier" or "lighter"?
   - If the company shut down tomorrow, would users be in real pain? Did this filing change that?

5. **Management's product instinct**
   - When management discusses product/users, is the language concrete or bureaucratic?
   - Any impressive product insight, or any worrying sign of disconnection?

**Output requirement**: mark each sub-item 🟢 improving / 🟡 flat / 🔴 deteriorating, and give a Duan Yongping-style summary comment.

---

#### Agent 2: Financial-Quality Audit (Buffett's Lens)

**Core question: Is this company earning real money or fake money? Did the margin of safety change?**

> Buffett: "The first thing I do with every filing is turn to the cash-flow statement."

Analysis content:

1. **Extraction and verification of core financial data**
   - Revenue, gross profit, operating profit, net income — both GAAP/IFRS and non-GAAP/adjusted.
   - GAAP vs. non-GAAP gap: how large, where it sits, and whether it is widening or narrowing.
   - Cross-validate key figures against at least two sources.

   ```bash
   python3 tools/financial_rigor.py cross-validate \
     --metric "revenue" --values {value1} {value2} --sources "{source1}" "{source2}"
   ```

2. **Cash-flow analysis (most important)**
   - Operating cash flow vs. net income ratio (>100% good, <80% caution).
   - Free cash flow = operating cash flow − capex.
   - Capex composition: maintenance vs. expansion.
   - Buyback and dividend amounts.

3. **Earnings-quality checks**
   - Receivables growth vs. revenue growth.
   - Inventory growth vs. revenue growth.
   - Trend in the gap between operating cash flow and net income.
   - Any sudden increase in capitalized expenditure.
   - Share of non-recurring gains.

4. **Balance-sheet health**
   - Change in net cash / net debt.
   - Change in days-receivable / days-inventory turnover.
   - Impairment risk in goodwill and intangibles.

5. **Valuation and margin-of-safety update**

   ```bash
   python3 tools/financial_rigor.py verify-market-cap \
     --price {price} --shares {shares} --reported {reported market cap} --currency {currency}
   python3 tools/financial_rigor.py verify-valuation \
     --price {price} --eps {EPS} --bvps {book value per share}
   python3 tools/financial_rigor.py three-scenario \
     --price {price} --eps {EPS} --shares {shares, billions} \
     --growth {bull} {base} {bear} --pe {bull PE} {base PE} {bear PE}
   ```

**Output requirement**: attach the tool output for every calculation, mark earnings-quality with 🟢/🟡/🔴 signal lights, and give a Buffett-style summary comment.

---

#### Agent 3: Reading the Competitive Landscape (Munger's Lens)

**Core question: What does this filing reveal about changes in the competitive landscape?**

> Munger: "I want to know where I'm going to die, so I'll never go there."

Analysis content:

1. **Infer competitive changes from the filing's data**
   - Revenue growth vs. industry growth — outperforming or lagging?
   - Change in gross margin reflecting intensifying/easing competition.
   - Change in the marketing-expense ratio — does it cost more to acquire customers now?
   - R&D spend — proactive investment or forced follow-through?

2. **Same-period comparison against competitors**
   - Compare key metrics against major competitors for the same period (where published).
   - Compare growth, margins, and investment intensity.
   - Who is winning? Who is losing?

3. **Management's discussion of competition**
   - How is the competitive environment described on the call?
   - Any competitors named? Is the tone confident or anxious?
   - Any new competitive threat?

4. **Industry-trend signals**
   - Impact of technological change (AI/new platforms, etc.).
   - Impact of regulatory change on the competitive landscape.
   - Consumer/demand-side trends.

5. **Munger-style inversion**
   - What would kill this company? Does this filing point to any of those threats?
   - Looking back in 5 years, will this filing be a "turning point"?

**Output requirement**: a competitive-landscape verdict (strengthening/flat/deteriorating), a competitor-comparison table, and a Munger-style inversion comment.

---

#### Agent 4: Risk-Signal Hunter (Li Lu's Lens)

**Core question: What is management hiding in this filing? Which signals are flashing?**

> Li Lu: "The most important thing in investing is to avoid permanent loss of capital."

Analysis content:

1. **Management-tone analysis**
   - Read the management discussion and call remarks paragraph by paragraph, flagging signals:
   - 🟢 candor signal (proactively admits problems) / 🟢 clarity signal (quantified targets)
   - 🔴 vagueness signal (empty talk) / 🔴 deflection signal (answering a different question) / 🔴 externalizing blame

2. **Promise tracking**
   - Management's specific commitments last period vs. what was actually delivered this period, item by item.
   - Duan Yongping: "To judge whether management is reliable, check whether they did what they said they would."

3. **Footnotes and hidden information**
   - Related-party transactions, dilution from share-based comp, contingent liabilities.
   - Accounting-policy changes, segment-margin differences.
   - Changes in customer/supplier concentration.

4. **Selected earnings-call Q&A**
   - The 3-5 sharpest analyst questions and a quality score for management's answers.

5. **Permanent-loss risk**
   - Any signal that could lead to permanent loss of capital?
   - New developments in regulatory/compliance/litigation risk.
   - Any irreversible wrong decision by management?

**Output requirement**: a management-credibility score ★1-5, a promise-fulfillment rate, a risk-signal checklist, and a Li Lu-style summary comment.

---

### Step 4: Track Progress

Show the user live progress:

```
📊 {Company} {Period} Earnings Review Progress
━━━━━━━━━━━━━━━━━━━━━━━
Stage 1 · Research
  ☐ Duan Yongping · Business nature   ⏳ Analyzing...
  ☐ Buffett · Financial quality       ⏳ Analyzing...
  ☐ Munger · Competitive landscape    ⏳ Analyzing...
  ☐ Li Lu · Risk signals              ⏳ Analyzing...
Stage 2 · Synthesis                   ⏸ Waiting
```

As each report arrives, update progress and show its core findings (3-5 items).

---

## Stage 2: Team Lead Synthesizes the Research Report

Once all 4 research reports are in, the Team Lead integrates them into the final research report.

**Synthesis principles** — this is not stapling reports together; it is finding intersections and contradictions:

1. **Points of consensus across the four perspectives**: conclusions all four masters agree on carry the highest confidence.
2. **Points of contradiction across the four perspectives**: e.g. Duan Yongping says the business improved but Munger says competition is deteriorating — this kind of contradiction is the most valuable analysis.
3. **The overlooked corner**: what none of the four emphasized — could that be exactly the most important thing?

#### Research-Report Structure

```markdown
# {Company} {Period} Earnings Review Report
**Four Masters Reading in Parallel | {Date}**

## 1. One-Sentence Conclusion
> 50-100 words: beat/in line/miss, the core change, and the impact on the investment thesis.

## 2. The 3 Most Important Changes This Period
Focus on the changes that truly matter; don't list data. Under 100 words each.

## 3. Four-Masters Scorecard
| Perspective | Master | Core Question | Conclusion | Score | vs. Prior |
|-------------|--------|---------------|------------|-------|-----------|

## 4. Core Data at a Glance
Key financial and operating metrics table (current vs. prior vs. YoY)

## 5. Deep Analysis by Perspective
The 3-5 most important findings for each perspective

## 6. Management Tone and Promise Tracking
Promise-fulfillment table + tone-change analysis

## 7. What Would the Four Masters Do?
| Master | If Holding | If Not Holding | Rationale |

## 8. Conclusion
1. Beat / in line / miss?
2. Thesis impact: reinforced / no impact / weakened / broken
3. Next catalyst
4. Action recommendation
```

---

## Output Files

Use English/latin folder names.

```
reports/{Company}/
├── {Company}-earnings-{Period}.md              ← Final synthesized research report
├── {Company}-earnings-{Period}-DuanYongping.md ← Reading of the business nature
├── {Company}-earnings-{Period}-Buffett.md      ← Financial-quality audit
├── {Company}-earnings-{Period}-Munger.md       ← Reading of the competitive landscape
└── {Company}-earnings-{Period}-LiLu.md         ← Risk-signal analysis
```

Example: `reports/Petrobras/Petrobras-earnings-2025Q4.md`

## Data Spot-Check (Release Gate)

Run the spot-check on the final report:

```bash
python3 tools/report_audit.py extract \
  --report reports/{Company}/{Company}-earnings-{Period}.md

python3 tools/report_audit.py verdict \
  --results '<completed JSON>' \
  --report {report filename}
```

**[PASS]** all items pass → releasable; **[RETURN]** any item fails → fix and re-audit.

## Relationship to Other Skills

| Skill | Positioning | When to Use |
|-------|-------------|-------------|
| `/earnings-review` | Single-Agent deep earnings review | A quick pass from a single perspective |
| **`/earnings-team` (this Skill)** | **Four-Agent team deep read + synthesized report** | **Key filings for important companies, when depth is needed** |
| `/investment-team` | Four-Agent full company research | First time researching a company |

## Key Principles

- **Read the original, not the summary**: obtain primary sources by every means possible.
- **Four perspectives, not four departments**: they must cross-check and challenge each other, not each speak in isolation.
- **The Team Lead's value is integrated judgment**: find the intersections and the contradictions, not a staple job.
- **Conclusions must be clear**: no "overall broadly in line but with a few points worth watching".
- **Contrarian testing throughout**: every positive finding comes with counter-evidence.
- **Objectivity**: separate fact from opinion; present both sides; be honest about uncertainty; cite sources (at least 2 for key data); use ★ ratings (1-5, no half-stars). All output reports are written in English.
- **Data accuracy**: cross-validate key figures and verify the arithmetic with `tools/financial_rigor.py`.
