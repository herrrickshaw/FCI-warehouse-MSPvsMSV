# Fertiliser Demand, New Fertiliser Schemes, and the Cost of Crop Production

*Collected 2026-07-23. Companion data: `data/fertiliser_demand.csv`, `data/cost_of_production.csv`.
All PIB citations verified against exact PRID URLs on www.pib.gov.in. LMT = lakh metric tonnes.*

This report adds the **input side** of the farm-economics ledger to the MSP-vs-MSV analysis:
what it costs to grow the grain the state later buys, and how the fertiliser subsidy — the
single largest input subsidy — feeds through CACP's cost formula into the MSP itself.

---

## 1. Fertiliser demand: level, mix, dependence, and scenarios

### 1.1 The demand picture (DBT PoS sales, all-India, LMT)

| Product | 2022-23 | 2023-24 | 2024-25 | 2025-26 (till 18.03.26) |
|---|---|---|---|---|
| Urea | 357.26 | 357.81 | 387.92 | 387.51 |
| DAP | 105.31 | 109.73 | 96.29 | 98.57 |
| MOP | 16.32 | 16.45 | 22.02 | 21.81 |
| NPKS complexes | 107.31 | 116.80 | 149.72 | 147.15 |
| **Total (these four)** | **586.20** | **600.79** | **655.95** | **655.04** |

Source: DoF Rajya Sabha reply, [PIB PRID 2244621](https://pib.gov.in/PressReleasePage.aspx?PRID=2244621) (24-Mar-2026).
Older benchmarks: urea sales 320.20 LMT (2018-19) and 336.97 LMT (2019-20)
([PRID 1640400](https://pib.gov.in/PressReleasePage.aspx?PRID=1640400)) — i.e. urea demand grew
~21% over six years (2018-19→2024-25), ~3.2%/yr. Total fertiliser requirement assessed for
2024-25 was 722.04 LMT against availability of 834.64 LMT
([PRID 2215303](https://pib.gov.in/PressReleasePage.aspx?PRID=2215303)).

Three structural shifts inside the mix (2022-23 → 2024-25):
- **NPKS complexes +39.5%** (107.31→149.72) — the big winner, partly displacing DAP;
- **DAP −8.6%** (105.31→96.29) — supply-shock rationing (China export curbs) plus deliberate
  policy steering toward complexes and SSP;
- **MOP +35%** off a tiny base (16.32→22.02) — recovering after the 2022 price spike collapsed use;
- **Urea +8.6%** — the subsidised workhorse keeps growing despite "balanced use" messaging.

### 1.2 Import dependence (verified against the task's priors)

| Product | Import share of consumption | Basis |
|---|---|---|
| Urea | ~15–25% and falling | Imports 98.28 LMT in 2020-21 ([PRID 1810907](https://pib.gov.in/PressReleasePage.aspx?PRID=1810907)) vs sales ~357 LMT ⇒ ~28% peak; domestic production 306.67 LMT vs sales 387.92 LMT in 2024-25 ⇒ implied gap ~21% (derived); 42.7 LMT already secured via global tenders for Kharif 2026 ([PRID 2287221](https://pib.gov.in/PressReleasePage.aspx?PRID=2287221)) |
| DAP | **~52%** | Imports 56.71/109.73 LMT (2023-24), 49.72/96.29 (2024-25) — both ≈52% ([PRID 2154208](https://pib.gov.in/PressReleasePage.aspx?PRID=2154208)). China's share collapsed from 22.28 LMT (2023-24) to 8.47 LMT (2024-25) ([PRID 2237491](https://pib.gov.in/PressReleasePage.aspx?PRID=2237491)) |
| MOP | **~100%** | No domestic potash mining; only partial substitute is PDM (potash from molasses), inducted under NBS since Rabi 2021 ([PRID 2239643](https://pib.gov.in/PressReleasePage.aspx?PRID=2239643)) |

The task's priors (urea ~20-25%, DAP ~55-60%, MOP 100%) are **broadly confirmed**, with DAP
now slightly lower (~52%) and urea trending below 20% as new plants ramp.

Cross-validation from local prior work: fertiliser imports (HS31) grew **+118.9% over 8 years
(11.8% CAGR)** — the fastest-growing high-value import chapter in India's basket (validated
against Commerce TIA Portal and PIB to within rounding, 2026-07-18; see
`~/india-trade-data-analysis/README.md`). That momentum is a *value* story (2022-23 price
shock stacked on volumes) — but it is exactly the exposure the domestic capacity build
(§2.4) is racing against. DPIIT IEM filings independently show fertiliser plant investment
intentions scaling up fastest among chapters — the supply-side response signal.

### 1.3 Subsidy outgo (₹ crore, DBT-released)

| FY | Outgo | Source |
|---|---|---|
| 2019-20 | 83,466.51 | [PRID 2040811](https://pib.gov.in/PressReleasePage.aspx?PRID=2040811) |
| 2020-21 | 1,31,229.50 | same |
| 2021-22 | 1,57,640.10 | same |
| **2022-23** | **2,54,798.88** | [PRID 2148437](https://pib.gov.in/PressReleasePage.aspx?PRID=2148437) |
| 2023-24 | 1,95,420.51 | same |
| 2024-25 | 1,77,129.50 | same |
| 2025-26 | allocation 2,01,961.50; actual 1,92,857.77 (as on 16.03.2026) | [PRID 2244395](https://pib.gov.in/PressReleasePage.aspx?PRID=2244395) |

**Correction to the task's prior**: the peak was NOT FY22 at ₹1.53 lakh cr — FY22 was
₹1.58 lakh cr, and the true peak was **FY23 (2022-23) at ₹2.55 lakh crore** (the
Russia-Ukraine price-shock year). FY23 split: indigenous urea 1,27,311 + imported urea
41,366 + imported P&K 36,033 + indigenous P&K 50,090. The FY26 corridor is ₹1.9–2.0 lakh cr.

**Derived intensity** (labelled, not official): FY25 urea subsidy (1,03,319.5 + 21,000 =
₹1,24,320 cr) over 387.92 LMT of urea sold ≈ **₹32,000/tonne ≈ ₹1,440 per 45-kg bag**,
against a statutorily-fixed farmgate MRP of roughly ₹242/bag — i.e. the exchequer pays
~85% of the delivered cost of urea. This is the ratio a subsidy-reform scenario has to move.

### 1.4 Demand scenarios to 2030 (constructed — no official DoF/NITI 2030 projection was found in PIB)

No official published 2030 demand scenario surfaced in the PIB corpus (2017–2026) or
accessible DoF material. The following are **simple constructed scenarios**, clearly labelled:

- **(a) Business-as-usual**: urea at its 2018-19→2024-25 trend (~3%/yr) reaches **~455–470 LMT
  by 2030-31**; total four-product demand ~750–780 LMT. Reconciling forces: import-dependency
  momentum (HS31 +11.8% CAGR in value) vs domestic capacity build — six NIP-2012 plants
  (+76.2 LMTPA) took capacity from 207.54 to 283.74 LMTPA reassessed
  ([PRID 2244621](https://pib.gov.in/PressReleasePage.aspx?PRID=2244621); the July-2026 releases
  quote 269.42 LMTPA installed for 2026-27 — both figures appear in official releases), with
  Talcher (12.7 LMTPA, coal-gasification) and Namrup/AVFCCL (12.7 LMTPA) still to come. If both
  commission by ~2029 and NUP-2015 output holds, **urea imports approach zero around 2030 under
  BAU demand** — which is precisely the government's stated aim under NIPU-2026.
- **(b) PM-PRANAM / natural-farming shift**: the only official quantum is that 14 states cut
  consumption **15.14 LMT in FY24 vs their 3-yr average** (~2.5% of national consumption)
  ([PRID 2116211](https://pib.gov.in/PressReleasePage.aspx?PRID=2116211)); NMNF covers 8.8 lakh ha
  / 18.19 lakh farmers as on 05.03.2026 ([PRID 2244625](https://pib.gov.in/PressReleasePage.aspx?PRID=2244625))
  — ~0.6% of net sown area. Scaling that trajectory generously (reduction doubling every 2-3 years)
  gives **urea flat-to-−5% by 2030 (~370–390 LMT)** — a bend, not a break.
- **(c) Nano-urea substitution at claimed rates**: IFFCO's claim is one 500-ml bottle replaces
  one 45-kg bag. Current nano-urea capacity is 27.22 crore bottles/yr — **≡ ~122 LMT of
  conventional urea per year if the claim held at full utilisation**. Actual cumulative sales are
  only 10.68 crore bottles since inception (≈48 LMT-equivalent over ~4 years)
  ([PRID 2149781](https://pib.gov.in/PressReleasePage.aspx?PRID=2149781)). **Independent evidence
  is negative**: Punjab Agricultural University's two-year trials (2020-21, 2021-22; Sikka & Kalia,
  published in *Plant and Soil*) found **wheat yield −21.6%, rice −13%**, and grain-protein
  declines when nano urea substituted for conventional N, concluding it "cannot be recommended
  on wheat and rice" without 5–7 years of further evaluation
  ([Down To Earth](https://www.downtoearth.org.in/agriculture/dip-in-yield-low-protein-content-pau-field-experiment-finds-several-problems-with-nano-urea-93668)).
  Government-side field trials (5,800+ ICAR-supervised nano DAP/urea trials across 15 agro-climatic
  zones) are reported in [PRID 2246007](https://pib.gov.in/PressReleasePage.aspx?PRID=2246007)
  without published yield-parity results. Treat scenario (c) as **capped well below nameplate**:
  realistic displacement by 2030 is single-digit LMT unless the yield question is resolved.

---

## 2. New fertiliser schemes (each verified with PRID + date)

### 2.1 PM-PRANAM (approved by CCEA 28-Jun-2023)
Incentivises states/UTs to cut chemical-fertiliser consumption (urea, DAP, NPK, MOP) versus
their previous 3-year average: the state receives a grant equal to **50% of the fertiliser
subsidy saved**. Split: 95% to the state (of which 65% for capex, preferably as contributions
to Centrally Sponsored Schemes, 30% untied/IEC), 5% retained for monitoring/IEC/research/awards.
Funded entirely from subsidy savings — no separate budget line. Verified outcomes: 14 states
reduced consumption by 15.14 LMT in FY2023-24 (Rajasthan achieved none)
([PRID 2116211](https://pib.gov.in/PressReleasePage.aspx?PRID=2116211), 28-Mar-2025;
mechanics: [PRID 2239623](https://pib.gov.in/PressReleasePage.aspx?PRID=2239623), 13-Mar-2026
(LS Starred Q *211); [PRID 2246007](https://pib.gov.in/PressReleasePage.aspx?PRID=2246007), 27-Mar-2026;
[PRID 2043546](https://pib.gov.in/PressReleasePage.aspx?PRID=2043546), 09-Aug-2024).
*Note the 65/30 vs 95/5 split is stated slightly differently across the two 2026 releases;
both agree on 50%-of-savings and 95% to the state.*

### 2.2 One Nation One Fertiliser / PMBJP ("Bharat" brand)
Launched by the PM on 17-Oct-2022 at PM Kisan Samman Sammelan
([PRID 1868463](https://pib.gov.in/PressReleasePage.aspx?PRID=1868463) /
[1868565](https://pib.gov.in/PressReleasePage.aspx?PRID=1868565)): all subsidised fertilisers
sold under the single brand "Bharat" (Bharat Urea/DAP/MOP/NPK) with the Pradhan Mantri
Bhartiya Jan Urvarak Pariyojana logo occupying two-thirds of the bag; the subsidy scheme was
renamed PMBJP. Aim: uniform branding to underline that the subsidy is the government's
([GKToday](https://www.gktoday.in/bharat-brand-one-nation-one-fertiliser/),
[Testbook summary](https://testbook.com/ias-preparation/one-nation-one-fertiliser-scheme)).
No separate budget; it is a branding overlay on the existing subsidy.

### 2.3 Nano urea and nano DAP rollout
- 7 nano-urea plants (27.22 cr bottles/yr) and 3 nano-DAP plants (7.64 cr bottles/yr) set up by
  fertiliser companies (not the government); cumulative sales 10.68 cr (urea) and 2.75 cr (DAP)
  bottles since inception; 3 more plants (17 cr bottles/yr) announced
  ([PRID 2149781](https://pib.gov.in/PressReleasePage.aspx?PRID=2149781), 29-Jul-2025).
- Nano DAP notified under the Fertilizer Control Order 1985 (IFFCO, Coromandel, Zuari permitted)
  on bio-efficacy and toxicology trials; ICAR notes a "possibility of saving of granular DAP"
  ([PRID 2042536](https://pib.gov.in/PressReleasePage.aspx?PRID=2042536), 06-Aug-2024).
- IFFCO nano DAP launched 26-Apr-2023 ([PRID 1919980](https://pib.gov.in/PressReleasePage.aspx?PRID=1919980));
  Kalol liquid plant inaugurated 24-Oct-2023 ([PRID 1970561](https://pib.gov.in/PressReleasePage.aspx?PRID=1970561)).
- Independent skepticism: see §1.4(c) — PAU trials found yield/protein declines.

### 2.4 Urea plant revivals and new capacity (status as verified)

| Plant | Status | PRID |
|---|---|---|
| Gorakhpur (HURL, 12.7 LMTPA) | Dedicated by PM 07-Dec-2021 | [1778867](https://pib.gov.in/PressReleasePage.aspx?PRID=1778867) |
| Barauni (HURL, 12.7) | Commenced production 19-Oct-2022 | [1869233](https://pib.gov.in/PressReleasePage.aspx?PRID=1869233) |
| Ramagundam (RFCL, 12.7) | Dedicated by PM 12-Nov-2022 | [1875464](https://pib.gov.in/PressReleasePage.aspx?PRID=1875464) |
| Sindri (HURL, 12.7) | Dedicated by PM 01-Mar-2024 | [2010566](https://pib.gov.in/PressReleasePage.aspx?PRID=2010566) |
| Talcher (TFL, 12.7, coal-gasification) | Exclusive subsidy policy approved 20-Apr-2021; still under implementation as of Jul-2026 | [1712855](https://pib.gov.in/PressReleasePage.aspx?PRID=1712855), [2287221](https://pib.gov.in/PressReleasePage.aspx?PRID=2287221) |
| Namrup/AVFCCL (12.7, brownfield, Assam) | Cabinet-approved; PM Bhoomi Poojan 21-Dec-2025 | [2207185](https://pib.gov.in/PressReleasePage.aspx?PRID=2207185), [2244621](https://pib.gov.in/PressReleasePage.aspx?PRID=2244621) |

Plus two private NIP-2012 units already running (Matix Panagarh, Chambal Gadepan-III).
Result: urea production 225 LMT (2014-15) → record 314.07 LMT (2023-24), 306.67 LMT (2024-25).

### 2.5 NBS rate revisions 2024–26 (seasonal Cabinet approvals)
- Kharif 2025: ₹37,216.15 cr ([PRID 2116179](https://pib.gov.in/PressReleasePage.aspx?PRID=2116179), 28-Mar-2025)
- Rabi 2025-26: ₹37,952.29 cr; per-kg rates N ₹43.02 / P ₹47.96 / K ₹2.38 / S ₹2.87;
  DAP NBS rate ₹29,805/MT ([PRID 2183292](https://pib.gov.in/PressReleasePage.aspx?PRID=2183292), 28-Oct-2025;
  rate table in explainer [PRID 2211384](https://pib.gov.in/PressReleasePage.aspx?PRID=2211384)).
  This is the "₹38,000-crore fertiliser subsidy" the Agriculture Minister publicly thanked the PM for
  ([PRID 2183468](https://pib.gov.in/PressReleasePage.aspx?PRID=2183468)).
- Kharif 2026: ₹41,533.81 cr, +₹4,317 cr over Kharif 2025 ([PRID 2250060](https://pib.gov.in/PressReleasePage.aspx?PRID=2250060), 08-Apr-2026).
- 28 P&K grades now under NBS (22 in 2021); SSP freight subsidy since Kharif 2022; PDM under NBS since Rabi 2021.

### 2.6 DAP special package (the "₹3,850 cr one-time" — verified, and it's a series)
- Jul-2024 Cabinet: one-time special package **₹3,500/MT** on PoS DAP sales beyond NBS,
  01.04.2024–31.12.2024, ~₹2,625 cr ([PRID 2079048](https://pib.gov.in/PressReleasePage.aspx?PRID=2079048)).
- 01-Jan-2025 Cabinet: **extension from 01.01.2025 "till further orders", up to ~₹3,850 cr**
  ([PRID 2089259](https://pib.gov.in/PressReleasePage.aspx?PRID=2089259)) — this is the figure the
  task asked to verify; it is an extension of the ₹3,500/MT package, not a new rate.
- The ₹3,500/MT "other costs" provision continues to be cited as live support for domestic DAP
  in Mar-2026 ([PRID 2237491](https://pib.gov.in/PressReleasePage.aspx?PRID=2237491)).

### 2.7 Genuinely NEW 2026 scheme: NIPU-2026
**National Investment Policy for Urea-2026 for Atmanirbhar Bharat**, Cabinet-approved
**15-Jul-2026** ([PRID 2284801](https://pib.gov.in/PressReleasePage.aspx?PRID=2284801)): successor
to NIP-2012 (which expired Oct-2019). Key design: separation of fixed and variable costs, RoE
band 12–16%, fixed-cost conversion to INR after four years to kill forex risk; claimed saving
>₹250 cr per plant vs NIP-2012 terms. Also new: Cabinet-approved brownfield ammonia-urea complex
at Namrup (AVFCCL) and a greenfield push signalled by 33 operational units at 269.42 LMTPA.
Related: green-urea roadmap exploration ([PRID 2278167](https://pib.gov.in/PressReleasePage.aspx?PRID=2278167), 26-Jun-2026).

---

## 3. Cost of crop production: A2+FL vs C2, and the 50% claim on both bases

CACP publishes three cost concepts: **A2** (paid-out costs), **A2+FL** (A2 + imputed family
labour) and **C2** (A2+FL + rental value of own land + interest on own fixed capital). Since
Budget 2018-19 the government fixes MSP at **≥1.5× the all-India weighted A2+FL** — every
kharif/rabi MSP release prints "Cost" = A2+FL and a "margin over cost" column. The Swaminathan
Commission recommendation, and the farmer-movement demand, is 1.5× **C2**.

### 3.1 The two margins, side by side (all-India, ₹/quintal)

**Paddy (Common)** — the tightest of all crops:

| KMS | A2+FL | C2 | MSP | Margin over A2+FL | Margin over C2 |
|---|---|---|---|---|---|
| 2022-23 | 1,360 | 1,805 | 2,040 | 50% | **13.0%** |
| 2023-24 | 1,455 | 1,911 | 2,183 | 50% | **14.2%** |
| 2024-25 | 1,533 | 2,008 | 2,300 | 50% | **14.5%** |
| 2025-26 | 1,579 | 2,090 | 2,369 | 50% | **13.3%** |
| 2026-27 | 1,627 | n/a | 2,441 | 50% | n/a |

**Wheat** — the widest:

| RMS | A2+FL | C2 | MSP | Margin over A2+FL | Margin over C2 |
|---|---|---|---|---|---|
| 2022-23 | 1,008 | n/c | 2,015 | 100% | n/c |
| 2023-24 | 1,065 | 1,575 | 2,125 | 100% | **34.9%** |
| 2024-25 | 1,128 | 1,652 | 2,275 | 102% | **37.7%** |
| 2025-26 | 1,182 | 1,720 | 2,425 | 105% | **41.0%** |
| 2026-27 | 1,239 | 1,804 | 2,585 | 109% | **43.3%** |

Sources: MSP/A2+FL from the CCEA MSP releases (PRIDs
[1832174](https://pib.gov.in/PressReleasePage.aspx?PRID=1832174),
[1930443](https://pib.gov.in/PressReleasePage.aspx?PRID=1930443),
[2026698](https://pib.gov.in/PressReleasePage.aspx?PRID=2026698),
[2131986](https://pib.gov.in/PressReleasePage.aspx?PRID=2131986),
[2260618](https://pib.gov.in/PressReleasePage.aspx?PRID=2260618),
[1753109](https://pib.gov.in/PressReleasePage.aspx?PRID=1753109),
[1868761](https://pib.gov.in/PressReleasePage.aspx?PRID=1868761),
[1968731](https://pib.gov.in/PressReleasePage.aspx?PRID=1968731),
[2065310](https://pib.gov.in/PressReleasePage.aspx?PRID=2065310),
[2173567](https://pib.gov.in/PressReleasePage.aspx?PRID=2173567)); C2 from CACP price-policy-report
projections as compiled by [farmingcosmos](https://www.farmingcosmos.com/msp-of-crops-in-2025-26-rabi-marketing-season-versus-previous-projected-cop/)
(tables reproduce CACP A2/A2+FL/C2) and, for KMS 2022-23 paddy,
[Foundation for Agrarian Studies](https://fas.org.in/kharif-msp-announcement-has-to-reconcile-with-rising-costs-across-india/).
PIB **never publishes C2** — that asymmetry is itself the controversy.

**Reading**: the "50% over cost" claim is true on A2+FL *by construction* (paddy is pinned at
exactly 50% every single year — the MSP is reverse-engineered from the formula). On C2, paddy
farmers get 13–14.5%, not 50%; C2+50% for paddy in KMS 2025-26 would have been ₹3,135/qtl vs the
announced ₹2,369. Wheat's C2 margin (35→43%, rising) is close to the Swaminathan benchmark —
wheat MSP politics is cheaper to satisfy than paddy's. Across the full CSV, kharif crops in
KMS 2024-25 ranged from 10.4% (sunflower seed) to 35.6% (bajra) over C2; rabi crops in RMS
2026-27 from 14.0% (safflower) to 43.3% (wheat). In no case did MSP reach C2+50%.

### 3.2 State-wise cost variation (paddy)
CACP's all-India cost is a weighted average across states with wildly different structures:
older CACP/DES data show paddy A2+FL of ~₹702/qtl in Punjab vs ~₹2,102/qtl in Maharashtra
([PRS blog](https://prsindia.org/theprsblog/explained-recent-changes-in-msps?page=2&per-page=1)),
and 2021-22 cost-of-cultivation estimates of ₹840.55/qtl (Punjab) vs ₹1,037/qtl (Bihar)
([extension journal](https://www.extensionjournal.com/uploads/archives/S-7-11-29-473.pdf)) —
Punjab's canal-plus-free-power, high-yield system produces a quintal of paddy ~20–60% cheaper
than eastern states. A single national MSP therefore over-rewards Punjab (which also has the
procurement machinery) and under-covers Bihar (which barely gets MSP at all — cf. the
mandi-vs-MSP gap in `data/mandi_vs_msp_20260723.csv`). CACP's kharif 2023-24 report itself
concedes that nine state governments' cost estimates exceed CACP projections (AP's was 29%
higher: ₹1,955 vs ₹1,520 for 2022-23, per FAS). Full CACP state tables were not directly
accessible (cacp.da.gov.in PDFs not fetched); flagged as a gap.

### 3.3 The input-output subsidy loop: fertiliser subsidy → A2 → MSP → food subsidy

The mechanics: fertiliser is a paid-out input inside A2. MSP = 1.5 × A2+FL. Procurement at MSP
plus NFSA issue at ₹0 is the food subsidy. So **the fertiliser subsidy and the food subsidy are
two ends of one corridor** (~₹1.9 lakh cr + ~₹2 lakh cr in FY26): compressing the first
inflates the cost base that the second must buy out.

Evidence that the subsidy is what keeps the loop dormant (local prior work,
`~/india-trade-data-analysis/data/fertiliser_fuel_price_transmission_2012_to_2026.json`,
WPI item-level series 2012–2026):
- **WPI Urea is up only +13.8% since April 2012** — over fourteen years — despite the
  2021-23 global price shock, because the subsidy absorbs the border price; DAP (thinner,
  less consistent support) is up +38.4%; diesel (unsubsidised) +79.0%.
- Correlation of YoY growth with WPI headline: diesel r=0.92 (mechanical pass-through);
  urea r=−0.42 (the subsidy *severs* the link — urea's domestic price moves on policy
  decisions, not markets).

**What a subsidy cut would do (illustrative, derived)**: FY25 urea support ≈ ₹32,000/tonne
(§1.3). Paddy uses roughly 1.5–2 bags of urea per quintal-of-output-equivalent at typical
doses; more robustly, fertiliser+manure is on the order of 10–15% of paddy A2. Halving the
urea subsidy would roughly double the farmgate urea price (₹242 → ~₹960/bag at full
pass-through of half the ₹1,440/bag support), lifting paddy A2+FL by several percentage
points; the 1.5× formula then multiplies that increase by 1.5 into the MSP, and procurement
(~600+ LMT rice+wheat) multiplies it into the food-subsidy bill. The corridor conserves —
it does not shrink — fiscal exposure; it only moves it between budget lines. This is why
PM-PRANAM tries to shrink *volumes* (and shares the savings 50:50 with states) rather than
touch *rates*: rates feed straight back into MSP through CACP's own arithmetic.

### 3.4 MSV tie-in: input subsidies as the fourth leg of the price ladder

The main report's ladder is: mandi price → MSP → MSV (economic cost to FCI). This section adds
the rung *below* the mandi price: the **subsidised input floor**. The state pays ~85% of the
delivered cost of urea so that A2 stays low, so that MSP-at-1.5×A2+FL stays politically
presentable, so that the economic cost (MSV) of the grain FCI carries stays ~40% above MSP
rather than higher. Every rupee of fertiliser subsidy withdrawn reappears — multiplied through
the 1.5× formula and the procurement volume — in the MSP and then in FCI's economic cost.
Conversely, the input subsidy is also why the "50% over cost" headline is cheap to honour on
A2+FL: the state has already paid down the cost base it measures the margin against. On the
full-cost C2 basis — the one that includes the farmer's own land and capital — paddy's margin
has been stuck at 13–14.5% for five seasons, and that gap, not the headline, is what the
Swaminathan/C2+50% agitation is about.

---

## Gaps and caveats
- **Product-wise consumption before 2018-19** not collected from official sources (DoF annual
  report PDFs and FAI stats inaccessible from this machine; fert.nic.in dead per earlier
  sessions). Series starts 2016-17 for imports, 2018-19 (urea) / 2022-23 (all products) for sales.
- **C2** unavailable for KMS 2026-27 and RMS 2022-23 (CACP report PDFs not directly fetched);
  C2 values used are CACP projections as republished by farmingcosmos/FAS, not read from the
  CACP PDFs themselves.
- **State-wise CACP cost tables** (Punjab vs Bihar per-quintal, current seasons) not directly
  accessed; secondary citations only.
- Urea capacity is quoted as 283.74 LMTPA (Mar-2026 release, "2023-24") and 269.42 LMTPA
  (Jul-2026 releases, "reassessed/installed 2026-27") — both official; the discrepancy is
  reproduced as-is.
- 2025-26 sales are till 18.03.2026 (near-complete but not final).
- No official 2030 demand scenario exists in the sources searched; §1.4 scenarios are
  constructed and labelled as such.
