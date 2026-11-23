#!/usr/bin/env python3
"""Consolidated per-crop: import price/ton (DGCI&S) vs domestic processing margin vs
import-substitution savings, with the food-processing offtake channel.

Import unit values from data/trade_price_parity.csv (DGCI&S FY26). Rs/USD 88.5 (FY26 impl).
"""
from __future__ import annotations

import csv
import logging
from collections.abc import Iterable, Sequence
from pathlib import Path

from fci_msv.paths import DATA_DIR
from fci_msv.units import LMT_TO_TONNES, RS_PER_CRORE

log = logging.getLogger(__name__)

FX_RS_PER_USD = 88.5  # FY26 implied DGCI&S rate
DEFAULT_OUTPUT = DATA_DIR / "consolidated_savings_by_crop.csv"
HEADER = [
    "crop_stream", "product", "import_usd_per_t", "import_inr_per_t",
    "subst_volume_lmt", "potential_save_rs_cr", "domestic_margin_note", "food_processing_offtake",
]

# (crop, product, import_usd_t, subst_volume_lmt, dom_margin_note, offtake_channel)
# import_usd_t from trade_price_parity.csv (DGCI&S) or byproduct import price (verified)
InputRow = tuple[str, str, float, float, str, str]
ROWS: tuple[InputRow, ...] = (
    # OILS -----------------------------------------------------------------
    ("Rice→bran", "Rice bran oil (edible)", 1107, 7.7, "ex-mill Rs60 vs parity Rs105 = Rs45/kg + DORB feed", "Food processing: frying/snacks/HoReCa (232C smoke pt) + fortification mandate"),
    ("Oilseeds", "Mustard/groundnut oil", 1116, 0.0, "premium ~Rs136 vs palm Rs98; production-lever not in-yr", "Branded premium retail + food processing blends"),
    ("Cotton→seed", "Cottonseed oil", 1116, 2.0, "crush margin + meal byproduct", "Food processing + Vanaspati/HoReCa"),
    # PULSES (import price per ton, dal-processing margin) ------------------
    ("Pulses-tur", "Tur dal", 638, 5.0, "dal-milling margin ~8-12% + chuni feed", "Dal millers (NAFEX auction) + PDS pulse pilot"),
    ("Pulses-urad", "Urad dal", 838, 3.0, "dal-milling margin", "Dal millers + food processing (papad/snack)"),
    ("Pulses-masur", "Masur dal", 575, 4.0, "dal-milling margin", "Dal millers + institutional"),
    # WHEAT derivatives ----------------------------------------------------
    ("Wheat", "Vital wheat gluten", 1292, 0.13, "wet-mill gluten+starch; imports 13000 t/yr China 88%", "Food processing: bakery/meat-analogue/pet-food (captive)"),
    ("Wheat", "Wheat germ oil", 5000, 0.02, "high-value nutraceutical, wasted germ fraction", "Nutraceutical/cosmetic brands + export"),
    ("Wheat", "Fortified atta (PDS)", 0, 0.0, "captive PDS demand, no import", "Government PDS/ICDS (captive offtake)"),
    # RICE husk / bran high-value tail ------------------------------------
    ("Rice→husk", "Precipitated silica", 980, 1.0, "raw RHA Rs1-3.5 -> silica ~Rs40-90/kg, ~30x jump", "Tyre/industrial (45% tyre demand); import substitution"),
    ("Rice→bran", "Gamma oryzanol", 120000, 0.005, "global USD2.6bn; India mkt only USD6.5mn vs #1 RBO", "Nutraceutical/cosmetic export + fortification"),
    ("Rice→bran", "Tocotrienols/Vit-E", 200000, 0.004, "imports 60-70%; feedstock DD Rs45-75/kg domestic", "Fortification input (captive) + pharma"),
    # MAIZE ----------------------------------------------------------------
    ("Maize", "Starch/HFCS/sorbitol", 420, 3.0, "wet-milling; India imports refined derivatives", "Food/pharma/paper processing"),
    ("Maize", "Corn gluten meal", 500, 0.0, "60% protein; India EXPORTS to 25+ countries", "Feed export (already positive)"),
    # OILSEED meal / soy specialty ----------------------------------------
    ("Oilseeds", "Soy lecithin (specialty)", 1300, 0.2, "imports specialty grades; domestic feed-grade only", "Food processing emulsifier (captive)"),
    ("Oilseeds", "Soy/pea protein isolate", 3000, 0.3, "India exports some; plant-protein trend", "Food processing + export"),
)


def saving_rs_cr(usd_per_t: float, volume_lmt: float, fx: float = FX_RS_PER_USD) -> float:
    """Import-substitution saving (Rs crore/yr) for ``volume_lmt`` LMT priced at ``usd_per_t``."""
    inr_t = usd_per_t * fx
    return volume_lmt * LMT_TO_TONNES * inr_t / RS_PER_CRORE if usd_per_t else 0  # LMT*1e5 t * Rs/t / 1e7 = Rs cr


def savings_row(row: InputRow, fx: float = FX_RS_PER_USD) -> list[object]:
    """One output row: adds Rs/t import price and rounded potential saving (Rs crore/yr)."""
    crop, prod, usd_t, vol, margin, chan = row
    return [crop, prod, usd_t, round(usd_t * fx), vol, round(saving_rs_cr(usd_t, vol, fx)), margin, chan]


def compute(rows: Iterable[InputRow] = ROWS, fx: float = FX_RS_PER_USD) -> tuple[list[list[object]], float]:
    """(output rows, total potential saving in Rs crore/yr, unrounded)."""
    rows = list(rows)
    out = [savings_row(r, fx) for r in rows]
    total = 0.0
    for _crop, _prod, usd_t, vol, _margin, _chan in rows:
        total += saving_rs_cr(usd_t, vol, fx)
    return out, total


def render(rows: Sequence[InputRow] = ROWS, fx: float = FX_RS_PER_USD) -> list[str]:
    """Console table (the CLI output)."""
    lines = [
        f"{'crop/stream':<14}{'product':<24}{'imp Rs/t':>10}{'subst LMT':>10}{'save Rscr':>10}  offtake",
        "-" * 120,
    ]
    for crop, prod, usd_t, vol, _margin, chan in rows:
        lines.append(
            f"{crop:<14}{prod:<24}{usd_t * fx:>10,.0f}{vol:>10.2f}{saving_rs_cr(usd_t, vol, fx):>10,.0f}  {chan[:44]}"
        )
    _, total = compute(rows, fx)
    lines.append("-" * 120)
    lines.append(f"{'TOTAL potential import-substitution savings (illustrative):':<58}{total:>10,.0f} Rs cr/yr")
    lines.append("  (edible-oil block ~Rs 8,000 cr dominates; pulses dal-margin + wheat gluten + silica add the rest)")
    return lines


def write_csv(path: Path = DEFAULT_OUTPUT, rows: Iterable[InputRow] = ROWS, fx: float = FX_RS_PER_USD) -> Path:
    """Write the consolidated table to ``path`` and return it."""
    out, _ = compute(rows, fx)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(out)
    log.info("wrote %s", path)
    return path


def main(output: Path | None = None) -> None:
    """CLI entry point: print the table and write the CSV (default data/consolidated_savings_by_crop.csv)."""
    print("\n".join(render()))
    write_csv(output or DEFAULT_OUTPUT)
    print("\nwritten data/consolidated_savings_by_crop.csv")


if __name__ == "__main__":
    main()
