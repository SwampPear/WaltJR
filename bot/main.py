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

        self.dx_coefficient = 1000000000000000000

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

                data = {
                    'contract': contract_impl,
                    'priceSignature': contract['priceSignature'],
                    # swap signatures
                    'type': contract['type'] 
                }

                self.contracts.append(data)

    def get_price_option(self, contract):
        if contract['type'] == 'curve':
            raw_price = contract['contract'].get_function_by_signature(contract['priceSignature'])(0, 1, self.dx_coefficient).call()

            return raw_price / self.dx_coefficient
        
bot = Bot(os.getenv('ADDRESS'), os.getenv('PRIVATE_KEY'))

print(bot.get_price_option(bot.contracts[3]))