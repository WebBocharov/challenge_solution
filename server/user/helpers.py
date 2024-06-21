from web3 import Web3

# Can be changed to any other RPC
ganache_url = "https://ethereum-rpc.publicnode.com"

web3 = Web3(Web3.HTTPProvider(ganache_url))


def get_eth_balance(address):
    if not web3.is_address(address):
        raise ValueError("Invalid Ethereum address")

    address = web3.to_checksum_address(address)

    balance_wei = web3.eth.get_balance(address)

    balance_eth = web3.from_wei(balance_wei, 'ether')

    return balance_eth
