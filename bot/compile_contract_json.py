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

create_json('y', '0x45F783CCE6B7FF23B2ab2D70e416cdb7D6055f51', [{"name":"TokenExchange","inputs":[{"type":"address","name":"buyer","indexed":True},{"type":"int128","name":"sold_id","indexed":False},{"type":"uint256","name":"tokens_sold","indexed":False},{"type":"int128","name":"bought_id","indexed":False},{"type":"uint256","name":"tokens_bought","indexed":False}],"anonymous":False,"type":"event"},{"name":"TokenExchangeUnderlying","inputs":[{"type":"address","name":"buyer","indexed":True},{"type":"int128","name":"sold_id","indexed":False},{"type":"uint256","name":"tokens_sold","indexed":False},{"type":"int128","name":"bought_id","indexed":False},{"type":"uint256","name":"tokens_bought","indexed":False}],"anonymous":False,"type":"event"},{"name":"AddLiquidity","inputs":[{"type":"address","name":"provider","indexed":True},{"type":"uint256[4]","name":"token_amounts","indexed":False},{"type":"uint256[4]","name":"fees","indexed":False},{"type":"uint256","name":"invariant","indexed":False},{"type":"uint256","name":"token_supply","indexed":False}],"anonymous":False,"type":"event"},{"name":"RemoveLiquidity","inputs":[{"type":"address","name":"provider","indexed":True},{"type":"uint256[4]","name":"token_amounts","indexed":False},{"type":"uint256[4]","name":"fees","indexed":False},{"type":"uint256","name":"token_supply","indexed":False}],"anonymous":False,"type":"event"},{"name":"RemoveLiquidityImbalance","inputs":[{"type":"address","name":"provider","indexed":True},{"type":"uint256[4]","name":"token_amounts","indexed":False},{"type":"uint256[4]","name":"fees","indexed":False},{"type":"uint256","name":"invariant","indexed":False},{"type":"uint256","name":"token_supply","indexed":False}],"anonymous":False,"type":"event"},{"name":"CommitNewAdmin","inputs":[{"type":"uint256","name":"deadline","indexed":True,"unit":"sec"},{"type":"address","name":"admin","indexed":True}],"anonymous":False,"type":"event"},{"name":"NewAdmin","inputs":[{"type":"address","name":"admin","indexed":True}],"anonymous":False,"type":"event"},{"name":"CommitNewParameters","inputs":[{"type":"uint256","name":"deadline","indexed":True,"unit":"sec"},{"type":"uint256","name":"A","indexed":False},{"type":"uint256","name":"fee","indexed":False},{"type":"uint256","name":"admin_fee","indexed":False}],"anonymous":False,"type":"event"},{"name":"NewParameters","inputs":[{"type":"uint256","name":"A","indexed":False},{"type":"uint256","name":"fee","indexed":False},{"type":"uint256","name":"admin_fee","indexed":False}],"anonymous":False,"type":"event"},{"outputs":[],"inputs":[{"type":"address[4]","name":"_coins"},{"type":"address[4]","name":"_underlying_coins"},{"type":"address","name":"_pool_token"},{"type":"uint256","name":"_A"},{"type":"uint256","name":"_fee"}],"constant":False,"payable":False,"type":"constructor"},{"name":"get_virtual_price","outputs":[{"type":"uint256","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":1535185},{"name":"calc_token_amount","outputs":[{"type":"uint256","name":"out"}],"inputs":[{"type":"uint256[4]","name":"amounts"},{"type":"bool","name":"deposit"}],"constant":True,"payable":False,"type":"function","gas":6067881},{"name":"add_liquidity","outputs":[],"inputs":[{"type":"uint256[4]","name":"amounts"},{"type":"uint256","name":"min_mint_amount"}],"constant":False,"payable":False,"type":"function","gas":9327083},{"name":"get_dy","outputs":[{"type":"uint256","name":"out"}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"}],"constant":True,"payable":False,"type":"function","gas":3454227},{"name":"get_dx","outputs":[{"type":"uint256","name":"out"}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dy"}],"constant":True,"payable":False,"type":"function","gas":3454232},{"name":"get_dy_underlying","outputs":[{"type":"uint256","name":"out"}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"}],"constant":True,"payable":False,"type":"function","gas":3454087},{"name":"get_dx_underlying","outputs":[{"type":"uint256","name":"out"}],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dy"}],"constant":True,"payable":False,"type":"function","gas":3454093},{"name":"exchange","outputs":[],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"},{"type":"uint256","name":"min_dy"}],"constant":False,"payable":False,"type":"function","gas":7030208},{"name":"exchange_underlying","outputs":[],"inputs":[{"type":"int128","name":"i"},{"type":"int128","name":"j"},{"type":"uint256","name":"dx"},{"type":"uint256","name":"min_dy"}],"constant":False,"payable":False,"type":"function","gas":7050194},{"name":"remove_liquidity","outputs":[],"inputs":[{"type":"uint256","name":"_amount"},{"type":"uint256[4]","name":"min_amounts"}],"constant":False,"payable":False,"type":"function","gas":240409},{"name":"remove_liquidity_imbalance","outputs":[],"inputs":[{"type":"uint256[4]","name":"amounts"},{"type":"uint256","name":"max_burn_amount"}],"constant":False,"payable":False,"type":"function","gas":9326310},{"name":"commit_new_parameters","outputs":[],"inputs":[{"type":"uint256","name":"amplification"},{"type":"uint256","name":"new_fee"},{"type":"uint256","name":"new_admin_fee"}],"constant":False,"payable":False,"type":"function","gas":145867},{"name":"apply_new_parameters","outputs":[],"inputs":[],"constant":False,"payable":False,"type":"function","gas":133482},{"name":"revert_new_parameters","outputs":[],"inputs":[],"constant":False,"payable":False,"type":"function","gas":21805},{"name":"commit_transfer_ownership","outputs":[],"inputs":[{"type":"address","name":"_owner"}],"constant":False,"payable":False,"type":"function","gas":74482},{"name":"apply_transfer_ownership","outputs":[],"inputs":[],"constant":False,"payable":False,"type":"function","gas":60538},{"name":"revert_transfer_ownership","outputs":[],"inputs":[],"constant":False,"payable":False,"type":"function","gas":21895},{"name":"withdraw_admin_fees","outputs":[],"inputs":[],"constant":False,"payable":False,"type":"function","gas":22667},{"name":"kill_me","outputs":[],"inputs":[],"constant":False,"payable":False,"type":"function","gas":37848},{"name":"unkill_me","outputs":[],"inputs":[],"constant":False,"payable":False,"type":"function","gas":21985},{"name":"coins","outputs":[{"type":"address","name":"out"}],"inputs":[{"type":"int128","name":"arg0"}],"constant":True,"payable":False,"type":"function","gas":2160},{"name":"underlying_coins","outputs":[{"type":"address","name":"out"}],"inputs":[{"type":"int128","name":"arg0"}],"constant":True,"payable":False,"type":"function","gas":2190},{"name":"balances","outputs":[{"type":"uint256","name":"out"}],"inputs":[{"type":"int128","name":"arg0"}],"constant":True,"payable":False,"type":"function","gas":2220},{"name":"A","outputs":[{"type":"uint256","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2051},{"name":"fee","outputs":[{"type":"uint256","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2081},{"name":"admin_fee","outputs":[{"type":"uint256","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2111},{"name":"owner","outputs":[{"type":"address","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2141},{"name":"admin_actions_deadline","outputs":[{"type":"uint256","unit":"sec","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2171},{"name":"transfer_ownership_deadline","outputs":[{"type":"uint256","unit":"sec","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2201},{"name":"future_A","outputs":[{"type":"uint256","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2231},{"name":"future_fee","outputs":[{"type":"uint256","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2261},{"name":"future_admin_fee","outputs":[{"type":"uint256","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2291},{"name":"future_owner","outputs":[{"type":"address","name":"out"}],"inputs":[],"constant":True,"payable":False,"type":"function","gas":2321}])