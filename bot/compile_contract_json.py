import json


CONTRACTS = 'contracts.json'

def write_json(pool, address, abi):
    data = []
    with open(CONTRACTS, 'r') as file:
        data = json.loads(file.read())
        
        new_data = {
            'pool': pool,
            'address': address,
            'abi': abi
        }

        data.append(new_data)

    with open(CONTRACTS, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


write_json('a', 'b', 'c')