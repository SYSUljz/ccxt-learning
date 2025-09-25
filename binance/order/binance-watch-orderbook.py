import os
import ccxt.pro
from asyncio import run

async def main():
    exchange = ccxt.pro.binance({
        'enableRateLimit': True,
        'options': {'defaultType': 'spot'}
    })
    exchange.set_sandbox_mode(True)
    await exchange.load_markets()

    while True:
        orderbook = await exchange.watch_order_book('ETH/USDT')
        print(exchange.iso8601(exchange.milliseconds()), 
              'ETH/USDT best:', orderbook['bids'][0], orderbook['asks'][0])

run(main())
