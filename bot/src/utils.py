def decimals(currency):
    if currency == 'dai': return 10 ** 18
    if currency == 'usdc': return 10 ** 6
    if currency == 'usdt': return 10 ** 6