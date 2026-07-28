---
name: political-risk
description: Assess a Brazilian (B3) company's exposure to government/state influence and political risk — ownership, management appointments, price controls, regulation, fiscal extraction, privatization catalysts, and election-cycle sensitivity — and judge whether it changes the investment thesis.
---

# Political & State-Influence Risk (Brazil / B3)

Run a structured political-risk assessment on $ARGUMENTS.

> In Brazil, buying a company often means underwriting its exposure to the State. The government appears as controlling shareholder, price-setter, regulator, lender, and tax authority — sometimes all at once. A business that is excellent on paper can still destroy shareholder value if the State uses it as a policy or fiscal tool. It can also *create* value — an implicit sovereign backstop, cheap BNDES funding, strategic protection, or a privatization that re-rates the whole company. This skill isolates that exposure so it can be **priced, not ignored**.
>
> **Munger, inverted:** "How could the government destroy — or rescue — this investment?" Answer that first.

Default market: Brazil / B3. Currency = Brazilian Real (R$, BRL); note USD ADRs where relevant. Output in English.

## When this matters most (and when it barely does)

| Exposure tier | Examples | How to run it |
|---|---|---|
| **State-controlled** | Petrobras (PETR4), Banco do Brasil (BBAS3), Sabesp (SBSP3), Eletrobras (ELET3/ELET6), Copel (CPLE6), Sanepar (SAPR11), Cemig (CMIG4), Copasa (CSMG3) | Full skill — this is the core case |
| **Heavily regulated** | Utilities (ANEEL), oil & gas (ANP), banks (BACEN), telecom (ANATEL), health plans (ANS), water/sanitation (ANA), toll/rail concessions (ANTT) | Full skill; focus on the regulatory + concession + pricing channels |
| **Policy/subsidy-dependent** | Agribusiness (Plano Safra credit), homebuilders (Minha Casa Minha Vida), BNDES-financed capex | Run channels 3–6 |
| **Largely private / lightly regulated** | WEG (WEGE3), Ambev (ABEV3), Localiza (RENT3), Weg-type industrials | Light pass — confirm low exposure and move on. **Say so explicitly; don't manufacture risk that isn't there.** |

If the company is in the last tier, the honest conclusion is "low state exposure" — a valid and valuable finding. Don't pad it.

## How to run it (execution flow)

1. **Classify** the company into an exposure tier above and state it.
2. **Pull the control facts** from primary sources (see "Where to find the facts").
3. **Assess each of the 7 channels** — present? mechanism? historical track record? — and rate each ★1–5.
4. **Assess control-change catalysts** (privatization / re-nationalization) separately — these are often the biggest single value drivers, up or down.
5. **Score** the overall rating using the rubric (worst material channel dominates — see below).
6. **Build election scenarios** for October 2026 (federal and/or the relevant state race).
7. **Run the historical track-record test** (mandatory, both directions).
8. **Deliver the verdict** — does this change the thesis, and by how much required margin of safety.

## Where to find the facts

- **Ownership, golden share, tag-along, share classes:** the company's *Estatuto Social* and *Formulário de Referência* (CVM, via the RAD portal at www.rad.cvm.gov.br), and B3's company page for the governance segment.
- **Whether Lei das Estatais (nº 13.303/2016) applies** and board composition: *Formulário de Referência* + the company's governance/IR pages.
- **Pricing/tariff regime & regulation:** the sector regulator's site (ANP, ANEEL, ANATEL, ANS, ANA, ANTT), concession contracts, tariff-review calendars.
- **Fiscal/dividend history:** CVM filings, *fatos relevantes*, dividend/JCP history.
- **Elections & polls:** reputable Brazilian polling (Datafolha, Quaest, Ipec) and financial media (Valor, Brazil Journal, InfoMoney); prefer the connected MCP market-data tools + WebSearch/WebFetch over any scraping.
- Cross-verify every key control fact (ownership %, golden share, appointment history) with **≥2 independent sources**.

## The seven influence channels

Rate each channel's threat ★1–5 (1 = negligible, 5 = thesis-defining). Cite a source for every factual claim, with dates.

1. **Ownership & control.** Who holds the votes? Federal *União*, a state or municipal government, BNDES/BNDESPar, or state-linked pension funds (Previ, Petros, Funcef)? Is there a **golden share** (*ação de classe especial*) giving veto rights? Separate voting control from economic interest (ON …3 / PN …4 / UNIT …11). What is the tag-along right for the class you'd actually buy?
2. **Management appointment.** Are the CEO and board politically appointed or subject to political turnover? Document the appointment history and its correlation with election cycles. Does **Lei das Estatais** apply, and are its independence/quarantine rules being respected or eroded?
3. **Pricing & policy.** Can the government set or pressure the company's prices? (fuel import-parity policy at Petrobras; tariff reviews at ANEEL / sanitation tariffs; directed credit and rate pressure at Banco do Brasil). Who bears the gap when prices are held below cost — the controller, or minority shareholders?
4. **Regulation.** Which regulator governs the company? Concession/permit renewal risk and timing; pending *marco regulatório* changes; expropriation-by-regulation history.
5. **Fiscal extraction.** Is the company used as a fiscal tool — special/extraordinary dividends or JCP demanded by the controller to plug a budget, forced investment programs, royalties/CFEM, windfall or sector-specific taxes, "parafiscal" obligations?
6. **Capital-allocation interference.** Pressure to over-invest, pursue non-economic/social-political projects, make policy-driven M&A, or extend subsidized lending. Historically the single largest source of value destruction in Brazilian estatais.
7. **Election / political-cycle sensitivity.** How does the thesis shift across plausible outcomes of the **October 2026 general elections**? Identify the *relevant* race: **federally-controlled** names (Petrobras, BB, Eletrobras) hinge on the **Presidential + Congressional** result; **state-controlled** names hinge on the **Governor** of the controlling state — also on the Oct-2026 ballot (e.g. Sabesp → São Paulo; Copel/Sanepar → Paraná; Cemig/Copasa → Minas Gerais). Note what polls suggest and what is already priced in.

## Control-change catalysts: privatization & re-nationalization (both directions)

Treat separately from the channels — these are step-changes, not gradual pressure:
- **Privatization / de-statization** is frequently the largest *positive* re-rating for a state company (recent precedents: Eletrobras 2022, Copel 2023–24, Sabesp 2024). Assess: is it on the political agenda, what stage (study / approved / executing), and what governance uplift (often a move toward Novo Mercado) it would bring.
- **Re-nationalization / tighter state grip** is the mirror risk: reversal of a privatization, a new controller-driven mandate, or a return to directed pricing.
- For each live catalyst, state probability (qualitative), trigger, and rough value impact.

## Historical track-record test (mandatory)

State involvement is not automatically bad. Judge from evidence, both ways:
- Find 2–3 concrete episodes where government influence **helped or hurt** minority holders (e.g., Petrobras' 2010–2016 value destruction under directed pricing + over-investment vs. its 2019–2021 governance-led recovery; a forced tariff freeze; a value-accretive privatization).
- For each: what happened, over what period, and the share-price/dividend consequence. Cite sources with dates.

## Scoring rubric (important)

**Political risk is not additive and is not an average.** A single ★5 channel — e.g., the State can freeze your selling price below cost at will — defines the investment regardless of how benign the other six channels are. Therefore:

- **Overall Political-Risk Rating ≈ the highest *material, live* channel score**, adjusted down only if strong mitigants genuinely neutralize it.
- ★1 negligible · ★2 minor/monitor · ★3 material, manageable, needs a discount · ★4 severe, thesis-shaping · ★5 thesis-defining / can override business quality.
- Weigh mitigants explicitly: governance segment (Novo Mercado / Nível 2 curb some abuses; many estatais list only PN or sit at Nível 1 — weaker), Lei das Estatais + independent board, tag-along, the current administration's track record with minorities, and revenue diversification away from the exposed segment.

## Output

Save to `reports/{Company}/{Company}-political-risk-{YYYYMMDD}.md`.

1. **One-line verdict** — the dominant political risk (or "low state exposure") and whether it changes the thesis.
2. **Channel scorecard:**

   | Channel | Present? | Mechanism | Track record | Threat ★ |
   |---|---|---|---|---|
   | Ownership & control | | | | ★ |
   | Management appointment | | | | ★ |
   | Pricing & policy | | | | ★ |
   | Regulation | | | | ★ |
   | Fiscal extraction | | | | ★ |
   | Capital allocation | | | | ★ |
   | Election-cycle | | | | ★ |

3. **Control-change catalysts** — privatization / re-nationalization: status, trigger, rough value impact (or "none live").
4. **Overall Political-Risk Rating** — ★1–5 per the rubric (worst material channel dominates), with the one sentence that justifies it.
5. **Election scenario table (Oct 2026)** — 2–3 outcomes of the *relevant* race (federal and/or state) → expected impact on the thesis → what is already priced in.
6. **Track-record evidence** — the 2–3 historical episodes, helpful and harmful, with dated sources.
7. **Does this change the thesis?** — one of: *no material change* / *raises the required margin of safety* / *thesis-breaking unless priced accordingly* — and **quantify it**: the incremental margin of safety or fair-value haircut you'd now demand (e.g., "require a further ~20–30% discount to intrinsic value").
8. **Monitor list** — specific triggers (CEO/board changes, tariff reviews, dividend-policy shifts, privatization steps, *fato relevante*, election polls, regulatory rulings).

## Principles

- **Objectivity above all.** Separate fact (sourced) from opinion (labelled). Present both sides — state control has upsides (backstop, scale, cheap funding, privatization optionality) as well as costs; show them.
- **No preset stance.** Lay out the channels and evidence, then let the rating fall out of the data. Don't assume "state = bad" or "state = safe."
- **Honest about uncertainty.** Political outcomes are genuinely uncertain — price the range; don't pretend to a point forecast.
- ★ ratings use whole stars (1–5), no half-stars.

## Relationship to other skills

- Feeds the **risk-assessor** role in `/investment-team` and Step 4 (Inversion & Risk) of `/investment-research`.
- The ownership/control facts overlap with the owner-alignment analysis in `/management-deep-dive`; reuse them.
- Pairs with `/news-pulse` when a state-linked name moves on a political headline.
- Findings that raise the required margin of safety should be carried into `/thesis-tracker`.
