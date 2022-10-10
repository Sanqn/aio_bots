from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_connection_file import dp, bot
from aiogram.dispatcher.filters import Text
from keyboards.keyboard_admin import kb_admin

ID = None


# States
class FormAdmin(StatesGroup):
    photo = State()  # Will be represented in storage as 'Form:name'
    name = State()  # Will be represented in storage as 'Form:name'
    description = State()  # Will be represented in storage as 'Form:age'
    price = State()  # Will be represented in storage as 'Form:gender'


#  Get id moderator
# @dp.message_handler(commands='moderator', is_chat_admin=True)
async def is_moderator(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Hi my moderator. What do you want?', reply_markup=kb_admin)
    await message.delete()


#  Starting a dialogue
# @dp.message_handler(commands='load', state=None)
async def start_admin_loader(message: types.Message):
    if message.from_user.id == ID:
        await FormAdmin.photo.set()
        await message.reply('Load your photo of food')


#  Out of state

# @dp.message_handler(state='*', commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cansel_load(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        # Cancel state and inform user about it
        await state.finish()
        await message.reply('load canceled')


#  Catch the first dict
# @dp.message_handler(content_types=['photo'], state=FormAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
            await FormAdmin.next()
            await message.reply('Input name food')


# @dp.message_handler(state=FormAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
            await FormAdmin.next()
            await message.reply('Input description')


# @dp.message_handler(state=FormAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
            await FormAdmin.next()
            await message.reply('Input price')


# @dp.message_handler(state=FormAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        async with state.proxy() as data:
            await message.reply(str(data))
            await state.finish()


# ==================== Register all handlers for start in main file ======================
def register_admin_handlers(dp: Dispatcher):
    dp.register_message_handler(is_moderator, commands='moderator', is_chat_admin=True)
    dp.register_message_handler(cansel_load, state='*', commands='cancel')
    dp.register_message_handler(cansel_load, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(start_admin_loader, commands='load', state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FormAdmin.photo)
    dp.register_message_handler(load_name, state=FormAdmin.name)
    dp.register_message_handler(load_description, state=FormAdmin.description)
    dp.register_message_handler(load_price, state=FormAdmin.price)

