from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from data.data import huobi_banks, binance_banks


# Subscribe Inlime Buttons
subscibe = InlineKeyboardButton('Подписаться ✏️', url='https://t.me/veneraclub', callback_data='subscibe')
get_subscibe = InlineKeyboardButton('Уже Подписался 📝', callback_data='get_subscibe')
subscibeMenu = InlineKeyboardMarkup().add(subscibe, get_subscibe)


# Start Buttons
check_button = InlineKeyboardButton('Check 🤖', callback_data='check')
faq_button = InlineKeyboardButton('FAQ ❓', callback_data='faq')
startMenu = InlineKeyboardMarkup(row_width=2).add(
	check_button,
	faq_button)


# Menu Button
''' Back Button In State'''
menuS_button = InlineKeyboardButton('Menu 🗒', callback_data='menuS')
mainSMenu = InlineKeyboardMarkup(row_width=2).add(menuS_button)

''' Back Button '''
menu_button = InlineKeyboardButton('Menu 🗒', callback_data='menu')
mainMenu = InlineKeyboardMarkup(row_width=2).add(menu_button)


# Exchange Buttons
binance_button = InlineKeyboardButton('Binance 🟠', callback_data='binance')
huobi_button = InlineKeyboardButton('Huobi 🟢', callback_data='huobi')
exchangeMenu = InlineKeyboardMarkup(row_width=2).add(
	binance_button, 
	huobi_button,
	menuS_button)


# Action Buttons 
buy_button = InlineKeyboardButton('📥 Buy', callback_data='buy')
sell_button = InlineKeyboardButton('📤 Sell', callback_data='sell')
actionMenu = InlineKeyboardMarkup(row_width=2).add(
	buy_button, 
	sell_button,
	menuS_button)


# Banks Buttons
def bankMenu(exchange):
	''' Return Banks Name as Inline Button '''
	menu = InlineKeyboardMarkup()
	match exchange:
		case 'binance':
			for bank in binance_banks():
				menu.insert(InlineKeyboardButton(
					text=bank, 
					callback_data=f'bank:{bank}'))
		case 'huobi':
			for bank in huobi_banks.items():
				menu.insert(InlineKeyboardButton(
					text=bank[0],
					callback_data=f'bank:{bank[1]}'))

	menu.insert(menuS_button)
	return menu


