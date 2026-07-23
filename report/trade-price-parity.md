# Trade Price Parity: India's Agri Exports/Imports vs MSP (FY2023-24 → FY2025-26)

*Collected 2026-07-23. Dataset: [`data/trade_price_parity.csv`](../data/trade_price_parity.csv)
(67 rows; rebuild with `data/build_trade_parity.py`; raw API captures in `data/raw_trade/`).*

All trade numbers are **DGCI&S** data served through APEDA AgriExchange's report APIs
(agriexchange.apeda.gov.in) and, for edible-oil HS lines, the Ministry of Commerce
**tradestat** portal (tradestat.commerce.gov.in). FY2025-26 is the **full year Apr-Mar,
provisional** — the portals' current reporting period had already rolled to 2026-27
(April-May) at collection time. Unit values are FOB (exports) / CIF (imports),
computed as value÷quantity from the same source table; the `fx_rate` column carries the
rate *implied by the source's own ₹-crore vs USD-mn columns* (FY24 ≈ 82.7-83.2,
FY25 ≈ 84.1-86.0, FY26 ≈ 87.5-90.4 — close to the FY-average USDINR 82.8 / 84.5 / ~86-88
convention used elsewhere in this repo).

Domestic references: KMS/RMS **2025-26 MSPs** (paddy 2369, wheat 2425, maize 2400,
tur 8000, moong 8768, urad 7800, gram 5650, masur 6700, groundnut 7263 ₹/qtl);
**rice** compared against a paddy-MSP-derived rice cost (2369 ÷ 0.67 outturn + milling ≈
₹3,700-4,000/qtl; 3,850 used); **sugar** against ex-mill realisation ₹38-39/kg (3,850;
the DFPD Minimum Selling Price is ₹31/kg, unchanged since Feb-2019). Comparing a
2025-26 MSP to FY24/FY25 unit values slightly overstates old-year gaps (MSPs were
lower then); the FY26 rows are the clean comparison.

## 1. Where export unit value sits vs MSP

| Crop (FY26 export) | UV $/t | UV ₹/qtl | Ref ₹/qtl | Gap |
|---|---|---|---|---|
| Basmati rice | 870 | 7,688 | 3,850 (rice cost) | **+100%** |
| Non-basmati rice | 390 | 3,449 | 3,850 (rice cost) | **−10%** |
| Wheat (residual flows) | 330 | 2,964 | 2,425 (MSP) | +22% (¹) |
| Maize | 293 | 2,622 | 2,400 (MSP) | +9% |
| Millets | 444 | 3,918 | 3,699 (jowar MSP, proxy) | +6% |
| Groundnut (kernels) | 1,041 | 9,178 | 7,263 in-shell / ~10,376 kernel-equiv | +26% / **−12%** |
| Sugar | 491 | 4,346 | 3,850 (ex-mill) | +13% |
| Pulses (mostly chana/kabuli/dals) | 972 | 8,597 | n/a | — |

(¹) On 0.3 LMT of NOC-only shipments under the ban — not a market price.

- **Basmati is the only grain decisively above export parity** — it exports at roughly
  double the common-rice cost basis and needs no support. India's rice export dominance
  (21.6 MMT combined in FY26 ≈ **~40% of world rice trade** of ~55-60 MMT) rests on
  basmati premia plus huge low-cost non-basmati volume.
- **Non-basmati rice exports sit essentially AT the paddy-MSP-derived cost** (−12% to
  +2% across FY24-FY26). MSP-priced paddy converts to rice at ≈ the world price; any
  MSP hike or rupee strength pushes common rice out of competitiveness. The state's
  procurement machine and the export market are bidding for the same grain at nearly
  the same price — which is why, in the 2022-24 inflation episode, the government had
  to *break* export parity administratively rather than let exports drain the pool.
- **Maize and millets export within ±10% of MSP** — thin margins, so flows swing hard:
  maize exports collapsed to 5.6 LMT in FY25 (UV ₹3,066 > MSP, i.e. only premium niches
  cleared) when ethanol demand pushed domestic mandi prices above world parity, and
  India simultaneously imported 9.7 LMT (the 5-LMT TRQ at 15% duty year); FY26 saw
  exports recover to 12.8 LMT and imports collapse to 0.6 LMT.
- **Groundnut basis matters**: exports (shelled kernels) fetch +26% over the *in-shell*
  MSP but ~−12% vs the kernel-equivalent MSP (7263 ÷ 0.70) — consistent with recurring
  PSS procurement in Gujarat: the mandi price of pods sits below MSP even while kernel
  exports look "profitable".
- **Sugar** exports at +13% over ex-mill (and +40% over the ₹31/kg MSP floor) — export
  parity is positive but the government caps volumes by quota (nil in 2023-24 season,
  10 LMT allowed Jan-2025) to protect domestic supply and ethanol diversion.

### The 2022-24 export-ban episodes deliberately broke export parity
- **Wheat: export ban 13-May-2022, still in force** through FY26 (only NOC/G2G flows —
  0.036-0.31 LMT/yr in the data vs 72 LMT exported in FY22). Domestic prices were held
  near MSP while world prices spiked ~40% above it.
- **Rice**: 20% export duty on white/paddy Sep-2022; **non-basmati white rice ban
  20-Jul-2023**; 20% duty on parboiled Aug-2023; basmati MEP $1,200→$950/t. All
  unwound Sep-Oct-2024 (ban lifted, MEP scrapped, duties zeroed) — visible in the data
  as FY25's jump to 14.1 MMT and FY26's record 15.0 MMT at a *lower* UV ($390/t).
- These bans are the mirror image of an MSV: where MSP defends the floor, export bans
  defended the *ceiling* by confiscating the export-parity premium from farmers.

## 2. Import parity below MSP — the pulses problem

| Import (FY26) | UV $/t CIF | UV ₹/qtl | MSP ₹/qtl | Gap | Duty status FY26 |
|---|---|---|---|---|---|
| Tur (14.8 LMT) | 639 | 5,659 | 8,000 | **−29%** | duty-free to 31-Mar-2026 |
| Urad (10.5 LMT) | 838 | 7,418 | 7,800 | −5% | duty-free to 31-Mar-2026 |
| Masur (11.5 LMT) | 575 | 5,145 | 6,700 | **−23%** | 10% from Mar-2025 |
| Yellow peas (11.1 LMT) | 358 | 3,164 | 5,650 (gram, substitute) | **−44%** | free → **30% from 01-Nov-2025** |
| Desi chana (10.1 LMT) | 532 | 4,813 | 5,650 | −15% | 10% from 01-Apr-2025 |
| Wheat (0.8 LMT) | 327 | 2,862 | 2,425 | +18% | 40% duty |
| Veg oils (169 LMT) | 1,150 | ₹101.7/kg | no MSP on oil | see §3 | crude 16.5% eff. (cut 30-May-2025) |

- **The sign flipped between FY25 and FY26.** In FY24-FY25 (El Niño shortage years)
  tur imported at +7 to +10% *above* MSP and urad at +13 to +19% — imports were the
  expensive marginal supply and MSP was not binding. In FY26 world prices broke and
  now **every major imported pulse lands below its MSP** (tur −29%, masur −23%, chana
  −15%, urad −5%). Landed CIF is before ~3-8% port-to-mandi costs, so the effective
  undercut is a few points smaller but still decisive for tur/masur/peas.
- **Yellow peas are the systemic leak**: no MSP of their own, CIF ₹3,164/qtl, and they
  substitute for chana (MSP 5,650) in dals and besan. The 21.6 LMT duty-free flood of
  FY25 is what pushed chana and even tur mandi prices down — the 30% duty from
  Nov-2025 (announced effect: reversing the free window) is the tariff response, and
  the FY26 volume already halved.
- Government policy is now visibly *tariff-reactive to this parity gap*: chana 10%
  (Apr-2025), masur 10% (Mar-2025), peas 30% (Nov-2025), while tur/urad — where the
  structural deficit persists — remain duty-free through Mar-2026.

## 3. Edible oils: import parity vs MSP-linked oilseed economics

There is no MSP on oil, but MSP-priced oilseeds imply a domestic oil cost: mustard MSP
₹5,950/qtl at ~33% oil recovery implies seed-cost-in-oil of ≈ ₹180/kg before crush
margin and meal credit (net ≈ ₹140-150/kg); groundnut and soybean MSPs imply similar
or higher. Against that, FY26 CIF unit values were **₹98/kg (crude palm), ₹98/kg
(crude soy), ₹107/kg (crude sun)** — imported oil undercuts MSP-linked domestic oil by
30-40% even after the 16.5% effective duty. This is why:
- India imports ~57% of consumption (169.4 LMT, $19.5 bn in FY26 — the single biggest
  agri-import bill, larger than pulses at $3.6 bn);
- duty policy whipsaws: crude BCD raised to 20% (27.5% eff.) on 14-Sep-2024 to defend
  the soybean/groundnut harvest, then **cut to 10% (16.5% eff.) on 30-May-2025** to
  tame retail inflation ([USDA FAS GAIN](https://www.fas.usda.gov/data/india-india-cuts-import-tax-crude-edible-oils-opportunities-us-soybean-oil),
  [Business Standard](https://www.business-standard.com/markets/commodities/india-slashes-import-duty-on-crude-edible-oils-to-curb-rising-food-prices-125053001844_1.html));
- the crude-vs-refined duty gap (16.5% vs 35.75%) collapsed RBD palmolein imports from
  21.2 LMT (FY24) to 3.4 LMT (FY26) — a clean demonstration that tariff structure, not
  parity alone, decides the flow mix.
- An oilseed MSV would face the full 30-40% parity gap × whatever volume is
  guaranteed; without a much higher tariff wall it is an open-ended cheque.

## 4. What this means for MSV design

1. **A volume guarantee priced at/above MSP for a crop whose import parity is below MSP
   is fiscally endless unless paired with tariff policy.** FY26 numbers make it
   concrete: guaranteeing tur offtake at ₹8,000 while the world delivers at ₹5,659
   means the scheme absorbs ≈ ₹2,340/qtl × unlimited arrivals (traders can even flip
   imported stock into the guarantee unless provenance is policed). Closing the tur gap
   needs a ~40% duty; masur ~30%; the current 0-10% duties don't close it.
2. **The tariff wall must be dynamic.** The same crops were *above* MSP parity in FY25
   — a fixed high duty then would have added to consumer inflation for nothing. An MSV
   needs a variable-levy companion (CACP has recommended exactly this direction on
   pulses tariffs) that tracks the CIF-vs-MSP gap each season.
3. **For rice and wheat an MSV adds nothing**: open-ended FCI procurement already *is*
   a volume guarantee, and export policy (2022-24 bans/duties) shows the state will
   suppress export parity rather than let it lift domestic prices. Non-basmati's
   ≈-parity position means the guarantee price effectively sets the world's marginal
   rice price at India's scale (~40% of trade) — an MSV there is trade policy, not
   just farm policy.
4. **Where export parity is comfortably above MSP (basmati, sugar at ex-mill,
   maize-in-normal-years), an MSV would never trigger** — the design question is only
   about the pulse/oilseed deficit crops, which is exactly where the import-parity
   arithmetic is worst.

## 5. Source status & gaps (honest list)

- **APEDA AgriExchange** (agriexchange.apeda.gov.in): fully reachable; the legacy
  `.aspx` endpoints (indexp/exportstatement.aspx etc.) are **404 — site rebuilt as an
  MVC app**. Data pulled from its JSON POST APIs (documented in
  `data/build_trade_parity.py`). Quantity units differ per API (MT vs kg) — validated
  against known totals before use.
- **tradestat.commerce.gov.in**: old EIDB paths 404, but the new Laravel app works
  with per-request CSRF tokens; used for edible-oil HS lines. Its quantities are
  float32-rounded (e.g. 6,101,000,192 kg) — ±0.01% artifact.
- **Niryat (niryat.gov.in)** — geo-fenced, unreachable from this machine; and even
  when reachable it publishes VALUES only (USD, with district/country lenses), not
  quantities, so it cannot produce unit values for price parity — DGCI&S/tradestat/
  APEDA remain the qty+value sources.
- **Vintage flags**: FY2025-26 trade rows are full-year but *provisional* DGCI&S; MSPs
  are 2025-26; duty statuses as of Jul-2026 per the cited notifications
  ([duty-free tur/urad to Mar-2026](https://utkarsh.com/current-affairs/national/economy-update/government-extends-the-free-import-of-urad-till-31st-march-2026),
  [chana 10% from Apr-2025](https://www.deccanherald.com/amp/story/business%2Fgovernment-levies-10-import-duty-on-chickpea-from-april-1-3467048),
  [yellow-pea 30% from Nov-2025](https://markets.financialcontent.com/siliconinvestor/article/marketminute-2025-10-31-indias-yellow-pea-import-duty-shake-up-a-global-ripple-in-agricultural-markets)).
- **Gaps**: (i) refined soy/sun oil HS lines not pulled (small vs crude); (ii) pulses
  *export* basket not decomposed to HS level (mostly chana/kabuli — no single MSP
  comparator); (iii) millet MSP comparison uses jowar as proxy; (iv) moong imports
  negligible (75 t FY26) — row kept for completeness without INR value; (v) APEDA's
  "42Head" pulses row differs ~5% from the DGCI&S principal-commodity pulses row
  (basket definition) — principal-commodity used; (vi) sugar rows are fiscal-year
  while quotas run Oct-Sep seasons — timing noted, not adjusted; (vii) FY24/FY25 gaps
  measured against 2025-26 MSPs (older MSPs were 3-8% lower).
