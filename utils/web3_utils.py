from web3 import Web3

def init_web3(rpc_url):
    return Web3(Web3.HTTPProvider(rpc_url))

def load_wallets(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f if line.strip()]