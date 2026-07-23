#!/usr/bin/env python3
"""
Holding economics of Indian agri commodities: does 1-3+ year storage beat carrying cost?

Inputs (same directory):
  wpi_commodity_monthly.csv  - OEA WPI (base 2011-12=100), monthly, Apr-2012..Apr-2026
  msp_series.csv             - CACP MSP series, crop years 2010-11..2026-27

Outputs:
  holding_economics_summary.csv  - commodity x window: price CAGR vs carry cost, verdict
  holding_horizon_returns.csv    - per-commodity 12/24/36-month harvest-buy return distributions
  holding_episodes.csv           - opportunistic (post-crash) episode-level outcomes

Carrying-cost model (all rates cited in report/holding-economics.md):
  storage  : CWC "Commodity-wise tariff FY 2024-25" (cewacor.nic.in), rate per 50-kg
             bag-equivalent per month in PAISE, class-C warehouse column (mid of A..K).
             Rs/qtl/month = paise * 2 / 100.
  insurance: CWC circular - Rs 0.05 per Rs 100 of stock value per month (0.6%/yr)
             where tariff is "Excl Ins." (pulses/oilseeds); foodgrain tariffs incl. insurance.
  interest : SBI Produce Marketing Loan against e-NWR, 1-yr MCLR + 0.80% -> ~9.8%/yr
             (base case 10%; other WHRs go to MCLR+3.60% ~12.6%).
  losses   : 0.5%/yr scientific covered storage (base), 1.0%/yr conservative
             (DFPD SOP 03.01.2022 fixes FCI storage loss/gain norms; FCI actual storage
             loss on rice now ~0.07%/yr; CAP and unscientific storage far worse).
Value per quintal for %-of-value conversion = latest MSP (crop year 2025-26); sugar uses
Rs 3,500/qtl (between Rs 3,100 Minimum Selling Price fixed Feb-2019 and ~Rs 3,700-4,000
ex-mill 2024-25) - flagged as an assumption.
"""
import pandas as pd
import numpy as np
from pathlib import Path

HERE = Path(__file__).resolve().parent

INTEREST = 0.10          # p.a., on commodity value (SBI PML e-NWR ~9.8%; band 9.8-12.6%)
LOSS = 0.005             # p.a., physical loss, covered scientific storage (band 0.5-1.0%)
INSURANCE_PM = 0.0005    # 0.05 per 100 value per month, where tariff excludes insurance

# storage Rs/qtl/month  (CWC FY24-25 commodity tariff, class C, 50kg-bag-equivalent)
# (commodity, storage Rs/qtl/mo, insurance_included?, value Rs/qtl, harvest trough month)
MODEL = {
    #                 st_rs   ins_inc  value   trough
    'paddy':          (19.40, True,   2369, 11),  # KMS 2025-26 MSP; kharif arrival Nov
    'rice_nonbasmati':(17.46, True,   3536, 11),  # paddy MSP / 0.67 out-turn (derived)
    'wheat':          (13.98, True,   2585, 4),   # RMS 2026-27 MSP; arrival Apr
    'maize':          (16.00, True,   2400, 11),
    'jowar':          (16.00, True,   3699, 11),
    'bajra':          (16.00, True,   2775, 10),
    'arhar_tur':      (17.12, False,  8000, 1),   # tur harvest Jan-Feb
    'gram':           (17.12, False,  5875, 4),   # rabi, arrival Mar-Apr
    'moong':          (17.12, False,  8768, 10),
    'urad':           (17.12, False,  7800, 10),
    'masur':          (17.12, False,  7000, 4),
    'rajma':          (17.12, False,  9000, 1),   # no MSP; mandi ~Rs 85-110/kg -> flagged
    'mustard_seed':   (15.38, False,  6200, 3),   # RMS 2026-27 MSP; arrival Mar
    'soybean':        (16.00, False,  5328, 11),
    'groundnut_seed': (26.48, False,  7263, 11),  # CWC groundnut-kernels rate
    'sugar':          (16.00, False,  3500, 12),  # value assumption, see docstring
}


def annual_carry_pct(c):
    st, ins_inc, val, _ = MODEL[c]
    storage = st * 12 / val
    insurance = 0.0 if ins_inc else INSURANCE_PM * 12
    return 100 * (storage + insurance + INTEREST + LOSS), 100 * storage


def load():
    wpi = pd.read_csv(HERE / 'wpi_commodity_monthly.csv')
    wpi['date'] = pd.to_datetime(wpi['date'])
    wide = wpi.pivot_table(index='date', columns='commodity', values='index').sort_index()
    return wide


def cagr(series, years):
    end = series.dropna().iloc[-1]
    end_dt = series.dropna().index[-1]
    start_dt = end_dt - pd.DateOffset(years=years)
    s = series.dropna()
    s = s[s.index <= start_dt]
    if s.empty:
        return np.nan
    start = s.iloc[-1]
    n = (end_dt - s.index[-1]).days / 365.25
    return 100 * ((end / start) ** (1 / n) - 1)


def horizon_returns(series, trough_month, months):
    """Buy every year in the harvest trough month, sell `months` later."""
    s = series.dropna()
    out = []
    for dt, v in s.items():
        if dt.month != trough_month:
            continue
        sell_dt = dt + pd.DateOffset(months=months)
        w = s[(s.index >= sell_dt - pd.Timedelta(days=16)) & (s.index <= sell_dt + pd.Timedelta(days=16))]
        if w.empty:
            continue
        out.append({'buy_date': dt.strftime('%Y-%m'), 'ret_pct': 100 * (w.iloc[0] / v - 1)})
    return pd.DataFrame(out)


def crash_episodes(series, carry_pa, months_hold=24, crash_thresh=-0.10):
    """Opportunistic: enter after trailing-12m fall <= -10%, hold `months_hold`.
    Success = nominal return beats compounded carry over the holding period.
    Non-overlapping episodes (skip forward past each entry's holding window)."""
    s = series.dropna()
    r12 = s / s.shift(12) - 1
    eps, i = [], 0
    idx = list(s.index)
    while i < len(idx):
        dt = idx[i]
        if pd.notna(r12.get(dt)) and r12[dt] <= crash_thresh:
            sell_dt = dt + pd.DateOffset(months=months_hold)
            w = s[(s.index >= sell_dt - pd.Timedelta(days=16)) & (s.index <= sell_dt + pd.Timedelta(days=16))]
            if not w.empty:
                gross = 100 * (w.iloc[0] / s[dt] - 1)
                hurdle = 100 * ((1 + carry_pa / 100) ** (months_hold / 12) - 1)
                eps.append({'entry': dt.strftime('%Y-%m'), 'trailing_12m_pct': round(100 * r12[dt], 1),
                            'gross_ret_pct': round(gross, 1), 'carry_hurdle_pct': round(hurdle, 1),
                            'net_pct': round(gross - hurdle, 1), 'paid_off': gross > hurdle})
            i += months_hold  # non-overlapping
        else:
            i += 1
    return pd.DataFrame(eps)


def main():
    wide = load()
    comms = [c for c in MODEL if c in wide.columns]
    summary, hz_rows, ep_rows = [], [], []

    for c in comms:
        s = wide[c]
        carry, storage_pct = annual_carry_pct(c)
        for label, yrs in [('5y', 5), ('10y', 10), ('14y_full', 14)]:
            g = cagr(s, yrs)
            summary.append({'commodity': c, 'window': label,
                            'price_cagr_pct': round(g, 2),
                            'carry_cost_pct': round(carry, 2),
                            'storage_component_pct': round(storage_pct, 2),
                            'net_annual_pct': round(g - carry, 2),
                            'verdict': 'HOLD PAYS' if g - carry > 0 else 'CARRY EXCEEDS APPRECIATION'})
        for m in (12, 24, 36):
            hr = horizon_returns(s, MODEL[c][3], m)
            if hr.empty:
                continue
            ann_carry_h = 100 * ((1 + carry / 100) ** (m / 12) - 1)
            hz_rows.append({'commodity': c, 'horizon_months': m, 'n_years': len(hr),
                            'mean_ret_pct': round(hr.ret_pct.mean(), 1),
                            'median_ret_pct': round(hr.ret_pct.median(), 1),
                            'min_ret_pct': round(hr.ret_pct.min(), 1),
                            'max_ret_pct': round(hr.ret_pct.max(), 1),
                            'pct_positive': round(100 * (hr.ret_pct > 0).mean(), 0),
                            'carry_hurdle_pct': round(ann_carry_h, 1),
                            'pct_beat_carry': round(100 * (hr.ret_pct > ann_carry_h).mean(), 0),
                            'mean_net_pct': round(hr.ret_pct.mean() - ann_carry_h, 1)})
        ep = crash_episodes(s, carry)
        if not ep.empty:
            ep.insert(0, 'commodity', c)
            ep_rows.append(ep)

    pd.DataFrame(summary).to_csv(HERE / 'holding_economics_summary.csv', index=False)
    pd.DataFrame(hz_rows).to_csv(HERE / 'holding_horizon_returns.csv', index=False)
    eps = pd.concat(ep_rows, ignore_index=True) if ep_rows else pd.DataFrame()
    eps.to_csv(HERE / 'holding_episodes.csv', index=False)

    print('=== summary (14y window) ===')
    sm = pd.DataFrame(summary)
    print(sm[sm.window == '14y_full'].to_string(index=False))
    print('\n=== horizon returns ===')
    print(pd.DataFrame(hz_rows).to_string(index=False))
    if not eps.empty:
        print('\n=== opportunistic episodes: pay-off fraction ===')
        print(eps.groupby('commodity').agg(n=('paid_off', 'size'), paid=('paid_off', 'sum'),
                                           mean_net=('net_pct', 'mean')).to_string())


if __name__ == '__main__':
    main()
