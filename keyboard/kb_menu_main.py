from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#Переменные для кнопок
catalog_name_btn = '🗂 Каталог'
buy_name_btn = '🛒 Купить'
delivery_name_btn = '💰 Оплата и доставка 📦'
size_name_btn = '📐 Таблица размеров'
contact_name_btn = '📞 Наши контакты'
yes_name_btn = '👍 Да'
not_name_btn = '👎 Нет'
menu_name_btn = '💤 Основное меню'
cancelUser_name_btn = '❌ Отменить оформление заказа'
info_name_btn = "❗Важно"


#Основное меню
btn_1 = KeyboardButton(catalog_name_btn)
btn_2 = KeyboardButton(buy_name_btn)
btn_3 = KeyboardButton(delivery_name_btn)
btn_4 = KeyboardButton(size_name_btn)
btn_5 = KeyboardButton(contact_name_btn)
btn_6 = KeyboardButton(info_name_btn)

kb_menu_user = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
kb_menu_user.row(btn_1, btn_2).row(btn_3, btn_4).row(btn_5, btn_6)

# Отмена заказа
cancelUserBNT = KeyboardButton(cancelUser_name_btn)
kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(cancelUserBNT)

#Стартовое меню Инлайн
inbtn_yes = InlineKeyboardButton(text=yes_name_btn, callback_data='start_yes')
inbtn_not = InlineKeyboardButton(text=not_name_btn, callback_data='start_not')
kbIn_start = InlineKeyboardMarkup(row_width=2).add(inbtn_yes,inbtn_not)

#Запрос телефона
btn_sendPhone = KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
kb_sendPhone = ReplyKeyboardMarkup().add(btn_sendPhone).add(cancelUserBNT)
