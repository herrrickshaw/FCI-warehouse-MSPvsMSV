# Farmer income: current estimate, the doubling goal, and progress

*Estimate from official surveys (NSSO SAS, NABARD NAFIS) and the Dalwai Committee target,
per PIB. Data: [`data/farmer_income_dfi.csv`](../data/farmer_income_dfi.csv). July 2026.
Ties the project's mill + CBG-loop thesis to the Doubling Farmers' Income (DFI) goal.*

## 1. Current farmer income — the estimate

Two official surveys, converging:

| Source | Year | Monthly income (agri household) | Change |
|---|---|---|---|
| NSSO SAS (70th round) | 2012-13 | **₹6,426** | baseline |
| NSO SAS (77th round) | 2018-19 | **₹10,218** | +59% (nominal) |
| NABARD NAFIS-1 | 2016-17 | ₹8,059 (all rural) | — |
| NABARD NAFIS-2 | 2021-22 | **₹13,661** (agri household) | +57.6% in 5 yrs, 9.5% nominal CAGR |

So the current estimate is **~₹13,661/month per agricultural household (NAFIS 2021-22)** — about
₹1.64 lakh/year. TN sits above the national average (SAS 2018-19 ~₹11,900/month).

**The composition matters more than the level** (SAS 2018-19):

| Income source | Share |
|---|---|
| Wages (farm + non-farm labour) | **40%** |
| Crop cultivation | **37%** |
| Animal husbandry | 15% |
| Non-farm business | 6% |
| Land leasing | 1% |

Crop income is only ~37% of the total. **The farmer is already a diversified earner** — which
is exactly why the DFI strategy, and this project's mill+CBG thesis, target *value-addition,
cost-reduction, byproduct income, and non-farm earnings* rather than crop price alone.

## 2. The goal — Doubling Farmers' Income (DFI), per PIB

- **Inter-Ministerial (Dalwai) Committee**, constituted April 2016; final 14-volume report
  Sept 2018 ([PIB brief](https://www.pib.gov.in/PressNoteDetails.aspx?NoteId=150574&ModuleId=3)).
- **Target: double farmers' *real* income from the 2015-16 base by 2022-23** — aggregate
  ₹8.5 lakh crore → ₹18.5 lakh crore.
- **Critical framing**: the government clarified the target is at *constant prices* (real,
  inflation-adjusted), not nominal — a much harder bar.
- **Required real CAGR: 10.4%/yr** (2015-16→2022-23). For context, it took **22 years** to
  double at the historical 3.31% real CAGR (1993-94→2015-16) — so the target asked for a
  3× acceleration ([NITI Aayog via PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2114892)).

## 3. Progress — the honest verdict

**Nominal income rose ~57–70%; *real* doubling was not achieved by 2022-23, and the target
has effectively lapsed into an ongoing income-enhancement framing.**

- Nominal: SAS +59% (2012-13→2018-19); NAFIS +57.6% (2016-17→2021-22). Even *nominally*,
  income is ~1.6–1.7× the base — not a clean 2×.
- Real: the 10.4% real CAGR needed was never sustained. NITI Aayog itself noted **real farm
  income *declined* between 2011-12 and 2015-16** — the run-up went the wrong way.
- The 2022 deadline passed without an official "achieved" declaration; the government reframed
  toward continuous income support (PM-KISAN, MSP, PM-AASHA) rather than the doubling headline.
- Farm household *debt* also rose over the period, so net-worth gains lag income gains.

**Fair summary:** meaningful nominal gains (~9.5% CAGR, beating nominal GDP), real gains
modest and short of doubling, target quietly reframed. Not a failure of direction — a failure
of the (very ambitious) timeline.

### The exact real number — deflated by CPI-AL (MoSPI)

The right deflator for farm households is **CPI-AL (Consumer Price Index for Agricultural
Labourers)** — their own consumption basket, not general CPI. Pulling it from MoSPI's CPIALRL
series (base 1986-87, All-India, June):

| | 2016-17 | 2021-22 | Change |
|---|---|---|---|
| CPI-AL index | 877 | 1,125 | **+28.3%** inflation |
| Nominal income (agri household) | ₹8,059 | ₹13,661 | +69.5% |
| **Real income (deflated)** | | | **+32.1%** |
| Real CAGR | | | **~5.7%/yr** |

So over the five-year NAFIS window, **real farm income grew ~32% (agri household) — a real
CAGR of ~5.7%/yr against the 10.4%/yr the doubling target required.** On the all-rural series
it is even lower (+22.8% real, 4.2%/yr). The SAS window (2012-13→2018-19) gives a similar
~32% real gain.

**The precise verdict: real farm income grew about a quarter to a third — not doubled. The
achieved real pace (~4–6%/yr) was roughly half the 10.4%/yr the target demanded.** That is the
exact, MoSPI-deflated version of "real doubling missed," and it is a *better* number than the
nominal headlines because CPI-AL is the farmer's actual cost-of-living index.

## 3b. The metric to monitor — Real Farm Income Index (RFII)

Turn the verdict into a **trackable, inflation-adjusted metric**. Define:

> **RFII = (nominal agri-household income ÷ base income) ÷ (CPI-AL ÷ base CPI-AL) × 100**
> Base 2016-17 = 100. **Doubling target = 200 (real).** Deflator = CPI-AL (the farm
> household's own cost-of-living basket).

Reproducible tracker: [`data/rfii_monitor.py`](../data/rfii_monitor.py) →
[`data/real_farm_income_index.csv`](../data/real_farm_income_index.csv).

| Year | Nominal ₹/mo | CPI-AL (1986-87) | **RFII** | Gap to 200 |
|---|---|---|---|---|
| 2016-17 | 8,059 | 877 | 99.1 | 100.9 |
| 2018-19 | 10,218 | 950 | 116.0 | 84.0 |
| **2021-22 (last measured)** | 13,661 | 1,125 | **130.9** | **69.1** |
| 2024-25 (projected*) | ~19,640 | 1,320 | ~160 | ~40 |

*Projection assumes nominal income continued at the 9.5% CAGR — **unconfirmed until the next
SAS/NAFIS survey.** The latest MoSPI CPI-AL print is 1,320 (cumulative **+52% inflation since
2015-16** — that is the deflator eating the nominal gains).

**Reading the monitor:** the last *measured* real index is **130.9** — about a third of the way
from 100 to the 200 doubling line. At the achieved ~5.7%/yr real pace, RFII reaches 200 around
**2030** — roughly 8 years past the 2022-23 DFI deadline.

**Refresh cadence:** the CPI-AL deflator updates **monthly** (MoSPI `CPIALRL`, base 1986-87,
All-India, General Index) — so the *real* value of the last measured income can be re-marked
every month; the nominal income point refreshes only on a new **SAS/NAFIS** survey (~5-yearly).
Edit the two dicts in `rfii_monitor.py` when either lands and re-run. This is the single
number that tells you, in the farmer's own price terms, how far the doubling actually got.

## 4. Where this project fits the DFI goal

The Dalwai Committee named **seven income sources**: crop productivity, livestock, resource-use
efficiency (cost saving), cropping intensity, diversification to high-value crops, real prices,
and the shift from farm to non-farm. The mill + CBG loop modelled in this project hits **four of
the seven at once** — and precisely the ones that move the 63% of income that *isn't* crop
cultivation:

1. **Real prices** — an integrated mill's assured local offtake lifts farmgate oilseed/copra/
   paddy prices (~5–8%).
2. **Cost reduction** — the CBG loop cuts cost of production ~8% (CNG fuel + residue income;
   [diesel-cng report](diesel-cng-cost-of-production.md)).
3. **Resource efficiency** — residue/husk/shell/cake become income or captive energy instead
   of waste.
4. **Non-farm income** — FPO/cooperative ownership gives the farmer a share of the ₹7 cr
   processing margin (the [oil-mill model](../pitch/TN-Combined-Oil-Mill-Model.xlsx)).

No single intervention doubles income — but the combination the DFI strategy calls for
(value-addition + real prices + cost-cut + non-farm earnings) is exactly what the
grain/oil-processing-plus-CBG-loop delivers, anchored in the crops the farmer already grows.
That is the through-line of this whole project: **the byproducts the system throws away —
bran, husk, cake, residue — are the underused income the DFI goal needs.**

## Caveats

Survey incomes are self-reported and definitional (SAS "agricultural household" ≠ NAFIS "rural
household" exactly — the two series are aligned in direction, not identical in base). "Real
doubling" verdicts depend on the deflator chosen; different analysts reach different exact
figures, but none find the 2× real target met by 2022-23. State variation is wide (Punjab,
Haryana, Kerala, TN above average; eastern states below). The DFI-contribution figures in §4
are directional model outputs from this project, not measured outcomes.
