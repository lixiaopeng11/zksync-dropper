**Project Title:** zkDropper — Multi-Wallet zkSync Automation Tool

**Short Description:**  
zkDropper is an open-source multi-wallet automation framework designed to batch call smart contracts on zkSync Era (Sepolia), primarily used for minting, testing, or airdrop strategy workflows.

**Motivation:**  
Many airdrop programs and smart contract testing processes involve repetitive calls across multiple wallets. zkDropper eliminates manual steps by offering a scriptable structure that works with any compatible contract ABI and supports future Layer 2s like Scroll or Linea.

**How to Use:**  
Update the config files (`wallets.txt`, `contracts.json`, etc.), and run `main.py`. The system will automatically process each wallet against your chosen chain and contract.

**Tools/Tech Stack:** Python, Web3.py, zkSync RPC, JSON ABI

**License:** MIT  
**GitHub:** https://github.com/yourname/zksync-dropper