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

        logging.info('Contracts initialized')
        self.contracts = self._init_contracts(contracts_file)

        logging.info('Graph initialized')
        self.graph = self._init_graph()


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

        pass


    def _init_graph(self):
        """
        Initializes the primary Graph object to be used by this Bot.
        """
        
        _data = self._format_init_graph_data()
        _graph = Graph(_data)

        return _graph


    def _get_exchange_rate(self, exchange, i, j):
        """
        Gets the current exchange rate at some exchange.
        """

        pass
    

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

        pass


    def _execute_swap(self, path):
        """
        Executes a swap among successive vertices in a path.
        """

        pass


    def run(self):
        """
        Main program loop for the Bot class.
        """

        pass
