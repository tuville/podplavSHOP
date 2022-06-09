from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, dp
from keyboard.kb_menu_main import kb_menu_user, kb_cancel, cancelUser_name_btn
from keyboard.kb_checkout import kb_size, kb_growth, kb_brand
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

chatID = '-1001671561122'

class buyerData (StatesGroup):
    FullName_buyer = State()
    rb_name = State()
    size_rb = State()
    growth_rb = State()
    branding_rb = State()
    amount_rb = State()
    adress_byer = State()
    phoneNumber = State()
    comment = State()

#Начало покупки

@dp.callback_query_handler(lambda c: c.data == 'buy_yes')
async def buy_yes_callback (call: types.CallbackQuery):
    await buyerData.FullName_buyer.set()  # Устанавливаем состояние
    await call.message.answer('Укажите ФИО полностью', reply_markup=kb_cancel)

@dp.callback_query_handler(lambda c: c.data == 'buy_not')
async def buy_not_callback (call: types.CallbackQuery):
    await call.message.answer('Очень жаль! Возвращайся за покупкой', reply_markup=kb_menu_user)

async def start_buy(message: types.Message):
    await message.answer(f"Отлично, <b>{message.from_user.first_name}</b>! Вы сделали правильный выбор.\n"
                         "Перед оформлением заказа ознакомьтесь с таблицей размеров! \n"
                         "Продолжаем оформление заказа?", reply_markup=InlineKeyboardMarkup(row_width=2).\
                         insert(InlineKeyboardButton(text='Да', callback_data='buy_yes')).\
                        insert(InlineKeyboardButton(text='Нет', callback_data='buy_not')))

#Кнопка "Отменить"
async def button_buy_cancel (message: types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("❌ ❌ ❌ <b>Оформление заказа отменено!</b> ❌ ❌ ❌"
                                                 "", reply_markup=kb_menu_user)

#Принимаем первое состояние = ФИО покупателя ===>>> берем следующее состояние  = Наименование РБ
async def buy_name_buyer(message: types.Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    await buyerData.next()
    await bot.send_message(message.from_user.id, "Напишите название костюма, который хотите приобрести"
                                                 "", reply_markup=kb_cancel)

#Приняли состояние  = Наименование РБ ===>>> берем следующее состояние  = Размер РБ
async def buy_rb_name(message: types.Message, state: FSMContext):
    await state.update_data(rb_name=message.text)
    await buyerData.next()
    await bot.send_message(message.from_user.id, "Выберите размер, если нужного нет - напишите!", reply_markup=kb_size)

#Приняли состояние = Размер РБ ===>>> берем следующее состояние  =  Рост РБ
async def buy_size_rb(message: types.Message, state: FSMContext):
    await state.update_data(rb_size=message.text)
    await buyerData.next()
    await bot.send_message(message.from_user.id, "Выберите рост, если сомневаетесь - напишите свой рост", reply_markup=kb_growth)

#Приняли состояние = Размер РБ ===>>> берем следующее состояние  =  Количество РБ
async def buy_growth_rb(message: types.Message, state: FSMContext):
    await state.update_data(rb_growth=message.text)
    await buyerData.next()
    await bot.send_message(message.from_user.id, "Сколько Вам необходимо костюмов?", reply_markup=kb_cancel)


#Приняли состояние = Размер РБ ===>>> берем следующее состояние  =  Количество РБ
async def buy_branding_rb(message: types.Message, state: FSMContext):
    await state.update_data(rb_amount=message.text)
    await buyerData.next()
    await bot.send_message(message.from_user.id, "Какое клеймение нанести: «РБ» или «РБ-0» (если оно не нужно напишите «нет»"
                                                 "", reply_markup=kb_brand)

#Приняли состояние = Количество РБ ===>>> берем следующее состояние  = Адрес доставки
async def buy_amount_rb(message: types.Message, state: FSMContext):
    await state.update_data(rb_branding=message.text)
    await buyerData.next()
    await bot.send_message(message.from_user.id, "Укажите адрес доставки в следующем формате:\n\n "
                                                 "- Республика/край/область;\n"
                                                 "- населенный пункт;\n"
                                                 "- улица, номер дома (корпус), квартира;\n"
                                                 "- индекс.", reply_markup=kb_cancel)

#Приняли состояние = Адрес доставки ===>>> берем следующее состояние  = Контактный телефон
async def buy_adress_byer(message: types.Message, state: FSMContext):
    await state.update_data(adress=message.text)
    await buyerData.next()
    await bot.send_message(message.from_user.id, "Введите Ваш номер телефона для подтверждения заказа!"
                                                 "", reply_markup=kb_cancel)

#Приняли состояние = Контактный телефон ===>>> берем следующее состояние  = Комментарий
async def buy_phoneNumber(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await buyerData.next()
    await bot.send_message(message.from_user.id, "Сейчас Вы можете указать пожелания или другие заметки"
                                                 "", reply_markup=kb_cancel)

#Приняли состояние  = Контактный телефон ===>>> берем следующее состояние  = Комментарий
async def buy_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    userdata = await state.get_data()
    await bot.send_message(chatID, f"<b> ✅ Сделан заказ от пользователя: @{message.from_user.username}! </b>\n\n"
                                    f"<b>✔️ ФИО покупателя:</b> {userdata['fullname']}\n"
                                    f"<b>✔️ Контактный телефон:</b> {userdata['phone']}\n"
                                    f"<b>✔️ Адрес получателя:</b> {userdata['adress']}\n"
                                    f"<b>✔️ Наименование товара:</b> {userdata['rb_name']}\n"
                                    f"<b>✔️ Размер товара:</b> {userdata['rb_size']}\n"
                                    f"<b>✔️ Размер товара:</b> {userdata['rb_growth']}\n"
                                    f"<b>✔️ Клеймение:</b> {userdata['rb_branding']}\n"
                                    f"<b>✔️ Количество товара:</b> {userdata['rb_amount']}\n"
                                    f"<b>✔️ Примечание:</b> {userdata['comment']}")
    await bot.send_message(message.from_user.id, "Спасибо! Ваш заказ оформлен и отправлен менеджеру. "
                                                 "В ближайшее время с Вами свяжутся для подтверждения и оплаты."
                                                 "", reply_markup=kb_menu_user)
    await state.finish()

def register_handlers_checkout(dp: Dispatcher):
    dp.register_message_handler(start_buy)
    dp.register_message_handler(button_buy_cancel, Text(equals=cancelUser_name_btn, ignore_case=True), state="*")
    dp.register_message_handler(buy_name_buyer, state=buyerData.FullName_buyer)
    dp.register_message_handler(buy_rb_name, state=buyerData.rb_name)
    dp.register_message_handler(buy_size_rb, state=buyerData.size_rb)
    dp.register_message_handler(buy_growth_rb, state=buyerData.growth_rb)
    dp.register_message_handler(buy_branding_rb, state=buyerData.branding_rb)
    dp.register_message_handler(buy_amount_rb, state=buyerData.amount_rb)
    dp.register_message_handler(buy_adress_byer, state=buyerData.adress_byer)
    dp.register_message_handler(buy_phoneNumber, state=buyerData.phoneNumber)
    dp.register_message_handler(buy_comment, state=buyerData.comment)
