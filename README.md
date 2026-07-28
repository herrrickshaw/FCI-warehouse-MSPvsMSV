# FCI Warehouse · MSP vs MSV

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/herrrickshaw/FCI-warehouse-MSPvsMSV/blob/main/notebooks/fci_msp_msv_analysis.ipynb)

Research + data project evaluating India's foodgrain procurement system and whether a
**Minimum Support Volume (MSV)** guarantee — government committing to buy a minimum *quantity*
of each crop — could extend effective price support beyond rice and wheat, where the
**Minimum Support Price (MSP)** currently works in practice.

## Scope

1. **FCI procurement trends** (10–15 yrs) — rice/wheat volumes, state-wise concentration
   (Punjab/Haryana → MP/Telangana shifts), central pool stocks vs buffer norms, economic
   cost vs MSP, food subsidy burden.
2. **Why MSP ≈ rice + wheat only** — procurement infrastructure, PDS offtake linkage,
   Shanta Kumar committee farmer-coverage estimates.
3. **Existing extensions** — PM-AASHA (PSS / PDPS / PPSS), NAFED pulses & oilseeds,
   CCI cotton, and their outcomes.
4. **The MSV case** — volume-based guarantee design, fiscal cost debate (legal-MSP
   estimates), storage/disposal constraints, WTO AMS limits, US CCC / EU intervention
   analogues.
5. **Haryana case study** — food processing policy, backward linkages (Mera Pani Meri
   Virasat, Bhavantar Bharpai, 14-crops-at-MSP claim) and forward linkages
   (government-as-seller: HAFED processing units, FCI OMSS(D) sales to millers).
6. **Ethanol precedent** — FCI rice & NAFED/NCCF maize supplied to distilleries for the
   ethanol blending programme: evidence that policy can create industrial offtake for
   state-procured grain, and the conditions it requires.

## Dashboard highlights

**The one-picture argument** — MSP is announced for 23+ crops, sustained procurement volume exists for two:

![Procurement as % of production by crop](dashboard/screenshots/coverage_gap.png)

**Procurement trend & stocks vs buffer norms** — record buying, stocks pulling away from need:

![Rice & wheat procurement; central pool stocks vs norms](dashboard/screenshots/trend_and_stocks.png)

**Where the grain goes & who supplies it** — offtake by channel (incl. OMSS sales to processors) and Punjab-heavy wheat concentration:

![Offtake by channel; wheat procurement by state](dashboard/screenshots/offtake_and_states.png)

**The physical ceiling** — covered storage capacity, the hard constraint on any volume guarantee:

![Storage capacity by agency](dashboard/screenshots/storage_capacity.png)

Full dashboard: [`dashboard/index.html`](dashboard/index.html) (self-contained — clone and open, or serve locally; `?theme=dark` forces dark mode). Full-page views: [light](dashboard/screenshots/full_light.png) · [dark](dashboard/screenshots/full_dark.png). Reproduce the charts in Colab via the badge above.

## Reference

- [GLOSSARY.md](GLOSSARY.md) — every abbreviation used across the reports, expanded and categorised.

## Layout

| Path | Contents |
|---|---|
| `report/` | Cited research report (MSP vs MSV evaluation + Haryana case study) |
| `data/` | CSVs from DFPD Foodgrain Bulletin, FCI storage/capacity data, UPAg — with `MANIFEST.md` recording source URLs and gaps |
| `dashboard/` | Interactive HTML dashboard: procurement vs storage vs disposal (PDS / PMGKAY / OMSS / ethanol / exports) |

## Data sources

Official only: DFPD Monthly Foodgrain Bulletin, fci.gov.in, upag.gov.in, PIB, CACP,
Economic Survey — plus credible analyses (ICRIER, NITI Aayog, academic papers).
No fabricated or interpolated figures; every file's provenance is in `data/MANIFEST.md`.

## Status

- [x] Repo scaffold
- [x] Research report → `report/msp-vs-msv-main-report.md`
- [x] Haryana + ethanol brief → `report/haryana-food-processing-linkages.md`
- [x] Data collection → `data/` (6 CSVs + MANIFEST)
- [x] Dashboard → `dashboard/index.html` (self-contained, light/dark, table views)

## Published essay

**The Price of Grain** — the administered price ladder, farmer coverage, trade parity, and the MSP+MSV ratio framework: [report/pricing-msp-msv-published.html](report/pricing-msp-msv-published.html) (also live as a Claude artifact).

<!-- 
DATA LIBRARY LINK - Add this section to every repo README.md
This snippet provides discovery and documentation links.
-->

## 📊 Data Discovery

This repository is part of the **Global Data Library** — a unified catalog of 10,528 datasets across 40+ repositories.

### Quick Links

- **[Global Data Library README](.ruflo/DATA_LIBRARY_README.md)** — Full catalog, search API, and usage examples
- **[Data Library Python Interface](.ruflo/data-library/data_library.py)** — Query datasets programmatically
- **[Repository Scanner](.ruflo/data-library/repo_scanner.py)** — Reindex all repos to update the catalog

### Datasets in This Repository

The data catalog automatically inventories all datasets in this repo. To find your data:

```python
from data_library import DataLibrary

lib = DataLibrary()

# Search this repo's datasets
results = lib.search("", source="<repo-name>")

# Get dataset details
dataset = lib.get("<dataset_id>")
print(f"Rows: {dataset['row_count']}")
print(f"Freshness: {dataset['freshness_hours']} hours old")
print(f"Storage: {dataset['storage_tier']}")
```

### Browse the Full Catalog

**Market Coverage** (5 markets, 21,279 symbols):
- India (NSE/BSE): 2,364 instruments
- US (NASDAQ/NYSE): 7,442 instruments
- Europe (17 exchanges): 1,214 instruments
- Japan (TSE): 3,709 instruments
- Korea (KRX): 2,768 instruments

**Government Sources** (30+ ministries):
- MOSPI: 25 datasets (GDP, CPI, trade, agri, power)
- SEBI: 151,928 XBRL results + IPO pipeline
- PIB: 25+ ministry announcements
- DGFT: India trade data (monthly)
- Agmarknet: 300+ mandi prices (daily)
- NSE/MCX: Real-time derivatives chains

See [Global Data Library README](.ruflo/DATA_LIBRARY_README.md) for complete documentation.

### Finding Data Across All Repos

```python
# Find India OHLCV data (might be in multiple repos)
lib.search("india ohlcv", market="india")

# Get the fastest/freshest version
optimal = lib.get_optimal("india ohlcv", latency="<100ms", freshness="<1day")
# Returns: {"storage_tier": "cassandra", "path": "..."}

# Check data gaps
gaps = lib.gaps("india", date_from="2026-01-01")

# See which collectors are stale
status = lib.collectors_status()
```

---
