# Holding Economics: Does Storing Indian Agri Commodities for 1–3+ Years Beat Carrying Cost?

**Question.** Does it make business sense for a private actor to buy Indian agricultural commodities (grains, pulses, oilseeds, sugar) at harvest, store them in a professional warehouse for 1–3+ years, and sell later — i.e., does historic price appreciation beat the cost of carry?

**Answer: No — not systematically, for any of the 16 commodities tested, over any window (5y / 10y / 14y).** Wholesale price appreciation runs 2–6% a year; the full cost of carry runs 13–20% a year. The gap is −8 to −15 percentage points *per year of holding*, and it compounds. Even the opportunistic variant (buy only after a price crash, hold two years into the next deficit) paid off in only 3 of 27 historical episodes, all in minor coarse cereals. The only economic actor for whom multi-year grain holding "works" is the state — because it deliberately pays the negative carry as food-security policy and monetizes none of it.

---

## 1. Data

| Series | Source | Coverage |
|---|---|---|
| Monthly WPI, commodity level (base 2011-12=100) | Office of the Economic Adviser, `eaindustry.nic.in`, `indx_download_1112/monthly_index_202606.xls` (raw copy in `data/raw/`) | Apr 2012 – Apr 2026 (169 months) |
| MSP series, crop years 2010-11 → 2026-27 | CACP, `cacp.da.gov.in/Home/MSP` (backing dataset `json.json`, updated 13.05.2026; raw copy in `data/raw/cacp_msp.json`) | 234 crop-year rows |
| Cross-check of last 5 MSP years | DES, Ministry of Agriculture, "MSP Statement (English) as on 12.12.2025" PDF (`data/raw/msp_statement.pdf`) | KMS 2021-22 → RMS 2026-27 |
| Warehouse storage tariff | CWC, "Commodity-wise tariff for FY 2024-25", `cewacor.nic.in/Docs/Commodity_Basis_Tariff2425.pdf` (raw copy in `data/raw/`) | signed 22.03.2024 |

Commodities: paddy, rice (non-basmati), wheat, maize, jowar, bajra; arhar/tur, gram, moong, urad, masur, rajma; mustard seed (rape & mustard), soybean, groundnut seed; sugar. WPI-vs-MSP cross-check: MSP labeling conventions differ (CACP tags by crop year, DES by marketing season, offset by one year); values reconcile exactly — e.g., wheat crop year 2024-25 = RMS 2025-26 = ₹2,425/qtl in both.

**Note on window length.** The 2011-12-base WPI series begins Apr 2012, so the longest clean window is 14 years, not 15. Splicing to the 2004-05 base via OEA linking factors is possible but was not done (the conclusion is not marginal enough to change).

## 2. Carrying-cost model (every rate cited)

Annual carry (as % of commodity value) = **storage + insurance + interest + physical loss**.

| Component | Rate used | Source |
|---|---|---|
| Storage | CWC commodity-wise tariff FY 2024-25, quoted **per 50-kg bag-equivalent per month in paise**, class-C warehouse (middle of the A–K rating scale). Wheat 699 p = ₹13.98/qtl/mo; rice (non-basmati) ₹17.46; paddy ₹19.40; maize/bajra/jowar ₹16.00; pulses (25–50 kg bags) ₹17.12; soybean ₹16.00; mustard ₹15.38; groundnut kernels ₹26.48 | CWC `Commodity_Basis_Tariff2425.pdf`, pp. 1–7. Class-A (cheapest) rates are ~12% lower, class-K ~2.1× higher — class choice does not change any verdict |
| Insurance | ₹0.05 per ₹100 of stock value per month = 0.6%/yr, added only where the tariff row is marked "Excl Ins." (pulses, oilseeds, sugar); foodgrain rows are "Inc Ins." | CWC tariff circular 2017-18, para 9 (`cewacor.nic.in/Docs/tariff/tariff_all_ro_wh_com_co_2017_18_080317.pdf`); same convention in the FY24-25 commodity tariff's Inc/Excl-Ins column |
| Interest | 10% p.a. base case. SBI Produce Marketing Loan against e-NWR (₹3–50 lakh): 1-yr MCLR + 0.80% ≈ 9.8% at the ~9.0% MCLR prevailing 2024-25; against non-e-NWR warehouse receipts it rises to MCLR + 3.60% ≈ 12.6%. (The 7% subvented rate is small/marginal farmers only, ≤₹3 lakh, ≤6 months — not a trading operation.) | SBI Agri Banking, "Produce Marketing Loan" product page (sbi.bank.in); CGS-NPF guarantee fee 0.4%/1.0% p.a. (PIB, Dec 2024) not added |
| Physical loss | 0.5%/yr base (scientific covered storage); 1.0%/yr conservative. FCI's own storage loss on rice is now ~0.07%/yr (down from 0.39% in 2013, per Government statements Aug 2024) — a floor achieved at institutional scale; DFPD SOP dated 03.01.2022 fixes formal storage loss/gain norms for wheat and rice. Pulses in private storage suffer bruchid/moisture damage well above this. | `dfpd.gov.in` SOP Storage 03.01.2022; newsonair.gov.in 07.08.2024 |
| Value per qtl (denominator) | Latest MSP (crop year 2025-26): e.g. wheat ₹2,585, paddy ₹2,369, arhar ₹8,000, mustard ₹6,200. Sugar has no MSP — ₹3,500/qtl assumed (floor: ₹3,100 Minimum Selling Price fixed Feb 2019; ex-mill 2024-25 ran ≈ ₹3,700–4,000). Rajma has no MSP — ₹9,000/qtl assumed from mandi levels. Rice valued at paddy MSP ÷ 0.67 out-turn. | CACP MSP dataset; assumptions flagged |

**Resulting annual carry (base case):** cereals 15.7–20.3% of value (storage alone is 5–10% because grain is cheap per quintal — paddy is worst at 9.8% storage on a ₹2,369 value); pulses 13.4–14.6%; oilseeds 14.1–15.5%; sugar 16.6%. Roughly ₹350–450/qtl/yr for wheat — i.e. **₹3.5–4.5/kg/yr**, the same order as the widely-cited DFPD buffer carrying cost of ~₹5.6/kg (FCI runs costlier interest via cash-credit and adds establishment overheads).

Not modeled (all would worsen the private case): mandi fees/commission on entry and exit (1.5–4% round trip in most states), fumigation for non-fumigable-tariff stocks, quality discounts on aged stock (old rice sells at a *premium*, but old wheat/pulses at a discount), GST on warehouse services for non-agri-produce classifications.

## 3. Results

Computed by `data/holding_economics.py` from the two CSVs; full tables in `data/holding_economics_summary.csv` (CAGR vs carry, 3 windows × 16 commodities), `data/holding_horizon_returns.csv` (harvest-buy 12/24/36-month distributions), `data/holding_episodes.csv` (post-crash episodes).

### 3.1 Systematic holding — price CAGR vs carry (14-year window, Apr 2012 → Apr 2026)

| Commodity | WPI CAGR %/yr | Carry %/yr | Net %/yr | Verdict |
|---|---:|---:|---:|---|
| Paddy | 4.8 | 20.3 | **−15.5** | carry exceeds appreciation |
| Rice (non-basmati) | 4.5 | 16.4 | −12.0 | carry exceeds appreciation |
| Wheat | 5.2 | 17.0 | −11.8 | carry exceeds appreciation |
| Maize | 3.8 | 18.5 | −14.7 | carry exceeds appreciation |
| Jowar | 6.0 | 15.7 | −9.7 | carry exceeds appreciation |
| Bajra | 6.0 | 17.4 | −11.4 | carry exceeds appreciation |
| Arhar/tur | 5.7 | 13.7 | −7.9 | carry exceeds appreciation |
| Gram | 3.5 | 14.6 | −11.1 | carry exceeds appreciation |
| Moong | 4.9 | 13.4 | −8.5 | carry exceeds appreciation |
| Urad | 5.8 | 13.7 | **−7.9** (best) | carry exceeds appreciation |
| Masur | 4.7 | 14.0 | −9.4 | carry exceeds appreciation |
| Rajma | 4.0 | 13.4 | −9.4 | carry exceeds appreciation |
| Mustard seed | 4.2 | 14.1 | −9.9 | carry exceeds appreciation |
| Soybean | 4.5 | 14.7 | −10.2 | carry exceeds appreciation |
| Groundnut seed | 4.4 | 15.5 | −11.1 | carry exceeds appreciation |
| Sugar | 2.3 | 16.6 | −14.3 | carry exceeds appreciation |

5-year and 10-year windows change nothing: best 5y case is bajra (CAGR 10.7% vs carry 17.4%, net −6.8%/yr). **No commodity, no window, comes within 7 points of break-even.** Even at zero interest (own idle capital treated as free) the cereals still lose on storage+loss alone versus appreciation in most windows; the pulses would roughly break even at zero interest — which is precisely why holding is done by farmers in their own sheds, not by anyone renting warehouses and capital.

### 3.2 Harvest-trough buying, 12/24/36-month exits

Buying every year in the arrival-season trough month (e.g. Nov for kharif, Mar–Apr for rabi) and selling 1/2/3 years later — the trader's best-case systematic timing:

- **Gross returns are usually positive** (wheat: mean +5.3% at 12m, +15.7% at 36m, 86–100% of years positive) — prices do drift up. But against the carry hurdle (compounded 17–74% over 1–3 years), the **fraction of years that beat carry is 0% for paddy, rice, wheat, groundnut and sugar at every horizon**.
- The only years that ever beat full carry were pulse/coarse-cereal spike years: arhar 31% of 12m starts (2015-16 and 2023-24 spikes), urad 31%, moong/jowar 38%, maize/bajra 15–17%. Mean net after carry is still deeply negative everywhere (−6% to −61% depending on horizon).
- Longer holding makes it worse, not better: the carry hurdle compounds faster than prices appreciate. Mean net at 36 months is −19% (urad, best) to −61% (paddy, worst).

### 3.3 Opportunistic holding — buy the crash, sell the deficit

Rule tested: enter only when the trailing-12-month WPI change is ≤ −10% (a genuine crash, typically prices at/below MSP), hold 24 months, non-overlapping episodes. Success = gross return beats compounded carry.

**27 episodes across 14 commodities since 2013; only 3 paid off (11%)** — jowar (2 entries, 1 paid), bajra (2, 1), maize (2, 1). Every pulse episode failed: the 2017-18 pulse-glut entries (arhar −69% net, moong −46%, urad −33%, masur −62% net of carry) are the striking ones — after the 2016-17 crash, prices stayed below MSP for ~3 years because record procurement stocks overhung the market. Soybean: 0 of 4. Mustard: 0 of 3 (the 2022 entry caught the post-Ukraine unwind and lost 21% net).

Why the "buy low, wait for the deficit year" trade fails in India even though pulse prices do spike: **the state truncates the upside**. When tur/urad spiked in 2023-24, the Government (i) imposed stock limits on tur and urad under the Essential Commodities Act (order of 2 June 2023, tightened 21 June 2024), (ii) kept tur/urad/masur imports duty-free and extended free import of yellow peas (Dec 2023 onward), and (iii) offloaded buffer stocks through NAFED/NCCF. For cereals the cap is even harder: OMSS wheat/rice sales, the June 2023 wheat stock limits (first since 2008, re-imposed 2024), and export bans (wheat May 2022, non-basmati rice Jul 2023) mean a private holder is short a policy option: the state sells into every rally you were waiting for. Sugar is price-managed end to end (monthly release quotas, MSP floor, export quotas). Upside is clipped; downside (your carry) is not.

## 4. The FCI angle — the state pays this carry on purpose

FCI's published economics confirm the model from the public-sector side. Per PRS Legislative Research's analysis of the 2024-25 Food & Public Distribution demand for grants: FCI's **economic cost in 2024-25 was ≈ ₹39.8/kg for rice and ₹27.7/kg for wheat**, against pooled (MSP) cost of ≈ ₹34.3/kg rice-equivalent (paddy MSP ₹23.00/kg ÷ 0.67 out-turn) and ₹22.75/kg wheat — i.e., procurement incidentals + distribution + carrying add **~22% to acquisition cost even in year one**, before any multi-year buffer holding. The buffer-carrying component alone (storage + interest on stock value) is of order **₹5–6/kg/yr** (widely cited DFPD figure ~₹5.6/kg), which on ₹23–25/kg grain is 20-odd percent a year — matching this report's 17–20% private carry estimate for cereals.

The state carries ~600+ lakh tonnes at this negative yield because the product is food security, not return: it monetizes via free NFSA issue (Central Issue Price ₹0 since Jan 2023) and recovers nothing. **A private holder replicating FCI's behaviour on wheat — buy at MSP, hold 3 years in rented covered storage at 10% money — would lose roughly 44% of invested value net of the grain's own price appreciation** (36-month mean net, Table 3.2). That is the subsidy the exchequer books as "food subsidy" (₹2.0–2.4 lakh crore/yr budgets, 2024-25 → 2026-27): it is precisely the bill for holding grain whose carry exceeds its appreciation.

## 5. Verdict

1. **Systematic multi-year holding is not a business.** Every commodity's carry (13–20%/yr) exceeds its long-run wholesale appreciation (2–6%/yr) by a wide margin. This is structural, not cyclical: MSP-led procurement compresses the harvest trough (you cannot buy much below MSP), and stock releases/imports/export bans compress the deficit peak.
2. **Cheap grain is the worst hold.** Storage is charged per bag, not ad valorem, so paddy/maize/wheat carry 5–10%/yr in storage rent alone. Pulses and oilseeds (₹5,000–9,000/qtl) are the least-bad — carry ~13.5–14.5% — and they are also the only commodities whose price spikes occasionally cleared the hurdle.
3. **Opportunistic pulse-cycle trading paid off ~11% of the time historically** and requires surviving 40–70% drawdowns net of carry (2017-18). Post-2023 stock limits on tur/urad make the strategy legally capped in size and even less attractive.
4. **Where holding does pay** (outside this dataset's scope but consistent with it): intra-season arbitrage (harvest month → lean month within 6–9 months, before a second harvest arrives) sometimes clears carry for pulses/oilseeds; and farmer self-storage with subvented 7% credit and zero rent shifts the arithmetic — that is a working-capital smoothing decision, not an investment.
5. **If you want exposure to Indian agri inflation, own the storage, not the stored.** The warehouse operator earns ₹150–320/qtl/yr regardless of price direction — the exact cash flow that makes the holder's position uneconomic. (CWC's consistently profitable, dividend-paying record is the corporate confirmation.)

## 6. Caveats and gaps

- **WPI ≠ mandi price.** WPI is a wholesale index with its own weighting and quality mix; a trader's realized basis (specific mandi, specific grade) differs. Mandi-level troughs are somewhat deeper than WPI troughs, which would improve entry by a few points — nowhere near the 10–15 pt/yr gap.
- **14 years, not 15**: 2011-12-base WPI starts Apr 2012; earlier data exists on the 2004-05 base and could be spliced via OEA linking factors.
- **Storage tariff is CWC class-C FY 2024-25 applied across history.** Historic tariffs were lower in rupee terms, but so were commodity values; the % of value is roughly stable. Private/WDRA godowns in producing belts can be ~30–50% cheaper than CWC class C in the off-season — that still leaves carry ≥10%/yr.
- **Interest is the largest single component (10 of ~13–20 pts).** A holder with genuinely free capital still nets negative in cereals and near-zero in pulses before mandi fees and quality risk.
- **Loss assumption (0.5%/yr) is optimistic for pulses** in private storage (insect damage, moisture); FCI's 0.07% rice figure is professional, fumigated, rotated stock.
- **Policy truncation is asymmetric and has intensified**: stock limits (tur/urad 2023 & 2024; wheat 2023 & 2024), duty-free pulse imports and free yellow-pea imports in deficit years, OMSS releases, export bans (wheat 2022; non-basmati rice 2023-24). Historic spike returns (2015-16 pulses) likely overstate what today's policy regime would permit.
- **Sugar and rajma valuations are assumptions** (₹3,500 and ₹9,000/qtl respectively, flagged in the script); sugar additionally has monthly release quotas making free storage-arbitrage impossible for non-mills.
- **FCI buffer carrying cost** ~₹5.6/kg is a widely-reported DFPD-derived figure; the current-year official number sits in DFPD Foodgrain Bulletin / FCI annual report tables that are PDF-bound and were not machine-extracted here — flagged as the one number cited from secondary reporting rather than a primary file in `data/raw/`.

---
*Built 2026-07-23. Pipeline: `data/holding_economics.py` reads `data/wpi_commodity_monthly.csv` + `data/msp_series.csv` → writes `data/holding_economics_summary.csv`, `data/holding_horizon_returns.csv`, `data/holding_episodes.csv`. Raw sources preserved in `data/raw/`.*
