from aiogram.utils import executor
from config import dp
from data_base import db_script
from aiogram import types

async def on_statUp (_):
    print("Пуск бота произошел УСПЕШНО!")
    db_script.sqlDB_catalogRB_start()

from handlers import user_handler_md, admin_handler_md, checkout_handler_md

user_handler_md.register_handlers_user(dp)
admin_handler_md.register_handlers_admin(dp)
checkout_handler_md.register_handlers_checkout(dp)

@dp.message_handler()
async def empty_us(message: types.Message):
    await message.answer("Нет такой команды, ПОЛЬЗУЙТЕСЬ МЕНЮ")

executor.start_polling(dp, skip_updates=True, on_startup=on_statUp)