"""
Register the BNB 5% Threshold Agent on-chain using ERC-8004
Gasless on BSC Testnet via MegaFuel
"""
import os
from dotenv import load_dotenv
from bnbagent import ERC8004Agent, AgentEndpoint, EVMWalletProvider

load_dotenv()

def main():
    password = os.getenv("WALLET_PASSWORD")
    private_key = os.getenv("PRIVATE_KEY") or None

    if not password:
        print("ERROR: Set WALLET_PASSWORD in your .env file")
        return

    print("=" * 60)
    print("  REGISTERING AGENT ON BNB CHAIN (ERC-8004)")
    print("=" * 60)

    print("\n[1/3] Creating / loading wallet...")
    wallet = EVMWalletProvider(
        password=password,
        private_key=private_key
    )
    print(f"      Wallet: {wallet.address}")

    print("\n[2/3] Initializing BNBAgent SDK...")
    sdk = ERC8004Agent(
        network="bsc-testnet",
        wallet_provider=wallet,
        debug=True
    )

    agent_uri = sdk.generate_agent_uri(
        name="BNB-5pct-Threshold-Agent",
        description=(
            "MVP Momentum Agent on BNB Chain. "
            "Buys when price rises ≥5%, sells when price falls ≥5%. "
            "Paper trading ready. Built with official BNBAgent SDK (ERC-8004)."
        ),
        endpoints=[
            AgentEndpoint(
                name="status",
                endpoint="https://bnb-5pct-threshold-agent.vercel.app",
                version="1.0.0"
            )
        ]
    )

    print("\n[3/3] Submitting registration (gasless)...")
    result = sdk.register_agent(agent_uri=agent_uri)

    print("\n" + "=" * 60)
    print("  SUCCESS — AGENT REGISTERED ON BNB CHAIN")
    print("=" * 60)
    print(f"Agent ID     : {result.get('agentId')}")
    print(f"Tx Hash      : {result.get('transactionHash')}")
    print(f"Explorer     : https://testnet.bscscan.com/tx/{result.get('transactionHash')}")
    print("=" * 60)
    print("\nYour agent now has an official on-chain identity.")
    print("Next step: run  python main.py  to start paper trading.\n")

if __name__ == "__main__":
    main()
