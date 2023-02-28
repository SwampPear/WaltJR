import json
import logging
import time
import web3
from dotenv import load_dotenv
from eth import Eth
from algorithm import Graph
from utils import decimals


load_dotenv()


class Bot:
    """
    The automated engine combining each different component of this bot.
    """

    def __init__(self, public_key, private_key, contracts_file='bot/artifacts/contracts.json'):
        """
        Initializes this Bot object.
        """

        self.eth = Eth(public_key, private_key)
        self.w3 = self.eth.w3

        self.contracts = self._init_contracts(contracts_file)

        self.graph = self._init_graph()
        
        logging.info('WaltJR initialized')


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


    def _init_graph(self):
        """
        Initializes the primary Graph object to be used by this Bot.
        """

        data = [
            {
                'exchange': 'curve_3pool',
                'currencies': [
                    'dai',
                    'usdc',
                    'usdt'
                ],
                'pairs': [
                    {
                        'a': 'dai',
                        'b': 'usdc',
                        'rate': 1.5
                    },
                    {
                        'a': 'dai',
                        'b': 'usdt',
                        'rate': 2.5
                    },
                    {
                        'a': 'usdc',
                        'b': 'dai',
                        'rate': 3.5
                    },
                    {
                        'a': 'usdc',
                        'b': 'usdt',
                        'rate': 4.5
                    },
                    {
                        'a': 'usdt',
                        'b': 'dai',
                        'rate': 5.5
                    },
                    {
                        'a': 'usdt',
                        'b': 'usdc',
                        'rate': 6.5
                    }
                ]
            }
        ]

        _data = []

        for _contract in self.contracts:
            _exchange_data = {}

            _exchange = _contract['exchange']
            _currencies = []

            for _currency in _contract['currencies']:
                _currencies.append(_currency['name'])

            # get exchange rate between all pairs
            _pairs = []

            for _currency_a in _currencies:
                for _currency_b in _currencies:
                    if _currency_a != _currency_b:
                        _pair_data = {}

                        _rate = 1 #self.getExchangeRate

                        _pair_data['a'] = _currency_a
                        _pair_data['b'] = _currency_b
                        _pair_data['rate'] = _rate

                        _pairs.append(_pair_data)

            _exchange_data['exchange'] = _exchange
            _exchange_data['currencies'] = _currencies
            _exchange_data['pairs'] = _pairs

            _data.append(_exchange_data)

        _graph = Graph(data)

        return _graph


    def _get_exchange_rate_curve_3pool(self, exchange, i, j):
        """
        Gets the exchange rate for some pair on the Curve exchange.
        """

        _contract = []

        for _temp_contract in self.contracts:
            if exchange == _temp_contract['exchange']:
                _contract = _temp_contract

        _a = 0
        _b = 0

        for _currency in _contract['currencies']:
            if _currency['name'] == i:
                _a = _currency['number']

            if _currency['name'] == j:
                _b = _currency['number']

        _i_decimals = decimals(i)
        _j_decimals = decimals(j)

        _raw_price = _contract['contract_impl'].get_function_by_signature(
            'get_dy_underlying(int128,int128,uint256)'
        )(_a, _b, _i_decimals).call()

        return _raw_price / _j_decimals


    def _get_exchange_rate(self, exchange, i, j):
        """
        Gets the current exchange rate at some exchange.
        """

        if exchange == 'curve_3pool':
            return self._get_exchange_rate_curve_3pool(exchange, i, j)


    def _update_graph(self):
        """
        Updates the Graph object at some time interval with new exchange rate
        data for that time. Iterates through the vertices in graph and updates
        edges according to exchange rate.
        """

        for i in range(0, len(self.graph.vertices)):
            _vertex = self.graph.vertices[i]
            _exchange = _vertex.data_enum
            _a = _vertex.data_class

            for j in range(0, len(self.graph.vertices[i].edges)):
                _next_vertex = _vertex.edges[j][1]

                if _vertex.data_class != _next_vertex.data_class:
                    _b = _next_vertex.data_class
                    _rate = self._get_exchange_rate(_exchange, _a, _b)

                    self.graph.vertices[i].edges[j][0] = _rate


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
            self._update_graph()

            _optimal_path = self.graph.compute_optimal_path()
            print(_optimal_path)

            if _optimal_path != None:
                self._execute_swap(_optimal_path)

            time.sleep(10)

        logging.info('WaltJR terminated')
