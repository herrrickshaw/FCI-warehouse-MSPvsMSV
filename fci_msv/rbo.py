#!/usr/bin/env python3
"""RBO extraction savings across scenarios of rice-volume processed + demand-security.

Grounded: all-India bran ~98 LMT (verified ~9.8 MT); govt CMR paddy 832 LMT (KMS24-25);
oil yield 16%; import parity Rs105/kg; ex-mill Rs60/kg (DORB credit); DORB Rs15/kg.
"""
from __future__ import annotations

from collections.abc import Iterable

from fci_msv.units import lmt_at_rs_per_kg_to_crore as cr

BRAN_ALLINDIA_LMT = 98.0  # LMT total rice bran [verified]
PADDY_GOVT_LMT = 832.0  # LMT govt-procured paddy [verified]
PADDY_ALLINDIA_LMT = 2045.0  # LMT (rice 1370 / 0.67) [derived]
GOVT_BRAN_SHARE = PADDY_GOVT_LMT / PADDY_ALLINDIA_LMT  # govt's share of the bran
BRAN_GOVT_LMT = BRAN_ALLINDIA_LMT * GOVT_BRAN_SHARE  # govt-touchable bran, LMT
OIL_YIELD = 0.16  # bran -> crude RBO
DORB_YIELD = 0.78  # ~78% of bran -> de-oiled rice bran
PARITY_RS_PER_KG = 105  # Rs/kg import parity
EXMILL_RS_PER_KG = 60  # Rs/kg RBO ex-mill (with DORB credit)
DORB_PRICE_RS_PER_KG = 15  # Rs/kg de-oiled bran (feed)
BRAN_NOW_EXT_LMT = 50.0  # LMT bran already oil-extracted nationally [verified ~50%]
EDIBLE_OIL_IMPORT_BILL_RS_CR = 165_000  # ~Rs 1.65 lakh crore/yr

PROCESSED_SHARES = (0.25, 0.50, 0.75, 1.00)
BASES: tuple[tuple[str, float], ...] = (
    ("GOVERNMENT CMR bran", BRAN_GOVT_LMT),
    ("ALL-INDIA bran", BRAN_ALLINDIA_LMT),
)
DEMAND_CHANNELS: tuple[tuple[str, str], ...] = (
    ("Food processing (frying/snacks/bakery/HoReCa)",
     "high smoke pt 232C + oryzanol = superior frying oil; price-inelastic industrial demand"),
    ("Blend/fortification (Saffola-type + Vit A/D mandate)",
     "RBO-blend positioning; a fortification mandate can require inclusion"),
    ("Institutional (PDS/ICDS/mid-day-meal fortified oil)",
     "state offtake backstop, mirrors Bharat-brand"),
    ("Export (premium health oil)", "India already exports RBO; global oryzanol demand"),
    ("Byproduct (DORB->feed, acid oil->soap/oleochem)",
     "always-in-demand feed + oleochemical floor"),
)


def scenario(bran_base_lmt: float, pct: float) -> dict[str, float]:
    """Economics of extracting ``pct`` of a bran base (LMT); money in Rs crore."""
    bran = bran_base_lmt * pct
    oil = bran * OIL_YIELD
    dorb = bran * DORB_YIELD
    return {
        "pct": pct,
        "bran_lmt": bran,
        "oil_lmt": oil,
        "import_displaced_rs_cr": cr(oil, PARITY_RS_PER_KG),
        "net_margin_rs_cr": cr(oil, PARITY_RS_PER_KG - EXMILL_RS_PER_KG),
        "dorb_feed_rs_cr": cr(dorb, DORB_PRICE_RS_PER_KG),
    }


def scenarios(bran_base_lmt: float, shares: Iterable[float] = PROCESSED_SHARES) -> list[dict[str, float]]:
    """Scenario table for one bran base across processed shares."""
    return [scenario(bran_base_lmt, p) for p in shares]


def incremental() -> dict[str, float]:
    """Gain from the bran that currently goes to cattle feed instead of oil."""
    incr_bran = BRAN_ALLINDIA_LMT - BRAN_NOW_EXT_LMT
    incr_oil = incr_bran * OIL_YIELD
    displaced = cr(incr_oil, PARITY_RS_PER_KG)
    return {
        "bran_lmt": incr_bran,
        "oil_lmt": incr_oil,
        "import_displaced_rs_cr": displaced,
        "share_of_import_bill_pct": displaced / EDIBLE_OIL_IMPORT_BILL_RS_CR * 100,
        "net_gain_rs_cr": cr(incr_oil, PARITY_RS_PER_KG - EXMILL_RS_PER_KG),
        "dorb_feed_rs_cr": cr(incr_bran * DORB_YIELD, DORB_PRICE_RS_PER_KG),
    }


def render() -> list[str]:
    """Human-readable report lines (the CLI output)."""
    lines = [
        f"Govt-touchable bran: {BRAN_GOVT_LMT:.0f} LMT ({GOVT_BRAN_SHARE * 100:.0f}% of"
        f" {BRAN_ALLINDIA_LMT:.0f} LMT all-India)\n"
    ]
    for base_name, bran_base in BASES:
        lines.append(f"=== {base_name}: {bran_base:.0f} LMT ===")
        lines.append(
            f"{'% processed':>12}{'bran LMT':>10}{'RBO LMT':>9}{'imp displ':>11}{'net margin':>11}{'DORB feed':>10}"
        )
        for s in scenarios(bran_base):
            lines.append(
                f"{s['pct'] * 100:>11.0f}%{s['bran_lmt']:>10.1f}{s['oil_lmt']:>9.1f}"
                f"{s['import_displaced_rs_cr']:>10,.0f}{s['net_margin_rs_cr']:>11,.0f}{s['dorb_feed_rs_cr']:>10,.0f}"
            )
        lines.append("")

    inc = incremental()
    lines.append(f"INCREMENTAL (the ~{inc['bran_lmt']:.0f} LMT bran now going to CATTLE FEED, not oil):")
    lines.append(
        f"  -> +{inc['oil_lmt']:.1f} LMT RBO -> Rs {inc['import_displaced_rs_cr']:,.0f} cr import displaced"
        f" (~{inc['share_of_import_bill_pct']:.0f}% of ~Rs1.65 L-cr oil bill)"
    )
    lines.append(
        f"  net economic gain Rs {inc['net_gain_rs_cr']:,.0f} cr + DORB feed Rs {inc['dorb_feed_rs_cr']:,.0f} cr\n"
    )

    lines.append("--- DEMAND-SECURITY LEVERS (if branded-consumer RBO demand softens) ---")
    total_rbo_potential = BRAN_ALLINDIA_LMT * OIL_YIELD
    lines.append(f"Full RBO potential: {total_rbo_potential:.1f} LMT. Demand floors that absorb it:")
    for channel, why in DEMAND_CHANNELS:
        lines.append(f"  * {channel}\n      {why}")
    return lines


def main() -> None:
    """CLI entry point: print the scenario report."""
    print("\n".join(render()))


if __name__ == "__main__":
    main()
