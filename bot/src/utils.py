def decimals(currency):
    _mapping = {
        'dai': 10 ** 18,
        'usdc': 10 ** 6,
        'usdt': 10 ** 6
    }

    return _mapping[currency]


def address(currency):
    _mapping = {
        'dai':'0x6B175474E89094C44Da98b954EedeAC495271d0F',
        'usdc':'0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48',
        'usdt':'0xdAC17F958D2ee523a2206206994597C13D831ec7'
    }

    return _mapping[currency]