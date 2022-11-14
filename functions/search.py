from functions.convert import conver_binance, convert_huobi
from data.headers import binance_headers
from data.data import binance_data
import requests, json


""" Functions Search Ad """

# Ad Search in Binance
async def binance(action='BUY', coin='USDT', volume='1000', bank='QIWI'):
	''' Search ads on p2p Binance according to specified criteria '''
	response=requests.post(
		'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', 
		headers=binance_headers, 
		json=binance_data(
			coin=coin, 
			action=action,
			volume=volume,
			bank=bank), 
		timeout=10).json()
	item=response['data'][0]
	if item['advertiser']['userGrade'] > 2:
		merch='\U00002714'
	else:
		merch=''
	bank=[]
	for b in item['adv']['tradeMethods']:
		bank.append(b['tradeMethodName'])
	return result(
		exchange="<a href='https://www.binance.info/ru/activity/referral-entry/CPA?fromActivityPage=true&ref=CPA_00P2G3TCHK'>Binance</a>",
		action=action,
		price=float(item['adv']['price']),
		coin=coin,
		usdt=conver_binance(
			coin=coin,
			price=float(item['adv']['price'])),
		user=f"<a href='https://p2p.binance.com/ru/advertiserDetail?advertiserNo={item['advertiser']['userNo']}'>{item['advertiser']['nickName']}</a>",
		orders=item['advertiser']['monthOrderCount'],
		reating=round(float((item['advertiser']['monthFinishRate'])*100), 2),
		minLimit=item['adv']['minSingleTransAmount'],
		maxLimit=item['adv']['maxSingleTransAmount'],
		merch=merch, 
		bank=bank)


# Ad Search in Huobi
async def huobi(coin, action, bank, volume):
	''' Search ads on p2p Huobi according to specified criteria '''
	try:
		response=requests.get(f'https://otc-api.trygofast.com/v1/data/trade-market?coinId={coin[1]}&currency=11&tradeType={action}&currPage=1&payMethod={bank}&acceptOrder=0&country=&blockType=general&online=1&range=0&amount={volume}&onlyTradable=false&isFollowed=false').json()['data']
		for i in response:
			banks=[]
			for x in i['payMethods']:
				banks.append(x['name'])
			if i['merchantTags'] != 'None':
				merch='\U00002714'
			else:
				merch=''
			return result(
				exchange="<a href='https://www.huobi.com/ru-ru/v/register/double-invite/?invite_code=48vd5223&inviter_id=11345710'>Huobi</a>",
				action=action,
				price=i['price'],
				coin=coin[0],
				usdt=convert_huobi(
					coin=coin[0],
					price=float(i['price']),
					volume=float(volume),
					action=action),
				user=f"<a href='https://www.huobi.com/ru-ru/fiat-crypto/trader/{i['uid']}'>{i['userName']}</a>",
				orders=i['tradeMonthTimes'],
				reating=i['orderCompleteRate'],
				minLimit=i['minTradeLimit'],
				maxLimit=i['maxTradeLimit'],
				merch=merch,
				bank=banks)
	except: pass


# Changing the result format
def result(exchange, action, price, coin,
	usdt,user, orders, reating, 
	minLimit, maxLimit, merch, bank):
	''' Display ad search results in the correct format '''
	return {
		'Exchange': exchange,
		'Action': action,
		'Price': price,
		'Coin': coin,
		'USDT': (round(float(usdt), 2)),
		'User': user,
		'UserOrders': orders,
		'UserReating': reating,
		'MinLimit': minLimit,
		'MaxLimit': maxLimit,
		'Merchant': merch,
		'Bank': bank
		}