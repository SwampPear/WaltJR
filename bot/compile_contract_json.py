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

create_json('rai', '0x618788357D0EBd8A37e763ADab3bc575D54c2C7d', [{"name":"TokenExchange","inputs":[{"name":"buyer","type":"address","indexed":True},{"name":"sold_id","type":"int128","indexed":False},{"name":"tokens_sold","type":"uint256","indexed":False},{"name":"bought_id","type":"int128","indexed":False},{"name":"tokens_bought","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"name":"TokenExchangeUnderlying","inputs":[{"name":"buyer","type":"address","indexed":True},{"name":"sold_id","type":"int128","indexed":False},{"name":"tokens_sold","type":"uint256","indexed":False},{"name":"bought_id","type":"int128","indexed":False},{"name":"tokens_bought","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"name":"AddLiquidity","inputs":[{"name":"provider","type":"address","indexed":True},{"name":"token_amounts","type":"uint256[2]","indexed":False},{"name":"fees","type":"uint256[2]","indexed":False},{"name":"invariant","type":"uint256","indexed":False},{"name":"token_supply","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"name":"RemoveLiquidity","inputs":[{"name":"provider","type":"address","indexed":True},{"name":"token_amounts","type":"uint256[2]","indexed":False},{"name":"fees","type":"uint256[2]","indexed":False},{"name":"token_supply","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"name":"RemoveLiquidityOne","inputs":[{"name":"provider","type":"address","indexed":True},{"name":"token_amount","type":"uint256","indexed":False},{"name":"coin_amount","type":"uint256","indexed":False},{"name":"token_supply","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"name":"RemoveLiquidityImbalance","inputs":[{"name":"provider","type":"address","indexed":True},{"name":"token_amounts","type":"uint256[2]","indexed":False},{"name":"fees","type":"uint256[2]","indexed":False},{"name":"invariant","type":"uint256","indexed":False},{"name":"token_supply","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"name":"CommitNewAdmin","inputs":[{"name":"deadline","type":"uint256","indexed":True},{"name":"admin","type":"address","indexed":True}],"anonymous":False,"type":"event"},{"name":"NewAdmin","inputs":[{"name":"admin","type":"address","indexed":True}],"anonymous":False,"type":"event"},{"name":"CommitNewFee","inputs":[{"name":"deadline","type":"uint256","indexed":True},{"name":"fee","type":"uint256","indexed":False},{"name":"admin_fee","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"name":"NewFee","inputs":[{"name":"fee","type":"uint256","indexed":False},{"name":"admin_fee","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"name":"RampA","inputs":[{"name":"old_A","type":"uint256","indexed":False},{"name":"new_A","type":"uint256","indexed":False},{"name":"initial_time","type":"uint256","indexed":False},{"name":"future_time","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"name":"StopRampA","inputs":[{"name":"A","type":"uint256","indexed":False},{"name":"t","type":"uint256","indexed":False}],"anonymous":False,"type":"event"},{"stateMutability":"nonpayable","type":"constructor","inputs":[{"name":"_owner","type":"address"},{"name":"_coins","type":"address[2]"},{"name":"_pool_token","type":"address"},{"name":"_base_pool","type":"address"},{"name":"_redemption_price_snap","type":"address"},{"name":"_A","type":"uint256"},{"name":"_fee","type":"uint256"},{"name":"_admin_fee","type":"uint256"}],"outputs":[]},{"stateMutability":"view","type":"function","name":"A","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":10374},{"stateMutability":"view","type":"function","name":"A_precise","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":10336},{"stateMutability":"view","type":"function","name":"get_virtual_price","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":2070135},{"stateMutability":"view","type":"function","name":"get_virtual_price_2","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":2295357},{"stateMutability":"view","type":"function","name":"calc_token_amount","inputs":[{"name":"_amounts","type":"uint256[2]"},{"name":"_is_deposit","type":"bool"}],"outputs":[{"name":"","type":"uint256"}],"gas":4038330},{"stateMutability":"nonpayable","type":"function","name":"add_liquidity","inputs":[{"name":"_amounts","type":"uint256[2]"},{"name":"_min_mint_amount","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":6231201},{"stateMutability":"view","type":"function","name":"get_dy","inputs":[{"name":"i","type":"int128"},{"name":"j","type":"int128"},{"name":"_dx","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":2483148},{"stateMutability":"view","type":"function","name":"get_dy_underlying","inputs":[{"name":"i","type":"int128"},{"name":"j","type":"int128"},{"name":"_dx","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":2494262},{"stateMutability":"nonpayable","type":"function","name":"exchange","inputs":[{"name":"i","type":"int128"},{"name":"j","type":"int128"},{"name":"_dx","type":"uint256"},{"name":"_min_dy","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":2723828},{"stateMutability":"nonpayable","type":"function","name":"exchange_underlying","inputs":[{"name":"i","type":"int128"},{"name":"j","type":"int128"},{"name":"_dx","type":"uint256"},{"name":"_min_dy","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":2754318},{"stateMutability":"nonpayable","type":"function","name":"remove_liquidity","inputs":[{"name":"_amount","type":"uint256"},{"name":"_min_amounts","type":"uint256[2]"}],"outputs":[{"name":"","type":"uint256[2]"}],"gas":174423},{"stateMutability":"nonpayable","type":"function","name":"remove_liquidity_imbalance","inputs":[{"name":"_amounts","type":"uint256[2]"},{"name":"_max_burn_amount","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":6216452},{"stateMutability":"view","type":"function","name":"calc_withdraw_one_coin","inputs":[{"name":"_token_amount","type":"uint256"},{"name":"i","type":"int128"}],"outputs":[{"name":"","type":"uint256"}],"gas":8658},{"stateMutability":"nonpayable","type":"function","name":"remove_liquidity_one_coin","inputs":[{"name":"_token_amount","type":"uint256"},{"name":"i","type":"int128"},{"name":"_min_amount","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":4009643},{"stateMutability":"nonpayable","type":"function","name":"ramp_A","inputs":[{"name":"_future_A","type":"uint256"},{"name":"_future_time","type":"uint256"}],"outputs":[],"gas":159429},{"stateMutability":"nonpayable","type":"function","name":"stop_ramp_A","inputs":[],"outputs":[],"gas":154890},{"stateMutability":"nonpayable","type":"function","name":"commit_new_fee","inputs":[{"name":"_new_fee","type":"uint256"},{"name":"_new_admin_fee","type":"uint256"}],"outputs":[],"gas":112848},{"stateMutability":"nonpayable","type":"function","name":"apply_new_fee","inputs":[],"outputs":[],"gas":103529},{"stateMutability":"nonpayable","type":"function","name":"revert_new_parameters","inputs":[],"outputs":[],"gas":22982},{"stateMutability":"nonpayable","type":"function","name":"commit_transfer_ownership","inputs":[{"name":"_owner","type":"address"}],"outputs":[],"gas":77020},{"stateMutability":"nonpayable","type":"function","name":"apply_transfer_ownership","inputs":[],"outputs":[],"gas":65697},{"stateMutability":"nonpayable","type":"function","name":"revert_transfer_ownership","inputs":[],"outputs":[],"gas":23072},{"stateMutability":"view","type":"function","name":"admin_balances","inputs":[{"name":"i","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":7928},{"stateMutability":"nonpayable","type":"function","name":"withdraw_admin_fees","inputs":[],"outputs":[],"gas":22177},{"stateMutability":"nonpayable","type":"function","name":"kill_me","inputs":[],"outputs":[],"gas":40355},{"stateMutability":"nonpayable","type":"function","name":"unkill_me","inputs":[],"outputs":[],"gas":23192},{"stateMutability":"view","type":"function","name":"coins","inputs":[{"name":"arg0","type":"uint256"}],"outputs":[{"name":"","type":"address"}],"gas":3277},{"stateMutability":"view","type":"function","name":"balances","inputs":[{"name":"arg0","type":"uint256"}],"outputs":[{"name":"","type":"uint256"}],"gas":3307},{"stateMutability":"view","type":"function","name":"fee","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3228},{"stateMutability":"view","type":"function","name":"admin_fee","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3258},{"stateMutability":"view","type":"function","name":"owner","inputs":[],"outputs":[{"name":"","type":"address"}],"gas":3288},{"stateMutability":"view","type":"function","name":"lp_token","inputs":[],"outputs":[{"name":"","type":"address"}],"gas":3318},{"stateMutability":"view","type":"function","name":"redemption_price_snap","inputs":[],"outputs":[{"name":"","type":"address"}],"gas":3348},{"stateMutability":"view","type":"function","name":"base_pool","inputs":[],"outputs":[{"name":"","type":"address"}],"gas":3378},{"stateMutability":"view","type":"function","name":"base_virtual_price","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3408},{"stateMutability":"view","type":"function","name":"base_cache_updated","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3438},{"stateMutability":"view","type":"function","name":"base_coins","inputs":[{"name":"arg0","type":"uint256"}],"outputs":[{"name":"","type":"address"}],"gas":3577},{"stateMutability":"view","type":"function","name":"initial_A","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3498},{"stateMutability":"view","type":"function","name":"future_A","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3528},{"stateMutability":"view","type":"function","name":"initial_A_time","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3558},{"stateMutability":"view","type":"function","name":"future_A_time","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3588},{"stateMutability":"view","type":"function","name":"admin_actions_deadline","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3618},{"stateMutability":"view","type":"function","name":"transfer_ownership_deadline","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3648},{"stateMutability":"view","type":"function","name":"future_fee","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3678},{"stateMutability":"view","type":"function","name":"future_admin_fee","inputs":[],"outputs":[{"name":"","type":"uint256"}],"gas":3708},{"stateMutability":"view","type":"function","name":"future_owner","inputs":[],"outputs":[{"name":"","type":"address"}],"gas":3738}])