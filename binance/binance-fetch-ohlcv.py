# -*- coding: utf-8 -*-

import os
import sys
import asciichartpy as asciichart  # 注意是 asciichartpy


# -----------------------------------------------------------------------------

this_folder = os.path.dirname(os.path.abspath(__file__))
root_folder = os.path.dirname(os.path.dirname(this_folder))
sys.path.append(root_folder + '/python')
sys.path.append(this_folder)

# -----------------------------------------------------------------------------

import ccxt  # noqa: E402

# -----------------------------------------------------------------------------

binance = ccxt.binance()
symbol = 'BTC/USDT'
timeframe = '1m'

# each ohlcv candle is a list of [ timestamp, open, high, low, close, volume ]
index = 4  # use close price from each ohlcv candle

height = 15
length = 80


def print_chart(exchange, symbol, timeframe):

    print("\n" + exchange.name + ' ' + symbol + ' ' + timeframe + ' chart:')

    # get a list of ohlcv candles
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)

    # get the ohlCv (closing price, index == 4)
    series = [x[index] for x in ohlcv]

    # print the chart
    print("\n" + asciichart.plot(series[-length:], {'height': height}))  # print the chart

    last = ohlcv[len(ohlcv) - 1][index]  # last closing price
    return ohlcv



import plotly.graph_objects as go
import pandas as pd
df = pd.DataFrame(print_chart(binance, symbol, timeframe))
df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
df['Date'] = pd.to_datetime(df['Date'], unit='ms')
# 假设 df 包含 [Date, Open, High, Low, Close]
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open'], high=df['High'],
    low=df['Low'], close=df['Close']
)])
fig.update_layout(title="股票蜡烛图", xaxis_rangeslider_visible=False)
fig.show()

