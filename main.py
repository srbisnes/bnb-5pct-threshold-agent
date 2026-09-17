import time
from decimal import Decimal
from config import THRESHOLD, CHECK_INTERVAL
from oracle import get_bnb_price
from strategy import ThresholdStrategy

def main():
    print("🚀 Iniciando BNB 5% Threshold Agent (Paper Trading)")
    print(f"Threshold: {float(THRESHOLD)*100}%")
    print("-" * 55)

    strategy = ThresholdStrategy(threshold=THRESHOLD)

    while True:
        try:
            price = get_bnb_price()
            if price == 0:
                time.sleep(CHECK_INTERVAL)
                continue

            signal = strategy.update(price)

            change_str = f"{float(signal.change_pct)*100:.2f}%"
            print(f"[{time.strftime('%H:%M:%S')}] BNB: ${price} | Cambio: {change_str} | Señal: {signal.action}")

            if signal.action == "BUY":
                print(f"🟢 SEÑAL DE COMPRA ejecutada (Paper) a ${price}")
                strategy.on_trade("BUY", price)

            elif signal.action == "SELL":
                print(f"🔴 SEÑAL DE VENTA ejecutada (Paper) a ${price}")
                strategy.on_trade("SELL", price)

        except KeyboardInterrupt:
            print("\nAgente detenido por el usuario.")
            break
        except Exception as e:
            print(f"Error: {e}")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
