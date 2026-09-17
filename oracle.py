import requests
from decimal import Decimal

def get_bnb_price() -> Decimal:
    """Obtiene el precio actual de BNB en USDT desde Binance"""
    try:
        r = requests.get(
            "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT",
            timeout=10
        )
        r.raise_for_status()
        return Decimal(r.json()["price"])
    except Exception as e:
        print(f"Error obteniendo precio: {e}")
        return Decimal("0")
