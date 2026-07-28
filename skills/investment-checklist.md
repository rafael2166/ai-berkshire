# Buffett Value-Investing Pre-Purchase Checklist

Run a Buffett value-investing pre-purchase Checklist analysis on $ARGUMENTS.

Default market: Brazil / B3. Default tickers = PETR4, VALE3, ITUB4, BBAS3, WEGE3, ABEV3. Currency = Brazilian Real (R$, BRL); state the currency explicitly and note USD ADRs where relevant.

**Supported input formats**: one or more companies, separated by commas or spaces. For example: `PETR4, VALE3, ITUB4` or `WEGE3 ABEV3 BBAS3`

## Execution Flow

### Step 1: Parse the Input, Identify All Companies to Analyze

Parse all company names/tickers from $ARGUMENTS. For each company, determine:
- Full company name, ticker, and listing exchange (default B3; note SEC/NYSE/Nasdaq for US-listed ADRs)
- If the company is not listed, mark it as "unlisted" and give a brief note (whether an indirect investment route exists), and skip the full Checklist

### Step 1.5: AI Research Bias Warning

Do a quick "information richness" rating (A/B/C) for each company and note it in the report:

| Level | Criteria | Impact on the Checklist |
|------|---------|-----------------|
| Level A | Listed for years, ample data | Run normally, but beware the "consensus trap" — all metrics looking clear doesn't mean the outcome is truly certain |
| Level B | Limited data, some estimation needed | Flag every estimated metric with a confidence level; weight the "good business" judgment by data reliability |
| Level C | Information extremely scarce | Don't force-fill the six-gate table; honestly mark "insufficient data to judge" and focus on the verifiable core questions |

**Core principle**: The Checklist's goal is to **eliminate bad choices**. For Level C companies, "insufficient data" means neither "fail" nor "pass" — it should be honestly marked as "gray zone, needs additional first-hand information," rather than a rejection just because AI can't fill the table.

Duan Yongping has said there are two kinds of "I don't understand it" — one where the business is genuinely too complex to grasp, and one where you simply haven't spent the time to look. A limitation of AI research is that it easily conflates "little information" with "can't understand."

### Step 2: Parallel Data Collection

Use the Task tool to launch an independent background agent for **each company** to collect data (launch all companies in parallel simultaneously). Each agent collects:

1. **Profitability**: ROE (5-10 year trend), gross margin, net margin, free cash flow
2. **Valuation data**: current price, market cap, P/E (TTM), forward P/E, P/B, dividend yield
3. **Growth trend**: revenue/earnings growth over the past 3 years
4. **Financial health**: leverage, capex needs, cash reserves, net cash/net debt
5. **Competitive landscape**: market share, main rivals, share-change trend
6. **Moat evidence**: concrete evidence of brand / switching costs / network effects / economies of scale / technology barriers
7. **Management record**: CEO background, key decisions, ownership, capital-allocation record
8. **Latest developments**: major events in the past 6 months (results, M&A, regulation, management changes, etc.)

Prefer the MCP market-data tools (market-data server + finnhub) and WebSearch/WebFetch. For Brazilian (B3) companies, source filings from CVM via the RAD portal (www.rad.cvm.gov.br) plus the company's investor-relations (RI) site, with B3 market data; for US-listed ADRs, also use SEC filings. Financial data must come from two independent sources; any discrepancy >1% must be flagged.

### Step 3: Run the Six-Gate Checklist per Company

For each listed company, pass through the six gates in order:

---

#### Gate 1: Can I Understand This Business? (circle of competence)

Must answer:
- [ ] Can you explain in one sentence how this company makes money?
- [ ] What business will it most likely still be in 10 years from now?
- [ ] Which key variables decide success or failure?
- [ ] Does your understanding of this industry come from deep research or hearsay?

**Scoring standard** (★1-5):
- ★★★★★: Extremely simple, clear business model; high 10-year certainty (e.g. a brewer: brew and sell beer)
- ★★★★☆: Clear model but with a technical barrier; requires some domain knowledge to understand
- ★★★☆☆: Understandable model but low 10-year certainty; fast-changing industry
- ★★☆☆☆: Complex business lines or an industry in upheaval; hard to project the future
- ★☆☆☆☆: Entirely outside the circle of competence

**Hard reject**: if you can't even articulate how it makes money, mark it "outside circle of competence, no analysis."

---

#### Gate 2: Is This a Good Business? (economic characteristics)

Let the data speak; **key metrics must be computed precisely with the tool**:

```bash
python3 tools/financial_rigor.py verify-valuation \
  --price {price} --eps {EPS} --bvps {book value per share} --fcf-per-share {FCF per share} --dividend {dividend per share}
```

| Metric | Company Value | Reference Standard | Judgment |
|------|-----------|---------|------|
| ROE (5-year avg) | | >15% strong, >20% exceptional | |
| Gross margin | | >40% implies pricing power | |
| Free cash flow | | consistently positive, ≈ net income | |
| Capex intensity | | asset-light preferred over asset-heavy | |
| Leverage | | interest-bearing debt / net income < 3 years | |

**Scoring standard** (★1-5):
- ★★★★★: ROE >25%, high gross margin, strong FCF, asset-light, low leverage (all criteria met)
- ★★★★☆: 4 criteria met
- ★★★☆☆: 3 criteria met
- ★★☆☆☆: 2 criteria met, or deteriorating trend
- ★☆☆☆☆: most criteria unmet, or FCF persistently negative

---

#### Gate 3: Is the Moat Deep Enough? (competitive advantage)

Check item by item:

| Moat Type | Present? | Concrete Evidence | Widening or Narrowing? |
|-----------|---------|---------|--------------|
| Brand / pricing power | | | |
| Switching costs | | | |
| Network effects | | | |
| Cost / scale advantage | | | |
| Technology / patent barrier | | | |

Additional test: if you gave a competitor R$10 billion, could they replicate this business?

**Scoring standard** (★1-5):
- ★★★★★: multiple stacked moats, and widening
- ★★★★☆: at least one strong moat, and stable
- ★★★☆☆: has a moat but not deep, or unclear trend
- ★★☆☆☆: moat is being eroded
- ★☆☆☆☆: no discernible moat

---

#### Gate 4: Is Management Trustworthy? (the human factor)

| Check Item | Assessment |
|--------|------|
| Honesty (promises vs delivery) | |
| Capital-allocation ability (buyback/dividend/M&A record) | |
| Shareholder orientation (ownership, compensation) | |
| Owner mindset (founder vs professional manager) | |
| Corporate governance (related-party transactions, goodwill, audit) | |
| Can it run normally after the CEO leaves? | |

**Scoring standard** (★1-5):
- ★★★★★: founder at the helm, exceptional capital allocation, fully aligned interests
- ★★★★☆: excellent management with minor blemishes
- ★★★☆☆: adequate management but with governance concerns
- ★★☆☆☆: has integrity or governance problems
- ★☆☆☆☆: serious integrity problems (→ hard reject)

---

#### Gate 5: Is the Price Cheap Enough? (margin of safety)

| Metric | Value | Historical Percentile | Judgment |
|------|------|---------|------|
| P/E (TTM) | | | |
| Forward P/E | | | |
| P/B | | | |
| Dividend yield | | | |
| FCF Yield | | | |

Additional test (**must be computed precisely with the tool; no mental math**):
```bash
python3 tools/financial_rigor.py three-scenario \
  --price {price} --eps {EPS} --shares {shares} \
  --growth {bull} {base} {bear} --pe {bull PE} {base PE} {bear PE} --currency {currency}
```
- The valuation range across the three scenarios (take the tool's output)
- If your judgment is wrong, how much could you lose buying at the current price?
- If the stock halved, would you dare to add?

**Scoring standard** (★1-5):
- ★★★★★: below 50% of intrinsic value, extreme margin of safety
- ★★★★☆: ~70% of intrinsic value, good margin of safety
- ★★★☆☆: fair valuation, average margin of safety
- ★★☆☆☆: somewhat expensive, insufficient margin of safety
- ★☆☆☆☆: severely overvalued

---

#### Gate 6: Position Sizing and Decision Discipline (guard against emotional loss of control)

Check for these emotional signals:
- Do you want to buy because of FOMO?
- Do you want to buy only because someone recommended it?
- Could you accept a 5-year trading halt?
- Can you write the buy thesis clearly in under 200 words?

---

### Step 4: The Mirror Test

For each company, write out the mirror-test statement:

> "I am buying ___ (company) at R$___, because:
> 1. The essence of this business is ___, and I understand it;
> 2. Its moat is ___, and it is widening/narrowing;
> 3. Management is ___, and is/is not trustworthy;
> 4. The current price is ___% of intrinsic value, with/without a sufficient margin of safety;
> 5. Even if I'm wrong, downside risk is manageable/unmanageable, because ___."

**If you can't complete all 5 sentences = don't buy.** Clearly mark "pass" or "fail."

---

### Step 5: Quick-Reject List

Check each company against every item; triggering any one marks it "rejected":

- [ ] Can't articulate how the company makes money
- [ ] Free cash flow negative for 3 consecutive years with no improvement in sight
- [ ] Management has an integrity blemish
- [ ] Competitive advantage is being irreversibly eroded
- [ ] Depends on "a greater fool paying more" to make money (greater-fool game)
- [ ] Can't withstand the consequences of this investment going to zero
- [ ] The main reason to buy is "everyone else is buying" or "it's been going up lately"
- [ ] Can't write the buy thesis clearly in under 200 words

---

### Step 6: Output the Overview Comparison Table (required for multiple companies)

When analyzing multiple companies, you must generate a comparison overview table:

| Company | Checklist Pass? | Circle of Competence | Good Business | Moat | Management | Margin of Safety | Core Conclusion |
|------|----------------|--------|--------|--------|--------|---------|---------|
| | | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | |

---

### Step 7: Final Conclusion and Write to File

Give a clear conclusion for each company (don't dodge):
- ✅ **Passes the Checklist** (X/6 gates) — may proceed to the deep-research stage
- ❌ **Fails the Checklist** — state which red line was triggered
- ❓ **Gray zone** — state the key point of contention and what the investor must judge for themselves
- N/A — unlisted / cannot be bought

Write the full report to `reports/{CompanyName}/{CompanyName}-checklist-{YYYYMMDD}.md`, or for multi-company comparisons to `reports/{Company}-comparison-checklist-{YYYYMMDD}.md` at the reports root (English/latin folder names).

## Output Format Requirements

1. Each company gets its own chapter, containing: six-gate scoring table + core-data table + key risks (3-5) + mirror test + clear conclusion
2. For multiple companies, append the overview comparison table at the end
3. All scores must use the ★ symbol (★1-5), no half-stars
4. Data must note the source and timestamp; estimates must be marked "estimate"
5. End with a closing note echoing Buffett's maxim: "The first rule of investing is: don't lose money."
6. Style: direct, sharp, no filler. Weave in Buffett/Munger/Duan Yongping quotes as commentary
7. The report must be written in English, in Brazilian Real (R$) where currency applies

## Key Principles

- **Better to miss than to be wrong**: the Checklist's goal is to eliminate bad choices, not to find the best one
- **Be honest about the circle of competence**: if you don't understand it, say so; don't force an analysis
- **Margin of safety is the lifeline**: even a great company loses money if bought too expensive
- **The mirror test is not skippable**: if you can't state the reason clearly, don't buy — no exceptions

## Core Objectivity Principles (highest priority)

- **Objective, objective, objective** — all analysis must be grounded in facts and data; no subjective conjecture
- Strictly separate "fact" from "opinion"; opinions must be explicitly labeled
- **Present both sides**: every core judgment must carry a counter-argument so the reader can weigh it
- Be honest and say "uncertain" or "insufficient data" when appropriate
- Cite sources for all key data — at least 2 independent sources for critical figures
