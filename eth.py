import os
from dotenv import load_dotenv
from web3 import Web3
import web3
import json
import requests


load_dotenv()


class Eth:
    def __init__(self, 
        public_key, 
        private_key
    ):
        self.public_key = public_key
        self.private_key = private_key
        
        self.http_provider = Web3.HTTPProvider(os.getenv('INFURA_URL_ENDPOINT_SEPOLIA'))
        self.w3 = Web3(self.http_provider)

    def get_transaction_count(self):
        return self.w3.eth.getTransactionCount(self.public_key)

    def send_json_rpc_request(self, method, params):
        data = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': 0
        }

        response = requests.post(os.getenv('INFURA_URL_ENDPOINT_SEPOLIA'), json=data)

        return json.loads(response.text)['result']

    def estimate_gas(
        self, 
        block='latest',
        toAddress=None,
        gas=None,
        gas_price=None,
        value=None,
        data=None
    ):
        tx = {}

        if toAddress: tx['to'] = toAddress
        if gas: tx['gas'] = gas
        if gas_price: tx['gasPrice'] = gas_price
        if value: tx['value'] = value
        if data: tx['data'] = data

        return self.send_json_rpc_request(
            method='eth_estimateGas',
            params=[tx, block]
        )

    def gas_price(self):
        return self.send_json_rpc_request(
            method='eth_gasPrice',
            params=[]
        )

    def send_transaction(
        self,
        data=None,
        to_address=None,
        gas=None,
        gas_price=None,
        value=None,
        nonce=None
    ):
        tx = {
            'from': self.public_key,
        }

        if data: tx['data'] = data
        if to_address: tx['to'] = to_address
        if gas: tx['gas'] = gas
        if gas_price: tx['gasPrice'] = gas_price
        if value: tx['value'] = value
        if nonce: 
            tx['nonce'] = nonce
        else:
            tx['nonce'] = self.get_transaction_count()

        signed_tx = web3.eth.Account.sign_transaction(tx, self.private_key)

        #send transaction
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)

        #get transaction hash
        print(self.w3.toHex(tx_hash))
