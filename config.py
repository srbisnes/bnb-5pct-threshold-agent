import os
from dotenv import load_dotenv
from decimal import Decimal

load_dotenv()

WALLET_PASSWORD = os.getenv("WALLET_PASSWORD", "changeme")
PRIVATE_KEY = os.getenv("PRIVATE_KEY") or None
NETWORK = os.getenv("NETWORK", "bsc-testnet")
THRESHOLD = Decimal(os.getenv("THRESHOLD", "0.05"))
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", "30"))
