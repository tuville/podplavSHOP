import sqlite3 as sq
from aiogram.types import MediaGroup

from config import bot


def sqlDB_catalogRB_start():
    global base, cur
    base = sq.connect("catalog_rb.db")
    cur = base.cursor()
    if base:
        print("База данных подключена успешно!")
    base.execute('CREATE TABLE IF NOT EXISTS catalog (img1 TEXT, img2 TEXT, img3 TEXT, img4 TEXT,'
                 ' name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

async def sqlDB_catalogRB_add(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO catalog VALUES (?,?,?,?,?,?,?)', tuple(data.values()))
        base.commit()

async def sqlDB_catalogRB_read(message):
    for ret in cur.execute('SELECT * FROM catalog').fetchall():
        photoCatalog = MediaGroup()
        photoCatalog.attach_photo(ret[0])
        photoCatalog.attach_photo(ret[1])
        photoCatalog.attach_photo(ret[2])
        photoCatalog.attach_photo(ret[3], caption=f'<b>{ret[4]}</b>\n\n'
                                                    f'<b>📋 Описание:</b> {ret[5]}\n\n'
                                                    f'<b>💰 Цена:</b> {ret[-1]} RUB')
        await message.answer_media_group(photoCatalog)

async def sqlDB_catalogRB_read_to_delete():
    return cur.execute('SELECT * FROM catalog').fetchall()


async def sqlDB_catalogRB_delete_command(data):
    cur.execute('DELETE FROM catalog WHERE name == ?', (data,))
    base.commit()