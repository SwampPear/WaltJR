import os
import json
import web3
from dotenv import load_dotenv
from eth import Eth


load_dotenv()


class Bot:
    def __init__(self, public_key, private_key):
        self.eth = Eth(public_key, private_key)
        self.w3 = self.eth.w3

        self.contracts = []
        self.price_signatures = []
        self.swap_signatures = []

        with open('contracts.json', 'r') as file:
            contract_data = json.loads(file.read())

            for contract in contract_data:
                contract_impl = self.w3.eth.contract(
                    address=contract['address'], 
                    abi=contract['abi']
                )

                self.contracts.append(contract_impl)

        # 1000000000000000000

        a = self.contracts[0].get_function_by_signature('get_dy(int128,int128,uint256)')(0, 1, 1000000000000000000).call()
        print(a)

        
bot = Bot(os.getenv('ADDRESS'), os.getenv('PRIVATE_KEY'))