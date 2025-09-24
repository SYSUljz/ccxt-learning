# -*- coding: utf-8 -*-

import os
import sys
from pprint import pprint

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root + '/python')

import ccxt  # noqa: E402

print('CCXT Version:', ccxt.__version__)

exchange = ccxt.binance({
    'apiKey': os.getenv('BINANCE_API_KEY'),
    'secret': os.getenv('BINANCE_SECRET'),
    'options': {
        'defaultType': 'spot',
    },
})

exchange.set_sandbox_mode(True)  # comment if you're not using the testnet
markets = exchange.load_markets()
exchange.verbose = True  # debug output

balance = exchange.fetch_balance()
pprint(balance['ETH'])
open_orders = exchange.fetch_open_orders('ETH/USDT')
pprint(open_orders)