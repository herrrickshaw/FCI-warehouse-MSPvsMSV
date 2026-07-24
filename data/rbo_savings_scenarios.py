#!/usr/bin/env python3
"""RBO extraction savings across scenarios of rice-volume processed + demand-security.
Grounded: all-India bran ~98 LMT (verified ~9.8 MT); govt CMR paddy 832 LMT (KMS24-25);
oil yield 16%; import parity Rs105/kg; ex-mill Rs60/kg (DORB credit); DORB Rs15/kg.
"""
BRAN_ALLINDIA   = 98.0     # LMT total rice bran [verified]
PADDY_GOVT      = 832.0    # LMT govt-procured paddy [verified]
PADDY_ALLINDIA  = 2045.0   # LMT (rice 1370 / 0.67) [derived]
GOVT_BRAN_SHARE = PADDY_GOVT/PADDY_ALLINDIA          # govt's share of the bran
BRAN_GOVT       = BRAN_ALLINDIA*GOVT_BRAN_SHARE      # govt-touchable bran, LMT
OIL_YIELD   = 0.16
PARITY      = 105          # Rs/kg import parity
EXMILL      = 60           # Rs/kg RBO ex-mill (with DORB credit)
DORB_PRICE  = 15           # Rs/kg de-oiled bran (feed)
BRAN_NOW_EXT= 50.0         # LMT bran already oil-extracted nationally [verified ~50%]

def cr(lmt_oil, rs_per_kg):   # LMT oil * Rs/kg -> Rs crore
    return lmt_oil*1e5*1000*rs_per_kg/1e7   # 1 LMT=1e5 t=1e8 kg

print(f"Govt-touchable bran: {BRAN_GOVT:.0f} LMT ({GOVT_BRAN_SHARE*100:.0f}% of {BRAN_ALLINDIA:.0f} LMT all-India)\n")

for base_name, bran_base in [("GOVERNMENT CMR bran", BRAN_GOVT), ("ALL-INDIA bran", BRAN_ALLINDIA)]:
    print(f"=== {base_name}: {bran_base:.0f} LMT ===")
    print(f"{'% processed':>12}{'bran LMT':>10}{'RBO LMT':>9}{'imp displ':>11}{'net margin':>11}{'DORB feed':>10}")
    for pct in [0.25, 0.50, 0.75, 1.00]:
        bran = bran_base*pct
        oil  = bran*OIL_YIELD
        dorb = bran*0.78                      # ~78% of bran -> DORB
        imp_displ = cr(oil, PARITY)           # gross import bill displaced
        margin    = cr(oil, PARITY-EXMILL)    # net economic gain on the oil
        dorb_rev  = cr(dorb, DORB_PRICE)      # feed revenue (also feed-import substitution)
        print(f"{pct*100:>11.0f}%{bran:>10.1f}{oil:>9.1f}{imp_displ:>10,.0f}{margin:>11,.0f}{dorb_rev:>10,.0f}")
    print()

# incremental over current national extraction
incr_bran = BRAN_ALLINDIA - BRAN_NOW_EXT
incr_oil  = incr_bran*OIL_YIELD
print(f"INCREMENTAL (the ~{incr_bran:.0f} LMT bran now going to CATTLE FEED, not oil):")
print(f"  -> +{incr_oil:.1f} LMT RBO -> Rs {cr(incr_oil,PARITY):,.0f} cr import displaced (~{cr(incr_oil,PARITY)/165000*100:.0f}% of ~Rs1.65 L-cr oil bill)")
print(f"  net economic gain Rs {cr(incr_oil,PARITY-EXMILL):,.0f} cr + DORB feed Rs {cr(incr_bran*0.78,DORB_PRICE):,.0f} cr\n")

# ---- DEMAND SECURITY: where the oil goes if consumer demand drops ----
print("--- DEMAND-SECURITY LEVERS (if branded-consumer RBO demand softens) ---")
total_rbo_potential = BRAN_ALLINDIA*OIL_YIELD
print(f"Full RBO potential: {total_rbo_potential:.1f} LMT. Demand floors that absorb it:")
channels = [
 ("Food processing (frying/snacks/bakery/HoReCa)", "high smoke pt 232C + oryzanol = superior frying oil; price-inelastic industrial demand"),
 ("Blend/fortification (Saffola-type + Vit A/D mandate)", "RBO-blend positioning; a fortification mandate can require inclusion"),
 ("Institutional (PDS/ICDS/mid-day-meal fortified oil)", "state offtake backstop, mirrors Bharat-brand"),
 ("Export (premium health oil)", "India already exports RBO; global oryzanol demand"),
 ("Byproduct (DORB->feed, acid oil->soap/oleochem)", "always-in-demand feed + oleochemical floor"),
]
for c,why in channels: print(f"  * {c}\n      {why}")
