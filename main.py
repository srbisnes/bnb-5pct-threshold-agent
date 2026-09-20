"""
BNB 5% Threshold Agent - Main Loop (Paper Trading)
MVP Demo Ready · Auditable · Zero Capital
"""
import time
from decimal import Decimal
from config import THRESHOLD, CHECK_INTERVAL
from oracle import get_bnb_price
from strategy import ThresholdStrategy

def main():
    print("=" * 60)
    print("  BNB 5% THRESHOLD AGENT — MVP DEMO")
    print("  Mode: Paper Trading (Zero Capital)")
    print("  Strategy: Buy ≥ +5%  |  Sell ≤ -5%")
    print("=" * 60)
    print(f"Threshold : {float(THRESHOLD)*100}%")
    print(f"Interval  : {CHECK_INTERVAL}s")
    print("-" * 60)

    strategy = ThresholdStrategy(threshold=THRESHOLD)
    signals_count = {"BUY": 0, "SELL": 0}

    while True:
        try:
            price = get_bnb_price()
            if price == 0:
                print("[WARN] Price feed failed, retrying...")
                time.sleep(CHECK_INTERVAL)
                continue

            signal = strategy.update(price)
            change_pct = float(signal.change_pct) * 100

            status = f"[{time.strftime('%H:%M:%S')}] BNB ${price:.2f} | Δ {change_pct:+.2f}% | {signal.action}"
            print(status)

            if signal.action == "BUY":
                print(f"  >>> GREEN SIGNAL: BUY executed (Paper) @ ${price:.2f}")
                strategy.on_trade("BUY", price)
                signals_count["BUY"] += 1

            elif signal.action == "SELL":
                print(f"  >>> RED SIGNAL: SELL executed (Paper) @ ${price:.2f}")
                strategy.on_trade("SELL", price)
                signals_count["SELL"] += 1

        except KeyboardInterrupt:
            print("\n" + "=" * 60)
            print("Agent stopped by user.")
            print(f"Total BUY signals : {signals_count['BUY']}")
            print(f"Total SELL signals: {signals_count['SELL']}")
            print("=" * 60)
            break
        except Exception as e:
            print(f"[ERROR] {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
