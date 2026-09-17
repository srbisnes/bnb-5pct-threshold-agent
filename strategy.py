from decimal import Decimal
from dataclasses import dataclass
from typing import Optional

@dataclass
class Signal:
    action: str          # BUY | SELL | HOLD
    price: Decimal
    change_pct: Decimal

class ThresholdStrategy:
    def __init__(self, threshold: Decimal = Decimal("0.05")):
        self.threshold = threshold
        self.reference_price: Optional[Decimal] = None
        self.position = False  # True = estamos comprados (paper)

    def update(self, current_price: Decimal) -> Signal:
        if current_price <= 0:
            return Signal("HOLD", current_price, Decimal("0"))

        if self.reference_price is None:
            self.reference_price = current_price
            print(f"Precio de referencia inicial: ${current_price}")
            return Signal("HOLD", current_price, Decimal("0"))

        change = (current_price - self.reference_price) / self.reference_price

        if change >= self.threshold and not self.position:
            return Signal("BUY", current_price, change)

        if change <= -self.threshold and self.position:
            return Signal("SELL", current_price, change)

        return Signal("HOLD", current_price, change)

    def on_trade(self, action: str, price: Decimal):
        if action == "BUY":
            self.position = True
        elif action == "SELL":
            self.position = False
        self.reference_price = price
        print(f"Referencia actualizada a: ${price}")
