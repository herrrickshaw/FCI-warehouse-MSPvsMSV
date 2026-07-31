# Warehouse utilisation, FIFO vs LIFO — how long grain actually sits, and the dead layer

*Quantifying FCI warehouse utilisation from the DFPD Foodgrain Bulletin's stock and scheme-dispersal
data, using FIFO vs LIFO inventory logic to expose the slow-moving base. July 2026. Data:
[`data/warehouse_utilisation_fifo_lifo.csv`](../data/warehouse_utilisation_fifo_lifo.csv),
[`data/stocks_vs_norms.csv`](../data/stocks_vs_norms.csv). Source series:
[DFPD Foodgrain Bulletin Archive](https://dfpd.gov.in/home/FoodGrainArchive?language=1).*

## The flow: ~610 LMT in, ~610 LMT out, ~542 LMT sitting

The central pool is a tank: **procurement ~820 LMT/yr flows in** (rice ~520 + wheat ~300), **~610 LMT/yr
flows out** through the schemes, and **~542 LMT sits in storage on average** (48 monthly observations,
2021-2024). Scheme-wise, the outflow is overwhelmingly the ration system:

| Scheme (2024-25 allocation) | LMT | Share |
|---|---:|---:|
| **TPDS / NFSA** (AAY + PHH + Tide-Over) | 553.1 | **90.9%** |
| WBNP / ICDS | 25.8 | 4.2% |
| PM-POSHAN (mid-day meal) | 23.0 | 3.8% |
| Other Welfare (hostels, SAG) | 4.8 | 0.8% |
| Additional (festival/calamity) | 1.7 | 0.3% |
| **Total** | **608.3** | 100% |

## Utilisation — 60% average, but 101% at the peak

Against ~900 LMT of covered+CAP capacity:

| | Stock (LMT) | Utilisation |
|---|---:|---:|
| **Peak** (Jun-2021) | 910 | **101%** — overflow into open CAP / extra hired space |
| **Average** | 542 | **60%** |
| **Trough** (Jan-2023) | 298 | **33%** |

The system runs at a **comfortable 60% on average but periodically breaches 100%** — the mid-2021 record
brushed the covered-godown ceiling and forced grain onto open Cover-and-Plinth plinths and emergency hired
space. That volatility (33%→101% within 18 months) is *why* FCI keeps 70% of its network on hire rather
than building owned capacity for a peak it only hits occasionally.

## FIFO — grain sits ~11 months on average

Turnover = annual offtake ÷ average stock = **610 / 542 = 1.13× per year.** Under **FIFO** (first-in,
first-out — the correct, spoilage-minimising discipline), average residence time = 12 / 1.13 =
**~10.7 months.** So even run perfectly, a typical grain lot sits **close to a year** before it is issued —
consistent with a buffer held ~2× above norm. That is the carrying cost the
[holding-economics](holding-economics.md) and [fiscal-rationalisation](fiscal-rationalisation-procurement-vs-processing.md)
reports price at ~₹5.6/kg/yr.

## LIFO — the ~298 LMT dead layer that never moves

The revealing number is the **trough: the pool never fell below ~298 LMT** in four years. Under a **LIFO**
regime (last-in-first-out — what happens physically when fresh grain is stacked on top and issued first,
or when depots ship the most accessible lots), that **~298 LMT base layer is never touched — it ages 2–3+
crop years, the classic FCI old-stock deterioration problem.** Only the **~244 LMT "working layer"** (average
minus trough) actually churns.

| Layer | LMT | Behaviour |
|---|---:|---|
| Working layer (cycles) | ~244 | issued within months; healthy turnover |
| **Static base (LIFO-trapped)** | **~298** | never cycles; ages, deteriorates, becomes feed/ethanol/write-off |
| Peak-season surplus (above norm ~411) | variable | slow-moving; the disposal (OMSS) problem |

**The implication for the biorefinery thesis:** the ~298 LMT static base and the above-norm surplus are
*exactly* the grain that should be diverted to **processing** rather than left to age. FIFO discipline (issue
oldest first) plus routing the static base into value-addition — RBO from milled paddy, fortification, OMSS
feedstock — converts a deteriorating, carry-bleeding dead layer into a value stream. **The dead layer is not
a storage problem to solve with more godowns; it is a feedstock waiting for a processing offtake.**

## Recommendations

1. **Enforce FIFO issue discipline + depot-level stock ageing transparency** (the IISFM/DOS plumbing exists;
   [publication doesn't](iisfm-depot-coverage.md)) — surface the LIFO-trapped lots.
2. **Route the ~298 LMT static base + above-norm surplus to processing**, not indefinite storage — the
   clearest use of the [World's Largest Grain Storage Plan](national-fci-fpo-food-processing-psu.md)'s
   PACS processing units.
3. **Size owned/cooperative capacity to the average (~542 LMT), hire for the peak (~910)** — stop paying to
   own capacity for a 101% event that lasts weeks.

## Caveats

Stock series is DFPD Foodgrain Bulletin (rice+wheat+coarse "total", 48 monthly obs 2021-2024); capacity ~900
LMT is a mid-period covered+CAP approximation (851→918 LMT over the window — see
[storage-scenario](../dashboard/storage-scenario.html)). Offtake ~610 LMT is the 2024-25 *allocation*
(actual lifting runs slightly lower). FIFO residence and LIFO dead-layer are **inventory-accounting models
applied to aggregate stock**, not lot-level depot data (which is login-gated in IISFM/DOS) — they bound the
behaviour, they don't track individual lots. "LIFO" here is the physical worst case (oldest grain stranded),
not an accounting election. Turnover/residence are all-India aggregates; individual depots vary widely.
Research synthesis, not an operational audit.
