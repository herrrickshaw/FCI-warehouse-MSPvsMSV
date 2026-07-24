#!/usr/bin/env python3
"""Rice husk+bran -> oil -> acid-oil -> biodiesel blending scenarios.
Answers: at different bran-utilisation levels, (a) how much edible RBO (import
substitution), (b) how much acid oil -> biodiesel, (c) what blend % (Bx) results.
Every constant labelled with source/basis. Deterministic, not a forecast.
"""

# ---- DENOMINATORS (verified) ----
DIESEL_MMT      = 91.4            # India HSD consumption FY25 (PPAC) [verified]
DIESEL_DENS     = 0.832          # kg/L -> diesel volume
DIESEL_BN_L     = DIESEL_MMT*1e9/DIESEL_DENS/1e9   # billion litres/yr
DIESEL_CR_L     = DIESEL_BN_L*100                  # crore litres
print(f"Diesel pool: {DIESEL_MMT} MMT = {DIESEL_BN_L:.0f} bn L = {DIESEL_CR_L:.0f} cr L/yr")
print(f"  B1 needs {DIESEL_CR_L*0.01:.0f} cr L | B5 needs {DIESEL_CR_L*0.05:.0f} cr L of biodiesel\n")

# ---- RICE BRAN STOCK (verified) ----
BRAN_TOTAL_LMT  = 98.0           # total rice bran output potential [verified ~9.8 MT]
BRAN_NOW_OILEXT = 0.50           # ~50% currently solvent-extracted; rest -> cattle feed [verified]
OIL_YIELD       = 0.16           # bran -> crude RBO, 16-18% [verified ~18%; 16% conservative whole-bran]
ACID_FRAC       = 0.10           # crude RBO -> acid oil (FFA/soapstock) on refining, 8-12% [derived]
BD_PER_LMT_ACID = 10.8           # 1 LMT acid oil -> ~10.8 cr L biodiesel (0.95 conv, 0.88 dens) [derived]
IMPORT_PARITY   = 105            # Rs/kg landed palm/edible-oil parity [reported 100-110]
RBO_EXMILL      = 65             # Rs/kg domestic crude RBO ex-mill [reported 55-75]

print(f"{'bran util':>10}{'RBO LMT':>9}{'edible+':>9}{'imp save':>10}{'acidoil':>9}{'biodsl':>9}{'blend':>8}")
print(f"{'(% stock)':>10}{'(total)':>9}{'vs now':>9}{'Rs cr':>10}{'LMT':>9}{'cr L':>9}{'level':>8}")
rbo_now = BRAN_TOTAL_LMT*BRAN_NOW_OILEXT*OIL_YIELD
for util in [0.50, 0.60, 0.75, 0.90, 1.00]:
    bran_ext = BRAN_TOTAL_LMT*util
    rbo      = bran_ext*OIL_YIELD                 # total crude RBO, LMT
    edible_incr = max(rbo - rbo_now, 0)           # incremental vs current, LMT
    imp_save = edible_incr*100_000*1000*IMPORT_PARITY/1e7  # Rs cr (1 LMT=100k t, /1e7 to cr)
    acid     = rbo*ACID_FRAC                       # acid oil, LMT
    biodsl   = acid*BD_PER_LMT_ACID               # biodiesel, cr L (acid-oil-only, food-safe)
    blend    = biodsl/DIESEL_CR_L*100             # % blend
    print(f"{util*100:>9.0f}%{rbo:>9.1f}{edible_incr:>+9.1f}{imp_save:>10,.0f}{acid:>9.2f}{biodsl:>9.1f}{'B'+format(blend,'.2f'):>8}")

print("\n--- If ALL crude RBO diverted to fuel (NOT recommended, burns edible oil) ---")
rbo_full = BRAN_TOTAL_LMT*1.0*OIL_YIELD
bd_full  = rbo_full*10.8   # cr L
print(f"  100% bran, whole RBO->biodiesel: {bd_full:.0f} cr L = B{bd_full/DIESEL_CR_L*100:.1f}  (absurd: displaces cooking oil India imports)")

print("\n--- To reach B1 / B5 from the WHOLE realistic non-edible waste basket ---")
uco    = 4.0     # collectible used cooking oil, LMT [reported ~3-5 of ~30 generated]
tallow = 1.5     # animal fat/tallow, LMT [reported]
acid_100 = BRAN_TOTAL_LMT*OIL_YIELD*ACID_FRAC
basket = acid_100 + uco + tallow
bd_basket = (acid_100+uco+tallow)*10.8
print(f"  rice acid oil {acid_100:.2f} + UCO {uco} + tallow {tallow} = {basket:.1f} LMT lipid")
print(f"  -> {bd_basket:.0f} cr L biodiesel = B{bd_basket/DIESEL_CR_L*100:.2f}  (still < B1)")
b5_need = DIESEL_CR_L*0.05
oil_for_b5 = b5_need/BD_PER_LMT_ACID*ACID_FRAC  # nonsense via acid; compute direct oil

print(f"  B5 needs ~{b5_need:.0f} cr L biodiesel = ~{b5_need/10.8:.0f} LMT of oil feedstock")
print(f"    = ~1/3 of India's entire ~250 LMT edible-oil supply. Physically impossible from waste alone.")

# ---- HUSK: energy enabler, NOT a blending feedstock ----
print("\n--- Husk (energy lever, does NOT blend into diesel) ---")
HUSK_TOTAL_LMT = 183.0    # ~22% of paddy at govt+all-India scale [derived]
HUSK_MWH_PER_T = 0.5      # ~0.5 MWh electricity per tonne husk [reported ~3000-3600 kcal/kg]
husk_gwh = HUSK_TOTAL_LMT*100_000*HUSK_MWH_PER_T/1000
print(f"  {HUSK_TOTAL_LMT} LMT husk -> ~{husk_gwh:,.0f} GWh/yr potential (power the extraction/esterification + grid/silica)")
print(f"  Husk role = process-energy self-sufficiency + carbon credit, not a blend component.")
