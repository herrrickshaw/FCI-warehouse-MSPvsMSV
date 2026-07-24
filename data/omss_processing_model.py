#!/usr/bin/env python3
"""OMSS/grain processing unit economics -> business returns.
All prices Rs/qtl unless noted. Conversion ratios & byproduct values from
published milling norms (FCI CMR outturn 67% rice; roller-flour ~76% atta/maida
+ ~22% bran; conservative). This is a DETERMINISTIC unit-economics model, not a
forecast — every input is labelled with its source vintage.
"""

# ---- WHEAT -> ATTA (roller flour mill buying OMSS wheat) ----
wheat_omss   = 2550     # OMSS(D) reserve price 2025-26 (repo: haryana brief)
wheat_mandi  = 2500     # mandi median 23-Jul-2026 (repo: mandi_vs_msp)
# outturn per 100 kg wheat: 76 kg atta/maida/suji + 22 kg bran (2 kg loss)
atta_yield, bran_yield = 0.76, 0.22
atta_price   = 3300     # wholesale atta ~Rs 33/kg (Bharat Atta MRP 27.5; open ~30-34)
bran_price   = 1900     # wheat bran (feed) ~Rs 19/kg
proc_cost_wheat = 180   # milling+power+packing+labour ~Rs 1.8/kg (industry est.)

def mill_econ(grain_cost, yields_prices, proc):
    revenue = sum(y*p for y,p in yields_prices)
    gross   = revenue - grain_cost
    ebitda  = gross - proc
    return revenue, gross, ebitda

for label, wcost in [("OMSS-sourced", wheat_omss), ("mandi-sourced", wheat_mandi)]:
    rev, gr, eb = mill_econ(wcost, [(atta_yield,atta_price),(bran_yield,bran_price)], proc_cost_wheat)
    print(f"WHEAT->ATTA {label}: grain {wcost} | revenue {rev:.0f} | gross {gr:.0f} | EBITDA {eb:.0f}/qtl ({eb/rev*100:.1f}% margin)")

# ---- PADDY/RICE -> milled rice ----
# Miller buys paddy at mandi (or does CMR for govt). Custom milling = fixed fee.
paddy_mandi  = 2385     # mandi median 23-Jul-2026
rice_yield   = 0.67     # CMR outturn
bran_rice_yield, husk_yield = 0.08, 0.22
rice_wholesale = 3400   # common milled rice ~Rs 34/kg wholesale
ricebran_price = 2200; husk_price = 300
proc_cost_paddy = 150
# per qtl PADDY:
rev = rice_yield*rice_wholesale + bran_rice_yield*ricebran_price + husk_yield*husk_price
eb  = rev - paddy_mandi - proc_cost_paddy
print(f"PADDY->RICE open-market: paddy {paddy_mandi} | revenue {rev:.0f} | EBITDA {eb:.0f}/qtl ({eb/rev*100:.1f}% margin)")
# CMR (govt custom milling) — miller earns a FIXED fee, no price risk:
cmr_fee = 15  # Rs/qtl milling charge (repo: Haryana brief, +bonus) — plus retains bran/husk
byproduct = bran_rice_yield*ricebran_price + husk_yield*husk_price
print(f"PADDY->RICE custom-milling(CMR): fee {cmr_fee} + byproducts {byproduct:.0f} = {cmr_fee+byproduct:.0f}/qtl paddy (no price risk, govt owns grain)")

# ---- SCALE TO A BUSINESS ----
# A mid-size roller flour mill: 300 t/day, 300 days = 90,000 t/yr wheat throughput = 900,000 qtl
print("\n--- SCALE: 300 TPD flour mill (90,000 t/yr) ---")
tpd_qtl = 90000*10
eb_qtl = mill_econ(wheat_omss, [(atta_yield,atta_price),(bran_yield,bran_price)], proc_cost_wheat)[2]
annual_ebitda = eb_qtl*tpd_qtl
revenue_annual = mill_econ(wheat_omss,[(atta_yield,atta_price),(bran_yield,bran_price)],proc_cost_wheat)[0]*tpd_qtl
print(f"throughput 900,000 qtl/yr | EBITDA/qtl {eb_qtl:.0f} | annual EBITDA Rs {annual_ebitda/1e7:.1f} cr | revenue Rs {revenue_annual/1e7:.0f} cr | margin {annual_ebitda/revenue_annual*100:.1f}%")
# capex for 300 TPD mill ~Rs 40-60 cr; working capital ~Rs 30 cr
capex = 50e7; wc = 30e7
roce = annual_ebitda/(capex+wc)*100
print(f"capital employed ~Rs {(capex+wc)/1e7:.0f} cr (capex 50 + WC 30) | ROCE ~{roce:.0f}%")
