import os
import json
import requests
from dotenv import load_dotenv


load_dotenv()


def hex_to_dec(value):
        return int(value, 16)


class Gloss:
    def __init__(self, http_provider):
        self.http_provider = http_provider

    def send_json_rpc_request(self, method, params):
        data = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': 0
        }

        response = requests.post(self.http_provider, json=data)

        return json.loads(response.text)['result']

    def get_block_by_hash(self, block_hash: str, hydrated_transactions: bool):
        return self.send_json_rpc_request(
            method='eth_getBlockByHash',
            params=[block_hash, hydrated_transactions]
        )

    def get_block_by_number(self, block, hydrated_transactions):
        return self.send_json_rpc_request(
            method='eth_getBlockByNumber',
            params=[block, hydrated_transactions]
        )

    def get_block_transaction_count_by_hash(self, block_hash):
        return self.send_json_rpc_request(
            method='eth_getBlockTransactionCountByHash',
            params=[block_hash]
        )

    def get_block_transaction_count_by_number(self, block):
        return self.send_json_rpc_request(
            method='eth_getBlockTransactionCountByNumber',
            params=[block]
        )

    def get_uncle_count_by_block_hash(self, block_hash):
        return self.send_json_rpc_request(
            method='eth_getUncleCountByBlockHash',
            params=[block_hash]
        )

    def get_uncle_count_by_block_number(self, block):
        return self.send_json_rpc_request(
            method='eth_getUncleCountByBlockNumber',
            params=[block]
        )

    def chain_id(self):
        return self.send_json_rpc_request(
            method='eth_chainId',
            params=[]
        )

    def syncing(self):
        return self.send_json_rpc_request(
            method='eth_syncing',
            params=[]
        )

    def coinbase(self):
        return self.send_json_rpc_request(
            method='eth_coinbase',
            params=[],
            id=0
        )

    def accounts(self):
        return self.send_json_rpc_request(
            method='eth_accounts',
            params=[]
        )

    def block_number(self):
        return self.send_json_rpc_request(
            method='eth_blockNumber',
            params=[]
        )





        


gloss = Gloss(os.getenv('INFURA_URL_ENDPOINT_SEPOLIA'))
gloss.get_block_by_hash()
