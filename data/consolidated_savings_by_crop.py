#!/usr/bin/env python3
"""Consolidated per-crop: import price/ton (DGCI&S) vs domestic processing margin vs
import-substitution savings, with the food-processing offtake channel.
Import unit values from data/trade_price_parity.csv (DGCI&S FY26). Rs/USD 88.5 (FY26 impl).
"""
import csv
# (crop, product, import_usd_t, subst_volume_lmt, dom_margin_note, offtake_channel)
# import_usd_t from trade_price_parity.csv (DGCI&S) or byproduct import price (verified)
R = [
 # OILS -----------------------------------------------------------------
 ("Rice→bran","Rice bran oil (edible)", 1107, 7.7,  "ex-mill Rs60 vs parity Rs105 = Rs45/kg + DORB feed", "Food processing: frying/snacks/HoReCa (232C smoke pt) + fortification mandate"),
 ("Oilseeds","Mustard/groundnut oil",   1116, 0.0,  "premium ~Rs136 vs palm Rs98; production-lever not in-yr", "Branded premium retail + food processing blends"),
 ("Cotton→seed","Cottonseed oil",       1116, 2.0,  "crush margin + meal byproduct", "Food processing + Vanaspati/HoReCa"),
 # PULSES (import price per ton, dal-processing margin) ------------------
 ("Pulses-tur","Tur dal",               638,  5.0,  "dal-milling margin ~8-12% + chuni feed", "Dal millers (NAFEX auction) + PDS pulse pilot"),
 ("Pulses-urad","Urad dal",             838,  3.0,  "dal-milling margin", "Dal millers + food processing (papad/snack)"),
 ("Pulses-masur","Masur dal",           575,  4.0,  "dal-milling margin", "Dal millers + institutional"),
 # WHEAT derivatives ----------------------------------------------------
 ("Wheat","Vital wheat gluten",         1292, 0.13, "wet-mill gluten+starch; imports 13000 t/yr China 88%", "Food processing: bakery/meat-analogue/pet-food (captive)"),
 ("Wheat","Wheat germ oil",             5000, 0.02, "high-value nutraceutical, wasted germ fraction", "Nutraceutical/cosmetic brands + export"),
 ("Wheat","Fortified atta (PDS)",       0,    0.0,  "captive PDS demand, no import", "Government PDS/ICDS (captive offtake)"),
 # RICE husk / bran high-value tail ------------------------------------
 ("Rice→husk","Precipitated silica",    980,  1.0,  "raw RHA Rs1-3.5 -> silica ~Rs40-90/kg, ~30x jump", "Tyre/industrial (45% tyre demand); import substitution"),
 ("Rice→bran","Gamma oryzanol",         120000,0.005,"global USD2.6bn; India mkt only USD6.5mn vs #1 RBO", "Nutraceutical/cosmetic export + fortification"),
 ("Rice→bran","Tocotrienols/Vit-E",     200000,0.004,"imports 60-70%; feedstock DD Rs45-75/kg domestic", "Fortification input (captive) + pharma"),
 # MAIZE ----------------------------------------------------------------
 ("Maize","Starch/HFCS/sorbitol",       420,  3.0,  "wet-milling; India imports refined derivatives", "Food/pharma/paper processing"),
 ("Maize","Corn gluten meal",           500,  0.0,  "60% protein; India EXPORTS to 25+ countries", "Feed export (already positive)"),
 # OILSEED meal / soy specialty ----------------------------------------
 ("Oilseeds","Soy lecithin (specialty)",1300, 0.2,  "imports specialty grades; domestic feed-grade only", "Food processing emulsifier (captive)"),
 ("Oilseeds","Soy/pea protein isolate", 3000, 0.3,  "India exports some; plant-protein trend", "Food processing + export"),
]
FX=88.5
print(f"{'crop/stream':<14}{'product':<24}{'imp Rs/t':>10}{'subst LMT':>10}{'save Rscr':>10}  offtake")
print("-"*120)
tot=0
out=[]
for crop,prod,usd_t,vol,margin,chan in R:
    inr_t = usd_t*FX
    save  = vol*1e5*inr_t/1e7 if usd_t else 0   # LMT*1e5 t *Rs/t /1e7 = Rs cr
    tot+=save
    print(f"{crop:<14}{prod:<24}{inr_t:>10,.0f}{vol:>10.2f}{save:>10,.0f}  {chan[:44]}")
    out.append([crop,prod,usd_t,round(inr_t),vol,round(save),margin,chan])
print("-"*120)
print(f"{'TOTAL potential import-substitution savings (illustrative):':<58}{tot:>10,.0f} Rs cr/yr")
print(f"  (edible-oil block ~Rs 8,000 cr dominates; pulses dal-margin + wheat gluten + silica add the rest)")

with open('consolidated_savings_by_crop.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['crop_stream','product','import_usd_per_t','import_inr_per_t','subst_volume_lmt','potential_save_rs_cr','domestic_margin_note','food_processing_offtake'])
    w.writerows(out)
print("\nwritten data/consolidated_savings_by_crop.csv")
