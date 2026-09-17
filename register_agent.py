import os
from dotenv import load_dotenv
from bnbagent import ERC8004Agent, AgentEndpoint, EVMWalletProvider

load_dotenv()

def main():
    password = os.getenv("WALLET_PASSWORD")
    private_key = os.getenv("PRIVATE_KEY") or None

    if not password:
        print("Error: Debes configurar WALLET_PASSWORD en el archivo .env")
        return

    print("Creando / cargando wallet...")
    wallet = EVMWalletProvider(
        password=password,
        private_key=private_key
    )
    print(f"Wallet address: {wallet.address}")

    sdk = ERC8004Agent(
        network="bsc-testnet",
        wallet_provider=wallet,
        debug=True
    )

    agent_uri = sdk.generate_agent_uri(
        name="BNB-5pct-Threshold-Agent",
        description="Agente de momentum en BNB Chain: compra cuando sube 5%, vende cuando baja 5%. Paper trading + listo para ejecución real.",
        endpoints=[
            AgentEndpoint(
                name="status",
                endpoint="https://bnb-5pct-threshold-agent.vercel.app",
                version="1.0.0"
            )
        ]
    )

    print("Registrando agente en BSC Testnet (gasless)...")
    result = sdk.register_agent(agent_uri=agent_uri)

    print("\n✅ Agente registrado con éxito en BNB Chain!")
    print(f"Agent ID: {result.get('agentId')}")
    print(f"Transaction: {result.get('transactionHash')}")
    print(f"Explorer: https://testnet.bscscan.com/tx/{result.get('transactionHash')}")

if __name__ == "__main__":
    main()
