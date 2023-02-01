import json


CONTRACTS = 'contracts.json'

def create_json(pool, address, abi):
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


def read_json(pool):
    with open(CONTRACTS, 'r') as file:
        data = json.loads(file.read())

        for info in data:
            if info['pool'] == pool:
                return info['pool']


def update_json(pool, address=None, abi=None):
    with open(CONTRACTS, 'r') as file:
        data = json.loads(file.read())

        for info in data:
            if info['pool'] == pool:
                if address: info['address'] = address
                if abi: info['abi'] = abi
        
    with open(CONTRACTS, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def delete_json(pool):
    with open(CONTRACTS, 'r') as file:
        data = json.loads(file.read())

        for info in data:
            if info['pool'] == pool:
                data.pop(info)
        
    with open(CONTRACTS, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def price(pool, sig):
    with open(CONTRACTS, 'r') as file:
        data = json.loads(file.read())

        for info in data:
            if info['pool'] == pool:
                info['priceSignature'] = sig
        
    with open(CONTRACTS, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def coins_sig(pool, coin_signautre):

    with open(CONTRACTS, 'r') as file:
        data = json.loads(file.read())

        for info in data:
            if info['pool'] == pool:
                info['coinsSignature'] = coin_signautre
            
    with open(CONTRACTS, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)