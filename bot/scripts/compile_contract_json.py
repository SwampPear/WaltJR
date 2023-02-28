import json


CONTRACTS = '../artifacts/contracts.json'

def create_contract_data(exchange, address, currencies, abi):
    with open(CONTRACTS, 'r') as file:
        _data = []
        
        _new_data = {
            'exchange': exchange,
            'address': address,
            'currencies': currencies,
            'abi': abi
        }

        _data.append(_new_data)

    with open(CONTRACTS, 'w', encoding='utf-8') as file:
        json.dump(
            _data, 
            file, 
            ensure_ascii=False, 
            indent=4
        )


create_contract_data(
    exchange='pancakeswap',
)