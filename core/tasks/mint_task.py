from eth_account import Account
import json

def run_mint(web3, privkey, contract_info):
    acct = Account.from_key(privkey)
    try:
        with open(contract_info["abiPath"]) as f:
            abi = json.load(f)
        contract = web3.eth.contract(address=contract_info["contractAddress"], abi=abi)
        tx = contract.functions.mint() \
            .build_transaction({
                'from': acct.address,
                'nonce': web3.eth.get_transaction_count(acct.address),
                'gas': 200000,
                'gasPrice': web3.eth.gas_price
            })
        signed_tx = acct.sign_transaction(tx)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return web3.to_hex(tx_hash)
    except Exception as e:
        return f"Error: {str(e)}"