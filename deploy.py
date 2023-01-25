# TODO: write script to deploy a smart contract
"""
params: [
  {
    from: "0xb60e8dd61c5d32be8058bb8eb970870f07233155", address funding
    to: "", should be empty
    gas: "0x76c0", // 30400
    gasPrice: "0x9184e72a000", // 10000000000000
    value: "0x9184e72a", // 2441406250
    data: "0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675",
  },
]
"""
import sys
import os
from dotenv import load_dotenv

from eth import Eth


load_dotenv()


if __name__ == '__main__':
    eth = Eth(http_provider=os.getenv('INFURA_URL_ENDPOINT_SEPOLIA'))

    fromAddress = os.getenv('ADDRESS')
    # gas = estiamte gas function
    gas_price = eth.gas_price()
    # data = contract bytecode

    print(gas_price)

