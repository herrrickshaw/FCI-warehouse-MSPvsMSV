# Trade-data validation against DGCI&S TradeStat EIDB

*Cross-check of the project's trade figures against the authoritative primary source —
DGCI&S TradeStat EIDB commodity-wise (user-supplied, "Values in US$ Million", FY2024-25 &
FY2025-26 provisional, generated 30 Jul 2026). July 2026.*

## Result: the parity data is confirmed; one unit-label error was found and fixed

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

### 2. `wheat_products_trade_dgcis.csv` — unit error found & FIXED

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
