import configparser
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# ==================== Take date in config ======================
config = configparser.ConfigParser()
config.read("config.ini")

TOKEN = config['bot_token']['TOKEN']
# ===============================================================
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
