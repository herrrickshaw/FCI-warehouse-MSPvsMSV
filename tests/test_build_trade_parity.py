import csv
from pathlib import Path

import pytest

from conftest import DATA, run_copy


@pytest.fixture(scope="module")
def rebuilt(tmp_path_factory):
    tmp = tmp_path_factory.mktemp("parity")
    run_copy("build_trade_parity", tmp)
    return list(csv.DictReader(open(tmp / "trade_price_parity.csv")))


def test_script_reproduces_committed_csv(rebuilt):
    committed = list(csv.DictReader(open(DATA / "trade_price_parity.csv")))
    assert rebuilt == committed


def test_tur_fy26_unit_values_hand_computed(rebuilt):
    r = next(x for x in rebuilt if x["commodity"] == "tur/pigeon pea" and x["fy"] == "2025-26")
    # 947.07 USD mn / 1,483,348 t ; 8394.45 Rs cr / 14,833,480 qtl ; vs MSP 8000
    assert float(r["unit_value_usd_per_t"]) == pytest.approx(638.5)
    assert float(r["unit_value_inr_per_qtl"]) == 5659
    assert float(r["parity_gap_pct"]) == pytest.approx(-29.3)
    assert float(r["fx_rate"]) == pytest.approx(88.64)
    assert float(r["qty_lmt"]) == pytest.approx(14.833)


def test_missing_inr_value_gives_blank_unit_value_and_gap(rebuilt):
    r = next(x for x in rebuilt if x["commodity"] == "moong")
    assert r["unit_value_inr_per_qtl"] == "" and r["parity_gap_pct"] == ""
    assert r["fx_rate"] == "(implied source rate n/a)"


def test_no_reference_price_gives_blank_gap(rebuilt):
    r = next(x for x in rebuilt if x["commodity"] == "crude palm oil")
    assert r["parity_gap_pct"] == "" and r["domestic_ref_price_inr_per_qtl"] == ""
