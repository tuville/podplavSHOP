from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import dp, bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from data_base import db_script
from keyboard import kb_admin, kb_menu_main
from keyboard.kb_admin import kb_menu_admin
from keyboard.kb_menu_main import kb_menu_user
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, MediaGroup
from handlers import user_handler_md

ID = [892004718, 1022760278] #мой

class FSMAdmin(StatesGroup):
    photo1 = State()
    photo2 = State()
    photo3 = State()
    photo4 = State()
    name = State()
    description = State()
    price = State()

# Проверка пользователя на права администратора
async def check_root_admin (message: types.Message):
    if message.from_user.id in ID:
        await bot.send_message(message.from_user.id, f"Что тебе нужно, <b>барон {message.from_user.first_name}?</b> 🤠 🤠 🤠", reply_markup=kb_menu_admin)
    else:
        await bot.send_message(message.from_user.id, f"👮‍ ️👮‍ ️👮‍ ️КАРАУЛ!!! ️👮‍ ️👮‍ ️👮‍\n{message.from_user.first_name}, "
                                                     f"у Вас нет прав администратора, вернитесь в основное меню!!!"
                                                     f"", reply_markup=kb_menu_user)

# Начало диалога загрузки нового пункта в каталоге
async def start_load_catalog(message: types.Message):
    if message.from_user.id in ID:
        await FSMAdmin.photo1.set()
        await message.answer("1️⃣ <b>Шаг 1.</b> Загрузи фотографию #1 товара")
    else:
        await bot.send_message(message.from_user.id, f"👮‍ ️👮‍ ️👮‍ ️КАРАУЛ!!! ️👮‍ ️👮‍ ️👮‍\n{message.from_user.first_name}, "
                                                     f"у Вас нет прав администратора, вернитесь в основное меню!!!"
                                                     f"", reply_markup=kb_menu_user)

# Отмена загрузки
async def cancel_load (message: types.Message, state = FSMContext):
    if message.from_user.id in ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.answer("❌ ❌ ❌ <b>Загрузка ОТМЕНЕНА!</b> ❌ ❌ ❌", reply_markup=kb_menu_user)

async def load_photo1(message: types.Message, state: FSMContext):
    if message.from_user.id in ID:
        async with state.proxy() as data:
            data['photo1'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer("Загрузи фотографию #2 товара")

async def load_photo2(message: types.Message, state: FSMContext):
    if message.from_user.id in ID:
        async with state.proxy() as data:
            data['photo2'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer("Загрузи фотографию #3 товара")

async def load_photo3(message: types.Message, state: FSMContext):
    if message.from_user.id in ID:
        async with state.proxy() as data:
            data['photo3'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer("Загрузи фотографию #4 товара")

async def load_photo4(message: types.Message, state: FSMContext):
    if message.from_user.id in ID:
        async with state.proxy() as data:
            data['photo5'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer("2️⃣ <b>Шаг 2.</b> Напишите название товара")

# Загрузили фото, ловим второй ответ и записываем наименование
async def load_name (message: types.Message, state: FSMContext):
    if message.from_user.id in ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.answer("3️⃣ <b>Шаг 3.</b> Напишите описание товара")

# Записали наименование, ловим третий ответ и записываем описание товара
async def load_description (message: types.Message, state: FSMContext):
    if message.from_user.id in ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.answer("4️⃣ <b>Шаг 4.</b> Напишите цену товара")

# Записали описание, ловим четвертый записываем цену
async def load_price (message: types.Message, state: FSMContext):
    if message.from_user.id in ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await db_script.sqlDB_catalogRB_add(state)
        await state.finish()
        await message.answer("✅ ✅ ✅ Товар успешно загружен! 🥳 🥳 🥳")

@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run (callback_query: types.CallbackQuery):
    await db_script.sqlDB_catalogRB_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)

async def delete_item(message: types.Message):
    if message.from_user.id in ID:
        read = await db_script.sqlDB_catalogRB_read_to_delete()
        for ret in read:
            await message.answer(f'{ret[4]}\n'
                                 f'Цена: {ret[-1]}', reply_markup=InlineKeyboardMarkup().\
                    add(InlineKeyboardButton(f"Удалить {ret[4]}", callback_data=f'del {ret[4]}')))
    else:
        await message.answer(f"👮‍ ️👮‍ ️👮‍ ️КАРАУЛ!!! ️👮‍ ️👮‍ ️👮‍\n{message.from_user.first_name}, "
                            f"у Вас нет прав администратора, вернитесь в основное меню!!!", reply_markup=kb_menu_user)

async def buttonAdmin_catalog(message: types.Message):
    await user_handler_md.button_catalog(message)

async def backMainMenu(message: types.Message):
    await user_handler_md.button_main_menu(message)

def register_handlers_admin (dp: Dispatcher):
    dp.register_message_handler(check_root_admin, commands=['admin'])
    dp.register_message_handler(start_load_catalog, Text(equals=kb_admin.load_name_btn, ignore_case=True))
    dp.register_message_handler(cancel_load,Text(equals=kb_admin.cancel_name_btn, ignore_case=True), state="*")
    dp.register_message_handler(load_photo1, content_types=['photo'], state=FSMAdmin.photo1)
    dp.register_message_handler(load_photo2, content_types=['photo'], state=FSMAdmin.photo2)
    dp.register_message_handler(load_photo3, content_types=['photo'], state=FSMAdmin.photo3)
    dp.register_message_handler(load_photo4, content_types=['photo'], state=FSMAdmin.photo4)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_item, Text(equals=kb_admin.delete_name_btn, ignore_case=True))
    dp.register_message_handler(buttonAdmin_catalog, Text (equals=kb_menu_main.catalog_name_btn, ignore_case=True))
    dp.register_message_handler(backMainMenu, Text(equals=kb_menu_main.menu_name_btn, ignore_case=True))