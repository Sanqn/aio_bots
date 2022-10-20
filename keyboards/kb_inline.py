from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_inline = InlineKeyboardMarkup(row_width=2)

b1 = InlineKeyboardButton(text='google', url='https://google.com')
b2 = InlineKeyboardButton(text='yandex', url='https://yandex.ru')
links = [InlineKeyboardButton(text='youtube', url='https://youtube.ru'),
         InlineKeyboardButton(text='mail', url='https://mail.com'),
         InlineKeyboardButton(text='gitgub', url='https://github.com')
         ]
kb_inline.add(b1, b2).row(*links).insert(InlineKeyboardButton(text='jomm', url='https://joom.com'))

kb_inline_call = InlineKeyboardMarkup(row_width=1)
b_c1 = InlineKeyboardButton(text='push', callback_data='push')
kb_inline_call.add(b_c1)

c_b1 = InlineKeyboardButton(text='yes', callback_data='vote_yes')
c_b2 = InlineKeyboardButton(text='no', callback_data='vote_no')

kb_inline_callbask = InlineKeyboardMarkup(row_width=2)
kb_inline_callbask.add(c_b1, c_b2)

