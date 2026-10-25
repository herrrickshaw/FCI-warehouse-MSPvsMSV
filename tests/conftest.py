import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"


def load(name):
    spec = importlib.util.spec_from_file_location(name, DATA / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_copy(name, tmp_path):
    """Run a print-and-write script from a temp copy so its outputs land in tmp."""
    dst = tmp_path / f"{name}.py"
    shutil.copy(DATA / f"{name}.py", dst)
    res = subprocess.run([sys.executable, "-I", str(dst)], cwd=tmp_path,
                         capture_output=True, text=True, check=True)
    return res.stdout
