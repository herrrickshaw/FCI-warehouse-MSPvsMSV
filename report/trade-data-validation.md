# Trade-data validation against DGCI&S TradeStat EIDB

*Cross-check of the project's trade figures against the authoritative primary source —
DGCI&S TradeStat EIDB commodity-wise (user-supplied, "Values in US$ Million", FY2024-25 &
FY2025-26 provisional, generated 30 Jul 2026). July 2026.*

## Result: parity + rice + wheat confirmed; one unit-label error found and fixed

### 1. `trade_price_parity.csv` — CONFIRMED ✓

Every oil and pulse in the project's [`data/trade_price_parity.csv`](../data/trade_price_parity.csv)
`value_usd_mn` column matches TradeStat EIDB to the rounding:

| Commodity (import) | Parity CSV $mn (FY25-26) | TradeStat $mn | Match |
|---|---|---|---|
| Crude palm oil | 9,053 | 9,053 | ✓ |
| RBD palmolein | 372 | 372 | ✓ |
| Crude soybean oil | 5,257 | 5,257 | ✓ |
| Crude sunflower oil | 3,255 | 3,255 | ✓ |
| Tur / pigeon pea | 947 | 947 | ✓ |
| Urad | 880 | 880 | ✓ |
| Masur / lentil | 660 | 660 | ✓ |
| Desi chana | 537 | 537 | ✓ |
| Yellow peas | 398 | 398 | ✓ |
| Wheat | 28 | 28 | ✓ |

Basmati export also ties out: TradeStat $5,944 mn (FY24-25) = the APEDA ₹50,000 cr / $5.94 bn
figure cited in [demand-and-exports-highmargin.md](demand-and-exports-highmargin.md). So the
parity dataset the earlier agent built by reverse-engineering the APEDA/DGCI&S APIs is validated
against the primary customs source — no revision needed.

### 2. Rice export figures — CONFIRMED ✓

The rice figures in [demand-and-exports-highmargin.md](demand-and-exports-highmargin.md) tie out
exactly to TradeStat (FY2024-25, US$ mn):

| Rice | Report | TradeStat | Match |
|---|---|---|---|
| Basmati export | $5.94 bn (₹50,000 cr) | $5,944 mn | ✓ |
| Non-basmati export | $6.53 bn (₹55,408 cr) | $6,528 mn | ✓ |
| All rice export | ~$12.5 bn | $12,472 mn | ✓ |

**Data-continuity note:** in FY2025-26 DGCI&S *restructured the rice HS-8 codes* — the old
`10063020` (basmati) / `10063010` (parboiled) / `10063090` (other) show zero, replaced by new
granular codes (`10063012` parboiled basmati $2,814 mn, `10063019` parboiled other $3,555 mn,
`10063092` basmati $2,859 mn, `10063099` others $1,650 mn). Any rice export *time series* must
map old→new codes across the FY25/FY26 boundary or it will show a false cliff. The aggregate
(~$12 bn) is continuous; the code-level split is not.

### 3. Wheat trade — CONFIRMED ✓ (and it confirms the export ban)

| Wheat | TradeStat FY24-25 | FY25-26 | Reading |
|---|---|---|---|
| Export | $2.0 mn | $10.3 mn | **near-zero — the May-2022 export ban still binds** |
| Import | $43.5 mn | $27.6 mn | small, deficit-year grain |

India's wheat *export* is a rounding error ($2–10 mn) — confirming the export-ban context used
throughout the [diplomacy](rice-diplomacy-history.md) and [new-markets](new-markets-evaluation.md)
reports. Wheat *procurement* (300.35 LMT, RMS 2025-26) and *production* figures are DFPD/PIB/
Economic Survey series, not trade — separately cross-validated against ES Table 26
([data manifest](../data/MANIFEST.md)); TradeStat neither confirms nor contradicts them (different
domain).

### 4. `wheat_products_trade_dgcis.csv` — unit error found & FIXED

The wheat-products file was initially labelled **₹ crore**; the TradeStat header states
**"Values in US$ Million"**. The *numbers* were correct (60.7, 63.0, …) but the *unit* was
wrong — so pasta exports are **$63 mn**, not "₹63 cr (~$7.5 mn)". Corrected in the CSV, the
[wheat report](wheat-value-added-products.md), and the pitch deck. The pasta-vs-US-market ratio
moves from "under 0.5%" to "under 4%" — still a large opportunity, correctly sized.

## The lesson

TradeStat EIDB reports in **US$ Million**. Any figure pulled from it must carry that unit
explicitly. The parity CSV had it right; the wheat CSV did not — the cross-check caught it.
This is why the manifest records a source + vintage + unit per file, and why primary-source
validation is worth running when authoritative data lands.

*Source: user-supplied TradeStat-Eidb Export/Import Commodity-wise .xlsx (value + quantity,
FY24-25 & FY25-26), DGCI&S, generated 30 Jul 2026.*
