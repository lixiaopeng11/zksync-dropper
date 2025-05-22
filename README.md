# zkDropper

**zkDropper** is a plug-and-play multi-wallet automation tool designed to interact with zkSync Era (Sepolia) smart contracts for tasks such as `mint()` operations, with the goal of streamlining interaction workflows for airdrop qualification, QA testing, and dev tooling.

## 🔧 Features

- ⚙️ Multi-wallet support (load from `wallets.txt`)
- 🔁 Batch `mint()` calls to any deployed contract with a compatible ABI
- 📦 Configurable RPC, contract address, and ABI path
- 🧪 Designed for zero-cost zkSync Sepolia testing, but ready for mainnet deployment

## 📁 Structure

```
zksync_airdrop_bot/
├── main.py
├── config/
│   ├── wallets.txt
│   ├── rpc_config.json
│   ├── contracts.json
│   └── mint_abi.json
├── core/tasks/
│   └── mint_task.py
└── utils/
    └── web3_utils.py
```

## 🚀 Quick Start

1. Install dependencies:
```bash
pip install web3 eth-account
```

2. Update `config/wallets.txt` with private keys

3. Edit `contracts.json` with your contract address and ABI file

4. Run:
```bash
python main.py
```

## 🧠 Why zkDropper?

- Simplifies repetitive L2 interactions for testers and devs
- Makes qualifying for Layer 2 airdrops easier
- Adaptable for use with LayerZero, Scroll, Starknet (via ABI + RPC)

## 📬 Contact & Contributions

This is a public tool for education and developer productivity.  
Feel free to fork, PR, or use in hackathons.

Project maintained by an independent builder.