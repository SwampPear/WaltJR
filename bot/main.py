import os
import json
import time
import logging
import web3
from dotenv import load_dotenv
from eth import Eth


load_dotenv()

class Bot:
    def __init__(self, public_key, private_key, contract_db='contracts.json'):
        """
        Initializes the 'Bot' class.

        Implemeneted for:
        - curve
        - uniswap     (coming soon)
        - pancakeswap (coming soon)
        - sushiswap   (coming soon)
        - balancer    (coming soon)

        Arguments
        ---------
        public_key  (str) : the public key of the wallet to interact with
        private_key (str) : the private key of the wallet to interact with
        """
        # logging
        logging.basicConfig(
            filename='bot.log', 
            filemode='w', 
            format='%(asctime)s - %(message)s',
            datefmt='%d-%b-%y %H:%M:%S'
        )
        
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
        self.min_rate = 1

    
    def _get_exchange_rate(self, contract, i, j):
        """
        Returns the exchange rate between two currencies on an exchange designated by a given 
        contract.
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
        

    def _swap(self, i_address, j_address, i, j):
        """
        Executes the swap operation within the smart contract.
        """
        pass


    def _init_arbitrage_chances(self):
        """
        Initializes the data structure to be used to store arbitrage chances.
        """
        _arbitrage_chances = []

        # iterate through each contract
        for _contract in self.contracts:
            # create contract data to handle arbitrage chances
            _contract_data = {
                'address': _contract['address'],
                'arbitrageChances': []
            }

            # initialize each pair as false
            for _coin_i in self.coins:
                for _coin_j in self.coins:
                    if _coin_i != _coin_j:
                        _arbitrage_chance = {
                            'i': _coin_i,
                            'j': _coin_j,
                            'status': False,
                            'rate': 0
                        }

                        _contract_data['arbitrageChances'].append(
                            _arbitrage_chance
                        )

            _arbitrage_chances.append(_contract_data)

        return _arbitrage_chances


    def _update_arbitrage_chance(self, arbitrage_chances, address, i, j, status, rate):
        """
        Updates an individual arbitrage chance.
        """
        for _arbitrage_chance in arbitrage_chances:
            # update status based on address
            if address == _arbitrage_chance['address']:
                # iterate through each currency pair and update correct pair
                for _currency_pair in _arbitrage_chance['arbitrageChances']:
                    if _currency_pair['i'] == i and _currency_pair['j'] == j:
                        _currency_pair['status'] = status
                        _currency_pair['rate'] = rate

    
    def _update_arbitrage_chances(self, _arbitrage_chances):
        """
        Updates all arbitrage chances.
        """
        for _contract in self.contracts:
            for _coin_i in self.coins:
                for _coin_j in self.coins:
                    if _coin_i != _coin_j:
                        # get exchange rate and check above min
                        _rate = self._get_exchange_rate(
                            _contract, 
                            _coin_i, 
                            _coin_j
                        )

                        if _rate > self.min_rate:
                            self._update_arbitrage_chance(
                                _arbitrage_chances,
                                _contract['address'],
                                _coin_i,
                                _coin_j,
                                True,
                                _rate
                            )

                            logging.info(f'WaltJR found an arbitrage chance: {_coin_i} -> {_coin_j} at {_rate}.')

                        else:
                            self._update_arbitrage_chance(
                                _arbitrage_chances,
                                _contract['address'],
                                _coin_i,
                                _coin_j,
                                False,
                                _rate
                            )


    def _check_for_inverse_arbitrage(self, arbitrage_chances, address, i, j):
        """
        Checks for an inverse arbitrage chance based on a given address, i, and j and makes
        the swap.
        """
        _arbitrage_chance_found = False
        _address = ''
        _rate = 0

        for _arbitrage_data in arbitrage_chances:
            for _arbitrage_chance in _arbitrage_data['arbitrageChances']:
                if (_arbitrage_chance['status'] and 
                    _arbitrage_chance['i'] == j and 
                    _arbitrage_chance['j'] == i and 
                    _arbitrage_chance['rate'] > _rate
                ):
                    _arbitrage_chance_found = True
                    _address = _arbitrage_data['address']
                    _rate = _arbitrage_chance['rate']

        if _arbitrage_chance_found:
            logging.info(f'WaltJR found the maximum inverse arbitrage chance: {j} -> {i} at {_rate}.')

            self._swap(
                address,
                _address,
                i,
                j
            )

        else:
            logging.info(f'WaltJR failed to find the maximum inverse arbitrage chance.')


    def _execute_arbitrage(self, arbitrage_chances):
        """
        Executes arbitrage based on arbitrage chances.
        """
        _arbitrage_chance_found = False
        _address = ''
        _i = ''
        _j = ''
        _rate = 0

        for _arbitrage_data in arbitrage_chances:
            for _arbitrage_chance in _arbitrage_data['arbitrageChances']:
                if (_arbitrage_chance['status'] and 
                    _arbitrage_chance['rate'] > _rate
                ):
                    _arbitrage_chance_found = True
                    _address = _arbitrage_data['address']
                    _i = _arbitrage_chance['i']
                    _j = _arbitrage_chance['j']
                    _rate = _arbitrage_chance['rate']

        if _arbitrage_chance_found:
            logging.info(f'WaltJR found the maximum arbitrage chance: {_i} -> {_j} at {_rate}.')

            self._check_for_inverse_arbitrage(
                arbitrage_chances,
                _address,
                _i,
                _j
            )

        else:
            logging.info(f'WaltJR failed to find an arbitrage chance.')
        

    def run(self):
        """
        Main program loop for the bot.
        """
        _arbitrage_chances = self._init_arbitrage_chances()
        _should_terminate = False

        while not _should_terminate:
            logging.info('WaltJR initiated.')

            self._update_arbitrage_chances(_arbitrage_chances)
            self._execute_arbitrage(_arbitrage_chances)

            _should_terminate = True

        logging.info('WaltJR terminated.')



if __name__ == '__main__':
    logging.basicConfig(
        filename='bot.log', 
        filemode='w', 
        format='%(asctime)s - %(message)s',
        datefmt='%d-%b-%y %H:%M:%S',
        level = logging.INFO
    )
    
    bot = Bot(os.getenv('ADDRESS'), os.getenv('PRIVATE_KEY'))
    bot.run()