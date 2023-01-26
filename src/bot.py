import os
from dotenv import load_dotenv


load_dotenv()


class Bot:
    def __init__(self, http_provider):
        self.http_provider = http_provider
        self.eth = Eth(self.http_provider)
        