import ccxt
from config import API_KEY,API_SECRET
symbol = 'ZRX/USDT:USDT'

exchange_id = 'bybit'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})

exchange.set_sandbox_mode(True)

exchange.options['defaultType'] = 'future'
exchange.load_markets ()

response = exchange.fetchBalance()
print(response['USDT'])

