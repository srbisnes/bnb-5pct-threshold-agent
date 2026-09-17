# BNB 5% Threshold Agent

**Agente nativo de BNB Chain** con estrategia de momentum:

- **Compra** cuando BNB sube ≥ **5%**
- **Vende** cuando BNB baja ≥ **5%**

Incluye:
- Registro on-chain con **ERC-8004** (gasless en BSC Testnet)
- Paper Trading (funciona sin capital)
- Oráculo de precio real (Binance)
- Listo para pasar a ejecución real

## Quick Start

```bash
git clone https://github.com/srbisnes/bnb-5pct-threshold-agent.git
cd bnb-5pct-threshold-agent
pip install -r requirements.txt
cp .env.example .env
# Edita .env y pon una WALLET_PASSWORD

# 1. Registrar el agente en BNB Chain (solo una vez)
python register_agent.py

# 2. Correr el agente (paper trading)
python main.py
```

## Características

- Zero capital (paper trading)
- Gasless registration en testnet vía MegaFuel
- Estrategia limpia y transparente
- Código modular y listo para producción

## Estructura

- `register_agent.py` → Coloca el agente on-chain (ERC-8004)
- `main.py` → Loop principal del agente
- `strategy.py` → Lógica +5% / -5%
- `oracle.py` → Precio real de BNB
- `config.py` → Configuración

## Dashboard

El dashboard está desplegado en Vercel (ver link en el repositorio).

---

Hecho por [elcryptoboy](https://github.com/srbisnes) · Powered by BNBAgent SDK
