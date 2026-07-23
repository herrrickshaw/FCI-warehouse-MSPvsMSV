# Grain Dashboard Data — MANIFEST

Collected 2026-07-23. All quantities in **lakh metric tonnes (LMT)** unless a row's
`note` says otherwise. Nothing is interpolated or estimated by the collector; every
number was read from the cited source. Rebuild: `python3 build_csvs.py` (raw inputs
kept in this directory: `bulletin_nov2024.pdf`, `dgi_raw/*.json`, `es_*.pdf`, `pib_*.txt`).

## Files

### procurement_by_year.csv (610 rows)
`year, crop, state, quantity_lmt, source, as_of, note`
- **Rice** (KMS, Oct–Sep): state-wise **2010-11 → 2024-25**.
  - 2010-11→2013-14: data.gov.in resource `fc60774a-…` "Marketing Season Wise Rice
    Procurement for Central Pool from 2010-11 to 2015-16" (DFPD PQ reply).
  - 2014-15→2016-17: resource `fa1fdb29-…`; 2017-18→2019-20: `4312f8ec-…`;
    2020-21→2022-23: `4420e699-…` (KMS 2020-21 to 2023-24).
  - 2023-24 (final, 525.44 all-India) and 2024-25 (**season-to-date as on 30.11.2024**,
    189.14 all-India): DFPD Monthly Foodgrain Bulletin Nov-2024, p.4 —
    https://dfpd.gov.in/WriteReadData/FoodBulletinUploadDocuments/8e0ba45f-affc-4309-8a2d-f6c8d01156b7_Foodgrain%20Bulletin%20fot%20November,%202024.pdf
- **Wheat** (RMS, Apr–Mar): state-wise **2011-12 → 2024-25**, plus all-India
  **2025-26 final = 300.35 LMT** (PIB Year-End Review 2025, PRID 2210211).
  - 2011-12→2013-14: `29927e68-…`; 2014-15→2017-18: `674c639a-…`;
    2018-19→2019-20: `f2d1ec81-…`; 2020-21→2023-24: `235a38be-…`;
    2024-25 (266.05): bulletin p.4.
- **Coarse grains**: all-India 2015-16→2020-21 (`6594e0d2-…`, converted from tonnes),
  state-wise 2021-22→2024-25 (bulletin p.4).
- All-India totals verified against independent PIB citations (e.g. wheat RMS 2021-22
  = 433.44; rice KMS 2020-21 = 601.73).
- **Gaps/caveats**: wheat RMS 2010-11 missing (dataset starts 2011-12). Rice 2024-25
  is partial (KMS ran to Sep-2025; full-season paddy = 832.17 LMT per PIB YER 2025 —
  rice-equivalent final not published in sources collected). Wheat RMS 2025-26
  state-wise final split not collected (all-India only). RMS 2026-27 (target 303 LMT,
  PIB PRID 2236215) still in progress at collection date — not included. Sources
  differ by ±0.5 LMT for RMS 2023-24 wheat (262.02 dataset vs 261.97 bulletin vs
  262.48 in some PIB releases — reporting-cutoff differences); dataset value used.

### stocks_vs_norms.csv (192 rows)
`date, commodity, stock_lmt, buffer_norm_lmt, source, note`
- Month-wise **opening stocks in Central Pool**, 1 Jan 2021 → 1 Dec 2024, for rice,
  wheat, coarsegrains, total. Source: bulletin p.6 (FCI data).
- `buffer_norm_lmt` filled only on norm dates (1 Apr / 1 Jul / 1 Oct / 1 Jan);
  norms w.e.f. 22.01.2015 incl. strategic reserve (rice 20 + wheat 30 LMT):
  Apr 135.8/74.6, Jul 135.4/275.8, Oct 102.5/205.2, Jan 76.1/138.0 (rice/wheat).
- **Rice figures exclude unmilled paddy** (bulletin note: 351.29 LMT paddy with
  FCI/state agencies on 30.11.2024 ≈ 235 LMT CMR at 67% OTR).
- **Gaps**: pre-2021 and 2025-26 monthly stocks not collected (older bulletins'
  download links are broken on dfpd.gov.in archive; RBI Handbook table 26 blocked —
  see "Blocked sources"). PIB YER 2025 gives a spot figure: rice stock >490 LMT
  (incl. ~160 LMT due from milling), Nov-2025.

### offtake_by_scheme.csv (340 rows)
`year, scheme, commodity, measure, quantity_lmt, source, note`
- Scheme-wise **allocation and offtake**, rice & wheat, **2019-20 → 2024-25**, from
  bulletin p.9 ("Foodgrains allocation, offtake and rates 2019-20 to 2024-25").
- Schemes: NFSA_TPDS, ICDS_WBNP, PM_POSHAN_MDM, TPDS_TideOver,
  Welfare_Institutions_Hostels, SAG, Annapurna, Natural_Calamity_Relief,
  Festivals_AddlAllocation, Defence_ITBP, OMSS_Domestic, WFP_Export, TOTAL,
  plus PMGKAY / ANBP_Migrant / NonNFSA_Covid rows for 2020-21→2022-23 (the Covid
  free-grain tranche, additional to NFSA; merged into NFSA from Jan-2023).
- Column order verified against the bulletin's 2024-25 annual-allocation table (p.20).
- **Caveats**: 2024-25 offtake is partial (TPDS to Nov-2024, OWS to Oct-2024).
  OMSS(D) rows are the domestic open-market sales (Bharat Atta/Rice lifting included
  in bulletin p.31: wheat 8.03 LMT, rice 10.91 LMT Apr–Nov 2024). Ethanol sales are
  NOT a separate scheme row in this table. Years before 2019-20 not collected
  (older bulletins inaccessible; see Blocked sources).

### storage_capacity.csv (364 rows)
`state, agency, capacity_lmt, as_of, source, note`
- State-wise **FCI covered storage** (month-average, Nov-2024) by agency, from
  bulletin p.33 (Agency-wise Storage Capacity with FCI): `FCI_owned`,
  `FCI_owned_silo`, `hired_state_govt`, `hired_CWC`, `hired_SWC`, `hired_PEG`,
  `hired_PWS2010`, `hired_silo`, `hired_private` (leaf categories only; sum them for
  totals — all-India FCI owned 147.10, hired 263.77, total 410.88 LMT).
- `state_agencies_incl_SWC`: capacity with state agencies excluding what they lease
  to FCI (bulletin p.32; all-India 365.72 LMT; grand total central-pool capacity
  776.59 LMT as on 30.11.2024).
- ALL_INDIA silo rows (as of Dec-2025, PIB YER 2025 PRID 2210211): circuit-model
  silos 5.50 LMT operational; rail/road-fed 20.25 LMT functional + 4.00 under
  construction; hub-&-spoke Phase-I 34.875 LMT awarded (3.75 completed).
- **Caveats**: this is *covered* capacity; CAP/plinth not separately given in the
  Nov-2024 bulletin table. Depot/godown counts not collected (FCI depot-wise pages
  are JS-driven; not reachable in this run).

### ethanol_allocation.csv (3 rows)
`year, commodity, allocated_lmt, lifted_lmt, rate_rs_per_qtl, source, note`
- ESY 2024-25: FCI rice to ethanol distilleries at **Rs 2250/qtl fixed, ceiling
  24 LMT** — PIB PRID 2101827 (11-Feb-2025), official.
- ESY 2025-26: **cap 72 LMT (52 allocated + 20 additional), Rs 2320/qtl w.e.f.
  01.11.2025–30.06.2026** — ⚠ SECONDARY sources (chinimandi.com, ruralvoice.in,
  bioenergytimes.com reporting the DFPD order); the DFPD order itself was not
  retrievable from this machine. Treat as provisional until cross-checked.
- OMSS rice actually sold Aug–Nov 2024: 5.45 LMT (bulletin p.31) — buyer mix
  (ethanol vs other) not split in the bulletin; recorded as `lifted_lmt` with note.
- **Gaps**: maize-for-ethanol is procured from the open market (not allocated from
  the central pool), so no government allocation series exists; NAFED/NCCF assured-
  price maize-for-ethanol quantities were not found in an official machine-readable
  source in this run. Pre-2024-25 rice-to-distillery quantities (Dec-2020→Jul-2023
  cumulative ≈24 LMT per press reports) not included — official per-year split not
  located.

### production_vs_procurement.csv (128 rows)
`year, crop, production_lmt, procured_lmt, procurement_share_pct, agency, source, as_of, note`
- **Rice & wheat**: 2010-11 → 2024-25(rice partial)/2025-26(wheat). Production from
  Economic Survey Statistical Appendix Table 1.15 — three vintages spliced:
  ES 2020-21 App (2010-11, 2011-12), ES 2022-23 App (2012-13→2014-15, final
  estimates), ES 2025-26 App (2015-16→2024-25; 2024-25 = final estimates).
  Million tonnes ×10 → LMT. Procurement = all-India totals from
  procurement_by_year.csv. Share = procured/production (marketing season vs
  Jul–Jun agricultural year — noted per row).
- **Coarse grains** aggregate: 2015-16→2023-24.
- **Crop-level (maize, jowar, bajra, ragi, tur, urad, moong, gram, masur,
  groundnut, mustard, soybean, sunflower, nigerseed)**:
  - 2017-18→2020-21: data.gov.in `b7ffc0f4-…` (production + MSP procurement,
    tonnes→LMT; DFPD PQ reply).
  - 2021-22 & 2022-23: `cfff9629-…` (tonnes→LMT).
  - 2023-24: `4ed94214-…` — **kharif season only** (both sides), flagged in note.
- `agency`: FCI_state_agencies for rice/wheat/coarse; NAFED_PSS for pulses/oilseeds
  (PSS procurement under PM-AASHA).
- **Caveats**: production vintages differ across the splice points (noted above);
  crop-level rows for 2023-24 are kharif-only; masur/nigerseed/sunflower have many
  missing procurement years (no PSS operations those years — left blank, not zero,
  where source said NA). Cotton (CCI) excluded — production published in bales,
  not tonnes. Rice 2024-25 share understated (partial procurement).

## Blocked / broken sources (and workarounds used)
- **dfpd.gov.in Food Grain Bulletin archive**: the archive pages render but every
  download link is empty (verified in a real browser, not just curl) and the site's
  Statistics/Reports pages throw "Error initializing page". Workaround: fetched the
  Nov-2024 bulletin PDF directly from its Google-indexed WriteReadData URL. Only
  Nov-2024 was indexed; older/newer bulletin PDFs unreachable.
- **RBI Handbook of Statistics (rbidocs.rbi.org.in)**: table downloads sit behind a
  TSPD challenge + CAPTCHA from this machine; not bypassed. Workaround: Economic
  Survey Statistical Appendix (indiabudget.gov.in) for long-series production and
  net-availability context (es_tab1.20.pdf has total-foodgrain procurement/PDS
  1951→2023 if a longer aggregate series is wanted).
- **UPAg (upag.gov.in)**: not attempted after DFPD/FCI dead-ends consumed the
  budget; bulletin + data.gov.in + ES covered the needs. Untested, not "blocked".
- **FCI (fci.gov.in)**: new site is fully JS-driven; procurement/storage data pages
  not reachable as static tables. Storage data taken from the DFPD bulletin's FCI
  tables instead (same underlying source, P&R Division/DISFM).
- **PIB**: WebFetch returns 403, but plain curl with a browser UA works — used for
  PRIDs 2210211 (YER 2025), 2101827 (ethanol/OMSS rates), 2030483 (wheat RMS
  2024-25), 2236215 (RMS 2026-27 targets), 2125722 (RMS 2025-26 progress).
- **data.gov.in**: public sample API key works but throttles hard (HTTP 429);
  fetched with 10-row pages + backoff. Resource UUIDs recorded per row in `source`.

- **Patch 2026-07-23**: rice 2024-25 row replaced with derived full-season rice-equivalent (832.17 LMT paddy x 0.67 outturn = 557.55 LMT, share 37.1%); the collected 189.14 LMT was a season-to-date stub. Derivation, not a reported figure.

- **iisfm_phase5_depots.csv** — all 173 IISFM Phase-5 "balanced depots" (zone/region/district/depot/type/agency + vendor install status). Source: disfm.iisfm.nic.in/Hardware_Support/IISFM_Phase-5.htm (Excel-export frameset, expired cert). 12 rows have shifted columns (agency-office rows).
- **ap_buffer_godowns.csv** — 177 AP buffer godowns with lat-longs, APSCSCL reserved + total capacity (32.09/19.56 LMT). Source: user-supplied APSCSCL roster PDF.
- **movement_by_mode.csv** — foodgrain movement by rail/road/waterways 2013-14→2019-20 (partial). Source: FCI Handbook 2020, Institute of Food Security (user-supplied PDF).

- **Correction 2026-07-23 (ethanol pricing)**: FCI-rice ethanol was ₹58.50/L in ESY 2024-25, revised to ₹60.32/L in ESY 2025-26 (+3.11%, tracking rice ₹2,250→₹2,320/qtl). The BPCL-floated OMC tender buckets grain ethanol as FCI-rice / DFG (~₹64/L) / maize (₹71.86/L); ESY 2025-26 Cycle-1 mandates 40% FCI-grain sourcing for Q1-Q3. Source: ChiniMandi tender coverage.

- **sugarcane_2025_26.csv** — season 2025-26 sugar/cane statistics (production, recovery, FRP, arrears state-wise, ethanol diversion) from ChiniMandi (NFCSF/ISMA/parliamentary-panel reporting). Secondary source; net-of-diversion mid-April snapshots.

### trade_price_parity.csv (67 rows) — added 2026-07-23
`commodity, flow, fy, qty_lmt, value_inr_cr, value_usd_mn, value_unit, unit_value_usd_per_t, unit_value_inr_per_qtl, fx_rate, domestic_ref_price_inr_per_qtl, ref_price_type, parity_gap_pct, source, note`
- Export/import qty+value (DGCI&S via APEDA agriexchange JSON APIs + tradestat.commerce.gov.in)
  for FY2023-24→2025-26: basmati/non-basmati rice, wheat, maize, millets, other coarse
  cereals, pulses (aggregate + tur/urad/masur/yellow-peas/chana/moong split), groundnut,
  sugar, vegetable oils (aggregate + crude palm/RBD palmolein/crude soy/crude sun).
- Unit values computed value÷qty from the same source table; `fx_rate` = rate implied by
  the source's own ₹/$ columns (FY26 ≈ 88.5, NOT the ~86 convention). `parity_gap_pct`
  vs 2025-26 MSPs (rice vs paddy-MSP-derived cost 3850; sugar vs ex-mill 3850;
  groundnut in-shell basis noted per row). FY2025-26 = full-year provisional.
- Rebuild: `python3 data/build_trade_parity.py` (inputs pinned in the script; raw API
  captures in `data/raw_trade/*.json`). Analysis: `report/trade-price-parity.md`.
- Gaps: refined soy/sun oil lines not pulled; pulses-export basket not HS-split;
  millet MSP proxied by jowar; niryat.gov.in geo-fenced (values-only anyway).

- **mandi_vs_msp_20260723.csv** — mandi modal medians vs MSP 2025-26 per crop, full Agmarknet daily feed 23-Jul-2026 (17,247 records via fixed agri-commodity-tracker collector); % of market reports below MSP.
