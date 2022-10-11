# This multy page file with many imports!!!!!!!!!!!!!!!!!!!!!
# dir handlers, create_connection_file.py


from aiogram.utils import executor
from create_connection_file import dp
from handlers import client, other, admin
from data_base import db


# ==================== Client part ======================
async def on_startup(_):
    print('Bot started')
    db.sql_db_start()


async def on_shutdown(_):
    print('Bot shutdown')


client.register_client_handlers(dp)
admin.register_admin_handlers(dp)
other.register_other_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup,
                       on_shutdown=on_shutdown)  # if bot ofline, don't get message after run bot
