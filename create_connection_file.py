#  ModuleNotFoundError: No module named 'aiogram'
# if the .bat file not start bor by first start inpot this string: python -m pip install -U aiogram

import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

storage = MemoryStorage()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
