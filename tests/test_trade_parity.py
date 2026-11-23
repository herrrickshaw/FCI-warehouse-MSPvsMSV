"""data/build_trade_parity.py: derived unit values, implied FX and parity gap in the generated CSV."""
import csv

import pytest

from conftest import run_script


@pytest.fixture
def built(repo, capsys):
    g = run_script("build_trade_parity")
    with open(repo / "data/trade_price_parity.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    return g, rows, capsys.readouterr().out


def row(rows, commodity, flow, fy):
    (r,) = [r for r in rows if (r["commodity"], r["flow"], r["fy"]) == (commodity, flow, fy)]
    return r


def test_output_location_header_and_row_count(built, repo):
    g, rows, out = built
    assert out.strip() == f"wrote {repo / 'data/trade_price_parity.csv'}"
    assert len(rows) == len(g["ROWS"]) == 67
    assert list(rows[0]) == ["commodity", "flow", "fy", "qty_lmt", "value_inr_cr", "value_usd_mn", "value_unit", "unit_value_usd_per_t",
                             "unit_value_inr_per_qtl", "fx_rate", "domestic_ref_price_inr_per_qtl", "ref_price_type", "parity_gap_pct", "source", "note"]
    assert {r["flow"] for r in rows} == {"export", "import"} and {r["fy"] for r in rows} == {"2023-24", "2024-25", "2025-26"}
    assert all(r["value_unit"] == "Rs crore + USD million" for r in rows)


def test_basmati_export_derivations(built):
    _, rows, _ = built
    r = row(rows, "basmati rice", "export", "2025-26")
    assert r["qty_lmt"] == "65.218"                                                    # 6521797 t / 1e5, 3 dp
    assert r["unit_value_usd_per_t"] == str(round(5672.77 * 1e6 / 6521797, 1))
    uv = round(50137.13 * 1e7 / (6521797 * 10), 0)
    assert r["unit_value_inr_per_qtl"] == str(uv)
    assert r["fx_rate"] == str(round(50137.13 * 10 / 5672.77, 2))
    assert r["domestic_ref_price_inr_per_qtl"] == "3850" and r["parity_gap_pct"] == str(round((uv - 3850) / 3850 * 100, 1))
    assert r["source"].endswith("GenerateExportStatement/Index") and r["note"] == "FY26 full-year provisional DGCI&S"


def test_fx_matches_the_fiscal_year_rates_in_the_docstring(built):
    _, rows, _ = built
    for fy, lo, hi in (("2023-24", 82.0, 83.5), ("2024-25", 84.0, 85.6), ("2025-26", 88.0, 89.0)):
        fx = float(row(rows, "basmati rice", "export", fy)["fx_rate"])
        assert lo < fx < hi


def test_rows_without_reference_price_have_blank_gap(built):
    _, rows, _ = built
    for commodity, flow in (("pulses", "export"), ("vegetable oils (all)", "import"), ("crude palm oil", "import"), ("other coarse cereals (aggregate)", "export")):
        r = row(rows, commodity, flow, "2025-26")
        assert r["domestic_ref_price_inr_per_qtl"] == "" and r["ref_price_type"] == "" and r["parity_gap_pct"] == ""
        assert r["unit_value_inr_per_qtl"] != ""


def test_moong_row_without_inr_value(built):
    _, rows, _ = built
    r = row(rows, "moong", "import", "2025-26")
    assert r["value_inr_cr"] == "" and r["unit_value_inr_per_qtl"] == "" and r["parity_gap_pct"] == ""      # no INR value -> no gap
    assert r["fx_rate"] == "(implied source rate n/a)" and r["unit_value_usd_per_t"] == str(round(0.07 * 1e6 / 75, 1)) and r["qty_lmt"] == "0.001"
    assert r["domestic_ref_price_inr_per_qtl"] == "8768"


def test_import_parity_gap_signs(built):
    _, rows, _ = built
    tur = row(rows, "tur/pigeon pea", "import", "2025-26")
    assert float(tur["unit_value_inr_per_qtl"]) < 8000 and float(tur["parity_gap_pct"]) < 0           # imports landed below MSP
    pep = row(rows, "yellow peas", "import", "2024-25")
    assert float(pep["parity_gap_pct"]) == round((round(8093.91 * 1e7 / (2164583 * 10), 0) - 5650) / 5650 * 100, 1)


def test_all_numeric_columns_parse_and_are_positive(built):
    _, rows, _ = built
    for r in rows:
        assert float(r["qty_lmt"]) > 0 and float(r["value_usd_mn"]) > 0
        if r["value_inr_cr"]:
            assert float(r["value_inr_cr"]) > 0 and float(r["fx_rate"]) > 70
