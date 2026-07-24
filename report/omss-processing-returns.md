# Returns on the "buy government grain → process → sell" business

*Unit-economics model ([`data/omss_processing_model.py`](../data/omss_processing_model.py)) grounded in
verified company financials ([`data/agri_company_financials.csv`](../data/agri_company_financials.csv)).
Prices from the repo: OMSS reserve 2025-26, mandi medians 23-Jul-2026, published milling outturns.
July 2026.*

## The headline: returns rise the further you get from the grain

The business splits into three tiers, and the verified balance sheets of India's actual
grain processors confirm a clean ladder — **the money is not in sourcing government grain,
it is in branding what you make from it.**

| Tier | Business | EBITDA margin | PAT | ROCE | Real-world proof (latest FY) |
|---|---|---|---|---|---|
| 1 | Raw trading / crushing | **2–4%**, periodically loss | 0–2% | mid-teens | Cargill India 3% (FY24; **FY23 a −₹113 cr loss**), Bunge India 2.3% (FY24; FY23 loss), AWL blended 3.9% |
| 2a | Flour/rice milling (our model) | **7–8%** | — | ~22% | 300-TPD mill: ₹196/qtl EBITDA, ~₹18 cr on ₹263 cr revenue |
| 2b | Branded staple processing | **11–12%** | 7–9% | 12–19% | KRBL 12.0%/8.5%, LT Foods 11.3%/7.1% |

Branded processors earn **3–5× the raw trader's margin on the same grain** (KRBL/LT Foods
vs Cargill/Bunge). The value-add is brand + distribution, not milling — but it is
working-capital-heavy (basmati ages 286–358 inventory-days), so ROCE lands at 12–19%,
*below* the EBITDA margin.

## Finding 1 — there is no OMSS *arbitrage* today

OMSS wheat reserve price (₹2,550/qtl, 2025-26) sits **above** the mandi median
(₹2,500, 23-Jul-2026). Buying from FCI is a supply-*security* channel, not a buy-cheap
trade. Any return must come from the processing spread, and the raw spread is thin:

```
WHEAT → ATTA, OMSS-sourced:  grain ₹2,550 → atta+bran ₹2,926 → EBITDA ₹196/qtl (6.7%)
WHEAT → ATTA, mandi-sourced: grain ₹2,500 → atta+bran ₹2,926 → EBITDA ₹246/qtl (8.4%)
```

OMSS sourcing is *lower*-margin than the open mandi right now — confirming the channel
exists for price-stabilisation and assured supply, not to hand processors a cheap input.
This is exactly why pure traders (Cargill, Bunge) swing between 3% profit and outright
loss year to year: a thin spread fully exposed to price moves, matching the
holding-economics result that naked grain carries −8 to −15%/yr.

## Finding 2 — open-market rice milling barely breaks even, which is why CMR exists

```
PADDY → RICE, open market: paddy ₹2,385 → rice+bran+husk ₹2,520 → EBITDA −₹15/qtl (−0.6%)
```

At today's paddy-to-rice price relationship an independent miller who *buys* paddy makes
almost nothing. So millers don't buy paddy and take price risk — they mill the
government's grain under **Custom Milled Rice (CMR)** for a fixed fee and keep the
byproducts. That is where the real compensation hides.

## Finding 3 — the ₹7,600 cr byproduct giveaway (the invisible return)

Under CMR the state hands millers ~832 LMT of paddy a year (KMS 2024-25). The *visible*
compensation is the ~₹15/qtl milling fee — about **₹1,250 cr/yr**. But millers also retain
the **rice bran and husk**, worth:

```
gross byproduct value retained by millers:  ₹20,134 cr/yr
net of milling cost:                        ₹ 7,654 cr/yr
vs the visible ₹15/qtl milling fee:         ₹ 1,248 cr/yr
```

**The real return on the government-to-miller relationship is ~6× the fee the government
thinks it is paying** — and it is paid in bran, not rupees, so it never appears in a
budget line. Rice bran → rice-bran oil is the single most under-priced margin in the whole
chain; the state gives it away by accounting invisibility.

## What this means for the MSV / forward-sale design

1. **Never sell MSV grain on the expectation of a trading profit.** Tiers 1 and the
   holding-economics analysis agree: raw grain trading is a structurally thin 1–4% business
   that flips to loss in bad price years. The state should budget its disposal as a
   *cost recovery*, not a margin.
2. **Price the byproduct, don't gift it.** Auction CMR rights (and any MSV forward-sale
   that carries a byproduct stream) rather than awarding them at a fixed fee — the
   ~₹7,650 cr/yr of retained bran/husk value is money the state is currently leaving on
   the table across the whole procurement book.
3. **Capture Tier-2 margin where feasible via public brands.** The 11–12% branded-staple
   margin (KRBL/LT Foods) is exactly what Bharat Atta/Rice/Dal reaches for. Every quintal
   the state sells raw at the ₹2,550 OMSS reserve forgoes the ₹300–400/qtl brand margin
   that NAFED/NCCF (or a private offtaker) then captures — the HAFED own-processing model
   is the counter-example that keeps it public.
4. **Working capital is the moat, not milling.** Branded processors' returns are gated by
   ROCE (12–19%) because aged inventory ties up cash — a state trader emulating them needs
   patient capital and, critically, the hedging tools SEBI suspended (see the trader
   playbook): you cannot run a 300-day inventory book unhedged without becoming Thailand.

## Caveats

Unit economics use labelled price/yield inputs (atta ₹33/kg, bran ₹19/kg, rice ₹34/kg,
outturns 76%/67%); a ±₹1/kg swing in atta or bran realisation moves the milling margin
2–3 points, so treat the **structure** (processing > sourcing > trading; byproduct is the
hidden return) as the finding and the exact percentages as illustrative. Company margins
are latest-FY verified from screener.in / CRISIL rationales; ITC Agri (~8–9%) is a blended
trading + leaf-tobacco/spice figure, not a clean grain read; Cargill FY24 PAT and LDC/Olam
margins are unverified (audited/paywalled) — see the financials notes.
