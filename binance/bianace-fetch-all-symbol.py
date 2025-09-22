import ccxt

# 选择交易所
exchange = ccxt.binance()  # 例如 Binance

# 加载交易所所有市场
markets = exchange.load_markets()

# 获取所有 symbol 列表
symbols = list(markets.keys())

print(f"总共交易对数量: {len(symbols)}")
print(symbols)  # 打印所有 symbol