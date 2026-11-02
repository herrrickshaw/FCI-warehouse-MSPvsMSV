"""Unit constants shared by the scenario models.

Indian agri statistics mix LMT (lakh metric tonnes), crore rupees and
Rs/kg; these helpers keep the conversions in one place.
"""
from __future__ import annotations

LMT_TO_TONNES = 100_000  # 1 lakh metric tonnes = 1e5 t
TONNES_TO_KG = 1_000
RS_PER_CRORE = 1e7  # 1 crore = 1e7
RS_PER_LAKH_CRORE = 1e5  # crore per lakh-crore


def lmt_at_rs_per_kg_to_crore(qty_lmt: float, rs_per_kg: float) -> float:
    """Value of ``qty_lmt`` LMT priced at ``rs_per_kg`` Rs/kg, in Rs crore."""
    return qty_lmt * LMT_TO_TONNES * TONNES_TO_KG * rs_per_kg / RS_PER_CRORE
