from aiogram.dispatcher.filters import Text, CommandStart, CommandHelp
from aiogram.dispatcher import FSMContext
from dispatcher import dp, bot, BotDB 
from .decorators import check_sub
from data import messages as msg
from data import buttons as btn
from aiogram import types


# Start Message
@dp.message_handler(CommandStart())
@check_sub
async def start(message: types.Message):
    ''' Selecting a function in a bot '''
    if (not BotDB.user_exists(user_id=message.from_user.id)):
        BotDB.add_user(user_id=message.from_user.id)
    try:
        await bot.delete_message(message.from_user.id, message.message.message_id)
    except:
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(
        chat_id=message.from_user.id, 
        text=msg.start_msg,
        reply_markup=btn.startMenu)


# Back In Menu In State
@check_sub
@dp.callback_query_handler(text='menuS', state='*')
async def back_state(message: types.Message, state: FSMContext):
    ''' Back in Main Menu if State '''
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(
        chat_id=message.from_user.id, 
        text=msg.start_msg,
        reply_markup=btn.startMenu)


# Back In Menu And Get Subscribe
@check_sub
@dp.callback_query_handler(text='get_subscibe')
@dp.callback_query_handler(text='menu')
async def back(message: types.Message):
    ''' Back in Main Menu and 
        Channel subscription check button '''
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(
        chat_id=message.from_user.id, 
        text=msg.start_msg,
        reply_markup=btn.startMenu)


# FAQ and Help Message
@dp.callback_query_handler(text='faq')
@dp.message_handler(CommandHelp())
async def help(message: types.Message):
    ''' Return Help Message '''
    try:
        await bot.delete_message(message.from_user.id, message.message.message_id)
    except:
        await bot.delete_message(message.chat.id, message.message_id)
    await bot.send_message(
        chat_id=message.from_user.id, 
        text=msg.help_msg,
        disable_web_page_preview=True,
        reply_markup=btn.mainMenu)

