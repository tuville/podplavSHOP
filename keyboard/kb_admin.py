from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Переменные для кнопок
load_name_btn = '♻️ Загрузить'
delete_name_btn = '❌ Удалить'
cancel_name_btn = '↪️ Отменить'
look_catalog_name_btn = '🗒 Каталог'
back_menu_btn = "⚙️ Основное меню"

#Меню для редактирования каталога
btn_load = KeyboardButton(load_name_btn)
btn_delete = KeyboardButton(delete_name_btn)
btn_look_catalog = KeyboardButton(look_catalog_name_btn)
btn_cancelLoad = KeyboardButton(cancel_name_btn)
btn_backMenu = KeyboardButton(back_menu_btn)

kb_menu_admin = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)\
    .row(btn_load, btn_delete).row(btn_cancelLoad,btn_look_catalog).add(btn_backMenu)