import json
import logging
import web3
from dotenv import load_dotenv()
from eth import Eth
from algorithm import Graph


load_dotenv()


class Bot:
    """
    The automated engine combining each different component of this bot.
    """

    def __init__(self, public_key, private_key, contracts_file='../artifacts/contracts.json'):
        """
        Initializes this Bot object.
        """

        logging.info('WaltJR initialized')
        

        self.eth = Eth(public_key, private_key)
        self.w3 = self.eth.w3

        self.contracts = self._init_contracts(contracts_file)
        logging.info('Contracts initialized')

        
        self.graph = self._init_graph()
        logging.info('Graph initialized')


    def _init_contracts(self, contracts_file):
        """
        Initializes the contracts for this Bot with web3 implementation.
        """
        _data = []

        with open(contracts_file, 'r') as file:
            _data = json.loads(file.read())

            for _contract in _data:
                _contract_impl = self.w3.eth.contract(
                    address=_contract['address'],
                    abi=_contract['abi']
                )

                _contract['contract_impl'] = _contract_impl

        return _data


    def _format_init_graph_data(self):
        """
        Formats the initial data for the Graph based on exchange rates and exchange
        information at that moment.
        """

        _data = []
        
        for _contract in self.contracts:
            _exchange_data
            _exchange = _contract['exchange']
            _currencies = _contract['currencies']

            # get exchange rate between all pairs
            _pairs = []

            for _currency_a in _currencies:
                for _currency_b in currencies:
                    if _currency_a != _currency_b:
                        _pair_data = {}

                        _rate = 1 #self.getExchangeRate

                        _pair_data['a'] = _currency_a
                        _pair_data['b'] = _currency_b
                        _pair_date['rate'] = _rate

                        _pairs.append(_pair_data)

            _exchange_data['exchange'] = _exchange
            _exchange_data['currencies'] = _currencies
            _exchange_data['pairs'] = _pairs

            _data.append(_exchange_data)
        

    def _init_graph(self):
        """
        Initializes the primary Graph object to be used by this Bot.
        """
        
        _data = self._format_init_graph_data()
        _graph = Graph(_data)

        return _graph


    def _get_exchange_rate(self, contract, i, j):
        """
        Gets the current exchange rate at some exchange.
        """

        if contract['exchange'] == 'curve':
            _a = 0
            _b = 0

            for _coin in contract['coins']:
                if _coin['name'] == i:
                    _a = _coin['number']

                if _coin['name'] == j:
                    _b = _coin['number']

            _i_decimals = 0
            _j_decimals = 0

            if i == 'dai': _i_decimals = 10 ** 18
            if j == 'dai': _j_decimals = 10 ** 18
            if i == 'usdc': _i_decimals = 10 ** 6
            if j == 'usdc': _j_decimals = 10 ** 6
            if i == 'usdt': _i_decimals = 10 ** 6
            if j == 'usdt': _j_decimals = 10 ** 6

            _raw_price = contract['contract_impl'].get_function_by_signature(
                'get_dy_underlying(int128,int128,uint256)'
            )(a, b, _i_decimals).call()

            return _raw_price / _j_decimals
            
    

    def _update_graph(self):
        """
        Updates the Graph object at some time interval with new exchange rate
        data for that time.
        """
        
        pass


    def _compute_optimal_path(self):
        """
        Computes the optimal path of a swap to take place and returns it,
        otherwise returns None.
        """

        return self.graph.find_arbitrage()


    def _execute_swap(self, path):
        """
        Executes a swap among successive vertices in a path.
        """

        pass


    def run(self):
        """
        Main program loop for the Bot class.
        """

        _should_terminate = False
        
        while not _should_terminate:
            # update graph
            self._update_graph()

            # find optimal path
            _optimal_path = self._compute_optimal_path()

            # execute arbitrage on optimal path
            if _optimal_path != None:
                self._execute_swap(_optimal_path)

        logging.info('WaltJR terminated')
