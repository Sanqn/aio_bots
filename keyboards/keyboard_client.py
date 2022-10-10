from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/menu')
b2 = KeyboardButton('/location')
b3 = KeyboardButton('/time_work')

b4 = KeyboardButton('share my phone number', request_contact=True)
b5 = KeyboardButton('share my location', request_location=True)

#  resize_keyboard - resize button by screen gadgets
#  one_time_keyboard - hides buttons after one call
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

#  add - adds a button to the full width of the screen
#  insert - adds a button to an existing button in a row
kb_client.add(b1).insert(b2).insert(b3).row(b4, b5)

#  row - add buttons in a row
# kb_client.row(b1, b2, b3)