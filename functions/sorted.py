from data.data import binance_coins, huobi_coins
from functions.search import binance, huobi


# Add Binance Ads in List
async def binance_list(action, volume, bank):
	''' Retun in "price_list" Binance Ads '''
	price_list=[]
	for coin in binance_coins:
		price_list.append(
			await binance(
				coin=coin,
				action=action,
				volume=volume,
				bank=bank))
	return price_list


# Add Huobi Ads in List
async def huobi_list(action, volume, bank):
	''' Retun in "price_list" Huobi Ads '''
	match action:
		case 'buy': action='sell'
		case _: action='buy'
	price_list=[]
	for coin in huobi_coins.items():
		ad=await huobi(
			coin=coin,
			action=action,
			bank=bank,
			volume=volume
			)
		if ad != None: price_list.append(ad)
	return price_list


# Sorted Ads
def sorted_ads(action, ads):
	''' Sorted Ads by USDT key'''
	match  action:
		case 'sell':
			result=sorted(ads, key=lambda d:d['USDT'], reverse=True)
		case _:
			result=sorted(ads, key=lambda d:d['USDT'])
	return result[0]
	

# Bringing out the best
async def checker(exchange, action, volume, bank):
	''' Comparing the prices of all ads and displaying the best '''
	match exchange:
		case 'binance':
			price_list = await binance_list(
				action=action,
				volume=volume,
				bank=bank)
		case 'huobi':
			price_list = await huobi_list(
				action=action,
				volume=volume,
				bank=bank)
	return sorted_ads(action=action, ads=price_list)


