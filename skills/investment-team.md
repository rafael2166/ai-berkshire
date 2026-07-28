# Investment Research Team: Four-Role Parallel Analysis Framework

Run a team-based investment research analysis on $ARGUMENTS. Use the Team tools to create a genuine multi-agent parallel research team.

Default market: Brazil / B3. Default tickers = PETR4, VALE3, ITUB4, BBAS3, WEGE3, ABEV3. Currency = Brazilian Real (R$, BRL); state the currency explicitly and note USD ADRs where relevant.

## Execution Flow

### Step 1: Present the Team Framework

Show the user the following team structure and start once confirmed:

| Role | Responsibility | Analysis Framework |
|------|------|----------|
| **team-lead** (you) | Coordination, synthesis, final report | Combined four-master framework |
| **business-analyst** | Business model & moat analysis | Duan Yongping's lens |
| **financial-analyst** | Financial statements & valuation | Warren Buffett's lens |
| **industry-researcher** | Industry landscape & competitive dynamics | Charlie Munger's lens |
| **risk-assessor** | Risk assessment & management quality | Li Lu's lens |

### Step 1.5: AI Research Bias Assessment

Before creating the team, present the company's "AI researchability" assessment to the user:

**Information Richness Rating** (determines research strategy):
| Level | Characteristics | Strategy Adjustment |
|------|------|------------|
| Level A (information-rich) | Listed for years, broad analyst coverage | Focus the team on **contrarian testing** and **non-consensus angles**; avoid producing "correct but useless" output that merely echoes the market |
| Level B (moderate information) | Recently listed, limited coverage | Every estimated figure must carry a confidence level; team-lead flags "data sufficiency" during synthesis |
| Level C (information-scarce) | Obscure / newly listed / emerging-market | The team switches to "first-principles mode": don't chase report completeness; focus on a few core questions about the business's essence |

**Key reminder**: More information ≠ higher certainty, and less information ≠ lower certainty. The confidence AI can express ≠ the true certainty of the investment. Certainty comes from the business model itself, not from the volume of available information.

Communicate the rating to each agent, as it shapes their research approach.

### Step 1.75: WebSearch Permission Pre-check (critical · prevents silent agent degradation)

**Before** creating the team or launching any background agent, you must confirm that WebSearch permission has been granted.

**Why the pre-check is mandatory**: This skill launches 4 background sub-agents with `run_in_background: true`, and **background agents cannot surface an interactive permission prompt to the user**. If `WebSearch` is not on the `permissions.allow` allowlist in `.claude/settings.local.json`, the sub-agents' web searches will be **silently blocked**, causing them to degrade to answering purely from training knowledge (which has a cutoff date) while still producing framework-shaped output that "looks complete but was never actually online" — this is the most dangerous failure mode of this skill.

**Pre-check steps**:
1. Use Bash to check whether the allowlist includes WebSearch:
   ```bash
   grep -l '"WebSearch"' .claude/settings.local.json ~/.claude/settings.local.json 2>/dev/null
   ```
2. If neither path matches (i.e., not granted) → **stop, do not launch agents**, and tell the user:
   > ⚠️ WebSearch is not on the permission allowlist. Background research agents cannot access the internet and will degrade to answering from training knowledge only. Please add `"WebSearch"` to `permissions.allow` in `.claude/settings.local.json` (or run `/permissions` and enable it), then re-run this command.
3. If matched → proceed normally.

Note: the analyst also has MCP market-data tools available (the market-data server and finnhub) plus WebSearch/WebFetch; prefer those for market data and filings.

### Step 2: Create the Team

Create the team with TeamCreate:
- team_name: `{company}-research` (lowercase English, e.g. `petrobras-research`)
- agent_type: `team-lead`

### Step 3: Create the 4 Tasks

Create the following 4 tasks with TaskCreate (each needs a subject, description, and activeForm):

#### Task 1: Business Model Analysis
- subject: `Analyze {company}'s business model, moat, and user value`
- description includes:
  1. Business model essence: definition of the core business, revenue breakdown
  2. How the platform/product flywheel operates
  3. Moat analysis: brand / switching costs / network effects / economies of scale / technology barriers — verify each one
  4. User/customer value: what unique value does it create for each party
  5. Business matrix and synergies
  6. Assessment against Duan Yongping's "good business" standard: differentiation, pricing power, durable competitive advantage
  7. Requires searching the latest filings, industry reports, and other public information

#### Task 2: Financial and Valuation Analysis
- subject: `Analyze {company}'s financials, profitability, and valuation`
- description includes:
  1. Revenue, net income, and operating income trends over the past 3-5 years
  2. Profitability metrics: ROE, ROA, gross margin, operating margin
  3. Cash flow analysis: operating cash flow, free cash flow, capital expenditure
  4. Balance sheet health: cash reserves, leverage, liquidity
  5. Valuation analysis: P/E, P/S, P/B, EV, etc., versus historical and peer levels
  6. Margin-of-safety assessment: intrinsic value vs current price
  7. **Financial rigor verification (must use Bash to call the tools; no mental math)**:
     - Market-cap check: `python3 tools/financial_rigor.py verify-market-cap --price {price} --shares {shares} --reported {reported_market_cap} --currency {currency}`
     - Valuation check: `python3 tools/financial_rigor.py verify-valuation --price {price} --eps {EPS} --bvps {book value per share}`
     - Key-data cross-validation: `python3 tools/financial_rigor.py cross-validate --field {field} --values '{JSON}' --unit {unit}`
     - Three-scenario valuation: `python3 tools/financial_rigor.py three-scenario --price {price} --eps {EPS} --shares {shares} --growth {bull} {base} {bear} --pe {bull PE} {base PE} {bear PE}`
     - Embed the tool outputs directly into the report as a verification record

#### Task 3: Industry and Competitive Analysis
- subject: `Analyze the {industry} landscape and {company}'s competitive position`
- description includes:
  1. Industry size and growth: market size, growth rate, penetration
  2. Competitive landscape: main rivals' market share, strategy comparison
  3. Key-competitor threat assessment: analyze each major rival
  4. Landscape of each sub-segment
  5. Industry trends: technological change, regulatory impact, new entrants
  6. Value-chain analysis: value distribution across upstream/midstream/downstream
  7. Requires searching the latest industry data and competitive developments

#### Task 4: Risk and Management Assessment
- subject: `Assess {company}'s investment risks and management quality`
- description includes:
  1. Management assessment: CEO's circle of competence, integrity, strategic vision, capital-allocation ability, quality of past decisions
  2. Regulatory risk: current and potential regulatory impact
  3. Competitive risk: threat level from each rival
  4. Business risk: losses in new ventures, expansion uncertainty
  5. Macro risk: economic cycle and industry-cycle impact
  6. Governance structure: ownership structure, related-party transactions, shareholder-return policy
  7. Long-term certainty: what will the company look like in 10 years? What could disrupt its business model?
  8. Requires searching the latest regulatory developments, management commentary, etc.

### Step 4: Launch the 4 Parallel Agents

Use the Task tool to launch 4 agents simultaneously (**they must be called in parallel within a single message**):

Configuration for each agent:
- `subagent_type`: `general-purpose`
- `run_in_background`: `true`
- `team_name`: the corresponding team name
- `name`: the corresponding role name (business-analyst / financial-analyst / industry-researcher / risk-assessor)

Prompt template for each agent:

```
You are the "{role name}" on the {company} research team, responsible for analyzing {company} from {master}'s investment perspective.

Please complete Task #{task number}: {task subject}

Specific requirements:
{contents of the task description}

**Research method**:
- Use the MCP market-data tools (market-data server + finnhub) and WebSearch/WebFetch to gather the latest public information (filings, industry reports, news)
- **Financial data must come from two independent sources**, per the `skills/financial-data.md` conventions. For Brazilian (B3) companies, source filings from CVM via the RAD portal (www.rad.cvm.gov.br) plus the company's investor-relations (RI) site, and market data from B3; for US-listed ADRs, also use SEC filings. Any discrepancy >1% between the two sources must be flagged.
- Ensure the data is accurate; cite the source for every key figure
- Go deep in the analysis; do not stay at the surface
- **No faking when the network fails**: if WebSearch is blocked/unavailable, you must not pass off training knowledge as live results. Prominently flag at the top of the report "⚠️ This report could not go online; based on training knowledge (cutoff X); confidence downgraded", report this honestly to team-lead, and let team-lead decide whether to abort the research

**Output requirements**:
- The report must be thorough, using Markdown tables to present key data
- Every analytical dimension must have a clear conclusion and rating
- The report must end with an overall conclusion for that dimension
- The report must be written in English, in Brazilian Real (R$) where currency applies

**When done**:
1. Use TaskUpdate to mark Task #{task number} as completed
2. Send the full analysis report to team-lead via SendMessage (type: "message", recipient: "team-lead")
```

### Step 5: Receive Reports and Track Progress

- Show the user a live progress table (which agents are done, which are still researching)
- Each time a report arrives, update progress and present that report's key takeaways (3-5 bullets)
- Wait until all 4 reports have arrived

### Step 6: Shut Down Team Members

Once all reports are received, send a shutdown_request to each of the 4 agents (via SendMessage, type: "shutdown_request").

### Step 7: Synthesize the Final Report

Combine the 4 analysis reports and produce a final report with the following structure:

---

#### 1. One-Sentence Conclusion
> Summarize in one paragraph (50-100 words) whether the investment is worthwhile and the core logic

#### 2. Four-Dimension Scoring Table
| Dimension | Framework | Score (1-5 stars) | Core Judgment |
|------|------|------------|----------|

Overall score: X / 5

#### 3. Core Data Snapshot
Table of key financial and operating metrics (2-year comparison)

#### 4. Summary of Each Dimension
The 3-5 most important findings from each dimension

#### 5. Investment Thesis (Bull vs Bear)
- 🟢 Bull case (5-7 points)
- 🔴 Bear case (5-7 points)

#### 6. Buffett Pre-Purchase Checklist
| # | Check Item | Pass? | Notes |
10 core check items, assessed one by one

#### 7. Final Investment Recommendation
- Qualitative judgment table (business quality / management / valuation / timing)
- Tiered action table (aggressive / balanced / conservative → recommendation + price range)
- Key catalysts (3-5 add signals and 3-5 trim signals)

#### 8. Concluding Paragraph
100-200 word final summary

---

### Step 8: Save the Report

Write the reports into `reports/{CompanyName}/` using English/latin folder and file names:

```
reports/{CompanyName}/
├── final-report.md                        — Team Lead synthesis report
├── 01-business-model-duan-yongping.md
├── 02-financials-valuation-buffett.md
├── 03-industry-competition-munger.md
└── 04-risk-management-li-lu.md
```

### Step 9: Data Spot-Check (release gate)

```bash
# Step 1 — Extract the spot-check list (15% random sample)
python3 tools/report_audit.py extract \
  --report <report file path>

# Step 2 — For each item, pull the figure from a reliable source (see skills/financial-data.md)

# Step 3 — Output the pass/fail verdict
python3 tools/report_audit.py verdict \
  --results '<completed JSON>' \
  --report <report file name>
```

**[PASS]** all items pass → report may be published; **[REJECT]** any failure → fix and re-audit.

### Step 10: Clean Up the Team

Use TeamDelete to release team resources.

## Important Notes

1. **The 4 agents must be launched in parallel** — call the Task tool 4 times within a single message
2. **Agents report via SendMessage** — this is message-based communication, not file-based collaboration
3. **Data accuracy** — require agents to use the MCP market-data tools and WebSearch for the latest data, with key figures cross-validated
4. **Conclusions must be clear** — do not shy away from a buy/watch/avoid recommendation and a specific price range
5. **Every analysis must be data-backed** — attach data sources
6. **Be patient** — the 4 agents take a few minutes to research; keep updating the user on progress in real time
7. **Anti-bias awareness** — during synthesis, team-lead must assess: is each agent's analysis constrained by information availability? Has it converged too closely on the market consensus? The final report must include the "Information Richness Rating" and an "AI Research Limitations Statement"
8. **Honesty principle when information is scarce** — it is better to leave a gap in the report labeled "insufficient data" than to fill the framework with speculation to fake certainty

## Core Objectivity Principles (highest priority)

- **Objective, objective, objective** — all analysis must be grounded in facts and data; no subjective conjecture
- Strictly separate "fact" from "opinion": facts are backed by data; opinions must be explicitly labeled as "opinion" or "speculation"
- **Present both sides**: every core judgment must carry a counter-argument ("but on the other hand...") so the reader can weigh it
- Be honest and say "uncertain" or "insufficient data" when appropriate; do not fill certainty with speculation
- Cite sources for all key data — at least 2 independent sources for critical figures
- Use ★ ratings (1-5 stars, no half-stars)
- All skills and output reports are written in English
