"""Smoke test: every `data/*.py` script still runs as a standalone entry point."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "biodiesel_blending_scenarios.py",
    "omss_processing_model.py",
    "rbo_savings_scenarios.py",
    "rfii_monitor.py",
]


@pytest.mark.parametrize("script", SCRIPTS)
def test_script_runs_from_any_cwd(script, tmp_path):
    r = subprocess.run([sys.executable, str(REPO / "data" / script)], cwd=tmp_path, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    assert r.stdout == (REPO / "tests" / "golden" / script.replace(".py", ".stdout")).read_text()
