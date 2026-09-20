# BNB 5% Threshold Agent — MVP Demo Ready

**On-chain AI Trading Agent for BNB Chain**  
Momentum strategy: **Buy on +5%** · **Sell on -5%**  
Built with official **BNBAgent SDK** (ERC-8004 Identity)

[![BNB Chain](https://img.shields.io/badge/BNB_Chain-Native-F0B90B?style=flat&logo=binance)](https://www.bnbchain.org)
[![ERC-8004](https://img.shields.io/badge/ERC--8004-Agent_Identity-blue)](https://eips.ethereum.org/EIPS/eip-8004)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## What is this?

A complete **MVP** of an autonomous trading agent that lives on BNB Chain:

- Registers on-chain with **ERC-8004** (official BNBAgent SDK)
- Monitors real-time BNB price
- Executes a clear momentum rule (+5% buy / -5% sell)
- Runs in **Paper Trading** mode (zero capital required)
- Gasless registration on BSC Testnet
- Ready for demo, audit and extension to real execution

Perfect for BNB Builders events, hackathons and presentations.

---

## Live Demo

**Dashboard:** [Coming after Vercel deploy]  
**GitHub:** https://github.com/srbisnes/bnb-5pct-threshold-agent

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Frontend (Dashboard)              │
│          Live BNB price + Agent status              │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│              Agent Runtime (Python)                 │
│  • strategy.py     → +5% / -5% logic                │
│  • oracle.py       → Real BNB price (Binance)       │
│  • main.py         → Paper trading loop             │
│  • register_agent.py → ERC-8004 on-chain identity   │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│              BNB Chain (BSC Testnet)                │
│  • ERC-8004 Identity Registry                       │
│  • MegaFuel Paymaster (gasless)                     │
│  • Ready for ERC-8183 commerce layer                │
└─────────────────────────────────────────────────────┘
```

---

## Quick Start (Demo in < 3 minutes)

```bash
git clone https://github.com/srbisnes/bnb-5pct-threshold-agent.git
cd bnb-5pct-threshold-agent

pip install -r requirements.txt
cp .env.example .env
# Edit .env → set a WALLET_PASSWORD

# 1. Register the agent on-chain (gasless)
python register_agent.py

# 2. Run the agent (paper trading)
python main.py
```

You will see live signals in the terminal.

---

## Strategy Rules (Transparent & Auditable)

```python
if price_change >= +5% and no_position:
    BUY  → update reference price

if price_change <= -5% and has_position:
    SELL → update reference price
```

- Reference price is updated after every simulated trade
- Fully deterministic and easy to audit
- Designed to be extended with real execution, risk management and AI confirmation

---

## Security Notes (Important for Audit)

### Current Scope (MVP)
- Paper trading only → no real funds at risk
- No private key exposure in code
- Uses official BNBAgent SDK wallet abstraction
- Gasless registration via MegaFuel

### About Optimistic Settlement (ERC-8183)
When you later add the commerce layer:
- **OptimisticPolicy** assumes approval if no dispute is raised within the window
- Voters are **pre-whitelisted** (not chosen after the fact)
- Client must actively dispute bad work
- Recommended improvements for production: reputation (ERC-8004), staking, Karma proofs, or stricter policies

---

## Project Structure

```
├── main.py                 # Agent loop (paper trading)
├── register_agent.py       # ERC-8004 registration
├── strategy.py             # Core +5% / -5% logic
├── oracle.py               # Real BNB price feed
├── config.py               # Configuration
├── public/index.html       # Professional demo dashboard
├── requirements.txt
├── .env.example
└── README.md
```

---

## Roadmap (Post-MVP)

- [ ] Real trade execution (PancakeSwap)
- [ ] ERC-8183 commerce layer (so others can hire the agent)
- [ ] Telegram alerts
- [ ] Risk management (stop-loss, position sizing)
- [ ] Multi-timeframe confirmation
- [ ] Agent reputation dashboard

---

## License

MIT — free to use, modify and present.

Built for the BNB ecosystem by [elcryptoboy](https://github.com/srbisnes)
