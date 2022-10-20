from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/load')
# b2 = KeyboardButton('photo')
# b3 = KeyboardButton('name')
# b4 = KeyboardButton('description')
# b5 = KeyboardButton('price')
b6 = KeyboardButton('cancel')
b7 = KeyboardButton('/delete')

#  resize_keyboard - resize button by screen gadgets
#  one_time_keyboard - hides buttons after one call
kb_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

#  add - adds a button to the full width of the screen
#  insert - adds a button to an existing button in a row
kb_admin.row(b1, b6).row(b7)
# kb_admin.row(b1, b2, b3).row(b4, b5, b6)

#  row - add buttons in a row
# kb_client.row(b1, b2, b3)
