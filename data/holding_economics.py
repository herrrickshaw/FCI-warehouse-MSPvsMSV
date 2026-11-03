#!/usr/bin/env python3
"""Thin entry point kept for `python3 data/holding_economics.py`.

The model moved to `fci_msv.holding` (2026-11 refactor); edit it there.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fci_msv.holding import main  # noqa: E402

if __name__ == "__main__":
    main()
