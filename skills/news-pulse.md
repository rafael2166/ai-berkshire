---
name: news-pulse
description: Company News Pulse — fast attribution when a stock moves abnormally. Uses 4 parallel agents to reconnoiter company events / regulatory & policy / industry peers / market sentiment, producing an event timeline, a primary-cause judgment for the move, and a decision on whether to trigger a thesis review.
---

# Company News Pulse: Rapid Attribution Team for Abnormal Price Moves

Conduct recent-news reconnaissance and move attribution for $ARGUMENTS. **This is not deep research; it is rapid intelligence response** — the goal is to answer, within 10 minutes: "What has recently happened at this company? What is the real cause of the price move? Do we need to re-examine the investment thesis?"

## When to Use

- A held/watched stock moves sharply up or down (typical triggers: single-day ±5%, one-week ±10%)
- Price moves after earnings and you want to quickly understand what the market is reacting to
- You saw a news headline but aren't sure whether it's noise or a real signal
- **Not for**: full research (use `/investment-team`), deep earnings reading (use `/earnings-review`), long-term thesis tracking (use `/thesis-tracker`)

## Execution Flow

### Step 1: Confirm Parameters and Scenario

Clarify the following with the user (if not provided in $ARGUMENTS):

| Parameter | Notes | Default |
|------|------|------|
| **Company name** | Name or ticker (B3 ticker such as PETR4, or US ADR) | Required |
| **Time window** | Lookback days for news reconnaissance | Default 14 days; can shorten to 7 during earnings season |
| **Price move** | Up/down magnitude + period, e.g., "down 12% over 3 days" | Optional; if given, used to focus attribution |
| **Focus emphasis** | Company events / regulatory / industry / sentiment | Default: even weight across the four |

If the user only gives a company name, ask back first: "News over how many days? Is there a specific price move to explain?" — **do not silently assume**.

### Step 2: Grade Information Availability

Reference the A/B/C grading in `investment-team.md`, but with different dimensions:

| Grade | Characteristics | Reconnaissance strategy |
|------|------|---------|
| **A (information-rich)** | Large caps, broad media coverage, earnings season | The focus is **noise reduction and attribution** — too much information makes the real cause harder to find. Each agent must use judgment and filter out "restated" secondhand news |
| **B (moderate)** | Mid/small caps, average coverage | Standard mode; attach 1-2 independent sources to each key event |
| **C (information-scarce)** | Small-cap B3 names, recent IPOs, obscure companies | Switch to "sweep mode" — you may find no news that explains the move, and **that conclusion itself has value** (the move may be technical/flow-driven rather than fundamental) |

Tell each agent the grade, since it affects how they reconnoiter.

### Step 3: Create the Team

Use TeamCreate to create the team:
- `team_name`: `{company}-newspulse` (lowercase English, e.g., `petr4-newspulse`)
- `agent_type`: `team-lead`

### Step 4: Create the 4 Reconnaissance Tasks

Use TaskCreate to create the following 4 tasks:

#### Task 1: Company Event Reconnaissance (company-event-scout)

- **subject**: `Reconnoiter {company}'s own corporate events over the past {N} days`
- **description**:
  1. **Official disclosures**: recent filings on regulatory disclosure platforms — CVM via the RAD portal (www.rad.cvm.gov.br) and the company IR ("Relações com Investidores") site; SEC EDGAR for US-listed ADRs
  2. **Earnings and guidance**: latest quarterly/annual results, guidance, earnings-call highlights
  3. **Management actions**: executive changes, insider buying/selling, buybacks, dividends/JCP, equity incentives
  4. **Major business events**: new product launches, M&A/restructuring, divestitures, major clients/orders
  5. **Capital actions**: follow-on offerings, convertible debt, ADR conversions, delisting/tender proposals
  6. **Litigation and compliance**: lawsuits, self-disclosed compliance events
  7. Tag each event: **date / source link / one-sentence summary / likely relevance to the price move (high/medium/low)**
  8. Output a timeline table in reverse chronological order

#### Task 2: Regulatory and Policy (regulatory-watcher)

- **subject**: `Reconnoiter regulatory and policy changes in {industry/company} over the past {N} days`
- **description**:
  1. **Industry regulation**: new rules, fines, remediation orders, or licensing changes from Brazilian regulators — CVM (securities), BACEN (banking/monetary), and the relevant sector agency (ANP oil & gas, ANEEL electricity, ANATEL telecom, ANS health)
  2. **Antitrust and competition**: CADE investigations, fines, or blocked mergers (and US/other jurisdictions where the company operates)
  3. **Cross-border / trade policy**: tariffs, export controls, sanctions, and — for US-listed ADRs — SEC/US-side actions
  4. **Tax policy**: changes to ICMS, PIS/COFINS, corporate income tax, or sector-specific levies (e.g., mining royalties/CFEM, oil participations)
  5. **Sector-specific policy**: for example, fuel-pricing policy, electricity-tariff reviews, health-plan rules, financial-sector regulation
  6. **Monetary and FX**: BACEN Selic decisions and BRL exchange-rate/capital-flow changes that affect the company
  7. Tag each item: **date / source / degree of direct impact on the company (direct/indirect/unrelated)**
  8. Key judgment: has a "policy black swan" just landed?

#### Task 3: Industry and Competitors (industry-peer-analyst)

- **subject**: `Reconnoiter the industry landscape and peers of {company} over the past {N} days`
- **description**:
  1. **Direct competitors**: list 3-5 core competitors and check recent events for each (earnings, products, price wars, personnel)
  2. **Value chain up/downstream**: upstream raw materials/suppliers and downstream customers/channels — recent price, capacity, and order changes
  3. **Industry as a whole**: sector activity data, shipments, demand-side signals (consumption data, auction/tender data)
  4. **Substitution threats**: new technologies or business models disrupting the industry
  5. **Sector index performance**: recent performance of same-sector B3 stocks — is the company outperforming/underperforming/in line?
  6. Key judgment: **is this a company-specific event, or industry-wide beta?**
  7. Tag each event with source and date

#### Task 4: Market Sentiment and Sell-Side / Notable Investors (sentiment-tracker)

- **subject**: `Reconnoiter market sentiment and institutional-view changes for {company} over the past {N} days`
- **description**:
  1. **Sell-side rating changes**: recent rating/target-price changes from major banks and brokers (e.g., BTG Pactual, Itaú BBA, XP, and global houses like Goldman Sachs, Morgan Stanley, JPMorgan)
  2. **Institutional-holding changes**: 13F disclosures (for US ADRs), CVM ownership filings, and foreign-flow data on B3
  3. **Short data**: short interest, newly published short-seller reports (if any)
  4. **Notable-investor commentary**: use WebSearch / financial media to surface commentary from well-known investors on the company. This is **only relevant if the company is a known holding of a tracked investor** (e.g., Duan Yongping or Li Lu for US-listed names); otherwise skip to save time
  5. **Rumors and unconfirmed reports**: media-unverified rumors, social-media discussion hotspots (X / Reddit / local financial forums)
  6. **Technical signals**: whether key support/resistance was touched, block trades, unusual margin/short-selling activity
  7. Key judgment: **is this fundamental-driven or sentiment/flow-driven?**

### Step 5: Launch the 4 Agents in Parallel

**You must call the Task tool 4 times in parallel within a single message.** Configure each agent:
- `subagent_type`: `general-purpose`
- `run_in_background`: `true`
- `team_name`: `{company}-newspulse`
- `name`: the corresponding role name (company-event-scout / regulatory-watcher / industry-peer-analyst / sentiment-tracker)

Prompt template for each agent:

```
You are the "{role name}" in the {company} News Pulse team, responsible for reconnoitering the {reconnaissance dimension} dimension over the past {N} days.

Time window: {start date} ~ {today}
Price-move background: {price-move info provided by user; if none, write "no specific move, routine check"}
Information-availability grade: {A/B/C}

Please complete Task #{task number}: {task subject}

Specific reconnaissance requirements:
{contents of the task description}

**Reconnaissance method**:
- Prefer the connected MCP market-data tools (market-data server + finnhub) for prices, quotes, and fundamentals
- Use WebSearch for time-sensitive queries (add dates or "latest", "recent", "2026" to keywords)
- Use WebFetch to closely read primary sources for key events (original filings, earnings reports, regulatory documents)
- Do "independent-source verification" for each event — a rumor needs at least 2 independent sources
- **Do not be misled by clickbait**: flag events where the headline doesn't match the body as "headline misleading"

**Output format (important)**:
1. **Core findings**: the 3-5 most critical events, each in 1-2 sentences
2. **Full event timeline table** (reverse chronological):
   | Date | Event | Source | Relevance to price move | Persistence |
3. **Attribution conclusion for this dimension**: based on the events found, answer "Can this dimension explain the price move? What is the confidence level?"
4. **Data-gap statement**: what information was not found, what is doubtful, what needs more information
5. Strictly separate "fact" from "speculation", following the objectivity principles in CLAUDE.md

**When done**:
1. Use TaskUpdate to mark the task as completed
2. Send the full reconnaissance report to team-lead via SendMessage (type: "message", recipient: "team-lead")
```

### Step 6: Track Progress in Real Time

- Each time a reconnaissance report arrives, show the user that dimension's 3 core findings
- Wait until all 4 have arrived
- Once all 4 are in, send a shutdown_request to the 4 agents via SendMessage

### Step 7: team-lead Synthesized Attribution

Aggregate the 4 reconnaissance reports and output an **attribution report** (not a research report — the emphasis is "judgment"):

---

#### 1. One-Sentence Attribution
> In one sentence (30-60 words), state: the primary cause of this price move + secondary cause + nature (value event / sentiment swing / unknown)

#### 2. Full Event Timeline (all 4 dimensions merged)

Reverse chronological, merging events from all dimensions:

| Date | Dimension | Event | Source | Attribution weight |
|------|------|------|------|-----------|
| 2026-04-30 | Company | XX | link | 🔴 High |
| 2026-04-29 | Industry | XX | link | 🟡 Medium |
| 2026-04-28 | Sentiment | XX | link | ⚪ Low |

Weight legend: 🔴 High (enough to explain the move on its own) / 🟡 Medium (contributes partly) / ⚪ Low (background noise)

#### 3. Attribution Table

| Candidate explanation | Evidence | Counter-evidence | Confidence | Persistence |
|---------|------|------|------|--------|
| e.g., earnings miss | revenue 5% below expectations, gross margin down | one-off factor, management has an explanation | High | short-term 1-2 weeks |
| e.g., industry beta | peers down 8% over the same period | this stock fell notably more than the industry | Medium | in line with industry |

#### 4. Nature Judgment (Core Conclusion)

Check one:

- [ ] **Value event**: fundamentals genuinely changed (earnings, moat, management, end-state) — the thesis needs re-examination
- [ ] **Sentiment/technical swing**: no fundamental change; driven by flows/sentiment/beta — treat as opportunity or noise
- [ ] **Cause unknown**: no event found that matches the magnitude of the move — **this is the most dangerous conclusion**; either the market knows something (insider/front-running) or we missed an information source
- [ ] **Mixed**: part value event + part sentiment amplification

#### 5. Per-Dimension Reconnaissance Summary

For each dimension, the 3-5 most important findings + that dimension's attribution contribution.

#### 6. Action Recommendations

| Action | Recommended? | Rationale |
|------|--------|------|
| Trigger thesis review (`/thesis-tracker`) | | |
| Trigger deep earnings reading (`/earnings-review`) | | |
| Trigger management review (`/management-deep-dive`) | | |
| Position action (add/trim/hold) | | Suggestion only; the final decision rests with the user |
| Observe only | | |

#### 7. 7-30 Day Tracking Checklist

- [ ] Pending event 1 (e.g., 5/15 earnings call)
- [ ] Metric to track 2
- [ ] Key signal to watch 3

#### 8. Information-Gap Statement

Honestly list the doubts this reconnaissance could not resolve, the information not found, and items awaiting more disclosure. **Better to mark "uncertain" than to fill gaps with speculation.**

---

### Step 8: Save the Report

Write to `reports/{Company}/{Company}-news-{YYYYMMDD}.md`. If the `reports/{Company}/` directory does not exist, create it (this means no research report has yet been created for the company). Use English/latin company folder names.

### Step 9: Clean Up the Team

Use TeamDelete to release team resources.

## Key Principles

1. **Fast beats complete** — the core value of this skill is delivering an attribution judgment within 10-15 minutes; do not fall into deep analysis (that is other skills' job)
2. **Attribution over enumeration** — finding events is easy; the hard part is judging "which event deserves this price move." Subtract, don't add
3. **Be honest about "unknown"** — when no primary cause can be found, clearly write "cause unknown." This is more valuable than forcing a causal chain (the market may be front-running bad news)
4. **No preset stance** — don't lean toward "it's just sentiment, nothing's wrong" because you hold the stock. Write whichever way the evidence points
5. **Distinguish "catalyst" from "coincidence"** — events happening at the same time aren't necessarily the primary cause; check whether the magnitude of impact matches
6. **Respect information availability** — a C-grade company may simply have no findable news, and that conclusion itself must be written down
7. **Follow the objectivity principles in `CLAUDE.md`** — attach a data source to every judgment; separate fact from opinion
8. **Don't make decisions for the user** — provide attribution and an action checklist, but leave buy/sell decisions to the user
