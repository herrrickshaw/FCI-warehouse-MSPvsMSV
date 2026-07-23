# IISFM Phase-5 depot coverage — and where depot-level stock data actually lives

*Working note, 23 Jul 2026. Companion data: [`data/iisfm_phase5_depots.csv`](../data/iisfm_phase5_depots.csv), [`data/ap_buffer_godowns.csv`](../data/ap_buffer_godowns.csv), [`data/movement_by_mode.csv`](../data/movement_by_mode.csv).*

## 1. What the Phase-5 page contains — fully extracted

Source: [disfm.iisfm.nic.in/Hardware_Support/IISFM_Phase-5.htm](https://disfm.iisfm.nic.in/Hardware_Support/IISFM_Phase-5.htm)
(legacy NIC host, expired TLS cert; page is an Excel-export frameset with three sheets).

**All 173 "balanced depots"** of IISFM's fifth computerization phase are extracted to
`iisfm_phase5_depots.csv` with zone / region / district / depot name / depot type
(owned vs hired) / agency, plus the two hardware vendors' installation status
(HCL vs Tritron ICS: 133–136 installed-complete, 9–35 site-not-ready, 0–29 in-progress,
2 cancelled per vendor — the "Summary" sheet).

| Zone | Depots | Notes |
|---|---|---|
| South | 99 | 92 in the Andhra region alone — Phase 5 was largely an AP+South rollout |
| North | 39 | Punjab 17, J&K 6, Haryana 5, UP 5, Rajasthan 3 |
| East | 17 | West Bengal 7, Bihar 8 |
| West | 15 | Maharashtra 10, Chhattisgarh 3 |
| North-East | 3 | NEF region |

Type split: 114 hired vs 45 owned (+ 14 agency/office rows where the sheet's columns shift).
This matches the broader pattern in `storage_capacity.csv`: FCI's physical network is
majority-hired, so "FCI depot data" is really FCI + SWC/CWC/state-agency data.

## 2. Where the stock *levels* for these depots live — access map (probed, not assumed)

| Source | Level | Access | Verified status |
|---|---|---|---|
| **IRRS** ([irrs.iisfm.nic.in](https://irrs.iisfm.nic.in/)) — IISFM Rapid Reporting System | depot/FSD-wise stocks | 🔴 login-gated | Home page is a login form. One report page ([Show_Reports.aspx?RID=8](https://irrs.iisfm.nic.in/Show_Reports.aspx?RID=8), report RFRD-02) renders its region→district→depot form publicly and accepts cascading postbacks without auth, but the final report generation is session-gated — submits return the form unchanged. |
| **DISFM** ([disfm.iisfm.nic.in](https://disfm.iisfm.nic.in/)) — District Stock Accounting | district-wise stock accounts | 🔴 login-gated | `/HTML/RegionIndex.html` responds but its links (`checklist.asp`, `Menupage.asp`) require a session. The public part of the host is documentation: [user manual](https://disfm.iisfm.nic.in/download/DISFM_UserManual.pdf), [depot-code system](https://disfm.iisfm.nic.in/Download/130612_DCMS_How_To.pdf), and the Phase-5 hardware page itself. |
| **Depot Online System** ([fcidepotonline.gov.in](https://fcidepotonline.gov.in/)) — IISFM's successor | depot operations, real-time | 🔴 login-gated | Role-based dashboards for FCI management; no public view. |
| **FCI stocks page** ([fci.gov.in/stocks.php](https://fci.gov.in/stocks.php)) | region/state-wise, weekly | ✅ public | The finest-grained *public* stock series. |
| **DFPD Foodgrain Bulletin** | state-wise monthly stocks, all-India vs norms | ✅ public | Already collected → `stocks_vs_norms.csv` (bulletin archive links broken site-wide; Nov-2024 PDF recovered via search index). |
| **data.gov.in** | state-wise procurement/stocks; cotton MSP annexures | ✅ public (sample key caps 10 rows/page) | Already used for `procurement_by_year.csv`. No depot-wise stock dataset found in the catalog. |

**Bottom line:** depot-level *stock* data for the 173 Phase-5 depots is an internal FCI
system (IISFM → DOS); the public ladder stops one level up at region/state. Any MSV
monitoring design that needs depot-level transparency would require DFPD to publish
DOS extracts — the plumbing exists, the publication policy doesn't.

## 3. What we can reconstruct publicly at (near-)depot level

- **`ap_buffer_godowns.csv` — 177 AP buffer godowns with lat-longs** (APSCSCL roster,
  user-supplied PDF): district / revenue division / mandal / godown / category
  (SWC-own, SWC-HG, CWC, FCI, CSC, others), APSCSCL-reserved space and total capacity.
  Totals: **32.09 LMT capacity, 19.56 LMT reserved**. Since 92 of the 173 Phase-5 depots
  are in the Andhra region, this roster is the closest public *capacity-level* view of the
  Phase-5 footprint — and it is geocoded, so it can be mapped.
- **FSD Faridabad case study** (user-supplied depot-operations deck): owned covered
  38,340 MT + hired 162,842 MT + 20,000 MT silos (plus FSD Palwal 11,060 MT); receipts
  from mandi / custom-milled rice / rakes; issues via TPDS/AAY and inter-depot dispatch.
  A concrete example of the ~4:1 hired-to-owned skew at a single large depot.
- **Movement layer** (`movement_by_mode.csv`, FCI Handbook 2020): 380–467 LMT/year moved,
  85–90% by rail; >60% of procured stock crosses regions (surplus → deficit). Relevant to
  MSV: a volume guarantee for new crops/states inherits this rail-first logistics chain —
  depots without rakepoints (many of the 114 hired Phase-5 sites) can *hold* grain but
  are slow to *evacuate* it.

## 4. Follow-ups

- A registered (free) data.gov.in key lifts the 10-row page cap for bulk pulls.
- FCI weekly stocks PDFs (region-wise) could be time-seriesed into `data/` if regional
  granularity becomes needed — one PDF per week, stable URL pattern on fci.gov.in.
- If IRRS ever exposes RFRD-02 without a session (it renders the form today), the same
  postback chain scripted here yields depot-wise stocks directly; the probe script is
  reproducible from this note.
