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

  # from
  from_address = os.getenv('ADDRESS')
    
  # gasPrice
  gas_price = eth.gas_price()

  # data
  data_file = open("artifacts/Test/Test.bin", "r")
  data = data_file.read()
  data_file.close()

  data = '0x' + data

  # gas
  gas = eth.estimate_gas(
    block='latest',
    fromAddress=from_address,
    gas_price=gas_price,
    data=data
  )

  # send tx
  # sign tx
  signed_tx = eth.sign_transaction(
    from_address=from_address,
    data=data,
    gas_price=gas_price,
    gas=gas
  )

  # send raw tx
