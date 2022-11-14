from aiogram.dispatcher.filters import Text
from dispatcher import dp, bot, BotDB
from data import buttons as btn
from .decorators import admin
from aiogram import types


# Sending messages
@dp.message_handler(commands='sendall')
@admin
async def sendall(message: types.Message):
	''' Sending messages to all users with a check for activity '''
	text = message.text[9:]
	users = BotDB.get_users()
	for user in users:
		try:
			await bot.send_message(user[0], text)
			if int(user[1]) != 1:
				BotDB.set_active(user[0], 1)
		except:
			BotDB.set_active(user[0], 0)


# Getting statistics
@dp.message_handler(commands='static')
@admin
async def static(message: types.Message):
	''' Getting statistics about bot users '''
	card = f'''
Добавились в бота: {BotDB.all_users()}
Подписчиков в боте: {BotDB.all_active()}'''
	await bot.send_message(
		chat_id=message.from_user.id, 
        text=card)


