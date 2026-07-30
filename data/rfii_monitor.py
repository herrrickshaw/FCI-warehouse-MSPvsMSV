#!/usr/bin/env python3
"""Real Farm Income Index (RFII) — inflation-adjusted farmer-income monitor.

RFII = (nominal agri-household income / base income) / (CPI-AL / base CPI-AL) x 100
Base 2016-17 = 100.  Doubling-Farmers'-Income target = 200 (real).

Deflator: CPI-AL (Consumer Price Index for Agricultural Labourers) — the farm household's
own cost-of-living basket, the correct real-income deflator.

REFRESH CADENCE:
  * CPI-AL (deflator): MONTHLY, from MoSPI dataset CPIALRL (base 1986-87, All-India,
    indicator_code=1 General Index, state_code=99). MCP: get_data('CPIALRL', {...}).
    Or data.gov.in / Labour Bureau CPI-AL release.
  * Nominal income: on each new income survey — NSSO SAS (~5-yearly) or NABARD NAFIS.
    Between surveys the latest MEASURED point is 2021-22; anything later is a projection.

Edit the two dicts below when new prints land, then re-run.
"""
# CPI-AL General Index, base 1986-87, All-India (MoSPI CPIALRL) — update monthly
CPI_AL = {'2015-16':869, '2016-17':877, '2018-19':950, '2021-22':1125, '2024-25':1320}
# Nominal agri-household income ₹/month (SAS 2012-13/2018-19; NAFIS 2016-17/2021-22) — update on new survey
INCOME = {'2016-17':8059, '2018-19':10218, '2021-22':13661}
BASE_INC, BASE_CPI, TARGET = 8059, 869, 200

def rfii(year, income=None):
    inc = income or INCOME.get(year)
    return (inc/BASE_INC) / (CPI_AL[year]/BASE_CPI) * 100

if __name__ == "__main__":
    print(f"{'year':<12}{'₹/mo':>10}{'CPI-AL':>8}{'RFII':>8}{'gap to 200':>12}")
    last=None
    for y in INCOME:
        v=rfii(y); last=(y,v)
        print(f"{y:<12}{INCOME[y]:>10,}{CPI_AL[y]:>8}{v:>8.1f}{200-v:>12.1f}")
    infl=CPI_AL['2024-25']/BASE_CPI-1
    print(f"\nCumulative CPI-AL inflation since 2015-16: {infl:+.0%} (the deflator)")
    import math
    yrs=math.log(TARGET/last[1])/math.log(1.057)
    print(f"Last MEASURED RFII ({last[0]}): {last[1]:.1f} → doubling (200) ~{2022+round(yrs)} at 5.7%/yr real")
    print("REAL doubling status: NOT met by the 2022-23 DFI deadline; ~a third of the way.")
