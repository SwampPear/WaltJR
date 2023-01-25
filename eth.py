import json
import requests
from dotenv import load_dotenv


load_dotenv()


class Eth:
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
            params=[]
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

    # call

    def estimate_gas(
        self, 
        block,
        fromAddress=None,
        toAddress=None,
        gas=None,
        gas_price=None,
        value=None,
        data=None
    ):
        tx = {}

        if fromAddress: tx['from'] = fromAddress
        if toAddress: tx['to'] = toAddress
        if gas: tx['gas'] = gas
        if gas_price: tx['gasPrice'] = gas_price
        if value: tx['value'] = value
        #if data: tx['data'] = data

        return self.send_json_rpc_request(
            method='eth_estimateGas',
            params=[tx, block]
        )
        
    # create_access_list
    
    def gas_price(self):
        return self.send_json_rpc_request(
            method='eth_gasPrice',
            params=[]
        )

    # max_priority_fee_for_gas
    # fee_history
    # new_filter
    # new_block_filter
    # new_pending_transaction_filter
    # uninstall_filter
    # get_filter_changes
    # get_filter_logs
    # get_logs
    # mining
    # hash_rate
    # get_work
    # submit_work
    # submit_hashrate

    def sign(self, address, message):
        return self.send_json_rpc_request(
            method='eth_sign',
            params=[address, message]
        )

    def sign_transaction(
        self,
        fromAddress,
        data,
        toAddress=None,
        gas=None,
        gas_price=None,
        value=None,
        nonce=None
    ):
        tx_data = {
            fromAddress,
            data,
        }

        if toAddress: tx_data['to'] = toAddress
        if gas: tx_data['gas'] = gas
        if gas_price: tx_data['gasPrice'] = gas_price
        if value: tx_data['value'] = value
        if nonce: tx_data['nonce'] = nonce

        return self.send_json_rpc_request(
            method='eth_signTransaction',
            params=[tx_data]
        )

    def get_balance(self, address, block_number):
        return self.send_json_rpc_request(
            method='eth_getBalance',
            params=[address, block_number]
        )

    # get storage at
    # get transaction count
    # get code
    # get proof

    def send_transaction(
        self, 
        from_address, 
        data,
        to_address=None, 
        gas=None, 
        gas_price=None,
        value=None
    ):
        data = {
            'from': from_address,
            'data': data
        }

        if to_address: data['to'] = to_address
        if gas: data['gas'] = gas
        if gas_price: data['gasPrice'] = gas_price
        if value: data['value'] = value

        datatx = {
            'jsonrpc': '2.0',
            'method': 'eth_sendTransaction',
            'params': [data],
            'id': 0
        }

        response = requests.post(self.http_provider, json=datatx)

        print(json.loads(response.text))

    def send_raw_transaction(self, data):
        return self.send_json_rpc_request(
            method='eth_sendRawTransaction',
            params=[data]
        )

    # get transaction by hash
    # get transaction by block hash and index
    # get transaction by block number and index
    # get transaction receipt