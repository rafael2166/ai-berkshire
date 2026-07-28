# Investment Research: Buffett–Munger–Duan Yongping–Li Lu Combined Analysis Framework

Run a systematic investment research analysis on $ARGUMENTS.

Default market: Brazil / B3. Default tickers = PETR4, VALE3, ITUB4, BBAS3, WEGE3, ABEV3. Currency = Brazilian Real (R$, BRL); state the currency explicitly and note USD ADRs where relevant.

## Research Framework

Based on the methodologies of the four investing masters — Warren Buffett, Charlie Munger, Duan Yongping, and Li Lu — execute the research in the following seven modules, in order.

### Preliminary Step: AI Research Bias Awareness (mandatory)

Before starting the research, assess the company's "AI researchability" to identify potential data bias:

**Information Richness Rating**:
| Level | Characteristics | AI Research Trap | Countermeasure |
|------|------|-----------|---------|
| Level A (information-rich) | Listed for years, broad analyst coverage, heavy media reporting | Consensus too strong; AI output converges on market pricing, limited alpha | Focus on contrarian testing: why don't smart people buy? What risk is being overlooked? |
| Level B (moderate information) | Listed 1-3 years, limited coverage, some data must be estimated | AI may fill gaps with "reasonable guesses" — looks complete but is false certainty | Flag every estimate with a confidence level; distinguish "evidence-based estimate" from "invented filler" |
| Level C (information-scarce) | Just listed / obscure / emerging-market, almost no coverage | AI becomes overly conservative due to lack of data, wrongly reading "can't see clearly = bad" | Use first-principles questions (below) to extract the business's essence from limited information |

**First-Principles Method for Level C companies**:
When public information is insufficient, don't try to patch together a report that "looks complete." Instead, focus on the following bedrock questions:
1. Who is the customer? Why do they pay? Is there a substitute?
2. What drives repeat purchase — habit, lock-in, or continuously created new value?
3. Could a competitor with R$10 billion replicate this business?
4. What key decisions has management made? What judgment and values do those decisions reveal?

**Bias Self-Check List** (stay vigilant throughout the research):
- [ ] Does my sense of "certainty" come from the essence of the business, or from the volume of information?
- [ ] If I halved this company's available information, would my conclusion change?
- [ ] Is the AI's analysis highly similar to the market consensus? If so, where is my information edge?
- [ ] Am I underweighting the possibility of "very little public information but an excellent underlying business"?

Write the Information Richness Rating at the start of the report, and in the final conclusion note the difference between "AI research confidence" and "actual investment certainty."

### Step 1: Data Collection

> **Data-source conventions**: see `skills/financial-data.md`. All financial data must come from two independent sources; any discrepancy >1% must be flagged.
> - Brazilian (B3) companies: CVM via the RAD portal (www.rad.cvm.gov.br) + the company's investor-relations (RI) site (primary), with B3 market data and MCP market-data tools (market-data server + finnhub) as secondary/cross-check
> - US-listed ADRs: SEC filings + a third-party source (e.g. finnhub / market-data server)
> - Replace any legacy defaults (regulator/exchange filings) with "CVM / B3 (and SEC for US-listed ADRs)"

Use the Task tool to launch a background agent to collect the following data from the web (prefer the MCP market-data tools and WebSearch/WebFetch):

1. Revenue structure: latest fiscal year and trailing 4 quarters segment revenue, growth, and gross margin
2. Financial metrics: 5-year revenue, net income, gross margin, operating margin, free cash flow, cash reserves
3. Competitive landscape: market share, comparison with main rivals
4. Business model and moat: sources of core competitive advantage
5. Technical capabilities: core technology stack, R&D investment
6. Management: founder/CEO background, ownership percentage, record of key decisions
7. Industry outlook: TAM (total addressable market), growth forecasts
8. Risk factors: geopolitics, regulation, supply chain, etc.
9. Current valuation: market cap, P/E, P/S, PEG, EV/Revenue
10. Core bull and bear arguments from both sides

#### Data Cross-Validation (mandatory, using the financial-rigor tool)

After collecting data, you **must call `tools/financial_rigor.py` to programmatically verify key figures**, eliminating LLM mental-math errors.

**Data points that must be verified**:
- Total shares outstanding (confirmed from at least 2 sources — e.g. B3/exchange, the company's RI site, finnhub / market-data server)
- Current price and market cap (**manually compute price × shares and compare with the reported market cap, to catch unit errors**)
- Latest fiscal-year revenue and net income (confirmed from the company's annual report/CVM filing + at least 1 third-party source)
- Cash reserves and net cash (cash + short-term investments − total debt; watch for definitional differences)
- Management ownership percentage (distinguish economic interest from voting rights; watch for dual-class structures)

**Mandatory verification steps (call the tools via Bash)**:

Step 1 — Market-cap check (exact decimal, not floating point):
```bash
python3 tools/financial_rigor.py verify-market-cap \
  --price {price} --shares {shares} --reported {reported market cap} --currency {currency}
```

Step 2 — Multi-source cross-validation of key data:
```bash
python3 tools/financial_rigor.py cross-validate \
  --field {field name} --values '{"source1": value, "source2": value}' --unit {unit}
```
Run this for revenue, net income, and cash reserves separately.

Step 3 — Exact valuation-metric check (P/E, P/B, ROE, FCF Yield, etc.):
```bash
python3 tools/financial_rigor.py verify-valuation \
  --price {price} --eps {EPS} --bvps {book value per share} --fcf-per-share {FCF per share} --dividend {dividend per share}
```

**Verification rules**:
1. At least 2 independent sources for every key data point
2. When sources disagree, prefer the company's annual report / exchange (CVM / B3) data and note the reason for the difference
3. **Every figure involving a calculation must be verified with the tool; no LLM mental math**
4. Embed the tool outputs directly into the report appendix "Key Data Cross-Validation Record"
5. If the tool reports ❌ excessive deviation, you must investigate the cause before continuing the analysis

**Common error prevention**:
- Market-cap units: BRL billions vs USD billions (for ADRs) — easy to drop or add a zero
- FCF definition: sources may define capital expenditure differently (whether leases, acquisitions, etc. are included)
- Debt definition: whether operating-lease liabilities are included
- Ownership percentage: for dual-class companies, economic interest ≠ voting rights

### Step 2: Business Essence Analysis — Duan Yongping's "Right Business"

Analysis points:
- Define the essence of this business in one sentence
- Revenue-structure breakdown (chart)
- 5-year profitability trend (chart)
- Business-model canvas: one-time sale vs subscription/repeat purchase? Hardware vs software vs platform?
- Ecosystem stickiness / strength of customer lock-in
- Gross-margin level versus peers; explain why it is high/low
- Operating-leverage analysis
- **Duan Yongping-style probe**: What makes this a good business? If you could describe it in one sentence, what would it be?

### Step 3: Moat Assessment — Buffett's "Economic Moat"

Verify the five moat types one by one:

| Moat Type | Verification Method |
|-----------|---------|
| Brand / pricing power | Can it raise prices without losing volume? |
| Switching costs | How costly is it for customers to move to a competitor? |
| Network effects | Does the product get better as more users join? |
| Economies of scale | How large is the cost advantage from scale? |
| Technology / patent barriers | How many years ahead is the technology? Can it be copied? |

Analyze the moat trend: has it widened or narrowed over the past 5 years? Project the next 5 years.

**Buffett-style probe**: Will this moat still be here in 10 years? What could destroy it?

### Step 4: Inversion and Risk List — Munger's "Invert, Always Invert"

- List "all the paths by which this company could fail" (table: path / probability / severity)
- Historical analogy: find companies that were in a similar position historically — how did they end up?
- Cross-disciplinary analysis: cross-check using network-effect theory, technology-adoption curves, competitive game theory, etc.
- Bias self-check: narrative bias, anchoring, survivorship bias
- Collect the core bear-case arguments

**Munger-style probe**: Where am I most likely to be wrong? Why would smart people refuse to buy — or short — this company?

### Step 5: Management Assessment — Duan Yongping's "Right People" + Buffett's "Management Integrity"

- Review of the CEO/founder's key decisions (table: date / decision / outcome / rating)
- Capital-allocation ability: R&D return, M&A success rate, buyback timing
- Alignment with shareholders: management ownership, compensation structure, insider-selling record
- Organizational capability: team stability, key-person risk
- Corporate-culture characteristics

**Duan Yongping-style probe**: If the CEO retired, could this company keep its competitiveness?

### Step 6: Industry and Civilizational Trend — Li Lu's "Civilizational Evolution Framework"

- Judge whether the industry is undergoing a "civilization-level paradigm shift"
- Analogy to historical technological revolutions (steam engine / electricity / internet / AI)
- TAM growth curve and ceiling analysis
- The company's position in the industry value chain
- Technology-roadmap risk
- Customer/supplier concentration analysis

**Li Lu-style probe**: Looking back 20 years from now, is this company "the Standard Oil of its era" or "a flash-in-the-pan like 3Com"?

### Step 7: Valuation and Margin of Safety — Buffett's "Intrinsic Value" + Duan Yongping's "Right Price"

- Current market pricing (table of key valuation metrics) — **must be verified with the tool**
- Reverse DCF: what growth expectation does the current price imply?
- Three-scenario valuation — **must be computed precisely with the tool; no mental math**:
```bash
python3 tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {shares} \
  --growth {bull growth} {base growth} {bear growth} \
  --pe {bull PE} {base PE} {bear PE} --years 3 --currency {currency}
```
- Compare with the company's own historical valuation
- Compare with peer valuation

**Duan Yongping-style probe**: If the stock market closed for 5 years starting tomorrow, would you hold at this price?

### Step 8: Integrated Decision Memo

Summary table:

| Dimension | Conclusion | Confidence |
|------|------|--------|
| Business quality (Duan Yongping) | | |
| Moat (Buffett) | | |
| Management (Duan Yongping + Buffett) | | |
| Biggest risk (Munger) | | |
| Civilizational trend (Li Lu) | | |
| Valuation (Buffett + Duan Yongping) | | |

Final decision table:

| Strategy | Recommendation |
|------|------|
| If not holding | |
| If holding | |
| Sell signal | |
| Add signal | |

Simulated commentary from the four masters (in quote/callout format).

## Output Requirements

1. Every analysis must be data-backed, with sources attached
2. Use Markdown tables to present key data
3. Each module must end with the corresponding master's "probe"
4. Write the full report to `reports/{CompanyName}/{CompanyName}-research-{YYYYMMDD}.md` (English/latin folder names)
5. Conclusions must be clear; do not shy away from a buy/watch/avoid recommendation
6. The valuation section must give a specific price range
7. **The start of the report** must include the "Information Richness Rating" (A/B/C) and an "AI Research Limitations Statement"
8. **The end of the report** must distinguish "AI analysis confidence" from "investment certainty" — the former depends on the volume of information, the latter on the essence of the business. Tell the reader clearly which conclusions rest on sufficient data and which rest on reasoning from limited information
9. If the company is Level C (information-scarce), the report must end with a "List of Questions Requiring First-Hand Verification" — suggesting the reader fill AI's blind spots via field research, product experience, supply-chain interviews, etc.
10. The report must be written in English, in Brazilian Real (R$) where currency applies

## Core Objectivity Principles (highest priority)

- **Objective, objective, objective** — all analysis must be grounded in facts and data; no subjective conjecture
- Strictly separate "fact" from "opinion"; opinions must be explicitly labeled
- **Present both sides**: every core judgment must carry a counter-argument so the reader can weigh it
- Be honest and say "uncertain" or "insufficient data" when appropriate
- Cite sources for all key data — at least 2 independent sources for critical figures
- Use ★ ratings (1-5 stars, no half-stars)

## Data Spot-Check (release gate)

After writing the report to a file, you **must** run a data spot-check and only publish once it passes:

**Step 1 — Extract the spot-check list (15% random sample):**
```bash
python3 tools/report_audit.py extract \
  --report <report file path>
```
Outputs a JSON template with a `fetched_value` (to be filled in) for each item.

**Step 2 — Fetch and verify:**
For each data point in the list, pull the figure from a reliable source per the `skills/financial-data.md` conventions
(Brazilian companies: CVM/RAD + company RI site + B3 / MCP market-data tools; US-listed ADRs: SEC + a third-party source),
and fill in `fetched_value` / `fetched_source` / `fetched_value2` / `fetched_source2`.

**Step 3 — Output the verdict:**
```bash
python3 tools/report_audit.py verdict \
  --results '<completed JSON>' \
  --report <report file name>
```

- **[PASS]**: all spot-check points deviate ≤ 1% → report may be published
- **[REJECT]**: any point deviates > 1% → fix the corresponding data and re-check until it passes
