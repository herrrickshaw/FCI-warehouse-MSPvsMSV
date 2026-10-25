import pytest

from conftest import load

rf = load("rfii_monitor")


def test_rfii_formula_hand_computed():
    # (13661/8059) / (1125/869) * 100
    assert rf.rfii("2021-22") == pytest.approx((13661 / 8059) / (1125 / 869) * 100)


def test_rfii_accepts_override_income():
    assert rf.rfii("2018-19", income=8059 * 950 / 869) == pytest.approx(100.0)


def test_rfii_unknown_year_raises():
    with pytest.raises((KeyError, TypeError)):
        rf.rfii("2030-31")
