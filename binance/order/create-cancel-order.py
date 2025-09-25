import ccxt.pro
from pprint import pprint
from asyncio import run
import os
import sys


print('CCXT Version:', ccxt.__version__)


async def main():
    exchange = ccxt.pro.binance({
    'apiKey': os.getenv('BINANCE_API_KEY'),
    'secret': os.getenv('BINANCE_SECRET'),
    'options': {
        'defaultType': 'spot',
    },
    })
    exchange.set_sandbox_mode(True)
    markets = await exchange.load_markets()

    # exchange.verbose = True  # uncomment for debugging purposes if necessary

    symbol = 'ETH/USDT'
    type = 'market'  # or 'market'
    side = 'sell'  # or 'buy'
    amount = 0.002
    price = None  # or None

    order = await exchange.create_order(symbol, type, side, amount, price)
    #canceled = await exchange.cancel_order(order['id'], order['symbol'])

    pprint(order)

    await exchange.close()


run(main())

