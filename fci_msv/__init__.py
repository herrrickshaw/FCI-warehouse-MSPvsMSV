"""Deterministic scenario and unit-economics models behind the MSP-vs-MSV reports.

Each module is a pure computation layer (constants with units, functions that take
data in and return data out) plus a small ``main()`` used by the thin entry-point
scripts in ``data/``.  Nothing here fetches live data.
"""
from __future__ import annotations

__all__ = [
    "biodiesel",
    "consolidated_savings",
    "holding",
    "omss",
    "paths",
    "rbo",
    "rfii",
    "trade_parity",
    "units",
]
