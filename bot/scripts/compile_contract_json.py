import json


CONTRACTS = 'artifacts/contracts.json'

def create_contract_data(exchange, address, currencies, abi):
    with open(CONTRACTS, 'r') as file:
        _data = json.load(file)
        
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


def remove_pancakeswap():
    with open(CONTRACTS, 'r') as file:
        _old_data = []

        _data = json.load(file)
        
        for _keep_data in _data:
            if _keep_data['exchange'] == 'curve_3pool':
                _old_data.append(_keep_data)


    with open(CONTRACTS, 'w', encoding='utf-8') as file:
        json.dump(
            _old_data, 
            file, 
            ensure_ascii=False, 
            indent=4
        )