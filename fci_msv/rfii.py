#!/usr/bin/env python3
"""Real Farm Income Index (RFII) -- inflation-adjusted farmer-income monitor.

RFII = (nominal agri-household income / base income) / (CPI-AL / base CPI-AL) x 100
Base 2016-17 = 100.  Doubling-Farmers'-Income target = 200 (real).

Deflator: CPI-AL (Consumer Price Index for Agricultural Labourers) -- the farm household's
own cost-of-living basket, the correct real-income deflator.

REFRESH CADENCE:
  * CPI-AL (deflator): MONTHLY, from MoSPI dataset CPIALRL (base 1986-87, All-India,
    indicator_code=1 General Index, state_code=99). MCP: get_data('CPIALRL', {...}).
    Or data.gov.in / Labour Bureau CPI-AL release.
  * Nominal income: on each new income survey -- NSSO SAS (~5-yearly) or NABARD NAFIS.
    Between surveys the latest MEASURED point is 2021-22; anything later is a projection.

Edit the two dicts below when new prints land, then re-run.
"""
from __future__ import annotations

import math

# CPI-AL General Index, base 1986-87, All-India (MoSPI CPIALRL) -- update monthly
CPI_AL: dict[str, int] = {"2015-16": 869, "2016-17": 877, "2018-19": 950, "2021-22": 1125, "2024-25": 1320}
# Nominal agri-household income Rs/month (SAS 2012-13/2018-19; NAFIS 2016-17/2021-22) -- update on new survey
INCOME: dict[str, int] = {"2016-17": 8059, "2018-19": 10218, "2021-22": 13661}
BASE_INCOME_RS_MONTH = 8059  # NAFIS 2016-17
BASE_CPI_AL = 869  # 2015-16 print used as the deflator base
TARGET = 200  # real doubling
REAL_GROWTH_FACTOR = 1.057  # 1 + assumed real income growth per year (5.7%)
LAST_MEASURED_YEAR_END = 2022  # 2021-22 survey -> calendar anchor for the projection


def rfii(year: str, income: float | None = None) -> float:
    """RFII for a crop/survey year; ``income`` overrides the table value (Rs/month)."""
    inc = income or INCOME.get(year)
    return (inc / BASE_INCOME_RS_MONTH) / (CPI_AL[year] / BASE_CPI_AL) * 100


def series() -> list[tuple[str, float]]:
    """(year, RFII) for every measured income point, in table order."""
    return [(y, rfii(y)) for y in INCOME]


def years_to_target(last_rfii: float, growth_factor: float = REAL_GROWTH_FACTOR) -> float:
    """Years of compounding at ``growth_factor`` for ``last_rfii`` to reach TARGET."""
    return math.log(TARGET / last_rfii) / math.log(growth_factor)


def cumulative_inflation() -> float:
    """CPI-AL inflation from the base print to the latest print, as a fraction."""
    return CPI_AL["2024-25"] / BASE_CPI_AL - 1


def render() -> list[str]:
    """Human-readable report lines (the CLI output)."""
    lines = [f"{'year':<12}{'₹/mo':>10}{'CPI-AL':>8}{'RFII':>8}{'gap to 200':>12}"]
    pts = series()
    for y, v in pts:
        lines.append(f"{y:<12}{INCOME[y]:>10,}{CPI_AL[y]:>8}{v:>8.1f}{TARGET - v:>12.1f}")
    lines.append(f"\nCumulative CPI-AL inflation since 2015-16: {cumulative_inflation():+.0%} (the deflator)")
    last_year, last_val = pts[-1]
    yrs = years_to_target(last_val)
    lines.append(
        f"Last MEASURED RFII ({last_year}): {last_val:.1f} → doubling (200)"
        f" ~{LAST_MEASURED_YEAR_END + round(yrs)} at 5.7%/yr real"
    )
    lines.append("REAL doubling status: NOT met by the 2022-23 DFI deadline; ~a third of the way.")
    return lines


def main() -> None:
    """CLI entry point: print the RFII table."""
    print("\n".join(render()))


if __name__ == "__main__":
    main()
