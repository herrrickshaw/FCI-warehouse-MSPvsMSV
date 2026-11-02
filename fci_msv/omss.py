#!/usr/bin/env python3
"""OMSS/grain processing unit economics -> business returns.

All prices Rs/qtl unless noted. Conversion ratios & byproduct values from
published milling norms (FCI CMR outturn 67% rice; roller-flour ~76% atta/maida
+ ~22% bran; conservative). This is a DETERMINISTIC unit-economics model, not a
forecast -- every input is labelled with its source vintage.
"""
from __future__ import annotations

from collections.abc import Sequence

from fci_msv.units import RS_PER_CRORE

# ---- WHEAT -> ATTA (roller flour mill buying OMSS wheat), Rs/qtl ----
WHEAT_OMSS_RS_QTL = 2550  # OMSS(D) reserve price 2025-26 (repo: haryana brief)
WHEAT_MANDI_RS_QTL = 2500  # mandi median 23-Jul-2026 (repo: mandi_vs_msp)
# outturn per 100 kg wheat: 76 kg atta/maida/suji + 22 kg bran (2 kg loss)
ATTA_YIELD, WHEAT_BRAN_YIELD = 0.76, 0.22
ATTA_PRICE_RS_QTL = 3300  # wholesale atta ~Rs 33/kg (Bharat Atta MRP 27.5; open ~30-34)
WHEAT_BRAN_PRICE_RS_QTL = 1900  # wheat bran (feed) ~Rs 19/kg
PROC_COST_WHEAT_RS_QTL = 180  # milling+power+packing+labour ~Rs 1.8/kg (industry est.)
WHEAT_PRODUCTS: tuple[tuple[float, float], ...] = (
    (ATTA_YIELD, ATTA_PRICE_RS_QTL),
    (WHEAT_BRAN_YIELD, WHEAT_BRAN_PRICE_RS_QTL),
)

# ---- PADDY/RICE -> milled rice, Rs/qtl paddy ----
PADDY_MANDI_RS_QTL = 2385  # mandi median 23-Jul-2026
RICE_YIELD = 0.67  # CMR outturn
RICE_BRAN_YIELD, HUSK_YIELD = 0.08, 0.22
RICE_WHOLESALE_RS_QTL = 3400  # common milled rice ~Rs 34/kg wholesale
RICE_BRAN_PRICE_RS_QTL = 2200
HUSK_PRICE_RS_QTL = 300
PROC_COST_PADDY_RS_QTL = 150
CMR_FEE_RS_QTL = 15  # Rs/qtl milling charge (repo: Haryana brief, +bonus) -- plus retains bran/husk
RICE_PRODUCTS: tuple[tuple[float, float], ...] = (
    (RICE_YIELD, RICE_WHOLESALE_RS_QTL),
    (RICE_BRAN_YIELD, RICE_BRAN_PRICE_RS_QTL),
    (HUSK_YIELD, HUSK_PRICE_RS_QTL),
)

# ---- SCALE: a mid-size roller flour mill ----
MILL_TPD = 300  # tonnes/day
MILL_DAYS = 300  # operating days/yr
MILL_THROUGHPUT_QTL = MILL_TPD * MILL_DAYS * 10  # 90,000 t/yr = 900,000 qtl
MILL_CAPEX_RS = 50e7  # ~Rs 40-60 cr for a 300 TPD mill
MILL_WORKING_CAPITAL_RS = 30e7  # ~Rs 30 cr


def mill_econ(grain_cost: float, yields_prices: Sequence[tuple[float, float]], proc: float) -> tuple[float, float, float]:
    """Per-quintal (revenue, gross margin, EBITDA) for grain at ``grain_cost`` Rs/qtl.

    ``yields_prices`` is (yield fraction, product price Rs/qtl) per product.
    """
    revenue = sum(y * p for y, p in yields_prices)
    gross = revenue - grain_cost
    ebitda = gross - proc
    return revenue, gross, ebitda


def wheat_atta_cases() -> list[dict[str, float]]:
    """OMSS-sourced vs mandi-sourced wheat -> atta economics, Rs/qtl."""
    out = []
    for label, wcost in (("OMSS-sourced", WHEAT_OMSS_RS_QTL), ("mandi-sourced", WHEAT_MANDI_RS_QTL)):
        rev, gr, eb = mill_econ(wcost, WHEAT_PRODUCTS, PROC_COST_WHEAT_RS_QTL)
        out.append({"label": label, "grain": wcost, "revenue": rev, "gross": gr, "ebitda": eb})
    return out


def paddy_open_market() -> dict[str, float]:
    """Miller buying paddy at mandi: revenue and EBITDA per qtl paddy."""
    rev = sum(y * p for y, p in RICE_PRODUCTS)
    return {"paddy": PADDY_MANDI_RS_QTL, "revenue": rev, "ebitda": rev - PADDY_MANDI_RS_QTL - PROC_COST_PADDY_RS_QTL}


def paddy_cmr() -> dict[str, float]:
    """Custom milling for government: fixed fee + retained byproducts, Rs/qtl paddy."""
    byproduct = RICE_BRAN_YIELD * RICE_BRAN_PRICE_RS_QTL + HUSK_YIELD * HUSK_PRICE_RS_QTL
    return {"fee": CMR_FEE_RS_QTL, "byproduct": byproduct, "total": CMR_FEE_RS_QTL + byproduct}


def flour_mill_business() -> dict[str, float]:
    """Scale the OMSS wheat case to a 300 TPD mill: annual EBITDA, revenue, ROCE."""
    revenue_qtl, _, eb_qtl = mill_econ(WHEAT_OMSS_RS_QTL, WHEAT_PRODUCTS, PROC_COST_WHEAT_RS_QTL)
    annual_ebitda = eb_qtl * MILL_THROUGHPUT_QTL
    revenue_annual = revenue_qtl * MILL_THROUGHPUT_QTL
    capital = MILL_CAPEX_RS + MILL_WORKING_CAPITAL_RS
    return {
        "ebitda_qtl": eb_qtl,
        "annual_ebitda": annual_ebitda,
        "revenue_annual": revenue_annual,
        "margin_pct": annual_ebitda / revenue_annual * 100,
        "capital_employed": capital,
        "roce_pct": annual_ebitda / capital * 100,
    }


def render() -> list[str]:
    """Human-readable report lines (the CLI output)."""
    lines = []
    for c in wheat_atta_cases():
        lines.append(
            f"WHEAT->ATTA {c['label']}: grain {c['grain']} | revenue {c['revenue']:.0f}"
            f" | gross {c['gross']:.0f} | EBITDA {c['ebitda']:.0f}/qtl ({c['ebitda'] / c['revenue'] * 100:.1f}% margin)"
        )
    om = paddy_open_market()
    lines.append(
        f"PADDY->RICE open-market: paddy {om['paddy']} | revenue {om['revenue']:.0f}"
        f" | EBITDA {om['ebitda']:.0f}/qtl ({om['ebitda'] / om['revenue'] * 100:.1f}% margin)"
    )
    cm = paddy_cmr()
    lines.append(
        f"PADDY->RICE custom-milling(CMR): fee {cm['fee']} + byproducts {cm['byproduct']:.0f}"
        f" = {cm['total']:.0f}/qtl paddy (no price risk, govt owns grain)"
    )
    b = flour_mill_business()
    lines.append("\n--- SCALE: 300 TPD flour mill (90,000 t/yr) ---")
    lines.append(
        f"throughput 900,000 qtl/yr | EBITDA/qtl {b['ebitda_qtl']:.0f}"
        f" | annual EBITDA Rs {b['annual_ebitda'] / RS_PER_CRORE:.1f} cr"
        f" | revenue Rs {b['revenue_annual'] / RS_PER_CRORE:.0f} cr | margin {b['margin_pct']:.1f}%"
    )
    lines.append(
        f"capital employed ~Rs {b['capital_employed'] / RS_PER_CRORE:.0f} cr (capex 50 + WC 30)"
        f" | ROCE ~{b['roce_pct']:.0f}%"
    )
    return lines


def main() -> None:
    """CLI entry point: print the unit-economics report."""
    print("\n".join(render()))


if __name__ == "__main__":
    main()
