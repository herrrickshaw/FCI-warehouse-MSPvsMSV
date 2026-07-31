# The national build-out: FCI locations × FPOs per state, and the food-processing PSU to run it

*Scaling the [Tamil Nadu partner screen](fpo-processing-partners-tamilnadu.md) to all-India: where
FCI's storage network sits, where the farmer-aggregation (FPOs) sits, and the government vehicle that
could run a processing layer across both — including an existing, dormant DFPD PSU purpose-built for
it. Grounded in the DFPD Foodgrain Bulletin (storage), the SFAC 10,000-FPO registry, and igod.gov.in's
DFPD org list. July 2026. National companion to
[fiscal-rationalisation-procurement-vs-processing.md](fiscal-rationalisation-procurement-vs-processing.md),
[psu-agri-ventures-history.md](psu-agri-ventures-history.md) and [ppp-rice-mills.md](ppp-rice-mills.md).
Data: [`data/national_fci_fpo_by_state.csv`](../data/national_fci_fpo_by_state.csv).*

## The two networks, mapped per state

The processing model needs two things in the same place: **grain (FCI storage / procurement)** and
**farmers organised to supply feedstock (FPOs)**. Mapping both per state
([storage_capacity.csv](../data/storage_capacity.csv), Nov-2024 Foodgrain Bulletin; SFAC 10,000-FPO
registry, 24-02-2025):

| State | FCI+hired storage (LMT) | SFAC FPOs | Lead feedstock |
|---|---:|---:|---|
| **Madhya Pradesh** | **200.4** | 348 | wheat, soybean, pulses, mustard |
| **Punjab** | **174.5** | 78 | wheat, paddy (surplus) |
| **Haryana** | 100.2 | 119 | wheat, paddy, mustard |
| **Uttar Pradesh** | 47.2 | **758** | wheat, paddy, sugarcane |
| Chhattisgarh | 35.5 | 68 | paddy |
| Andhra Pradesh | 24.6 | 247 | paddy, groundnut |
| Telangana | 24.4 | 116 | paddy, groundnut |
| Maharashtra | 24.3 | 213 | soybean, tur, cotton, oilseeds |
| Bihar | 20.9 | 312 | paddy, wheat, pulses |
| Tamil Nadu | 20.9 | 90 | paddy, groundnut, pulses |
| West Bengal | 20.0 | 156 | paddy, oilseeds |
| Rajasthan | 16.4 | 225 | mustard, pulses, bajra |
| Odisha | 12.6 | 164 | paddy |
| Gujarat | 9.8 | 141 | groundnut, cotton, oilseeds |
| Karnataka | 9.7 | 52 | pulses, oilseeds, millets |

*(FCI figure is total covered storage — FCI-owned + hired CWC/SWC/PEG/private, Nov-2024; ~841 LMT
all-India. SFAC FPOs are the SFAC channel of the 10,000-FPO scheme only — 3,649 nationally; NABARD/
NCDC/other CBBOs register more, and India has ~45,000 FPOs in total.)*

## The finding: storage and farmer-aggregation are in *different* states

The map exposes a structural mismatch the national plan must design around:

- **The storage/surplus belt** — Punjab (175 LMT), MP (200), Haryana (100), Chhattisgarh (36) — is
  where FCI *holds* grain, but (except MP) is **thin on FPOs** (Punjab just 78).
- **The FPO-dense belt** — UP (758), Bihar (312), AP (247), Rajasthan (225), Maharashtra (213),
  Assam (176), Odisha (164) — is where farmers are *organised*, but (except UP) holds **far less FCI
  storage.**
- **Madhya Pradesh is the one state with both** — 200 LMT of storage *and* 348 FPOs *and* the
  soybean/pulses/mustard feedstock the deficit-crop thesis targets. **MP is the natural first hub.**

So the siting logic is not "put a plant where the grain is." It is: **oilseed/pulse processing goes to
the FPO-dense deficit-crop states (MP, Maharashtra, Rajasthan, AP), and rice-bran/surplus processing
goes to the storage belt (Punjab, Haryana, MP, Chhattisgarh) where the paddy is milled** — matching
each biorefinery stream to the state that has its feedstock *and* the aggregation to supply it.

## Suggested first hubs by stream

| Stream | Priority states (feedstock + FPOs + storage) |
|---|---|
| **Rice bran oil** | Punjab, Haryana, Chhattisgarh, UP, WB, Odisha (paddy belt + FCI milling) |
| **Soybean / oilseed crush** | **Madhya Pradesh**, Maharashtra, Rajasthan (soy/mustard + FPOs) |
| **Groundnut oil** | Gujarat, Andhra Pradesh, Tamil Nadu |
| **Dal milling (pulses)** | Madhya Pradesh, Maharashtra, Rajasthan, UP, Karnataka |
| **Maize wet-milling** | Bihar, Karnataka, Telangana, Andhra Pradesh |

## The vehicle: don't create a new PSU — revive the one DFPD already owns

The natural next question — "who runs this?" — has a surprising answer hiding in DFPD's own org chart.
Per [igod.gov.in](https://igod.gov.in)'s DFPD listing, the department already owns **three** delivery
bodies:

1. **Food Corporation of India (FCI)** — procurement, storage, the grain and the depots.
2. **Central Warehousing Corporation (CWC)** — the warehousing network.
3. **Hindustan Vegetable Oils Corporation Ltd (HVOC)** — a **CPSE built for vegetable-oil / vanaspati
   processing**, now largely dormant.

**India does not need to *create* a food-processing PSU — it needs to *revive* HVOC**, a vegetable-oils
processing corporation that already sits under the same department as the grain and the storage. That is
a materially stronger proposition than a green-field entity: the corporate shell, the DFPD mandate, and
the edible-oil remit already exist.

### Why revival beats creation — the project's own PSU-history lesson

This is exactly where [psu-agri-ventures-history.md](psu-agri-ventures-history.md) earns its keep. The
record is unambiguous:

- **The trading PSUs failed** — STC → PEC → NCEL serially collapsed because they **traded naked**, with
  no infrastructure moat, taking price risk on commodities.
- **The infrastructure PSUs survived** — CWC, NAFED, AMUL, Kendriya Bhandar endured because they owned
  **infrastructure, farmer-ownership or ring-fenced offtake**, not a trading book.

So a revived HVOC must be built as the **survivors** were, not the failures:

| Design rule | Why (from the PSU record) |
|---|---|
| **Infrastructure + processing, not trading** | STC/PEC/NCEL died trading naked; own plants and offtake instead |
| **FPO-fed, farmer-linked supply** | the AMUL/NAFED survival trait — feedstock from organised producers, not spot markets |
| **Ring-fenced, contracted offtake** | PDS edible-oil ([ONORC national offtake](msp-crops-refined-oil-source.md)), fortification mandates, food-processor contracts — the revenue backbone, not the open market |
| **JV/PPP for capital & know-how** | HVOC provides mandate + sites; a private/JV partner brings the crush/refining capital (the [PPP model](ppp-rice-mills.md)) |
| **Sit on the FCI/CWC network** | co-locate with the storage and the byproduct (bran) the sister PSUs already control |

### What a revived HVOC would actually do

- **Anchor the domestic edible-oil substitution** — the ₹1.68 lakh-cr import target: rice-bran oil from
  FCI-milled paddy bran, cottonseed, and oilseed crush from FPO-supplied seed
  ([msp-crops-refined-oil-source.md](msp-crops-refined-oil-source.md)).
- **Supply the PDS oil ration domestically** — replacing the imported palmolein states buy today
  ([the ₹3,800 cr Tamil Nadu bill and its analogues](msp-crops-refined-oil-source.md)) with domestic
  RBO, redirecting the subsidy to domestic jobs.
- **Bank the byproducts FCI gives away** — the ₹7,650 cr of free bran becomes HVOC's feedstock.
- **Run as the state's edible-oil arm** — the import-side counterpart to FCI's grain role: FCI holds
  the grain, HVOC processes the oil, CWC stores, FPOs supply, ONORC distributes.

## The cooperative layer — the AMUL-model network already being built

The PSU (HVOC) is the national *processing corporation*; the [PSU record](psu-agri-ventures-history.md)
says the *durable* form is farmer-owned cooperative infrastructure (AMUL, NAFED). India is building
exactly that right now, and the [National Cooperative Database](https://cooperatives.gov.in) quantifies it:

- **857,854 cooperatives** across 30 sectors (663,275 functional), incl. dedicated **Agro-Processing /
  Industrial**, **Marketing**, **Oilseeds** and **Sugar-Mill** cooperative sectors.
- **PACS cover ~83% of India's gram panchayats** (225,123 of 271,109 GPs) — a village-level aggregation
  grid far denser than any FPO or FCI network, now being made *multipurpose* (procurement centres,
  godowns, processing units).
- The **World's Largest Grain Storage Plan** is adding godowns/processing at PACS level — putting
  storage *and* value-addition at the village, complementing FCI's national depots.
- The Ministry of Cooperation's new national cooperatives are the marketing/processing arms:
  **NCOL** (organics), **NCEL** (exports), **BBSSL** (seeds), alongside **NAFED**, **NCCF**, **NCDFI**,
  **IFFCO/KRIBHCO** — 1,845 multi-state cooperative societies in all.

**So the vehicle is two-layered:** a revived **HVOC** as the national edible-oil processing CPSE, riding
the **PACS/cooperative grid** (village aggregation + new godowns) and the national cooperatives
(NCOL/NCEL/NAFED for organics, exports, procurement) as the farmer-owned supply-and-marketing network —
the AMUL model the PSU record says actually survives, at national scale. HVOC brings the processing
mandate; the cooperatives bring the farmer ownership and the last-mile aggregation.

## Recommendations

1. **Make MP the pilot hub** — the one state with storage + FPOs + oilseed feedstock; site a revived-HVOC
   soybean/mustard crush + a bran-oil unit there first.
2. **Revive HVOC as an infrastructure+processing CPSE, JV-capitalised** — explicitly *not* a trading arm;
   ring-fence it from price-taking per the STC/PEC/NCEL lesson.
3. **Wire it to the three sister bodies** — FCI (bran/feedstock + depots), CWC (storage), and the FPO
   network (supply); contract the offtake via PDS/ONORC and fortification mandates.
4. **Sequence by the map** — oilseed/pulse processing to the FPO-dense deficit states, rice-bran to the
   milling/storage belt; don't force one template on every state.

## Caveats

FCI storage is total covered capacity (owned + hired CWC/SWC/PEG/private), Nov-2024 Foodgrain Bulletin —
a capacity figure, not a depot count; FCI's ~2,000 depots are majority-hired, so "FCI locations" is really
FCI + agency storage ([iisfm-depot-coverage.md](iisfm-depot-coverage.md)). SFAC FPO counts are the SFAC
channel of the 10,000-FPO scheme only (3,649 as on 24-02-2025, machine-counted from the SFAC state-wise
PDF — treat ±small as parsing noise); NABARD/NCDC/other CBBOs add several thousand more, and total Indian
FPOs are ~45,000 (2024) — so per-state *SFAC* counts understate true FPO density and are a *relative*
indicator, not an absolute. Lead-feedstock tags are indicative from state cropping patterns. HVOC's
current operational status (assets, liabilities, revival feasibility) is **not** assessed here — the claim
is that a dormant edible-oils CPSE *exists* under DFPD (per igod.gov.in) and is the logical shell to
revive, not that revival is costless; a real proposal needs HVOC's balance sheet and a Cabinet/DIPAM view.
This is research synthesis and policy arithmetic, **not** investment, disinvestment, or fiscal advice.
