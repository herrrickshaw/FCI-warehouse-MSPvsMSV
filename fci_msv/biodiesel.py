#!/usr/bin/env python3
"""Rice husk+bran -> oil -> acid-oil -> biodiesel blending scenarios.

Answers: at different bran-utilisation levels, (a) how much edible RBO (import
substitution), (b) how much acid oil -> biodiesel, (c) what blend % (Bx) results.
Every constant labelled with source/basis. Deterministic, not a forecast.
"""
from __future__ import annotations

from collections.abc import Iterable

from fci_msv.units import lmt_at_rs_per_kg_to_crore

# ---- DENOMINATORS (verified) ----
DIESEL_MMT = 91.4  # India HSD consumption FY25 (PPAC), million t [verified]
DIESEL_DENSITY_KG_PER_L = 0.832  # kg/L -> diesel volume
DIESEL_BN_L = DIESEL_MMT * 1e9 / DIESEL_DENSITY_KG_PER_L / 1e9  # billion litres/yr
DIESEL_CR_L = DIESEL_BN_L * 100  # crore litres/yr

# ---- RICE BRAN STOCK (verified) ----
BRAN_TOTAL_LMT = 98.0  # total rice bran output potential, LMT [verified ~9.8 MT]
BRAN_NOW_OILEXT = 0.50  # ~50% currently solvent-extracted; rest -> cattle feed [verified]
OIL_YIELD = 0.16  # bran -> crude RBO, 16-18% [verified ~18%; 16% conservative whole-bran]
ACID_FRAC = 0.10  # crude RBO -> acid oil (FFA/soapstock) on refining, 8-12% [derived]
BD_PER_LMT_ACID = 10.8  # 1 LMT acid oil -> ~10.8 cr L biodiesel (0.95 conv, 0.88 dens) [derived]
IMPORT_PARITY_RS_PER_KG = 105  # Rs/kg landed palm/edible-oil parity [reported 100-110]
RBO_EXMILL_RS_PER_KG = 65  # Rs/kg domestic crude RBO ex-mill [reported 55-75]

# ---- NON-EDIBLE WASTE BASKET (LMT) ----
UCO_LMT = 4.0  # collectible used cooking oil [reported ~3-5 of ~30 generated]
TALLOW_LMT = 1.5  # animal fat/tallow [reported]
EDIBLE_OIL_SUPPLY_LMT = 250  # India's total edible-oil supply, approx

# ---- HUSK: energy enabler, NOT a blending feedstock ----
HUSK_TOTAL_LMT = 183.0  # ~22% of paddy at govt+all-India scale [derived]
HUSK_MWH_PER_T = 0.5  # ~0.5 MWh electricity per tonne husk [reported ~3000-3600 kcal/kg]

UTILISATION_LEVELS = (0.50, 0.60, 0.75, 0.90, 1.00)
B1, B5 = 0.01, 0.05  # blend fractions


def rbo_now_lmt() -> float:
    """Crude RBO already produced today (LMT) from the extracted half of the bran."""
    return BRAN_TOTAL_LMT * BRAN_NOW_OILEXT * OIL_YIELD


def scenario(util: float) -> dict[str, float]:
    """One bran-utilisation scenario; ``util`` is the fraction of total bran extracted."""
    bran_ext = BRAN_TOTAL_LMT * util
    rbo = bran_ext * OIL_YIELD  # total crude RBO, LMT
    edible_incr = max(rbo - rbo_now_lmt(), 0)  # incremental vs current, LMT
    imp_save = lmt_at_rs_per_kg_to_crore(edible_incr, IMPORT_PARITY_RS_PER_KG)  # Rs cr
    acid = rbo * ACID_FRAC  # acid oil, LMT
    biodsl = acid * BD_PER_LMT_ACID  # biodiesel, cr L (acid-oil-only, food-safe)
    blend = biodsl / DIESEL_CR_L * 100  # % blend
    return {
        "util": util,
        "rbo_lmt": rbo,
        "edible_incr_lmt": edible_incr,
        "import_save_rs_cr": imp_save,
        "acid_oil_lmt": acid,
        "biodiesel_cr_l": biodsl,
        "blend_pct": blend,
    }


def scenarios(levels: Iterable[float] = UTILISATION_LEVELS) -> list[dict[str, float]]:
    """Scenario table across bran-utilisation levels."""
    return [scenario(u) for u in levels]


def full_diversion_cr_l() -> float:
    """Biodiesel (cr L) if ALL crude RBO were burnt as fuel (not recommended)."""
    return BRAN_TOTAL_LMT * 1.0 * OIL_YIELD * BD_PER_LMT_ACID


def waste_basket() -> dict[str, float]:
    """Whole realistic non-edible lipid basket (rice acid oil + UCO + tallow)."""
    acid_100 = BRAN_TOTAL_LMT * OIL_YIELD * ACID_FRAC
    basket = acid_100 + UCO_LMT + TALLOW_LMT
    return {
        "acid_oil_lmt": acid_100,
        "basket_lmt": basket,
        "biodiesel_cr_l": basket * BD_PER_LMT_ACID,
    }


def b5_requirement() -> dict[str, float]:
    """Biodiesel (cr L) and oil feedstock (LMT) needed for a B5 blend."""
    need = DIESEL_CR_L * B5
    return {"biodiesel_cr_l": need, "oil_lmt": need / BD_PER_LMT_ACID}


def husk_energy_gwh() -> float:
    """Electricity potential (GWh/yr) of the national husk output."""
    return HUSK_TOTAL_LMT * 100_000 * HUSK_MWH_PER_T / 1000


def render() -> list[str]:
    """Human-readable report lines (the CLI output)."""
    lines = [
        f"Diesel pool: {DIESEL_MMT} MMT = {DIESEL_BN_L:.0f} bn L = {DIESEL_CR_L:.0f} cr L/yr",
        f"  B1 needs {DIESEL_CR_L * B1:.0f} cr L | B5 needs {DIESEL_CR_L * B5:.0f} cr L of biodiesel\n",
        f"{'bran util':>10}{'RBO LMT':>9}{'edible+':>9}{'imp save':>10}{'acidoil':>9}{'biodsl':>9}{'blend':>8}",
        f"{'(% stock)':>10}{'(total)':>9}{'vs now':>9}{'Rs cr':>10}{'LMT':>9}{'cr L':>9}{'level':>8}",
    ]
    for s in scenarios():
        blend_label = "B" + format(s["blend_pct"], ".2f")
        lines.append(
            f"{s['util'] * 100:>9.0f}%{s['rbo_lmt']:>9.1f}{s['edible_incr_lmt']:>+9.1f}"
            f"{s['import_save_rs_cr']:>10,.0f}{s['acid_oil_lmt']:>9.2f}{s['biodiesel_cr_l']:>9.1f}"
            f"{blend_label:>8}"
        )

    bd_full = full_diversion_cr_l()
    lines.append("\n--- If ALL crude RBO diverted to fuel (NOT recommended, burns edible oil) ---")
    lines.append(
        f"  100% bran, whole RBO->biodiesel: {bd_full:.0f} cr L = B{bd_full / DIESEL_CR_L * 100:.1f}"
        "  (absurd: displaces cooking oil India imports)"
    )

    wb = waste_basket()
    lines.append("\n--- To reach B1 / B5 from the WHOLE realistic non-edible waste basket ---")
    lines.append(
        f"  rice acid oil {wb['acid_oil_lmt']:.2f} + UCO {UCO_LMT} + tallow {TALLOW_LMT}"
        f" = {wb['basket_lmt']:.1f} LMT lipid"
    )
    lines.append(
        f"  -> {wb['biodiesel_cr_l']:.0f} cr L biodiesel"
        f" = B{wb['biodiesel_cr_l'] / DIESEL_CR_L * 100:.2f}  (still < B1)"
    )
    b5 = b5_requirement()
    lines.append(
        f"  B5 needs ~{b5['biodiesel_cr_l']:.0f} cr L biodiesel = ~{b5['oil_lmt']:.0f} LMT of oil feedstock"
    )
    lines.append(
        f"    = ~1/3 of India's entire ~{EDIBLE_OIL_SUPPLY_LMT} LMT edible-oil supply."
        " Physically impossible from waste alone."
    )

    lines.append("\n--- Husk (energy lever, does NOT blend into diesel) ---")
    lines.append(
        f"  {HUSK_TOTAL_LMT} LMT husk -> ~{husk_energy_gwh():,.0f} GWh/yr potential"
        " (power the extraction/esterification + grid/silica)"
    )
    lines.append("  Husk role = process-energy self-sufficiency + carbon credit, not a blend component.")
    return lines


def main() -> None:
    """CLI entry point: print the scenario report."""
    print("\n".join(render()))


if __name__ == "__main__":
    main()
