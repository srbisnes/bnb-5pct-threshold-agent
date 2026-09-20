# BNB 5% Threshold Agent — Professional MVP

**On-chain AI Trading Agent for BNB Chain**  
Momentum strategy + Risk Analysis + Profit Evaluator + Security Model

[![BNB Chain](https://img.shields.io/badge/BNB_Chain-Native-F0B90B?style=flat&logo=binance)](https://www.bnbchain.org)
[![ERC-8004](https://img.shields.io/badge/ERC--8004-Agent_Identity-blue)](https://eips.ethereum.org/EIPS/eip-8004)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Product Features (Professional Layer)

| Feature | Description |
|---------|-------------|
| **Live Price Oracle** | Real-time BNB/USDT from Binance |
| **Momentum Strategy** | Buy ≥ +5% · Sell ≤ -5% |
| **Risk Analysis** | Volatility, risk level, position sizing rules |
| **Profit Evaluator** | Interactive monthly PnL & ROI projection |
| **Best Hours** | Time windows with higher historical volatility |
| **Security Model** | ERC-8004 identity, paper-first, no keys in code, Optimistic-ready |
| **Interactive Dashboard** | Fully client-side professional UI |

---

## Security Model (Defined)

### Current (MVP)
- Paper trading only → zero real capital risk
- Official BNBAgent SDK wallet abstraction
- No private keys hardcoded
- Gasless registration on BSC Testnet (MegaFuel)
- Open source & auditable

### Designed for Production (ERC-8183 ready)
- Optimistic settlement with client dispute window
- Pre-whitelisted voters (not random)
- Future: Karma proofs / ZK evaluators / staking
- Reputation via ERC-8004

### Risk Rules Enforced in Product
- Max 2% capital risk per trade (configurable)
- Only one open position at a time
- Reference price updated after every signal
- Clear stop / take-profit logic (±5%)

---

## Quick Start

```bash
git clone https://github.com/srbisnes/bnb-5pct-threshold-agent.git
cd bnb-5pct-threshold-agent
pip install -r requirements.txt
cp .env.example .env
# Set WALLET_PASSWORD

python register_agent.py   # On-chain identity (ERC-8004)
python main.py             # Start paper trading
python analysis.py         # Run risk & profit modules
```

---

## Architecture

```
Dashboard (Interactive)
      ↓
Agent Runtime
  ├── strategy.py      → +5% / -5% logic
  ├── analysis.py      → Risk + Profit + Best Hours
  ├── oracle.py        → Live BNB price
  └── register_agent.py → ERC-8004 identity
      ↓
BNB Chain (BSC Testnet)
  └── Identity Registry + future Commerce layer
```

---

## License

MIT

Built for BNB Builders by [elcryptoboy](https://github.com/srbisnes)
