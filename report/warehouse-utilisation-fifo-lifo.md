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
regime (last-in-first-out — what would happen if fresh grain were stacked on top and issued first, or if
depots shipped the most accessible lots), that **~298 LMT base layer would never be touched and would age
2–3+ crop years** — the old-stock deterioration risk that a LIFO discipline creates. **FCI avoids this by
following FIFO** (§ reality check below), so in practice only the **~244 LMT "working layer"** (average minus
trough) needs to churn — but the ~298 LMT base still *sits*, cycling slowly, carrying cost the whole time.

| Layer | LMT | Behaviour |
|---|---:|---|
| Working layer (cycles) | ~244 | issued within months; healthy turnover |
| **Static base (LIFO-trapped)** | **~298** | *would* age/deteriorate under LIFO — the risk FCI's FIFO avoids (see reality check below) |
| Peak-season surplus (above norm ~411) | variable | slow-moving; the disposal (OMSS) problem |

## Reality check — FCI *does* follow FIFO, and spoilage is negligible

An important correction from the primary source ([Rajya Sabha UQ-2435, 17-Dec-2024, "Protection of Food
Grains"](https://sansad.in)): **FCI officially follows FIFO** — the answer states *"The principle of
'First in First Out' (FIFO) is followed so as to avoid longer storage of foodgrains in godowns,"* backed by
scientific storage, fumigation, and Damage Monitoring Cells at District/Regional/Zonal levels. And the
result shows it works — **damaged/non-issuable grain is a rounding error:**

| Year | Non-issuable accrued (LMT) | Off-take (LMT) | Non-issuable % of off-take |
|---|---:|---:|---:|
| 2019-20 | 0.019 | 455.1 | 0.004% |
| 2020-21 | 0.018 | 688.6 | 0.003% |
| 2021-22 | 0.017 | 766.1 | 0.002% |
| 2022-23 | 0.016 | 675.8 | 0.002% |
| 2023-24 | 0.103 | 470.7 | 0.022% |

So the LIFO "dead-layer rots" scenario is the **counterfactual FIFO avoids, not current reality** — actual
spoilage is **0.002–0.022% of off-take.** (The off-take series also confirms the model: 455–766 LMT/yr,
averaging ~611 LMT — the ~610 LMT assumption above is spot-on; the 766 LMT peak is the PMGKAY surge.)

**What "non-issuable" means** is fixed by the DFPD *Uniform Specifications* for procurement and issue
(No. 8-2/2019-S&I, KMS 2019-20): paddy moisture ≤17%, damaged/sprouted/weevilled ≤4%; rice damaged ≤3–4%,
foreign matter ≤0.5%, **brokens up to 25% (raw) / 16% (parboiled)**; issue-stocks are "ready" if refractions
run up to **20% in excess** of the uniform spec (A/B/C categorisation). Two things follow: (a) the tight
damage bands + the 20%-excess issue tolerance are *why* so little is written off; (b) the **25% broken-rice
allowance is itself a byproduct hook** — broken rice is a legitimate feedstock for ethanol, starch and rice
flour, another value stream inside the procured grain, alongside the bran→RBO route.

## The corrected implication for the biorefinery thesis

This sharpens — not weakens — the case, by moving it off the wrong argument:

- **Not "the grain is rotting"** — it isn't; FCI's FIFO + damage control keeps loss negligible.
- **It's "the static ~298 LMT base bleeds carrying cost while not being consumed"** — held at ~₹5.6/kg/yr
  ([holding-economics](holding-economics.md)), a ~298 LMT base is **~₹16,700 cr/yr of carry** on grain that
  the off-take cycle never draws down. The problem is **opportunity cost, not deterioration.**

So the ~298 LMT static base and the above-norm surplus are the grain to divert to **processing** — RBO from
milled paddy, fortification, OMSS feedstock — **not because it would otherwise spoil, but because processing
converts a carry-bleeding idle base into value.** The dead layer is not a storage or spoilage problem; it is
**a feedstock waiting for a processing offtake, and a carrying-cost line waiting to be retired.**

## Recommendations

1. **Publish depot-level stock ageing** (FIFO is followed and the IISFM/DOS plumbing exists;
   [publication doesn't](iisfm-depot-coverage.md)) — transparency on the age profile would confirm the
   static base and target it for diversion.
2. **Route the ~298 LMT static base + above-norm surplus to processing** — not to retire a spoilage risk
   (negligible) but to **stop the ~₹16,700 cr/yr of carrying cost** on an idle base and convert it to value
   via the [World's Largest Grain Storage Plan](national-fci-fpo-food-processing-psu.md)'s PACS processing units.
3. **Size owned/cooperative capacity to the average (~542 LMT), hire for the peak (~910)** — stop paying to
   own capacity for a 101% event that lasts weeks. *(The [CAG (Report 20 of 2023)](cag-audit-fci-findings.md)
   audited exactly this waste: ₹62.76 cr of avoidable hiring in Punjab/Haryana **despite own vacant CAP**, plus
   ₹170.26 cr in avoidable carry-over charges.)*

## Caveats

Stock series is DFPD Foodgrain Bulletin (rice+wheat+coarse "total", 48 monthly obs 2021-2024); capacity ~900
LMT is a mid-period covered+CAP approximation (851→918 LMT over the window — see
[storage-scenario](../dashboard/storage-scenario.html)). Offtake ~610 LMT is the 2024-25 *allocation*
(actual lifting runs slightly lower). FIFO residence and LIFO dead-layer are **inventory-accounting models
applied to aggregate stock**, not lot-level depot data (which is login-gated in IISFM/DOS) — they bound the
behaviour, they don't track individual lots. "LIFO" here is the counterfactual worst case (oldest grain stranded); FCI officially follows FIFO
(RS UQ-2435) and actual spoilage is 0.002-0.022% of off-take, so the dead-layer argument is about
carrying cost, not deterioration. Turnover/residence are all-India aggregates; individual depots vary widely.
Research synthesis, not an operational audit.
