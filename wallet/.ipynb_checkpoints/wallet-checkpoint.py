# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os 
from web3 import Web3, middleware, Account
from bit import PrivateKeyTestnet
# Import constants.py and necessary functions from bit and web3
from constants import *

from web3 import Account

# Load and set environment variables
load_dotenv("key.env")
mnemonic=os.getenv("mnemonic")

# Create a function called `derive_wallets`

def derive_wallets(coin,mnemonic,depth):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --cols=all --coin={coin} --numderive={depth} --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {ETH, BTCTEST}

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin,mnemonic):
    if coin == ETH:
        return Account.privateKeyToAccount(mnemonic)
    if coin == BTCTEST:
        return PrivateKeyTestNet(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(account, recipient, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": recipient, "value": amount}
    )
    return {
        "chainId": 333,
        "from": account.address,
        "to": recipient,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
    }

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(account, recipient, amount):
    tx = create_raw_tx(account, recipient, amount)
    signed_tx = account.sign_transaction(tx)
    result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(result.hex())
    return result.hex()
    