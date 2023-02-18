import os
import json
import web3
from dotenv import load_dotenv
from eth import Eth


load_dotenv()


class Bot:
    def __init__(self, public_key, private_key, contract_db='contracts.json'):
        """
        Initializes the 'Bot' class.

        Arguments
        ---------
        public_key  (str) : the public key of the wallet to interact with
        private_key (str) : the private key of the wallet to interact with
        """
        
        # eth interaction
        self.eth = Eth(public_key, private_key)
        self.w3 = self.eth.w3

        # contract interaction
        self.contracts = []

        # initialize contract data from json
        with open(contract_db, 'r') as file:
            self.contracts = json.loads(file.read())

            for _contract in self.contracts:
                _contract_impl = self.w3.eth.contract(
                    address=_contract['address'], 
                    abi=_contract['abi']
                )

                _contract['contract_impl'] = _contract_impl

        self.coins = ['dai', 'usdc', 'usdt']
        self.min_rate = 1.00001
        
        # bot tasks
        self.arbitrage_chances = []

        
    def swap(self):
        pass

    
    def run(self):
        for contract in self.contracts:
            # iterate through all contracts and check for arbitrage chances
            self.check_contract_for_arbitrage(contract)

            # check against local arbitrage chances
            _arbitrage_chances = self.check_for_arbitrage()

            # if chances are present, then execute swap
            if _arbitrage_chances:
                # execute swap
                pass

    def test(self):
        """
        Only used to test during implementation process
        """

        _contracts = self.contracts[0:2]

        
        for _contract in _contracts:
            self.check_contract_for_arbitrage(_contract)
            _arbitrage_chances = self.check_for_arbitrage()

                
    def check_contract_for_arbitrage(self, contract):
        # iterate through each available currency
        for currency_a in self.coins:

            # check rate against other available currencies
            for currency_b in self.coins:

                # pass if currency is same
                if currency_a != currency_b:
                    rate = self.get_rate(contract, currency_a, currency_b)
                    print(f'\033[92m{currency_a}\033[0m')
                    print(f'\033[92m{currency_b}\033[0m')
                    print(f'\033[91m{rate}\033[0m')
                    # append arbitrage chance
                    if rate > self.min_rate:
                        arbitrage = {
                            'a': currency_a,
                            'b': currency_b,
                            'contract': contract
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

    
    def get_rate(self, contract, i=None, j=None):
        """
        Returns the exchange rate between two currencies on an exchange designated by a given contract.

        Arguments
        ---------
        contract (json) : the contract object to interact with
        i         (str) : the name of the first currency to trade
        j         (str) : the name of the second currency to trade
        """
        
        if contract['type'] == 'curve':
            # map currency name to curve-readable int
            a = 0
            b = 0

            for coin in contract['coins']:
                if coin['name'] == i:
                    a = coin['number']

                if coin['name'] == j:
                    b = coin['number']

            # map currency to decimals
            i_decimals = 0
            j_decimals = 0

            if i == 'dai': i_decimals = 10 ** 18
            if j == 'dai': j_decimals = 10 ** 18
            if i == 'usdc': i_decimals = 10 ** 6
            if j == 'usdc': j_decimals = 10 ** 6
            if i == 'usdt': i_decimals = 10 ** 6
            if j == 'usdt': j_decimals = 10 ** 6

            raw_price = contract['contract_impl'].get_function_by_signature(
                contract['priceSignature']
            )(a, b, i_decimals).call()

            return raw_price / j_decimals
        
bot = Bot(os.getenv('ADDRESS'), os.getenv('PRIVATE_KEY'))

bot.test()
