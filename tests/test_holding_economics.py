import numpy as np
import pandas as pd
import pytest

from conftest import load

he = load("holding_economics")


def monthly(values, start="2012-04-01"):
    return pd.Series(values, index=pd.date_range(start, periods=len(values), freq="MS"), dtype=float)


def test_carry_foodgrain_tariff_includes_insurance():
    # paddy: 19.40 Rs/qtl/mo * 12 / 2369 = 9.827%; + 10% interest + 0.5% loss
    total, storage = he.annual_carry_pct("paddy")
    assert storage == pytest.approx(100 * 19.40 * 12 / 2369)
    assert total == pytest.approx(storage + 10 + 0.5)
    assert round(total, 2) == 20.33          # matches committed holding_economics_summary.csv


def test_carry_pulses_add_insurance_when_tariff_excludes_it():
    # tur: 17.12*12/8000 = 2.568% storage + 0.6% insurance + 10 + 0.5
    total, storage = he.annual_carry_pct("arhar_tur")
    assert storage == pytest.approx(2.568)
    assert total == pytest.approx(2.568 + 0.6 + 10.5)


def test_cagr_hand_computed_doubling_over_5_years():
    s = monthly(np.linspace(100, 200, 61))   # Apr-2012 .. Apr-2017, 100 -> 200
    assert he.cagr(s, 5) == pytest.approx(100 * (2 ** (1 / 5) - 1), rel=1e-3)


def test_cagr_nan_when_history_shorter_than_window():
    assert np.isnan(he.cagr(monthly([100.0] * 24), 5))


def test_horizon_returns_buy_trough_month_sell_later():
    vals = [100.0] * 36
    s = monthly(vals, start="2020-01-01")
    s[pd.Timestamp("2021-01-01")] = 110.0     # Jan-2020 buy, Jan-2021 sell: +10%
    hr = he.horizon_returns(s, trough_month=1, months=12)
    assert list(hr.buy_date) == ["2020-01", "2021-01"]   # 2022-01 has no sale date in range
    assert hr.ret_pct.iloc[0] == pytest.approx(10.0)
    assert hr.ret_pct.iloc[1] == pytest.approx(100 * (100 / 110 - 1))


def test_crash_episode_detected_and_non_overlapping():
    # 12 months at 100, crash to 85 (-15% y/y) for 3 months, then 100 for 30 months
    s = monthly([100.0] * 12 + [85.0] * 3 + [100.0] * 30, start="2015-01-01")
    eps = he.crash_episodes(s, carry_pa=10.0, months_hold=24)
    assert len(eps) == 1                     # later crash months skipped (non-overlapping)
    e = eps.iloc[0]
    assert e.entry == "2016-01"
    assert e.gross_ret_pct == pytest.approx(17.6)        # 100/85 - 1
    assert e.carry_hurdle_pct == pytest.approx(21.0)     # 1.1**2 - 1
    assert not e.paid_off


def test_summary_verdict_not_given_without_enough_history(tmp_path, monkeypatch):
    """A commodity whose WPI series is shorter than the window has cagr=NaN;
    'NaN - carry > 0' is False, so it was labelled CARRY EXCEEDS APPRECIATION."""
    dates = pd.date_range("2020-04-01", "2026-04-01", freq="MS")   # 6 years only
    pd.DataFrame({"date": dates, "commodity": "wheat",
                  "index": np.linspace(100, 160, len(dates))}).to_csv(
        tmp_path / "wpi_commodity_monthly.csv", index=False)
    monkeypatch.setattr(he, "HERE", tmp_path)
    he.main()
    out = pd.read_csv(tmp_path / "holding_economics_summary.csv")
    v10 = out[(out.commodity == "wheat") & (out.window == "10y")].iloc[0]
    assert v10.verdict != "CARRY EXCEEDS APPRECIATION"
    v5 = out[(out.commodity == "wheat") & (out.window == "5y")].iloc[0]
    assert v5.verdict in {"HOLD PAYS", "CARRY EXCEEDS APPRECIATION"}
