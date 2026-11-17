from __future__ import annotations

from fci_msv.units import LMT_TO_TONNES, RS_PER_CRORE, TONNES_TO_KG, lmt_at_rs_per_kg_to_crore


def test_one_lmt_at_one_rupee_per_kg_is_ten_crore():
    # 1 LMT = 1e5 t = 1e8 kg -> Rs 1e8 = Rs 10 crore
    assert lmt_at_rs_per_kg_to_crore(1, 1) == 10.0
    assert LMT_TO_TONNES * TONNES_TO_KG / RS_PER_CRORE == 10.0


def test_matches_original_inline_formula():
    assert lmt_at_rs_per_kg_to_crore(7.68, 105) == 7.68 * 1e5 * 1000 * 105 / 1e7
