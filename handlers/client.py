from aiogram import types, Dispatcher
from create_connection_file import dp, bot
from keyboards.keyboard_client import kb_client


# ==================== Client part ======================
# @dp.message_handler(lambda message: message.text in ['start', 'help'])
# @dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               f"\nWhat do you want?", reply_markup=kb_client)  # reply_markup - add button on screen
        await message.delete()
    except:
        await message.answer("If you wanna continue, connect Footbot:\nhttps://t.me/aiomarketfoodbot")


# @dp.message_handler(lambda message: message.text in ['location'])
# @dp.message_handler(commands=['location'])
async def location_command(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Our location: NY, wolf st. 34-12. link:\nhttps://footbot.com/location')


# @dp.message_handler(lambda message: message.text in ['time_work'])
# @dp.message_handler(commands=['time_work'])
async def time_worl_commands(message: types.Message):
    await bot.send_message(message.from_user.id, "We work from 4 to 7 o'clock, seven days a week")


# ==================== Register all handlers for start in main file ======================
def register_client_handlers(dp: Dispatcher):
    # lambda message - invokes the command without /
    dp.register_message_handler(send_welcome, lambda message: message.text in ['start', 'help'])
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(location_command, lambda message: message.text in ['location'])
    dp.register_message_handler(location_command, commands=['location'])
    dp.register_message_handler(time_worl_commands, lambda message: message.text in ['time_work'])
    dp.register_message_handler(time_worl_commands, commands=['time_work'])
