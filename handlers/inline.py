import hashlib
from aiogram import types, Dispatcher
from create_connection_file import dp, bot
from aiogram.types import InputTextMessageContent, InlineQueryResultArticle


# @dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = 'https://en.wikipedia.org/wiki/' + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()

    articles = [
        types.InlineQueryResultArticle(
            id=result_id,
            title='Page of Wikipedia',
            url=link,
            input_message_content=types.InputTextMessageContent(message_text=link))]
    await query.answer(articles, cache_time=1, is_personal=True)


def register_inline_handler(dp: Dispatcher):
    dp.register_inline_handler(inline_handler)
