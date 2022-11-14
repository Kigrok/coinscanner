from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from dispatcher import dp, bot, BotDB
from functions.checker import check
from .decorators import check_sub
from data import messages as msg
from data import buttons as btn
from data.state import Forma
from aiogram import types


# Check Message
@check_sub
@dp.callback_query_handler(text='check')
async def get_check(call: types.CallbackQuery):
	''' Choise of Checker '''
	await Forma.exchange.set()
	await bot.delete_message(call.from_user.id, call.message.message_id)
	await bot.send_message(
        chat_id=call.message.chat.id,
        text=msg.exchange_msg,
        reply_markup=btn.exchangeMenu)


# Exchange Message
@check_sub
@dp.callback_query_handler(text=['binance', 'huobi'], state=Forma.exchange)
async def exchange(call: types.CallbackQuery, state: FSMContext):
	''' Choice of exchanges '''
	async with state.proxy() as data:
		data['exchange'] = call.data
	await Forma.next()
	await bot.delete_message(call.from_user.id, call.message.message_id)
	await bot.send_message(
        chat_id=call.message.chat.id,
        text=msg.action_msg,
        reply_markup=btn.actionMenu)


# Action Message
@check_sub
@dp.callback_query_handler(text=['buy', 'sell'], state=Forma.action)
async def action(call: types.CallbackQuery, state: FSMContext):
	''' Choice of action '''
	async with state.proxy() as data:
		data['action'] = call.data
	await Forma.next()
	await bot.delete_message(call.from_user.id, call.message.message_id)
	await bot.send_message(
        chat_id=call.message.chat.id,
        text=msg.bank_msg,
        reply_markup=btn.bankMenu(exchange=data['exchange']))


# Bank Message
@check_sub
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('bank'), state=Forma.bank)
async def bank(call: types.CallbackQuery, state: FSMContext):
	''' Choice of bank '''
	async with state.proxy() as data:
		data['bank'] = (call.data).split(':')[1]
	await Forma.next()
	await bot.delete_message(call.from_user.id, call.message.message_id)
	await bot.send_message(
        chat_id=call.message.chat.id,
        text=msg.volume_msg,
        reply_markup=btn.mainSMenu)


# Volume Message
@check_sub
@dp.message_handler(lambda message: message.text.isdigit(), state=Forma.volume)
async def volume(message: types.Message, state: FSMContext):
	''' Choice of volume '''
	if int(message.text) < 500 or int(message.text) > 1000000:
		await bot.send_message(
	        chat_id=message.from_user.id,
	        text=msg.volume_error_msg,
	        reply_markup=btn.mainSMenu)
	else:
		async with state.proxy() as data:
			data['volume'] = str(message.text)
		await state.finish()
		await bot.send_message(
	        chat_id=message.from_user.id,
	        text=msg.waiting_msg,
	        reply_markup=types.ReplyKeyboardRemove())
		await bot.delete_message(message.chat.id, message.message_id)
		await check(
			bot=bot,
			chat_id=message.chat.id,
			exchange=data['exchange'],
			action=data['action'], 
			volume=data['volume'],
			bank=data['bank'])
