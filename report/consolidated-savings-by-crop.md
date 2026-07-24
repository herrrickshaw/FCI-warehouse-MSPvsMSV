# Consolidated per-crop savings: import price vs domestic margin vs food-processing offtake

*Master table tying DGCI&S import prices (per ton), domestic processing margins, and
import-substitution savings — with the government-to-food-processor offtake channel that
secures demand for each. Model: [`data/consolidated_savings_by_crop.py`](../data/consolidated_savings_by_crop.py) →
[`data/consolidated_savings_by_crop.csv`](../data/consolidated_savings_by_crop.csv). July 2026.*

## The three columns that decide every crop

For each product the government could make from what it procures:
- **Import price/ton (DGCI&S)** — what India pays to import the derivative today (the ceiling
  the domestic product competes against).
- **Domestic margin** — the processing spread India earns making it (from the verified
  company financials + crush/mill models).
- **Food-processing offtake** — the demand channel that keeps the product moving if consumer
  demand softens (the ethanol-style engineered-demand lever).

**Savings = substitutable volume × import price.** The offtake channel is what makes the
savings *bankable* rather than hypothetical.

## The master table

| Crop / stream | Product | Import ₹/t (DGCI&S) | Subst. vol (LMT) | Savings (₹ cr/yr) | Domestic margin | Food-processing offtake |
|---|---|---|---|---|---|---|
| **Rice→bran** | Rice bran oil | 97,970 | 7.70 | **7,544** | ₹60 ex-mill vs ₹105 parity = ₹45/kg + DORB | Frying/snacks/HoReCa (232°C) + fortification mandate |
| Pulses–tur | Tur dal | 56,463 | 5.00 | 2,823 | dal-mill 8–12% + chuni feed | Dal millers (NAFEX) + PDS pulse pilot |
| Pulses–urad | Urad dal | 74,163 | 3.00 | 2,225 | dal-mill margin | Dal millers + papad/snack processors |
| Pulses–masur | Masur dal | 50,888 | 4.00 | 2,036 | dal-mill margin | Dal millers + institutional |
| Cotton→seed | Cottonseed oil | 98,766 | 2.00 | 1,975 | crush margin + meal | Food processing + Vanaspati/HoReCa |
| Maize | Starch/HFCS/sorbitol | 37,170 | 3.00 | 1,115 | wet-mill spread | Food/pharma/paper processors |
| Rice→husk | Precipitated silica | 86,730 | 1.00 | 867 | RHA ₹1–3.5 → silica ~30× jump | Tyre/industrial (45% tyre demand) |
| Oilseeds | Soy/pea protein isolate | 265,500 | 0.30 | 796 | high vs meal | Food processing + export |
| Rice→bran | Gamma oryzanol | 10,620,000 | 0.005 | 531 | value-dense, volume-limited | Nutraceutical export + fortification |
| Rice→bran | Tocotrienols/Vit-E | 17,700,000 | 0.004 | 708 | imports 60–70% | Fortification input (captive) + pharma |
| Oilseeds | Soy lecithin (specialty) | 115,050 | 0.20 | 230 | imports specialty grades | Food-processing emulsifier (captive) |
| Wheat | Vital wheat gluten | 114,342 | 0.13 | 149 | wet-mill gluten+starch | Bakery/meat-analogue/pet-food (captive) |
| Wheat | Wheat germ oil | 442,500 | 0.02 | 88 | wasted germ fraction | Nutraceutical/cosmetic + export |
| Oilseeds | Mustard/groundnut oil | 98,766 | 0.00 | 0 | premium ₹136 vs palm ₹98 | Premium retail + processing blends |
| Maize | Corn gluten meal | 44,250 | 0.00 | 0 (already +) | 60% protein | Feed **export** — already positive |
| Wheat | Fortified atta (PDS) | — | — | captive | no import | Government PDS/ICDS (captive) |
| **Total** | | | | **~21,000** | | |

*Import prices are DGCI&S FY26 unit values (₹/USD 88.5) for the parent commodity, or the
byproduct's own import price where verified (gluten, silica, nutraceuticals). Volumes are
realistic substitutable ceilings, not production totals. Illustrative — a ±20% swing in any
volume moves the total ~₹2–4k cr.*

## Reading the table: four tiers of opportunity

1. **The edible-oil block dominates (~₹7,500 cr, RBO alone).** Highest single savings, lowest
   technical risk (capacity exists), and the deepest offtake (industrial frying is
   price-inelastic). This is the anchor.
2. **Pulses dal-processing (~₹7,000 cr across tur/urad/masur).** Not import substitution of
   the *oil* type but capturing the *dal-milling margin* the state currently gifts by selling
   pulses raw to millers — with the tariff as the precondition (tur import at ₹56,463/t
   undercuts MSP, so the floor must hold). Offtake: the existing dal-miller auction network.
3. **The scalable industrial mid-tier (~₹4,000 cr: silica, maize starch, cottonseed,
   protein isolate).** Real volume, real margin, needs modern integrated plants (the PPP
   white space) and food/industrial-processor offtake.
4. **The value-dense molecular tail (~₹1,700 cr: oryzanol, Vit-E, lecithin, gluten, germ
   oil).** High ₹/ton, small volume — the savings are modest but the *strategic* value is
   import-independence for fortification inputs (making India's own Vitamin-E from its own
   bran) and captive food-processing demand (gluten for bakery). Value density, not scale.

## The food-processing offtake is the common thread

Every row's demand is *contractable*, not consumer-dependent — the project's recurring
finding. The government selling to food-processing companies is the demand backbone:

- **Frying-oil supply contracts** (RBO, cottonseed oil) — industrial frying is decoupled from
  the retail shelf.
- **Ingredient supply** (starch, gluten, lecithin, protein) — food processors need these as
  inputs and currently import them.
- **Fortification mandates** (RBO, Vit-E, fortified atta/rice) — the state *creates* the
  demand, exactly as the ethanol blending mandate did for grain distilleries.
- **Feed/export floors** (DORB, oilmeal, corn gluten meal, chuni) — clear even if food demand
  doesn't.

So the savings in column 5 are not "if consumers buy it" — they are "if the government
contracts food-processor and institutional offtake," which it controls. That converts the
~₹21,000 cr from a hopeful market outcome into a policy-deliverable one.

## The headline: import the derivative, gift the feedstock

The table quantifies the pattern the byproduct-tree report named: across rice, wheat, maize,
pulses, oilseeds, and cotton, **India imports the processed derivative (RBO-equivalent oil,
dal, gluten, silica, Vitamin-E, lecithin, starch) while holding — and often gifting or
raw-exporting — the feedstock it already procures at MSP.** Capturing even the high-confidence
tiers (edible oil + pulses dal-margin + industrial mid-tier) is **~₹18,000–21,000 cr/yr of
import substitution and processing margin**, on feedstock the state already owns, sold through
offtake channels the state can contract.

## Caveats

Import prices are DGCI&S FY26-provisional parent-commodity unit values except where the
byproduct's own import price is verified (gluten $1,292/t, silica, nutraceuticals). Domestic
margins are from the verified company financials ([company-financials-notes.md](company-financials-notes.md))
and the crush/mill models, not audited plant P&Ls. Substitutable volumes are the analyst's
realistic ceilings; the nutraceutical tail is deliberately capped small (India's oryzanol
market is only ~$6.5 mn — the volume opportunity is tiny even though ₹/kg is huge). Pulses
"savings" assume the tariff floor holds (tur landed below MSP in FY26). Totals are
illustrative and additive across independent streams — not a single-plant projection.
