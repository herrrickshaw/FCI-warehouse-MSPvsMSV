"""The CSV builders must reproduce the tracked data files byte-for-byte (no live data)."""
from __future__ import annotations

import csv
from pathlib import Path

import pandas as pd
import pytest

from fci_msv import consolidated_savings, holding, trade_parity
from fci_msv.paths import DATA_DIR

GOLDEN = Path(__file__).parent / "golden"


def test_derive_row_basmati_2023_24():
    row = trade_parity.derive_row(trade_parity.ROWS[0])
    assert row[:4] == ["basmati rice", "export", "2023-24", 52.425]
    assert row[7] == 1113.4  # USD/t
    assert row[8] == 9230.0  # Rs/qtl
    assert row[9] == 82.9  # implied FX
    assert row[12] == 139.7  # parity gap %


def test_derive_row_handles_missing_inr_value():
    moong = next(r for r in trade_parity.ROWS if r[0] == "moong")
    row = trade_parity.derive_row(moong)
    assert row[4] == ""  # value_inr_cr blank
    assert row[8] == ""  # Rs/qtl blank
    assert row[9] == trade_parity.FX_NA
    assert row[12] == ""


def test_trade_parity_reproduces_tracked_csv(tmp_path):
    out = trade_parity.write_csv(tmp_path / "t.csv")
    assert out.read_bytes() == (DATA_DIR / "trade_price_parity.csv").read_bytes()
    assert len(trade_parity.build_rows()) == 67


def test_saving_rs_cr():
    assert consolidated_savings.saving_rs_cr(1107, 7.7) == pytest.approx(7544, abs=0.5)
    assert consolidated_savings.saving_rs_cr(0, 5.0) == 0


def test_consolidated_total():
    _, total = consolidated_savings.compute()
    assert round(total) == 21088


def test_consolidated_reproduces_tracked_csv_and_stdout(tmp_path, capsys):
    consolidated_savings.main(tmp_path / "c.csv")
    assert (tmp_path / "c.csv").read_bytes() == (DATA_DIR / "consolidated_savings_by_crop.csv").read_bytes()
    assert capsys.readouterr().out == (GOLDEN / "consolidated_savings_by_crop.stdout").read_text()


def test_annual_carry_pct_wheat():
    carry, storage = holding.annual_carry_pct("wheat")
    assert storage == pytest.approx(6.49, abs=0.01)
    assert carry == pytest.approx(16.99, abs=0.01)


def test_carry_hurdle_compounds():
    assert holding.carry_hurdle_pct(10, 24) == pytest.approx(21.0)


def test_cagr_on_synthetic_series():
    idx = pd.date_range("2015-01-01", periods=61, freq="MS")
    s = pd.Series([100 * 1.1 ** (i / 12) for i in range(61)], index=idx)
    assert holding.cagr(s, 5) == pytest.approx(10.0, abs=0.01)


def test_horizon_returns_synthetic():
    idx = pd.date_range("2015-01-01", periods=36, freq="MS")
    s = pd.Series(range(100, 136), index=idx)
    hr = holding.horizon_returns(s, trough_month=1, months=12)
    assert list(hr.buy_date) == ["2015-01", "2016-01"]
    assert hr.ret_pct.iloc[0] == pytest.approx(12.0)


def test_holding_reproduces_tracked_csvs_and_stdout(tmp_path, capsys):
    holding.main(out_dir=tmp_path)
    for name in (holding.SUMMARY_FILE, holding.HORIZON_FILE, holding.EPISODES_FILE):
        assert (tmp_path / name).read_bytes() == (DATA_DIR / name).read_bytes(), name
    assert capsys.readouterr().out == (GOLDEN / "holding_economics.stdout").read_text()
    with open(tmp_path / holding.SUMMARY_FILE) as f:
        assert sum(1 for _ in csv.reader(f)) == 1 + 16 * 3
