import web3
import os
from dotenv import load_dotenv
from eth import Eth


load_dotenv()

THREE_POOL_CONTRACT = '0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7'

class Bot:
    def __init__(self, public_key, private_key):
        self.eth = Eth(public_key, private_key)
        contract = self.eth.w3.eth.contract(address=THREE_POOL_CONTRACT)
       #abi = implementation.abi
        #pool = contract.from_abi("ESD Pool", "0xFD9f9784ac00432794c8D370d4910D2a3782324C", abi)


bot = Bot(os.getenv('ADDRESS'), os.getenv('PRIVATE_KEY'))