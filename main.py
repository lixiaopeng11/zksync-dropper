from utils.web3_utils import load_wallets, init_web3
from core.tasks.mint_task import run_mint
import json

wallets = load_wallets("config/wallets.txt")
rpc_config = json.load(open("config/rpc_config.json"))
contract_config = json.load(open("config/contracts.json"))

for chain, rpc_url in rpc_config.items():
    print(f"\n>>> 正在处理链：{chain}")
    web3 = init_web3(rpc_url)
    for pk in wallets:
        tx = run_mint(web3, pk, contract_config["zkSyncSepolia"])
        print(f"地址: {pk[-6:]}... TX: {tx}")