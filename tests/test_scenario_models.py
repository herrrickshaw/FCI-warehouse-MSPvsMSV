"""Characterisation tests: values captured from the pre-refactor scripts (2026-11)."""
from __future__ import annotations

import math
from pathlib import Path

import pytest

from fci_msv import biodiesel, omss, rbo, rfii

GOLDEN = Path(__file__).parent / "golden"


def golden(name: str) -> str:
    return (GOLDEN / f"{name}.stdout").read_text()


# ---- biodiesel ----------------------------------------------------------
def test_diesel_pool_denominators():
    assert round(biodiesel.DIESEL_BN_L) == 110
    assert round(biodiesel.DIESEL_CR_L) == 10986


def test_biodiesel_scenario_full_utilisation():
    s = biodiesel.scenario(1.0)
    assert s["rbo_lmt"] == pytest.approx(15.68)
    assert s["edible_incr_lmt"] == pytest.approx(7.84)
    assert s["import_save_rs_cr"] == pytest.approx(8232, abs=1)
    assert s["acid_oil_lmt"] == pytest.approx(1.568)
    assert s["biodiesel_cr_l"] == pytest.approx(16.93, abs=0.01)
    assert s["blend_pct"] == pytest.approx(0.154, abs=0.001)


def test_biodiesel_scenario_at_current_extraction_has_no_increment():
    s = biodiesel.scenario(biodiesel.BRAN_NOW_OILEXT)
    assert s["edible_incr_lmt"] == 0
    assert s["import_save_rs_cr"] == 0


def test_waste_basket_still_below_b1():
    wb = biodiesel.waste_basket()
    assert wb["basket_lmt"] == pytest.approx(7.07, abs=0.01)
    assert wb["biodiesel_cr_l"] / biodiesel.DIESEL_CR_L * 100 < 1.0


def test_biodiesel_render_matches_golden(capsys):
    biodiesel.main()
    assert capsys.readouterr().out == golden("biodiesel_blending_scenarios")


# ---- rbo ----------------------------------------------------------------
def test_rbo_govt_share():
    assert rbo.GOVT_BRAN_SHARE == pytest.approx(0.4068, abs=1e-4)
    assert rbo.BRAN_GOVT_LMT == pytest.approx(39.87, abs=0.01)


def test_rbo_all_india_full_processing():
    s = rbo.scenario(rbo.BRAN_ALLINDIA_LMT, 1.0)
    assert s["oil_lmt"] == pytest.approx(15.68)
    assert s["import_displaced_rs_cr"] == pytest.approx(16464)
    assert s["net_margin_rs_cr"] == pytest.approx(7056)
    assert s["dorb_feed_rs_cr"] == pytest.approx(11466)


def test_rbo_incremental():
    inc = rbo.incremental()
    assert inc["bran_lmt"] == 48.0
    assert inc["oil_lmt"] == pytest.approx(7.68)
    assert inc["import_displaced_rs_cr"] == pytest.approx(8064)
    assert round(inc["share_of_import_bill_pct"]) == 5


def test_rbo_render_matches_golden(capsys):
    rbo.main()
    assert capsys.readouterr().out == golden("rbo_savings_scenarios")


# ---- omss ---------------------------------------------------------------
def test_mill_econ_is_pure_arithmetic():
    assert omss.mill_econ(100, [(0.5, 300), (0.5, 100)], 20) == (200, 100, 80)


def test_wheat_atta_cases():
    omss_case, mandi_case = omss.wheat_atta_cases()
    assert omss_case["revenue"] == pytest.approx(2926)
    assert omss_case["ebitda"] == pytest.approx(196)
    assert mandi_case["ebitda"] == pytest.approx(246)


def test_paddy_cases():
    assert omss.paddy_open_market()["revenue"] == pytest.approx(2520)
    assert omss.paddy_open_market()["ebitda"] == pytest.approx(-15)
    assert omss.paddy_cmr()["total"] == pytest.approx(257)


def test_flour_mill_business():
    b = omss.flour_mill_business()
    assert b["annual_ebitda"] == pytest.approx(196 * 900_000)
    assert round(b["roce_pct"]) == 22


def test_omss_render_matches_golden(capsys):
    omss.main()
    assert capsys.readouterr().out == golden("omss_processing_model")


# ---- rfii ---------------------------------------------------------------
def test_rfii_last_measured_point():
    assert rfii.rfii("2021-22") == pytest.approx(130.9, abs=0.05)
    assert rfii.rfii("2016-17") == pytest.approx(99.1, abs=0.05)


def test_rfii_income_override():
    assert rfii.rfii("2021-22", income=2 * rfii.BASE_INCOME_RS_MONTH) == pytest.approx(
        200 / (rfii.CPI_AL["2021-22"] / rfii.BASE_CPI_AL)
    )


def test_years_to_target_projection():
    yrs = rfii.years_to_target(rfii.rfii("2021-22"))
    assert math.isclose(yrs, 7.64, abs_tol=0.01)
    assert rfii.LAST_MEASURED_YEAR_END + round(yrs) == 2030


def test_rfii_render_matches_golden(capsys):
    rfii.main()
    assert capsys.readouterr().out == golden("rfii_monitor")
