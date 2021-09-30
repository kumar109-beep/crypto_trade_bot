import bybit
import time

apiKey = 'CMXc6s35y6lsh5pBWC'
secretKey = 'GAcyWZD08h6iuEarrlWe1HgXXTaT5fUoQ78y'


print('running ...')
client = bybit.bybit(test=False, api_key=apiKey, api_secret=secretKey)
# print(client.LinearOrder.LinearOrder_replace(symbol="BTCUSDT", order_id="").result())
# info = client.Market.Market_symbolInfo().result()
# # print(info)
# # keys = 
# btc = info[0]['result'][0]['last_price']
# print(btc)

# print(client.Wallet.Wallet_getBalance(coin="BTC").result())
print(client.LinearPositions.LinearPositions_saveLeverage(symbol='BTCUSDT', buy_leverage=10, sell_leverage=10).result())
# print(client.LinearOrder.LinearOrder_new(side="Sell",symbol="BTCUSDT",order_type="Limit",qty=1,price=btc,time_in_force="GoodTillCancel",reduce_only=False, close_on_trigger=False).result())
# print(client.Positions.Positions_myPosition(symbol="BTCUSDT").result())
# print(client.LinearPositions.LinearPositions_myPosition(symbol="BTCUSDT").result())


