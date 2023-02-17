import os
import json
import web3
from dotenv import load_dotenv
from eth import Eth


load_dotenv()


class Bot:
    def __init__(self, public_key, private_key):
        # ethereum interface
        self.eth = Eth(public_key, private_key)
        self.w3 = self.eth.w3

        # contract interaction
        self.contract_data = []

        with open('contracts.json', 'r') as file:
            self.contract_data = json.loads(file.read())

            for contract in self.contract_data:
                address = contract['address']
                abi = contract['abi']

                contract_impl = self.w3.eth.contract(
                    address=contract['address'], 
                    abi=contract['abi']
                )

                contract['contract_impl'] = contract_impl

        # available currencies to trade
        self.available_currencies = ['dai', 'usdc', 'usdt']


        # minimum rate to chance on
        self.min_rate = 1.00001
        
        # bot tasks
        # mapping of arbitrage chances
        self.arbitrage_chances = []

    def swap(self):
        pass
    
    def run(self):
        for contract in self.contract_data:
            # iterate through all contracts and check for arbitrage chances
            self.check_contract_for_arbitrage(contract)

            # check against local arbitrage chances
            _arbitrage_chances = self.check_for_arbitrage()

            # if chances are present, then execute swap
            if _arbitrage_chances:
                # execute swap        

    def check_contract_for_arbitrage(self, contract):
        # iterate through each available currency
        for currency_a in self.available_currencies:

            # check rate against other available currencies
            for currency_b in self.available_currencies:

                # pass if currency is same
                if currency_a != currency_b:
                    rate = self.get_rate(contract, currency_a, currency_b)

                    # append arbitrage chance
                    if rate > self.min_rate:
                        arbitrage = {
                            a: currency_a,
                            b: currency_b,
                            contract: contract
                        }
                            
                        self.arbitrage_chances.append(arbitrage)
                        
    def check_for_arbitrage(self):
        # iterate through arbitrage chances and check if two inverse exchange rates are present
        for chance_a in self.arbitrage_chances:
            for chance_b in self.arbitrage_chances:

                # make sure arbitrage chance is not the same
                if chance_a != chance_b:
                    if chance_a['a'] == chance_b['b'] and chance_a['b'] == chance_b['a']:
                        
                        # emit arbitrage chance pair
                        return [chance_a, chance_b]

        # else return None
        return None        
                        
    def get_rate(self, contract, a=None, b=None):
        if contract['type'] == 'curve':
            a_number = 0
            b_number = 0

            for coin in contract['coins']:
                if coin['name'] == a:
                    a_number = coin['number']

                if coin['name'] == b:
                    b_number = coin['number']

            raw_price = contract['contract_impl'].get_function_by_signature(
                contract['priceSignature']
            )(a_number, b_number, (10 ** 18)).call()

            return raw_price / 1000000

    def test(self):
        for contract in self.contract_data:
            print(self.get_rate(contract, a='dai', b='usdc'))

        
bot = Bot(os.getenv('ADDRESS'), os.getenv('PRIVATE_KEY'))

bot.test()

# 1) continuously iterate through each of the contracts and check prices
# 2) if any rates are above 1, log and continue
# 3) simultaneoulsy iterate through logged rates and check if any inverse rates are present
# 4) as soon as an inverse pair is found, execute smart contract function
# 5) through each iteration of the smart contract function, check the price on

##############################################################################################
####################################### Testing Ground #######################################
##############################################################################################
