import random
import json
import string
from aiogram import types, Dispatcher
import configparser
from create_connection_file import dp

# ==================== Take list answers in config ======================
config = configparser.ConfigParser()
config.read("./config.ini")
list_answers = config['list_answers']['list_answers']
list_answers = list_answers.split(',, ')
print(list_answers)


# ==================== Message part ======================
# @dp.message_handler()
async def echo_send(message: types.Message):  # listen users
    if message.text == 'hi' or message.text == 'Hi':
        await message.answer(f'{random.choice(list_answers)} :)')

    elif message.text == 'my name' or message.text == 'My name':
        if message.from_user.first_name:
            await message.answer(f'Your name is {message.from_user.first_name}')
        else:
            await message.answer(f'Your name is {message.from_user.username}')

    elif {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('./cuss1.json')))):
        await message.reply(f'Do not cuss, {message.from_user.username}!')
        await message.delete()

    else:
        await message.answer(message.text)


def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(echo_send)
