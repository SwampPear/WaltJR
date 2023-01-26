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
  eth = Eth(os.getenv('ADDRESS'), os.getenv('PRIVATE_KEY'))

  # gasPrice
  gas_price = eth.gas_price()

  # data
  data_file = open("artifacts/Test/X.bin", "r")
  data = '0x' + data_file.read()
  data_file.close()

  data_file2 = open("artifacts/Test/X.bin-runtime", "r")
  data2 = '0x' + data_file2.read()
  data_file2.close()

  print(len(data))
  print(len(data2))

  print(gas_price)
  print(data)

  gas = eth.estimate_gas(
    gas_price=gas_price,
    data=data
  )

  # sign tx
  signed_tx = eth.send_transaction(
    gas_price=gas_price,
    gas='0xEE6B2',
    data=data
  )

