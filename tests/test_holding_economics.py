"""data/holding_economics.py: carrying-cost model, CAGR, harvest-month horizon returns and crash episodes on synthetic WPI series."""
import csv

import numpy as np
import pandas as pd
import pytest

from conftest import run_script


@pytest.fixture
def H(load):
    return load("holding_economics")


def monthly(values, start="2015-01-01"):
    idx = pd.date_range(start, periods=len(values), freq="MS")
    return pd.Series(values, index=idx, dtype=float)


# ------------------------------------------------------------------ carry cost
def test_annual_carry_pct_with_and_without_insurance(H):
    carry, storage = H.annual_carry_pct("paddy")                        # insurance included in the tariff
    assert storage == pytest.approx(100 * 19.40 * 12 / 2369)
    assert carry == pytest.approx(storage + 100 * (0.10 + 0.005))
    carry_g, storage_g = H.annual_carry_pct("gram")                     # tariff excludes insurance: + 0.05% a month
    assert storage_g == pytest.approx(100 * 17.12 * 12 / 5875)
    assert carry_g == pytest.approx(storage_g + 100 * (0.0005 * 12 + 0.10 + 0.005))
    assert set(H.MODEL) >= {"paddy", "wheat", "sugar", "rajma"} and len(H.MODEL) == 16


# ------------------------------------------------------------------ cagr
def test_cagr(H):
    s = monthly([100.0 * (1.1 ** (i / 12)) for i in range(121)])        # exactly +10% a year for 10 years
    assert H.cagr(s, 5) == pytest.approx(10.0, abs=0.05)
    assert H.cagr(s, 10) == pytest.approx(10.0, abs=0.05)
    assert np.isnan(H.cagr(s, 11))                                      # series is shorter than the window
    flat = monthly([50.0] * 40)
    assert H.cagr(flat, 2) == pytest.approx(0.0)
    gappy = monthly([100.0] * 14 + [np.nan, 121.0, np.nan])               # trailing NaNs are ignored: the last real print is the end point
    assert H.cagr(gappy, 1) == pytest.approx(100 * ((121 / 100) ** (1 / ((pd.Timestamp("2016-03-01") - pd.Timestamp("2015-03-01")).days / 365.25)) - 1))


# ------------------------------------------------------------------ horizon returns
def test_horizon_returns_buys_in_trough_month_only(H):
    s = monthly(list(range(100, 100 + 48)), "2020-01-01")               # +1 per month
    out = H.horizon_returns(s, trough_month=4, months=12)
    assert list(out.buy_date) == ["2020-04", "2021-04", "2022-04"]      # 2023-04 has no 12-month-later price
    assert out.ret_pct.iloc[0] == pytest.approx(100 * (115 / 103 - 1))
    assert out.ret_pct.iloc[1] == pytest.approx(100 * (127 / 115 - 1))
    out24 = H.horizon_returns(s, 4, 24)
    assert list(out24.buy_date) == ["2020-04", "2021-04"]
    assert H.horizon_returns(s, 4, 60).empty


def test_horizon_returns_skips_missing_sell_window(H):
    s = monthly([100.0] * 24, "2020-01-01")
    s = s.drop(pd.Timestamp("2021-04-01"))                              # the sell month is missing
    assert H.horizon_returns(s, 4, 12).empty
    s2 = monthly([100.0] * 36, "2020-01-01").drop(pd.Timestamp("2020-02-01"))
    assert list(H.horizon_returns(s2, 2, 12).buy_date) == ["2021-02"]                  # a missing BUY month is simply not a buy


# ------------------------------------------------------------------ crash episodes
def test_crash_episodes_thresholds_and_non_overlap(H):
    vals = [100.0] * 12 + [89.0] + [95.0] * 40                          # month 13 is -11% on a year earlier
    s = monthly(vals, "2020-01-01")
    eps = H.crash_episodes(s, carry_pa=10.0, months_hold=24)
    assert len(eps) == 1
    e = eps.iloc[0]
    assert e["entry"] == "2021-01" and e["trailing_12m_pct"] == -11.0
    assert e["gross_ret_pct"] == round(100 * (95 / 89 - 1), 1)
    assert e["carry_hurdle_pct"] == round(100 * (1.1 ** 2 - 1), 1) and e["net_pct"] == round(e["gross_ret_pct"] - e["carry_hurdle_pct"], 1)
    assert bool(e["paid_off"]) is False
    # a 10.5% fall qualifies, a 9.5% fall does not
    s2 = monthly([100.0] * 12 + [89.5] + [89.5] * 40, "2020-01-01")
    assert len(H.crash_episodes(s2, 10.0, 24)) == 1
    s3 = monthly([100.0] * 12 + [90.5] + [90.5] * 40, "2020-01-01")
    assert H.crash_episodes(s3, 10.0, 24).empty


def test_crash_episodes_paid_off_and_hold_months(H):
    s = monthly([100.0] * 12 + [80.0] + [80.0 + i for i in range(40)], "2020-01-01")
    eps = H.crash_episodes(s, carry_pa=5.0, months_hold=12)
    assert not eps.empty and bool(eps.iloc[0]["paid_off"]) is True
    assert eps.iloc[0]["carry_hurdle_pct"] == 5.0
    assert H.crash_episodes(monthly([100.0] * 30), 5.0).empty


def test_crash_episodes_without_sell_price_records_nothing(H):
    s = monthly([100.0] * 12 + [80.0] + [80.0] * 5, "2020-01-01")       # entry has no price 24 months later
    assert H.crash_episodes(s, 10.0, 24).empty


# ------------------------------------------------------------------ load + main
def write_wpi(repo, commodities, n=170):
    dates = pd.date_range("2012-04-01", periods=n, freq="MS")
    rows = []
    for k, c in enumerate(commodities):
        for i, d in enumerate(dates):
            rows.append({"date": d.strftime("%Y-%m-%d"), "commodity": c, "index": 100 + (k + 1) * i + (15 if i % 12 == 5 else 0)})
    pd.DataFrame(rows).to_csv(repo / "data/wpi_commodity_monthly.csv", index=False)


def test_load_pivots_wide(H, repo):
    write_wpi(repo, ["paddy", "wheat"], n=24)
    wide = H.load()
    assert list(wide.columns) == ["paddy", "wheat"] and len(wide) == 24 and wide.index.is_monotonic_increasing
    assert wide.loc["2012-04-01", "paddy"] == 100 and wide.loc["2012-05-01", "wheat"] == 102


def test_main_writes_three_csvs(repo, capsys):
    write_wpi(repo, ["paddy", "wheat", "not_in_model"])
    run_script("holding_economics")
    summ = pd.read_csv(repo / "data/holding_economics_summary.csv")
    assert set(summ.commodity) == {"paddy", "wheat"} and set(summ.window) == {"5y", "10y", "14y_full"} and len(summ) == 6
    p5 = summ[(summ.commodity == "paddy") & (summ.window == "5y")].iloc[0]
    carry = 100 * (19.40 * 12 / 2369 + 0.10 + 0.005)
    assert p5.carry_cost_pct == pytest.approx(round(carry, 2)) and p5.net_annual_pct == pytest.approx(round(p5.price_cagr_pct - round(carry, 2), 2), abs=0.011)
    assert p5.verdict == ("HOLD PAYS" if p5.price_cagr_pct - carry > 0 else "CARRY EXCEEDS APPRECIATION")
    hz = pd.read_csv(repo / "data/holding_horizon_returns.csv")
    assert set(hz.horizon_months) == {12, 24, 36} and set(hz.commodity) == {"paddy", "wheat"}
    row = hz[(hz.commodity == "paddy") & (hz.horizon_months == 24)].iloc[0]
    assert row.carry_hurdle_pct == round(100 * ((1 + carry / 100) ** 2 - 1), 1) and row.n_years >= 10
    assert row.min_ret_pct <= row.median_ret_pct <= row.max_ret_pct
    eps = repo / "data/holding_episodes.csv"
    assert eps.exists()
    out = capsys.readouterr().out
    assert "=== summary (14y window) ===" in out and "=== horizon returns ===" in out


def test_main_prints_episode_table_when_crashes_exist(repo, capsys):
    dates = pd.date_range("2012-04-01", periods=170, freq="MS")
    vals = [100.0 + (30 if (i // 18) % 2 == 0 else 0) - (i % 18) for i in range(170)]            # repeated sawtooth crashes
    pd.DataFrame({"date": dates.strftime("%Y-%m-%d"), "commodity": "wheat", "index": vals}).to_csv(repo / "data/wpi_commodity_monthly.csv", index=False)
    run_script("holding_economics")
    assert "=== opportunistic episodes: pay-off fraction ===" in capsys.readouterr().out
    eps = pd.read_csv(repo / "data/holding_episodes.csv")
    assert list(eps.columns)[:2] == ["commodity", "entry"] and set(eps.commodity) == {"wheat"}


def test_main_with_no_crash_episodes_writes_empty_file(repo, capsys):
    dates = pd.date_range("2012-04-01", periods=170, freq="MS")
    pd.DataFrame({"date": dates.strftime("%Y-%m-%d"), "commodity": "wheat", "index": np.linspace(100, 300, 170)}).to_csv(repo / "data/wpi_commodity_monthly.csv", index=False)
    run_script("holding_economics")
    assert "opportunistic episodes" not in capsys.readouterr().out
    assert (repo / "data/holding_episodes.csv").read_text().strip() in ("", '""')
