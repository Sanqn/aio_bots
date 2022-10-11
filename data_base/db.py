import sqlite3
from sqlite3 import Error
from create_connection_file import bot

con = None
cursor = None


def sql_db_start():
    global con, cursor
    con = sqlite3.connect('db_food.sqlite3')
    cursor = con.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS menu(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      photo TEXT,
      name TEXT UNIQUE,
      description TEXT,
      price TEXT
    )
    """
    try:
        if con:
            print('Connection to SQLite BD successfull')
        try:
            cursor.execute(query)
            con.commit()
            print('Table in BD created')
        except Error as e:
            print(f'Create table error {e}')
    except Error as e:
        print(f'Connection error {e}')


async def load_command_menu_db(state):
    async with state.proxy() as data:
        # print(tuple(data.values()))
        # print(data.values())
        # print('key', data.keys())
        # print('data', data)
        cursor.execute('INSERT INTO menu (photo, name, description, price) VALUES (?, ?, ?, ?)', tuple(data.values()))
        con.commit()


async def load_menu_from_db(message):
    # print(message)
    # print(message.from_user)
    # print(message.chat)
    # print(message.date)
    all_menu = cursor.execute('SELECT * FROM menu').fetchall()
    for rez in all_menu:
        # print('======================', rez, type(rez))
        # print(rez[1], rez[2], rez[3])
        await bot.send_photo(message.from_user.id, rez[1], f'{rez[2]}\nDescription - {rez[3]}\nPrice - {rez[-1]}')
