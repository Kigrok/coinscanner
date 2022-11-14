from data.config import CHANNEL, ADMIN
from data.messages import sub_msg
from data import buttons as btn
from dispatcher import bot


# Get status users in channel
def get_sub(chat_member):
    ''' Checking a user's status in a channel '''
    if chat_member['status'] == 'left':
        return True


# Get user's subscription in channel
def check_sub(func):
    ''' Checking a user's subscription to a channel ''' 
    async def wrapper(message):
        if get_sub(await bot.get_chat_member(chat_id=CHANNEL, user_id=message.from_user.id)):
            return await bot.send_message(
                chat_id=message.from_user.id, 
                text=sub_msg,
                reply_markup=btn.subscibeMenu)
        return await func(message)
    return wrapper


# Administrator Check
def admin(func):
    ''' Checking 'Administrator' Status '''
    async def wrapper(message):
        if int(message['from']['id']) != int(ADMIN) :
            return await message.reply('Access Denied', reply=False)
        return await func(message)
    return wrapper