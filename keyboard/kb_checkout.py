from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboard.kb_menu_main import cancelUserBNT

#Переменные для кнопок - размеры
name_size_46 = "44/46"
name_size_48 = "46/48"
name_size_50 = "48/50"
name_size_52 = "50/52"
name_size_54 = "52/54"
name_size_58 = "56/58"

#Переменные для кнопок - рост
name_growth_0 = "0 // 0-158"
name_growth_1 = "1 // 159-164"
name_growth_2 = "2 // 165-170"
name_growth_3 = "3 // 171-176"
name_growth_4 = "4 // 177-182"
name_growth_5 = "5 // 183-188"
name_growth_6 = "6 // 189-195"
name_growth_7 = "7 // 196-202"

#Переменные для кнопок - Клеймения
name_brand_rb = "РБ"
name_brand_rb0 = "РБ-0"
name_brand_not = "Нет"

#Клавиатура - Размеры
btn_size_46 = KeyboardButton(name_size_46)
btn_size_48 = KeyboardButton(name_size_48)
btn_size_50 = KeyboardButton(name_size_50)
btn_size_52 = KeyboardButton(name_size_52)
btn_size_54 = KeyboardButton(name_size_54)
btn_size_58 = KeyboardButton(name_size_58)

kb_size = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_size_46, btn_size_48, btn_size_50)\
    .row(btn_size_52, btn_size_54, btn_size_58)\
    .add(cancelUserBNT)

#Клавиатура - Рост
btn_growth_0 = KeyboardButton(name_growth_0)
btn_growth_1 = KeyboardButton(name_growth_1)
btn_growth_2 = KeyboardButton(name_growth_2)
btn_growth_3 = KeyboardButton(name_growth_3)
btn_growth_4 = KeyboardButton(name_growth_4)
btn_growth_5 = KeyboardButton(name_growth_5)
btn_growth_6 = KeyboardButton(name_growth_6)
btn_growth_7 = KeyboardButton(name_growth_7)

kb_growth = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_growth_0, btn_growth_1, btn_growth_2, btn_growth_3)\
    .row(btn_growth_4, btn_growth_5, btn_growth_6,btn_growth_7)\
    .add(cancelUserBNT)

#Клеймение
btn_brand_rb = KeyboardButton(name_brand_rb)
btn_brand_rb0 = KeyboardButton(name_brand_rb0)
btn_brand_not = KeyboardButton(name_brand_not)

kb_brand = ReplyKeyboardMarkup(resize_keyboard=True).row(btn_brand_rb, btn_brand_rb0, btn_brand_not).add(cancelUserBNT)