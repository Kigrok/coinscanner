from data.headers import binance_headers
import requests, json


""" Banks in crypto exchanges """

# Buttons Banks name in Huobi
huobi_banks={
	'QIWI': 9,
	'Yandex': 19,
	'ADVCash': 20,
	'PAYEER': 24,
	'Alfa-bank': 25,
	'VTB BANK': 27,
	'Tinkoff': 28,
	'Sberbank': 29,
	'Raiffeisenbank': 36,
	'SBP - Fast Bank Transfer': 69,
	'Otkritie Bank': 103,
	'Home Credit Bank': 172,
	'Ak Bars Bank': 176,
	'Gazprombank': 351,
	'MTS-Bank': 356,
	'Post Bank': 357,
	'Rosbank': 358,
	'Rosselkhozbank': 359
	}


# Buttons Banks name in Binance
def binance_banks():
	''' Get banks list in Binance '''
	bank=[]
	r=requests.post('https://p2p.binance.com/bapi/c2c/v2/public/c2c/adv/filter-conditions', 
		headers=binance_headers, 
		json={'fiat': 'RUB' }, 
		timeout=10).json()
	for i in r['data']['tradeMethods']:
		bank.append(i['identifier'])
	return(bank)


""" Data """

# Coin in crypto exchange 
binance_coins={'USDT', 'BTC', 'BUSD', 'BNB', 'ETH', 'RUB', 'SHIB'}
huobi_coins={'BTC': 1, 'ETH': 3, 'USDT': 2, 'LTC': 8, 'HT': 4, 'HUSD': 6, 'EOS': 5, 'XRP': 7}


# Data for Binance
def binance_data(coin='USDT', fiat='RUB', action='BUY', volume='1000', bank='QIWI'):
	''' Return Binance data '''
	data={
		'proMerchantAds': 'false',
		'page': 1,
		'rows': 1,
		'payTypes':[f'{bank}'],
		'countries':[],
		'publisherType': None,
		'asset': f'{coin}',
		'fiat': f'{fiat}',
		'merchantCheck': 'true',
		'tradeType': f'{action}',
		'transAmount': f'{volume}'
		}
	return data


