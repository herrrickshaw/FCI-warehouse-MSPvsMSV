# Biodiesel blending scenarios from rice husk + bran — the arithmetic verdict

*Deterministic scenario model ([`data/biodiesel_blending_scenarios.py`](../data/biodiesel_blending_scenarios.py)).
Denominators verified; conversion constants labelled. July 2026. Companion to
[oilseeds-biodiesel-consumption.md](oilseeds-biodiesel-consumption.md).*

## The question, and the blunt answer

*At different levels of rice husk + bran utilisation, what biodiesel blend (B1…B5) can
India actually reach, and what volume of rice bran oil makes cooking-oil imports cheaper?*

**Answer: the rice byproduct chain is a cooking-oil story, not a biodiesel story.** Full
utilisation of India's rice bran delivers **~₹8,200 cr/yr of edible-oil import substitution**
— but the "waste acidic oil" left after refining reaches only **~B0.15**, and *nothing* from
the rice chain (or even the whole national waste-lipid basket) can reach B1, let alone B5.
The husk is an *energy* lever, not a blend component. The two goals do not compete because
they operate at completely different scales.

## The cascade and its scale mismatch

```
100 kg paddy → 67 rice + 22 HUSK + 8 BRAN + 3 loss
   BRAN (8%)  → stabilise → solvent-extract → crude RBO (16% of bran)
       crude RBO → refine → EDIBLE rice bran oil  ←── the prize (imports ↓)
                          → acid oil (~10%)        ←── "waste acidic oil" → biodiesel
   HUSK (22%) → boiler power / silica / biochar    ←── energy, not fuel-blend
```

The mismatch is structural: India burns **~11,000 crore litres of diesel a year**
(91.4 MMT, PPAC FY25). B5 needs **549 crore litres** of biodiesel. The rice bran acid-oil
stream is measured in *single-digit* crore litres. Diesel demand is two-to-three orders of
magnitude larger than the food-safe lipid India can spare.

## Scenario table — bran utilisation → oil → import saving → biodiesel → blend

| Bran utilisation (% of ~98 LMT stock) | Total crude RBO (LMT) | Edible RBO vs today (LMT) | Import saving (₹ cr/yr) | Acid oil (LMT) | Biodiesel (cr L) | Blend level |
|---|---|---|---|---|---|---|
| 50% *(today)* | 7.8 | — | — | 0.78 | 8.5 | **B0.08** |
| 60% | 9.4 | +1.6 | 1,646 | 0.94 | 10.2 | B0.09 |
| 75% | 11.8 | +3.9 | 4,116 | 1.18 | 12.7 | B0.12 |
| 90% | 14.1 | +6.3 | 6,586 | 1.41 | 15.2 | B0.14 |
| **100%** | **15.7** | **+7.8** | **8,232** | **1.57** | **16.9** | **B0.15** |

*Constants: bran→crude RBO 16% (verified ~18%, conservative); acid oil 10% of crude
(derived, 8–12%); 1 LMT lipid → 10.8 cr L biodiesel (0.95 conversion, 0.88 density); import
parity ₹105/kg (reported 100–110). Bran stock ~98 LMT, ~50% currently oil-extracted, rest
to cattle feed (verified). Diesel 10,986 cr L/yr.*

## Reading the table: the two answers

**The cooking-oil answer is real and material.** India currently oil-extracts only ~half its
rice bran; the other half (~48 LMT) goes to cattle feed with the oil intact. Stabilising and
extracting the full stock lifts crude RBO from ~7.8 to ~15.7 LMT — an **incremental ~8 LMT of
edible oil worth ~₹8,200 cr/yr in displaced palm imports** (~5% of the ~₹1.6–1.7 lakh cr oil
bill), at an ex-mill cost (~₹65/kg) far below import parity (~₹105/kg). The crush capacity
already exists (SEA's ~30 MT). **This is the volume that makes cooking oil cheaper: roughly
doubling RBO output to ~15–16 LMT.**

**The biodiesel answer is a rounding error — and the arithmetic proves why B5 is unreachable
from food-safe feedstock:**

- **Acid-oil route (food-safe, recommended):** even 100% bran utilisation yields only ~1.57
  LMT acid oil → **16.9 cr L biodiesel = B0.15.** Cannot reach B1.
- **Whole crude RBO diverted to fuel (NOT recommended — burns edible oil India imports):**
  15.7 LMT → 169 cr L → only **B1.5**, and it would defeat the entire import-substitution
  purpose.
- **The whole realistic national non-edible waste basket** — rice acid oil (1.57) + collectible
  used cooking oil (~4 LMT of ~30 generated) + tallow (~1.5) ≈ 7.1 LMT → **76 cr L = B0.69.**
  Still below B1.
- **B5 needs ~51 LMT of oil feedstock — roughly a fifth-to-a-third of India's entire ~250 LMT
  edible-oil supply.** There is no food-safe way to get there. This is precisely why India's
  20%-biodiesel mission collapsed and why it must *not* be re-attempted on edible oil.

## Husk: the energy multiplier, not a blend feedstock

Rice husk (~183 LMT at government + all-India milling scale) is cellulosic and high-silica —
it does **not** transesterify into biodiesel. Its role is **process energy**: husk-fired
boilers already power rice mills and grain distilleries; ~183 LMT husk carries **~9,150 GWh/yr**
of generation potential. In the integrated model, husk supplies the heat for bran
stabilisation, solvent extraction, and esterification — making the edible-oil + residual-
biodiesel chain **energy-self-sufficient and low-carbon**, plus grid power and silica as
side revenue. Husk raises the *viability and carbon score* of the cascade; it adds zero to
the blend percentage.

## The verdict for policy

1. **Chase the cooking oil, not the blend.** The rice bran chain's payoff is ~₹8,200 cr/yr
   of edible-oil import substitution — real, sure, and using existing capacity. The biodiesel
   from it is B0.15 — worth capturing as a residual, worthless as a blending strategy.
2. **Biodiesel from rice is strictly a residual.** Only the non-edible acid oil goes to fuel,
   *after* the edible oil is extracted. India should never divert extractable edible bran oil
   to diesel while importing 56% of its cooking oil — the US distillers-oil-to-biodiesel model
   does not transfer.
3. **B5 is a mirage on food-safe feedstock.** The honest number: even the entire national
   waste-lipid basket is < B1. A meaningful biodiesel program would need dedicated non-edible
   plantation (the failed jatropha path) or would compete with food — which is why the
   blending ambition belongs to *ethanol* (where surplus grain/cane exists) and not to
   biodiesel (where India is structurally oil-deficient).
4. **Husk funds the process.** Use husk energy to make the extraction chain self-powered and
   carbon-favourable — the enabler that turns the ₹8,200 cr edible prize from a cost centre
   into a low-carbon, self-financing operation.

## Caveats

Bran stock (~98 LMT) and current extraction (~50%) are verified national figures; the
government-touchable subset is smaller (FCI hands paddy to CMR millers who keep the bran —
the ₹7,650 cr giveaway). Oil yield (16%), acid-oil fraction (10%), and the lipid→biodiesel
factor (10.8 cr L/LMT) are labelled engineering constants — a ±2 pt swing in yield moves the
import-saving ~₹1,000 cr but does not change the biodiesel verdict (the scale gap is 100×+).
UCO-collectible (~4 LMT) and tallow (~1.5 LMT) are reported order-of-magnitude, not audited.
Husk GWh assumes ~0.5 MWh/tonne and full collection.
