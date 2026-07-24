# RBO extraction: savings by volume processed, and securing demand if consumption drops

*Scenario model ([`data/rbo_savings_scenarios.py`](../data/rbo_savings_scenarios.py)) grounded
in ICRA's edible-oil thematic (~225 LMT consumption, 2021) and DGCI&S import data. July 2026.
Extends [biodiesel-blending-scenarios.md](biodiesel-blending-scenarios.md) and
[rice-mill-business-model.md](rice-mill-business-model.md).*

## Two questions

1. If rice-bran-oil extraction is applied to only *part* of the rice volume, how much is
   saved — at each level?
2. If consumer demand for RBO softens, what market levers keep the oil flowing (so the
   extraction investment isn't stranded)?

## Part 1 — savings by share of rice volume processed

Two bases: what the **government can directly direct** (the bran in its ~832 LMT of CMR
paddy ≈ **40 LMT bran**, 41% of the national total) and the **all-India ceiling** (~98 LMT
bran). Oil yield 16%; import parity ₹105/kg; ex-mill ₹60/kg (after the DORB feed credit);
DORB feed ₹15/kg. "Import displaced" = the forex/import-bill reduction; "net margin" = the
economic gain after extraction cost; "DORB feed" = the byproduct revenue (itself feed-import
substitution).

### Government-directed (CMR bran, ~40 LMT)

| Share processed | Bran (LMT) | RBO (LMT) | Import displaced (₹ cr) | Net margin (₹ cr) | DORB feed (₹ cr) |
|---|---|---|---|---|---|
| 25% | 10.0 | 1.6 | 1,675 | 718 | 1,166 |
| 50% | 19.9 | 3.2 | 3,349 | 1,435 | 2,332 |
| 75% | 29.9 | 4.8 | 5,024 | 2,153 | 3,499 |
| **100%** | **39.9** | **6.4** | **6,698** | **2,871** | **4,665** |

### All-India (98 LMT bran)

| Share processed | Bran (LMT) | RBO (LMT) | Import displaced (₹ cr) | Net margin (₹ cr) | DORB feed (₹ cr) |
|---|---|---|---|---|---|
| 25% | 24.5 | 3.9 | 4,116 | 1,764 | 2,866 |
| 50% | 49.0 | 7.8 | 8,232 | 3,528 | 5,733 |
| 75% | 73.5 | 11.8 | 12,348 | 5,292 | 8,600 |
| **100%** | **98.0** | **15.7** | **16,464** | **7,056** | **11,466** |

**The realistic near-term prize** is the incremental capture: ~48 LMT of bran currently goes
to **cattle feed with the oil intact** rather than to extraction. Routing it to
stabilise-and-extract yields **+7.7 LMT RBO → ₹8,064 cr of import displaced (~5% of the
~₹1.65 lakh-cr edible-oil bill)**, ₹3,456 cr net economic gain, plus ₹5,616 cr of DORB feed.
Every 25 percentage points of the government's own CMR bran processed ≈ **₹1,675 cr** of
import saved — a linear, dial-able lever.

## Part 2 — securing demand if consumer consumption drops

The risk: if branded-consumer RBO demand softens (price competition from palm, preference
shifts), does the extraction investment strand? **No — because RBO has an unusually deep
demand floor below the consumer shelf.** The same forward-linkage/offtake-contract logic the
project applied to grain (OMSS-to-processors, the ethanol mandate) applies here: engineered
demand channels backstop volatile consumer demand.

Five demand floors, in order of robustness:

1. **Food processing (the big one).** RBO is *technically superior* for industrial frying —
   smoke point ~232 °C and oryzanol give oxidative stability that palm and soft oils lack.
   Snack/namkeen, bakery, instant-food, and HoReCa frying are **price-inelastic industrial
   demand** that doesn't track the retail-oil shelf. This is where palm hides today (invisible
   industrial use); RBO can take share on performance. Selling government/co-op RBO to food
   processors on supply contracts is the primary demand backstop.
2. **Blending & fortification mandate.** RBO is already the health-positioned blend base
   (Saffola-type). A mandated inclusion in blended oils, or in the edible-oil Vitamin-A/D
   fortification programme, converts a marketing choice into a demand floor — the
   demand-*creation* lever, mirroring the ethanol blending mandate.
3. **Institutional offtake (PDS / ICDS / mid-day-meal).** Fortified RBO or RBO-blend into
   state nutrition programmes is a state-controlled demand backstop — the Bharat-brand model
   applied to oil.
4. **Export.** India already exports RBO; global oryzanol/health-oil demand is a premium
   outlet for surplus.
5. **Byproduct floors (the most secure of all).** DORB → feed is always in demand (India runs
   a feed-protein deficit); acid oil → soap/oleochemicals/biodiesel. The byproducts clear
   even if the oil doesn't.

**The lever, stated as policy:** the state does not need consumer demand to underwrite RBO
extraction — it can *contract* the demand. A food-processing supply agreement + a
fortification-inclusion mandate + institutional offtake together form a demand backbone
independent of the retail shelf, exactly as the ethanol blending mandate underwrites grain
distilleries. Consumer demand becomes the upside, not the precondition.

## Why this matters for the MSV/processing thesis

The savings scale linearly and controllably with the share of rice processed — so the
government can size the RBO push to its appetite (a 25% CMR-bran start saves ~₹1,675 cr; full
national capture ~₹16,464 cr gross). And because the demand can be contracted through food
processing and fortification, the extraction investment is de-risked the same way the ethanol
programme de-risked distilleries — a policy-created offtake floor. The bran the state gives
away today ([omss-processing-returns.md](omss-processing-returns.md), ₹7,650 cr) is the
feedstock; food-processing + fortification offtake is the demand; the ₹8,000-16,000 cr import
saving is the prize.

## Caveats

Bran (98 LMT all-India; ~40 LMT govt-touchable via CMR share) and 50%-already-extracted are
verified national figures; the government share is derived from its paddy share (~41%). Oil
yield 16% (conservative; ~18% achievable), parity ₹105/kg and ex-mill ₹60/kg are labelled
engineering/price assumptions — a ±2 pt yield swing moves each scenario ~10%. Consumption
~225 LMT (ICRA oil-year-2021; ~250 LMT current). RBO frying superiority (smoke point,
oryzanol) is established food science; the *scale* of processor demand it can capture is not
separately quantified here. Fortification-mandate and institutional-offtake volumes are
policy levers, not current commitments. DFPD's edible-oil-scenario page returned a server
error at access; consumption/import anchors are from ICRA + DGCI&S instead.
