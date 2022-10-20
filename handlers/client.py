from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from create_connection_file import dp, bot
from keyboards.keyboard_client import kb_client
from keyboards.kb_inline import kb_inline, kb_inline_call, kb_inline_callbask
from data_base import db

vote_answer = dict()


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


async def inline_button(message: types.Message):
    await message.answer('links', reply_markup=kb_inline)


# ==================================== CallbackQuery ================================================
async def inline_button_call(message: types.Message):
    await message.answer('push button', reply_markup=kb_inline_call)


@dp.callback_query_handler(text='push')  # answer on callback_data='push' in kb_inline.py file
async def call_answer_push(callback: types.CallbackQuery):
    # await callback.answer('Wow you push my button!!!!!!!!!!!')  # if call this command you get pop-up window
    await callback.message.answer(
        'Wow you push my button!!!!!!!!!!!')  # if call this command, you must call next callback
    # and you call pop-up window (You push this button) and Wow you push my button!!!!!!!!!!!
    await callback.answer('You push button', show_alert=True)


# ====================================================================================================

# ==================================== CallbackQueryAvoid ================================================
@dp.message_handler(commands=['vote'])
async def inline_button_call_vote(message: types.Message):
    await message.answer('Vote for product brand', reply_markup=kb_inline_callbask)


@dp.callback_query_handler(Text(startswith='vote_'))  # answer on callback_data='vote_'
async def call_answer_vote(callback: types.CallbackQuery):
    rez = callback.data.split('_')[1]
    if str(callback.from_user.id) not in vote_answer:
        vote_answer[f'{callback.from_user.id}'] = rez
        await callback.answer('You voted')
    else:
        await callback.answer('You have already voted', show_alert=True)


# ====================================================================================================


# @dp.message_handler(lambda message: message.text in ['menu'])
# @dp.message_handler(commands=['menu'])
async def push_menu(message: types.Message):
    await db.load_menu_from_db(message)


# ==================== Register all handlers for start in main file ======================
def register_client_handlers(dp: Dispatcher):
    # lambda message - invokes the command without /
    dp.register_message_handler(send_welcome, lambda message: message.text in ['start', 'help'])
    dp.register_message_handler(send_welcome, commands=['start', 'help'])
    dp.register_message_handler(location_command, lambda message: message.text in ['location'])
    dp.register_message_handler(location_command, commands=['location'])
    dp.register_message_handler(time_worl_commands, lambda message: message.text in ['time_work'])
    dp.register_message_handler(time_worl_commands, commands=['time_work'])
    dp.register_message_handler(inline_button, lambda message: message.text in ['Link', 'link'])
    dp.register_message_handler(inline_button, commands=['link'])
    dp.register_message_handler(inline_button_call, lambda message: message.text in ['Call', 'call'])
    dp.register_message_handler(inline_button_call, commands=['call'])
    dp.register_message_handler(push_menu, lambda message: message.text in ['menu'])
    dp.register_message_handler(push_menu, commands=['menu'])
