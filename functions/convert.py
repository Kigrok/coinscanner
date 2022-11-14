from data.headers import huobi_headers
import requests, json

""" Converting Functions """

# Coin price search in Binance
def get_price(coin):
	''' Get coin market price in Binance '''
	match coin:
		case 'USDT':
			return '1.00'
		case _:
			if coin == 'RUB':
				params={'symbol' : f'USDT{coin}'}
			else:
				params={'symbol' : f'{coin}USDT'}
			response=requests.get('https://api.binance.com/api/v3/avgPrice', params=params).json()
			return float(response['price'])


# Get convert coin to USDT in Binance 
def conver_binance(coin, price):
	''' Convert coin to USDT
		ad price / price coin in Binance or 
		ad price * price coin in Binance '''
	match coin:
		case 'RUB':
			result=float(price)*float(get_price(coin=coin))
		case _:
			result=float(price)/float(get_price(coin=coin))
	return float(result)


# Get convert coin to USDT in Huobi 
def convert_huobi(coin, price, volume, action):
	''' Convert coin to USDT
		If sell, volume / ad price and add result in Huobi Convert,
		If buy, 100 USDT / Coin in Huobi Convert and result * ad price and / 100 '''
	match coin:
		case 'USDT':
			result=price
		case _:
			if action == 'sell':
				value=volume/price
				if value < 1: number=6
				else: number=3
				response=requests.get(f'https://otc-api.trygofast.com/v1/trade/exchange/quote?quoteAsset={coin.strip()}&cryptoAsset=USDT&side=buy&amount={str(round(float(value), number))}&type=amount&currency=cny', 
					headers=huobi_headers, 
					timeout=10).json()['data'][0]
				result=float(volume)/float(response['quantity'])
			else:
				response=requests.get(f'https://otc-api.trygofast.com/v1/trade/exchange/quote?quoteAsset=USDT&cryptoAsset={coin.strip()}&side=buy&amount=100&type=amount&currency=cny', 
					headers=huobi_headers, 
					timeout=10).json()['data'][0]
				result=(float(response['quantity'])*float(price))/100
	return float(result)