"""data/*.py scenario models: they print their results (and some write a CSV beside themselves), so each is run end to end
as ``__main__`` inside a sandbox and its numbers are checked against hand calculations."""
import csv
import math

import pytest

from conftest import run_script


def out_lines(capsys):
    return capsys.readouterr().out.splitlines()


# ================================================================== rfii_monitor
def test_rfii_function_matches_formula(load):
    R = load("rfii_monitor")
    assert R.rfii("2016-17") == pytest.approx(8059 / 8059 / (877 / 869) * 100)
    assert R.rfii("2021-22") == pytest.approx((13661 / 8059) / (1125 / 869) * 100)
    assert R.rfii("2024-25", income=9000) == pytest.approx((9000 / 8059) / (1320 / 869) * 100)           # explicit income overrides the table
    with pytest.raises(TypeError):
        R.rfii("2015-16")                                          # CPI exists, income does not (None / int)
    with pytest.raises(KeyError):
        R.rfii("1999-00", income=1)
    assert R.BASE_INC == R.INCOME["2016-17"] and R.BASE_CPI == R.CPI_AL["2015-16"] and R.TARGET == 200


def test_rfii_report(capsys):
    run_script("rfii_monitor")
    out = out_lines(capsys)
    assert out[0].split() == ["year", "₹/mo", "CPI-AL", "RFII", "gap", "to", "200"]
    rows = {l.split()[0]: l.split() for l in out[1:4]}
    assert rows["2016-17"][1:] == ["8,059", "877", "99.1", "100.9"]
    assert rows["2021-22"][1] == "13,661"
    last = (13661 / 8059) / (1125 / 869) * 100
    assert f"{last:.1f}" == rows["2021-22"][3]
    assert any(l.startswith("Cumulative CPI-AL inflation since 2015-16: +52%") for l in out)
    years = math.log(200 / last) / math.log(1.057)
    assert f"Last MEASURED RFII (2021-22): {last:.1f} → doubling (200) ~{2022 + round(years)} at 5.7%/yr real" in out
    assert out[-1].startswith("REAL doubling status: NOT met")


# ================================================================== consolidated_savings_by_crop
def test_consolidated_savings(capsys):
    g = run_script("consolidated_savings_by_crop")
    with open("consolidated_savings_by_crop.csv", newline="") as f:
        rows = list(csv.reader(f))
    assert rows[0][:6] == ["crop_stream", "product", "import_usd_per_t", "import_inr_per_t", "subst_volume_lmt", "potential_save_rs_cr"]
    assert len(rows) == 1 + len(g["R"]) == 17
    rbo = next(r for r in rows if r[1] == "Rice bran oil (edible)")
    assert rbo[2:6] == ["1107", str(round(1107 * 88.5)), "7.7", str(round(7.7 * 1e5 * 1107 * 88.5 / 1e7))]
    assert next(r for r in rows if r[1] == "Fortified atta (PDS)")[5] == "0"                           # no import price -> zero saving
    assert next(r for r in rows if r[1] == "Corn gluten meal")[5] == "0"
    expected_total = sum(v * 1e5 * u * 88.5 / 1e7 for _, _, u, v, _, _ in g["R"] if u)
    assert g["tot"] == pytest.approx(expected_total)
    out = out_lines(capsys)
    total_line = next(l for l in out if l.startswith("TOTAL potential"))
    assert total_line.rstrip().endswith(f"{expected_total:,.0f} Rs cr/yr")
    assert out[0].split()[:3] == ["crop/stream", "product", "imp"] and out[-1] == "written data/consolidated_savings_by_crop.csv"
    assert int(rbo[5]) == round(7.7 * 1e5 * 1107 * 88.5 / 1e7) and g["FX"] == 88.5


# ================================================================== omss_processing_model
def test_omss_model(capsys):
    g = run_script("omss_processing_model")
    rev, gross, ebitda = g["mill_econ"](2550, [(0.76, 3300), (0.22, 1900)], 180)
    assert rev == pytest.approx(0.76 * 3300 + 0.22 * 1900) and gross == pytest.approx(rev - 2550) and ebitda == pytest.approx(gross - 180)
    assert g["mill_econ"](100, [], 0) == (0, -100, -100)
    out = out_lines(capsys)
    assert out[0] == "WHEAT->ATTA OMSS-sourced: grain 2550 | revenue 2926 | gross 376 | EBITDA 196/qtl (6.7% margin)"
    assert out[1] == "WHEAT->ATTA mandi-sourced: grain 2500 | revenue 2926 | gross 426 | EBITDA 246/qtl (8.4% margin)"
    rice_rev = 0.67 * 3400 + 0.08 * 2200 + 0.22 * 300
    assert out[2] == f"PADDY->RICE open-market: paddy 2385 | revenue {rice_rev:.0f} | EBITDA {rice_rev - 2385 - 150:.0f}/qtl ({(rice_rev - 2385 - 150) / rice_rev * 100:.1f}% margin)"
    byp = 0.08 * 2200 + 0.22 * 300
    assert out[3] == f"PADDY->RICE custom-milling(CMR): fee 15 + byproducts {byp:.0f} = {15 + byp:.0f}/qtl paddy (no price risk, govt owns grain)"
    annual = 196 * 900000
    assert any(l.startswith("throughput 900,000 qtl/yr | EBITDA/qtl 196 | annual EBITDA Rs 17.6 cr | revenue Rs 263 cr | margin 6.7%") for l in out)
    roce = annual / (80e7) * 100
    assert out[-1] == f"capital employed ~Rs 80 cr (capex 50 + WC 30) | ROCE ~{roce:.0f}%"


# ================================================================== rbo_savings_scenarios
def test_rbo_scenarios(capsys):
    g = run_script("rbo_savings_scenarios")
    assert g["cr"](1.0, 100) == pytest.approx(1000.0)                                                             # 1 LMT = 1e8 kg; x Rs100/kg = Rs 1e10 = 1,000 crore
    assert g["GOVT_BRAN_SHARE"] == pytest.approx(832 / 2045) and g["BRAN_GOVT"] == pytest.approx(98 * 832 / 2045)
    out = out_lines(capsys)
    assert out[0] == f"Govt-touchable bran: {98 * 832 / 2045:.0f} LMT ({832 / 2045 * 100:.0f}% of 98 LMT all-India)"
    assert "=== GOVERNMENT CMR bran: 40 LMT ===" in out and "=== ALL-INDIA bran: 98 LMT ===" in out
    rows100 = [l for l in out if l.strip().startswith("100%")]
    govt = 98 * 832 / 2045
    assert rows100[0].split()[:3] == ["100%", f"{govt:.1f}", f"{govt * 0.16:.1f}"]
    row100 = rows100[1]
    oil = 98 * 0.16
    cr = lambda lmt, rs: lmt * 1e5 * 1000 * rs / 1e7
    assert row100.split() == ["100%", "98.0", f"{oil:.1f}", f"{cr(oil, 105):,.0f}", f"{cr(oil, 45):,.0f}", f"{cr(98 * 0.78, 15):,.0f}"]
    incr_oil = (98 - 50) * 0.16
    assert any(l.startswith(f"INCREMENTAL (the ~48 LMT bran now going to CATTLE FEED, not oil):") for l in out)
    assert f"  -> +{incr_oil:.1f} LMT RBO -> Rs {cr(incr_oil, 105):,.0f} cr import displaced (~{cr(incr_oil, 105) / 165000 * 100:.0f}% of ~Rs1.65 L-cr oil bill)" in out
    assert f"Full RBO potential: {98 * 0.16:.1f} LMT. Demand floors that absorb it:" in out
    assert sum(1 for l in out if l.startswith("  * ")) == 5


# ================================================================== biodiesel_blending_scenarios
def test_biodiesel_scenarios(capsys):
    g = run_script("biodiesel_blending_scenarios")
    diesel_cr_l = 91.4 / 0.832 * 100
    assert g["DIESEL_CR_L"] == pytest.approx(diesel_cr_l)
    out = out_lines(capsys)
    assert out[0] == f"Diesel pool: 91.4 MMT = {91.4 / 0.832:.0f} bn L = {diesel_cr_l:.0f} cr L/yr"
    assert out[1] == f"  B1 needs {diesel_cr_l * 0.01:.0f} cr L | B5 needs {diesel_cr_l * 0.05:.0f} cr L of biodiesel"
    rbo_now = 98 * 0.5 * 0.16
    rows = {l.split()[0]: l.split() for l in out if l.strip().endswith(tuple("0123456789")) and l.strip()[0].isdigit() and "%" in l.split()[0]}
    r50 = rows["50%"]
    assert r50[1] == f"{98 * 0.5 * 0.16:.1f}" and r50[2] == "+0.0" and r50[3] == "0"                              # 50% utilisation == today's extraction: nothing incremental
    r100 = rows["100%"]
    rbo = 98 * 0.16
    assert r100[2] == f"{rbo - rbo_now:+.1f}"
    assert r100[3] == f"{(rbo - rbo_now) * 100_000 * 1000 * 105 / 1e7:,.0f}"
    assert r100[4] == f"{rbo * 0.1:.2f}" and r100[5] == f"{rbo * 0.1 * 10.8:.1f}" and r100[6] == f"B{rbo * 0.1 * 10.8 / diesel_cr_l * 100:.2f}"
    assert f"  100% bran, whole RBO->biodiesel: {rbo * 10.8:.0f} cr L = B{rbo * 10.8 / diesel_cr_l * 100:.1f}  (absurd: displaces cooking oil India imports)" in out
    acid = rbo * 0.1
    assert f"  rice acid oil {acid:.2f} + UCO 4.0 + tallow 1.5 = {acid + 5.5:.1f} LMT lipid" in out
    assert any(l.startswith(f"  -> {(acid + 5.5) * 10.8:.0f} cr L biodiesel = B{(acid + 5.5) * 10.8 / diesel_cr_l * 100:.2f}") for l in out)
    assert f"  B5 needs ~{diesel_cr_l * 0.05:.0f} cr L biodiesel = ~{diesel_cr_l * 0.05 / 10.8:.0f} LMT of oil feedstock" in out
    assert f"  183.0 LMT husk -> ~{183 * 100_000 * 0.5 / 1000:,.0f} GWh/yr potential (power the extraction/esterification + grid/silica)" in out
