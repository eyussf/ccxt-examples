import ccxt

exchange_id = 'binance'
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

exchange.options['defaultType'] = 'future'

exchange.load_markets ()

symbol="ATOM/USDT"

positions = exchange.fetch_positions(symbols=[symbol])

for i in positions:
    side = i['side']
    symbol = i["info"]['symbol']
    amount = i["info"]['positionAmt']


    if side == 'long':

        exchange.create_order(symbol=symbol, side='sell', type='MARKET', amount=1000, params={'hedged': 'true', "positionSide":"LONG",'closePosition':'Close-All'})

    elif side == 'short':
        exchange.create_order(symbol=symbol, side='buy', type='MARKET', amount=1000, params={'hedged': 'true', "positionSide":"SHORT",'closePosition':'Close-All'})
        