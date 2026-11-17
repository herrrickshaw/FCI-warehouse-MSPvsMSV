"""Smoke + hand-check tests for the print-only scenario scripts, run from temp copies."""
import csv
import re

import pytest

from conftest import run_copy


def test_biodiesel_pool_and_conversion_constants(tmp_path):
    out = run_copy("biodiesel_blending_scenarios", tmp_path)
    # 91.4 MMT / 0.832 kg/L = 109.86 bn L = 10,986 crore L
    assert "Diesel pool: 91.4 MMT = 110 bn L = 10986 cr L/yr" in out
    assert "B5 needs 549 cr L" in out


def test_biodiesel_b5_share_of_edible_oil_stated_correctly(tmp_path):
    """B5 = 549 cr L / 10.8 cr L per LMT = ~51 LMT of oil = ~20% of a 250 LMT
    edible-oil supply. The script printed a hard-coded '~1/3'."""
    out = run_copy("biodiesel_blending_scenarios", tmp_path)
    assert "~51 LMT" in out
    assert "1/3" not in out


def test_omss_wheat_atta_unit_economics(tmp_path):
    out = run_copy("omss_processing_model", tmp_path)
    # revenue = 0.76*3300 + 0.22*1900 = 2926 ; gross = 2926-2550 = 376 ; EBITDA = 196
    assert "WHEAT->ATTA OMSS-sourced: grain 2550 | revenue 2926 | gross 376 | EBITDA 196/qtl" in out


def test_rbo_govt_bran_share(tmp_path):
    out = run_copy("rbo_savings_scenarios", tmp_path)
    # 98 * 832/2045 = 39.87 LMT, 41%
    assert "Govt-touchable bran: 40 LMT (41% of 98 LMT all-India)" in out


def test_consolidated_savings_total(tmp_path):
    out = run_copy("consolidated_savings_by_crop", tmp_path)
    rows = list(csv.DictReader(open(tmp_path / "consolidated_savings_by_crop.csv")))
    rbo = next(r for r in rows if r["product"] == "Rice bran oil (edible)")
    # 7.7 LMT * 1e5 t * 1107 USD/t * 88.5 / 1e7 = 7,544 Rs cr
    assert int(rbo["potential_save_rs_cr"]) == 7544
    zero = next(r for r in rows if r["product"] == "Fortified atta (PDS)")
    assert int(zero["potential_save_rs_cr"]) == 0
    total = sum(int(r["potential_save_rs_cr"]) for r in rows)
    m = re.search(r"illustrative\):\s+([\d,]+) Rs cr", out)
    assert abs(int(m.group(1).replace(",", "")) - total) <= len(rows)   # rounding only
