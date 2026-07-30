# Does diesel → CNG substitution lower the cost of crop production?

*Applied to the CACP A2+FL cost-of-production data (KMS/RMS 2025-26) in
[`data/cost_of_production.csv`](../data/cost_of_production.csv). Result in
[`data/diesel_cng_cost_impact.csv`](../data/diesel_cng_cost_impact.csv). July 2026.*

## Short answer: yes, but modestly (~2–4% of A2+FL) at today's prices — and the real prize is the circular residue-to-CBG loop

Diesel is a real input in A2 cost (machine operations + diesel-pump irrigation + transport), so
substituting it with CNG does lower the cost of production. But the effect is smaller than the
headline claims suggest, for two reasons the arithmetic makes clear.

## The two numbers that bound the effect

**1. Fuel is only ~8–14% of A2+FL.** CACP's A2 covers seed, fertiliser, pesticide, hired labour,
machine hire, fuel and irrigation. The *diesel* portion — tractor-operation fuel + diesel-pump
irrigation — is roughly **8–14%** of A2+FL (highest for paddy and diesel-irrigated crops, lowest
for rainfed). Machine charges alone rose ~367% for paddy (₹1,493→₹6,973/ha, 2006-07→2018-19),
so the mechanisation cost is real, but *fuel* is only part of the machine charge (the rest is
machinery capital + operator).

**2. CNG saves ~24% on the fuel bill today — not the 50% of 2021.** At current Tamil Nadu prices
(**diesel ₹99.65/L, CNG ₹84.50–97/kg**), and adjusting for CNG engines' ~10% lower efficiency:

```
Diesel  ₹99.65/L ÷ 38.6 MJ/L  = ₹2.58/MJ
CNG     ₹84.50/kg ÷ 48 MJ/kg ÷ 0.90 eff = ₹1.96/MJ
Fuel-cost saving = 24%
```

The PIB launch (2021) claimed **~50% saving and >₹1 lakh/yr per tractor** — but that was at
diesel ₹77.43/L vs CNG ₹42/kg, a much wider gap ([PIB PRID 1697555](https://pib.gov.in/Pressreleaseshare.aspx?PRID=1697555)).
The diesel-CNG price gap has since *narrowed*, so today's saving is ~24%, not 50%.

**Combined: A2+FL falls by ≈ fuel-share (8–14%) × fuel-saving (24%) = ~2–4%.**

## Per-crop effect (CACP A2+FL, 2025-26)

| Crop | A2+FL ₹/qtl | Diesel share | CNG saving ₹/qtl | A2 cut % |
|---|---|---|---|---|
| Paddy | 1,579 | 14% | ~53 | 3.4% |
| Wheat | 1,239 | 11% | ~33 | 2.7% |
| Groundnut | 4,842 | 11% | ~129 | 2.7% |
| Cotton | 5,140 | 12% | ~112 | 2.2% |
| Tur | 5,496 | 9% | ~120 | 2.2% |
| Maize | 1,544 | 10% | ~37 | 2.4% |
| Sugarcane | (per ha) | 13% | — | ~3.1% |

*Average across 20 CACP crops: ~2.2% A2+FL reduction. Full table in the CSV. Diesel-fuel
share is estimated (machine-op fuel + diesel irrigation) — CACP publishes machine charges and
irrigation charges but not a clean "diesel" line, so the share is an informed split, labelled
as such.*

## Where the effect is bigger than the average

1. **Diesel-pump irrigation → CNG/CBG (or solar).** Where farmers run diesel pumps (much of
   eastern India, unelectrified pockets), diesel is a *larger* slice of A2 and the substitution
   saves more — often the single biggest diesel line. CBG or solar pumping beats both.
2. **Custom-hire tractor fleets.** A tractor doing 1,000+ hrs/yr of custom work saves
   **~₹50,000–70,000/yr** at today's 24% gap (down from the ₹1 lakh at 2021's 50% gap) — enough
   to matter for the FPO/custom-hire-centre economics, less so for a single smallholder.

## The real prize: the circular parali → CBG → tractor loop

The PIB framing points to where the value actually compounds — **Waste to Wealth**. Under SATAT
(80 CBG plants commissioned by 30.11.2024, 72 under construction), crop **stubble/parali** — today
burned, causing the Delhi-NCR smog and a ₹-per-tonne disposal cost — becomes **Bio-CNG**. That
closes a loop this whole project keeps finding:

- **Residue income**: the farmer sells parali/straw to the CBG plant (turns a disposal cost into revenue).
- **Fuel saving**: the CBG fuels the CNG tractor at ~24% below diesel.
- **Emission cut**: ~70% lower emissions vs diesel (PIB), plus no stubble burning.
- **Byproduct**: CBG spent-slurry → FOM (fermented organic manure), cutting the fertiliser line of A2 too.

So the honest cost-of-production answer has two layers: the *direct* fuel substitution shaves
~2–4% off A2+FL, but the *circular* version — grow crop → residue to CBG → CBG fuels the tractor
→ slurry replaces fertiliser — attacks three A2 lines at once (fuel, residue-disposal, fertiliser)
and adds a residue-sale income. That is the same byproduct-cascade logic as the rice-biorefinery,
applied to the farm's own energy.

## The CBG loop, quantified — three layers, not one

Adding the three loop layers to the CACP A2+FL data
([`data/cbg_loop_cost_impact.csv`](../data/cbg_loop_cost_impact.csv)) — **CNG fuel saving
(24% on the diesel share) + FOM fertiliser offset (slurry replaces ~15% of chemical fertiliser)
+ net residue income (removable straw sold to the CBG plant, after baling/transport cost):**

| Crop | A2+FL ₹/qtl | + CNG fuel ₹ | + FOM offset ₹ | + Net residue income ₹ | **Total benefit ₹/qtl** | **Net A2 improvement** |
|---|---|---|---|---|---|---|
| **Wheat** | 1,239 | 33 | 30 | 99 | **161** | **13.0%** |
| **Paddy** | 1,627 | 55 | 39 | 90 | **184** | **11.3%** |
| Maize | 1,544 | 37 | 37 | 55 | 129 | 8.4% |
| Cotton | 5,140 | 148 | 123 | 135 | 406 | 7.9% |
| Groundnut | 4,842 | 128 | 116 | 28 | 272 | 5.6% |
| Tur | 5,496 | 119 | 132 | 52 | 303 | 5.5% |
| **Average (20 crops)** | | | | | | **~6.8%** |

**The residue income is the dominant lever for the straw-heavy cereals** (paddy, wheat) — exactly
the crops whose stubble is burned today. Monetising that straw (₹90–99/qtl) outweighs the fuel
saving (₹33–55/qtl) and the FOM offset combined. So the loop is really a *residue-monetisation*
story with fuel and fertiliser savings on top:

- **Fuel swap alone: ~2–4%** of A2+FL (small).
- **Full CBG loop: ~7–13% for cereals, ~6.8% average** — 2–4× the fuel-only effect.

The direct answer to "does diesel→CNG lower the cost of production" is *a little*; the honest answer
to "does the CBG loop it enables lower the cost of production" is *materially — and most for the
paddy/wheat stubble that is a burning liability today.*

*Loop-model caveats: removable straw is taken at 50–60% (the rest returns to the soil); net
residue price is ₹700–1,200/tonne after baling/transport (gross CBG-feedstock price minus
collection cost); FOM replaces ~15% of the fertiliser line. All are conservative, labelled
assumptions — the loop only realises where a CBG plant sits within collection range (SATAT
corridors), and the residue "income" is a farm-revenue offset to gross cost, not a cut in A2 inputs.*

## Caveats

- CNG-tractor adoption is nascent (first diesel-converted unit 2021; few OEM models; conversion
  capex ~₹50k–₹1 lakh). Rural CNG/CBG refuelling infrastructure is thin outside gas-grid corridors.
- The 24% fuel saving moves with the diesel-CNG price gap — it was 50% in 2021 and could widen
  again; it is *not* a fixed number. Solar pumping is often the cheaper irrigation substitution.
- Diesel-fuel share of A2 is an informed estimate from CACP machine + irrigation charges, not a
  published "diesel" line; treat the ~2–4% as an order-of-magnitude, not a precise figure.
- The circular CBG loop's economics depend on a CBG plant within collection range — real in the
  SATAT corridors (Punjab, UP, Maharashtra), not yet everywhere.

## Sources

CACP A2+FL: repo `cost_of_production.csv` (PIB MSP releases). Fuel prices: TN retail, Jul 2026
(diesel Chennai ₹99.65/L; CNG Chennai ₹97, Nagapattinam ₹84.50/kg). CNG-tractor economics &
emissions: [PIB PRID 1697067](https://pib.gov.in/PressReleasePage.aspx?PRID=1697067),
[PRID 1697555](https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1697555). SATAT/CBG status:
PIB (80 plants as on 30.11.2024). Machine-charge trend: CACP cost-of-cultivation analyses.
Energy contents: diesel 38.6 MJ/L, CNG 48 MJ/kg (standard). Illustrative — not investment advice.
