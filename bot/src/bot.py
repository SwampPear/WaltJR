import json
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

        self.eth = Eth(public_key, private_key)
        self.w3 = self.eth.w3

        self.contracts = self._init_contracts(contracts_file)
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

    def _update_graph(self):
        """
        Updates the Graph object at some time interval with new exchange rate
        data for that time.
        """
        
        pass
        
