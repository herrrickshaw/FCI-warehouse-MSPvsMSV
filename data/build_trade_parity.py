#!/usr/bin/env python3
"""Build data/trade_price_parity.csv from raw_trade/*.json (collected 2026-07-23).

Sources (all fetched 2026-07-23):
- APEDA AgriExchange 3-Year Export Statement (DGCI&S principal commodities):
  https://agriexchange.apeda.gov.in/India/GenerateExportStatement/Index
  (POST /India/GenerateExportStatement/GetExportStatement) -> raw_trade/export_statement.json
  Quantity in MT, values Rs crore + USD million. FY2025-26 = full year Apr-Mar
  (portal's current period is 2026-27 Apr-May, so 2025-26 is closed provisional DGCI&S).
- APEDA product report (42Head) for Maize / Millet / Pulses(APEDA basket) exports:
  https://agriexchange.apeda.gov.in/India/GenerateAPEDAProductReport/Index
  (POST GenerateIndExpApedaProduct; values captured in-browser 2026-07-23; MT).
- APEDA Import Statement (APEDA products):
  https://agriexchange.apeda.gov.in/India/GenerateImportStatement/Index -> import_statement_APEDA.json (MT)
- APEDA HS-8-digit import report (pulses split):
  https://agriexchange.apeda.gov.in/India/IndiaImportGenReport/Index -> import_pulses_hs.json (KG)
- APEDA India Import of Principal Commodities (VEGETABLE OILS aggregate):
  https://agriexchange.apeda.gov.in/India/IndiaImportPrincipalCommodities/Index -> import_vegoils.json (KG)
- DGCI&S tradestat commodity-wise import (edible-oil HS codes):
  https://tradestat.commerce.gov.in/eidb/commodity_wise_import -> tradestat_oils_raw.json (KGS)

Domestic reference prices (Rs/qtl) are KMS/RMS 2025-26 MSPs per the repo's MSP tables;
sugar uses the DFPD Minimum Selling Price (Rs 31/kg, unchanged since Feb-2019) and an
ex-mill realisation band of Rs 38-39/kg (3850 midpoint used).
Rice reference: paddy MSP 2369 / 0.67 outturn + milling & handling ~= 3700-4000; 3850 used.
Groundnut caveat: MSP is for in-shell pods; exports are mostly shelled kernels
(~70% outturn) - kernel-equivalent MSP ~= 7263/0.70 = 10376 noted per row.

fx_rate = implied DGCI&S rate (Rs crore value / USD mn value * 10) computed per row when
both currencies come from the source; this is the actual conversion embedded in the data
(FY24 ~82.7, FY25 ~84.9, FY26 ~88.5 - close to the FY-average USDINR 82.8/84.5/86 the
task sheet suggested; the source-implied rate is used so INR and USD columns reconcile).
"""
import csv, os

OUT = os.path.join(os.path.dirname(__file__), "trade_price_parity.csv")

APEDA_EXP = "https://agriexchange.apeda.gov.in/India/GenerateExportStatement/Index"
APEDA_42H = "https://agriexchange.apeda.gov.in/India/GenerateAPEDAProductReport/Index"
APEDA_IMP = "https://agriexchange.apeda.gov.in/India/GenerateImportStatement/Index"
APEDA_HS = "https://agriexchange.apeda.gov.in/India/IndiaImportGenReport/Index"
APEDA_PC = "https://agriexchange.apeda.gov.in/India/IndiaImportPrincipalCommodities/Index"
TRADESTAT = "https://tradestat.commerce.gov.in/eidb/commodity_wise_import"

# (commodity, flow, fy, qty_tonnes, inr_cr, usd_mn, dom_ref, ref_type, source, note)
ROWS = [
    # ---------------- EXPORTS (DGCI&S principal commodities via APEDA, MT) ----------------
    ("basmati rice", "export", "2023-24", 5242511, 48389.21, 5837.13, 3850,
     "paddy MSP 2369/0.67 + milling (3700-4000 band, 3850 used)", APEDA_EXP,
     "premium aromatic; MEP $1200->$950/t Aug-Oct 2023, MEP removed Sep-2024"),
    ("basmati rice", "export", "2024-25", 6065456, 50311.89, 5944.48, 3850,
     "paddy MSP 2369/0.67 + milling (3700-4000 band, 3850 used)", APEDA_EXP, ""),
    ("basmati rice", "export", "2025-26", 6521797, 50137.13, 5672.77, 3850,
     "paddy MSP 2369/0.67 + milling (3700-4000 band, 3850 used)", APEDA_EXP,
     "FY26 full-year provisional DGCI&S"),
    ("non-basmati rice", "export", "2023-24", 11116713, 37804.42, 4570.05, 3850,
     "paddy MSP 2369/0.67 + milling (3700-4000 band, 3850 used)", APEDA_EXP,
     "white-rice export BAN Jul-2023 + 20% duty on parboiled in force all year; mix skewed to parboiled/premium"),
    ("non-basmati rice", "export", "2024-25", 14128955, 55407.15, 6527.58, 3850,
     "paddy MSP 2369/0.67 + milling (3700-4000 band, 3850 used)", APEDA_EXP,
     "ban lifted Sep-2024 (MEP $490 briefly, scrapped Oct-2024); duties removed"),
    ("non-basmati rice", "export", "2025-26", 15044689, 51893.54, 5864.59, 3850,
     "paddy MSP 2369/0.67 + milling (3700-4000 band, 3850 used)", APEDA_EXP,
     "record volume, unit value fell with world prices; FY26 provisional"),
    ("wheat", "export", "2023-24", 188284, 470.83, 56.66, 2425,
     "MSP RMS 2025-26", APEDA_EXP,
     "export BAN since 13-May-2022 (govt-to-govt/NOC only); residual flows"),
    ("wheat", "export", "2024-25", 3566, 17.22, 2.03, 2425, "MSP RMS 2025-26", APEDA_EXP,
     "ban in force; negligible qty - unit value not meaningful"),
    ("wheat", "export", "2025-26", 31186, 92.42, 10.29, 2425, "MSP RMS 2025-26", APEDA_EXP,
     "ban in force; small NOC flows; FY26 provisional"),
    ("maize", "export", "2023-24", 1442671, 3660.10, 443.53, 2400,
     "MSP KMS 2025-26", APEDA_42H, "APEDA 42Head product report (maize separated from other cereals)"),
    ("maize", "export", "2024-25", 556417, 1705.93, 201.17, 2400, "MSP KMS 2025-26", APEDA_42H,
     "exports collapsed - domestic ethanol demand pushed mandi > world price; India net importer this year"),
    ("maize", "export", "2025-26", 1280761, 3357.53, 374.78, 2400, "MSP KMS 2025-26", APEDA_42H,
     "FY26 provisional"),
    ("millets", "export", "2023-24", 132985, 488.53, 58.94, 3699,
     "MSP KMS 2025-26 jowar-hybrid (proxy; bajra 2775, ragi 4886)", APEDA_42H,
     "APEDA 'Millet' product; MSP proxy - millet basket spans jowar/bajra/ragi"),
    ("millets", "export", "2024-25", 121365, 502.35, 59.20, 3699,
     "MSP KMS 2025-26 jowar-hybrid (proxy; bajra 2775, ragi 4886)", APEDA_42H, ""),
    ("millets", "export", "2025-26", 138689, 543.40, 61.57, 3699,
     "MSP KMS 2025-26 jowar-hybrid (proxy; bajra 2775, ragi 4886)", APEDA_42H, "FY26 provisional"),
    ("other coarse cereals (aggregate)", "export", "2023-24", 1596680, 4274.10, 517.65, None,
     "", APEDA_EXP, "DGCI&S 'OTHER CEREALS' principal commodity = maize+millets+barley etc; overlaps maize/millet rows"),
    ("other coarse cereals (aggregate)", "export", "2024-25", 704111, 2297.24, 270.88, None,
     "", APEDA_EXP, ""),
    ("other coarse cereals (aggregate)", "export", "2025-26", 1433070, 3983.73, 445.67, None,
     "", APEDA_EXP, "FY26 provisional"),
    ("pulses", "export", "2023-24", 594164, 5332.95, 644.01, None, "", APEDA_EXP,
     "export basket is mostly chickpea/kabuli & processed dals - not comparable to any single MSP"),
    ("pulses", "export", "2024-25", 730731, 6595.65, 778.17, None, "", APEDA_EXP, ""),
    ("pulses", "export", "2025-26", 974578, 8378.71, 947.33, None, "", APEDA_EXP, "FY26 provisional"),
    ("groundnut", "export", "2023-24", 680688, 7135.12, 860.70, 7263,
     "MSP KMS 2025-26 (in-shell; kernel-equiv ~10376 at 70% outturn)", APEDA_EXP,
     "exports mostly shelled kernels HS1202 - compare vs kernel-equivalent MSP"),
    ("groundnut", "export", "2024-25", 746315, 6728.41, 794.99, 7263,
     "MSP KMS 2025-26 (in-shell; kernel-equiv ~10376 at 70% outturn)", APEDA_EXP, ""),
    ("groundnut", "export", "2025-26", 663818, 6092.22, 690.93, 7263,
     "MSP KMS 2025-26 (in-shell; kernel-equiv ~10376 at 70% outturn)", APEDA_EXP, "FY26 provisional"),
    ("sugar", "export", "2023-24", 4360622, 23390.49, 2822.25, 3850,
     "ex-mill realisation 38-39 Rs/kg (MSP-sugar 3100)", APEDA_EXP,
     "exports restricted from Oct-2023 (quota nil in 2023-24 season); FY qty includes early-FY shipments"),
    ("sugar", "export", "2024-25", 3687792, 18287.50, 2159.40, 3850,
     "ex-mill realisation 38-39 Rs/kg (MSP-sugar 3100)", APEDA_EXP,
     "10 LMT export quota allowed Jan-2025 for 2024-25 season"),
    ("sugar", "export", "2025-26", 4248792, 18464.98, 2087.35, 3850,
     "ex-mill realisation 38-39 Rs/kg (MSP-sugar 3100)", APEDA_EXP, "FY26 provisional"),

    # ---------------- IMPORTS ----------------
    ("pulses (all)", "import", "2023-24", 4775311, 31307.05, 3772.04, None, "", APEDA_IMP,
     "APEDA import statement (DGCI&S); MT"),
    ("pulses (all)", "import", "2024-25", 7343820, 47002.12, 5545.52, None, "", APEDA_IMP,
     "record import year"),
    ("pulses (all)", "import", "2025-26", 6044494, 32312.23, 3631.47, None, "", APEDA_IMP,
     "FY26 provisional"),
    ("tur/pigeon pea", "import", "2023-24", 771025, 6595.02, 794.58, 8000, "MSP KMS 2025-26", APEDA_HS,
     "HS 07136000; imports duty-free (exemption extended to 31-Mar-2026)"),
    ("tur/pigeon pea", "import", "2024-25", 1223293, 10812.16, 1285.40, 8000, "MSP KMS 2025-26", APEDA_HS, ""),
    ("tur/pigeon pea", "import", "2025-26", 1483348, 8394.45, 947.07, 8000, "MSP KMS 2025-26", APEDA_HS,
     "FY26 provisional; import parity fell WELL below MSP as world prices eased"),
    ("urad", "import", "2023-24", 624222, 5500.10, 662.62, 7800, "MSP KMS 2025-26", APEDA_HS,
     "HS 07133110 (Vigna mungo); duty-free to 31-Mar-2026"),
    ("urad", "import", "2024-25", 820259, 7630.90, 902.14, 7800, "MSP KMS 2025-26", APEDA_HS, ""),
    ("urad", "import", "2025-26", 1050511, 7792.29, 880.37, 7800, "MSP KMS 2025-26", APEDA_HS, "FY26 provisional"),
    ("masur/lentil", "import", "2023-24", 1676095, 10657.74, 1285.04, 6700, "MSP RMS 2025-26", APEDA_HS,
     "HS 07134000; 10% import duty re-imposed Mar-2025"),
    ("masur/lentil", "import", "2024-25", 1219290, 7785.69, 916.03, 6700, "MSP RMS 2025-26", APEDA_HS, ""),
    ("masur/lentil", "import", "2025-26", 1146929, 5900.97, 659.72, 6700, "MSP RMS 2025-26", APEDA_HS, "FY26 provisional"),
    ("yellow peas", "import", "2023-24", 1169210, 4776.43, 574.67, 5650,
     "gram MSP RMS 2025-26 (substitute; peas have no MSP)", APEDA_HS,
     "HS 07131010; duty-free window opened Dec-2023"),
    ("yellow peas", "import", "2024-25", 2164583, 8093.91, 960.58, 5650,
     "gram MSP RMS 2025-26 (substitute; peas have no MSP)", APEDA_HS, "peak duty-free inflow"),
    ("yellow peas", "import", "2025-26", 1111743, 3517.89, 397.66, 5650,
     "gram MSP RMS 2025-26 (substitute; peas have no MSP)", APEDA_HS,
     "30% duty re-imposed 01-Nov-2025 (reversing duty-free window); FY26 provisional"),
    ("desi chana", "import", "2023-24", 163992, 929.18, 111.64, 5650, "MSP RMS 2025-26", APEDA_HS,
     "HS 07132020; duty-free May-2024 to Mar-2025, 10% duty from 01-Apr-2025"),
    ("desi chana", "import", "2024-25", 1506023, 9605.95, 1116.64, 5650, "MSP RMS 2025-26", APEDA_HS, ""),
    ("desi chana", "import", "2025-26", 1006601, 4844.96, 535.86, 5650, "MSP RMS 2025-26", APEDA_HS, "FY26 provisional"),
    ("moong", "import", "2025-26", 75, None, 0.07, 8768, "MSP KMS 2025-26", APEDA_HS,
     "HS 07133190; imports negligible (75 t) - India self-sufficient in moong; INR value below source rounding"),
    ("wheat", "import", "2023-24", 103601, 312.43, 37.66, 2425, "MSP RMS 2025-26", APEDA_IMP,
     "40% import duty in force; niche specialty imports only"),
    ("wheat", "import", "2024-25", 125462, 369.01, 43.49, 2425, "MSP RMS 2025-26", APEDA_IMP, ""),
    ("wheat", "import", "2025-26", 84434, 241.68, 27.57, 2425, "MSP RMS 2025-26", APEDA_IMP, "FY26 provisional"),
    ("maize", "import", "2023-24", 137094, 320.86, 38.66, 2400, "MSP KMS 2025-26", APEDA_IMP,
     "50% MFN duty; 5-LMT TRQ at 15% opened 2024-25 for ethanol-driven deficit"),
    ("maize", "import", "2024-25", 970070, 2189.16, 259.81, 2400, "MSP KMS 2025-26", APEDA_IMP,
     "TRQ year - India became net maize importer"),
    ("maize", "import", "2025-26", 58978, 200.09, 22.86, 2400, "MSP KMS 2025-26", APEDA_IMP, "FY26 provisional"),
    ("vegetable oils (all)", "import", "2023-24", 15520478, 123078.72, 14859.25, None, "", APEDA_PC,
     "DGCI&S principal commodity; ~57% of domestic consumption imported"),
    ("vegetable oils (all)", "import", "2024-25", 16409657, 146449.67, 17333.14, None, "", APEDA_PC, ""),
    ("vegetable oils (all)", "import", "2025-26", 16939819, 172200.31, 19488.41, None, "", APEDA_PC, "FY26 provisional"),
    ("crude palm oil", "import", "2023-24", 6782450, 51641.46, 6236.07, None, "", TRADESTAT,
     "HS 15111000; BCD 0-5.5% eff. till Sep-2024"),
    ("crude palm oil", "import", "2024-25", 6101000, 53960.87, 6402.12, None, "", TRADESTAT,
     "20% BCD (27.5% eff.) from 14-Sep-2024"),
    ("crude palm oil", "import", "2025-26", 8174911, 80151.61, 9052.91, None, "", TRADESTAT,
     "BCD cut to 10% (16.5% eff.) 30-May-2025; FY26 provisional"),
    ("RBD palmolein", "import", "2023-24", 2115550, 15850.78, 1915.25, None, "", TRADESTAT,
     "HS 15119020; refined duty 12.5-13.75% eff. till Sep-2024"),
    ("RBD palmolein", "import", "2024-25", 1705280, 15163.30, 1796.73, None, "", TRADESTAT,
     "32.5% BCD (35.75% eff.) from Sep-2024"),
    ("RBD palmolein", "import", "2025-26", 342549, 3219.66, 371.93, None, "", TRADESTAT,
     "wide crude-refined duty gap collapsed refined imports; FY26 provisional"),
    ("crude soybean oil", "import", "2023-24", 3128570, 27229.77, 3294.05, None, "", TRADESTAT, "HS 15071000"),
    ("crude soybean oil", "import", "2024-25", 4519920, 39451.15, 4662.24, None, "", TRADESTAT, ""),
    ("crude soybean oil", "import", "2025-26", 4710588, 46350.25, 5256.81, None, "", TRADESTAT, "FY26 provisional"),
    ("crude sunflower oil", "import", "2023-24", 3268410, 26318.81, 3180.09, None, "", TRADESTAT, "HS 15121110"),
    ("crude sunflower oil", "import", "2024-25", 3505490, 30987.52, 3665.95, None, "", TRADESTAT, ""),
    ("crude sunflower oil", "import", "2025-26", 2682132, 28798.32, 3254.83, None, "", TRADESTAT, "FY26 provisional"),
]

with open(OUT, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["commodity", "flow", "fy", "qty_lmt", "value_inr_cr", "value_usd_mn",
                "value_unit", "unit_value_usd_per_t", "unit_value_inr_per_qtl", "fx_rate",
                "domestic_ref_price_inr_per_qtl", "ref_price_type", "parity_gap_pct",
                "source", "note"])
    for (com, flow, fy, qty_t, inr_cr, usd_mn, ref, reftype, src, note) in ROWS:
        qty_lmt = round(qty_t / 1e5, 3)
        uv_usd = round(usd_mn * 1e6 / qty_t, 1) if usd_mn and qty_t else ""
        uv_inr_qtl = round(inr_cr * 1e7 / (qty_t * 10), 0) if inr_cr and qty_t else ""
        fx = round(inr_cr * 10 / usd_mn, 2) if (inr_cr and usd_mn) else ""
        gap = round((uv_inr_qtl - ref) / ref * 100, 1) if (ref and uv_inr_qtl != "") else ""
        w.writerow([com, flow, fy, qty_lmt, inr_cr if inr_cr else "", usd_mn,
                    "Rs crore + USD million", uv_usd, uv_inr_qtl,
                    fx if fx else "(implied source rate n/a)", ref if ref else "",
                    reftype, gap, src, note])
print("wrote", OUT)
