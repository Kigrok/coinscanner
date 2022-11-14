from handlers import actions, check, admin
from dispatcher import dp, bot
from aiogram import executor
import logging


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)