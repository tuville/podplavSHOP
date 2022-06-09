from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from config import dp, bot
from data_base import db_script
from handlers import checkout_handler_md
from keyboard import kb_menu_main
from keyboard.kb_menu_main import kb_menu_user

async def command_start(message: types.Message):
    await message.answer(f'👋🏼 <b>{message.from_user.first_name}</b>, приветствуем Вас в нашем магазине!\n\n'
                         'Здесь представлены рабочие костюмы, разработанные специально для Военно-морского флота⚓️\n\n'
                         '‼️АКЦИЯ‼️ Каждый 5️⃣ костюм обойдется Вам со скидкой 50%🎁\n'
                         'Подробности уточняйте в разделе "❗️Важно" или у нашего менеджера.\n\n'
                         'По всем интересующим вопросам , а также групповым заказам,'
                         'Вы можете обратиться к нашему медеджеру: @manager_podplav📲\n\n'
                         'Начать просмотр ⬇️', reply_markup=kb_menu_main.kbIn_start)

@dp.callback_query_handler(lambda c: c.data == 'start_yes')
async def start_yes_callback (call: types.CallbackQuery):
    await call.message.answer('Отлично! Хороших покупок!', reply_markup=kb_menu_user)
    await button_catalog(call.message)

@dp.callback_query_handler(lambda c: c.data == 'start_not')
async def start_not_callback (call: types.CallbackQuery):
    await call.message.answer('Очень жаль, но согласитесь, что ничего не потеряете, посмотрев каталог одним глазком?🫣', reply_markup=kb_menu_user)

# Кнопка "Основное меню"
async def button_main_menu(message: types.Message):
    await message.answer('Вы в основном меню! выбери пункт меню!', reply_markup=kb_menu_user)

#Кнопка "Наши контакты"
async def button_contact(message: types.Message):
    await message.answer('<b>Наши контакты:</b>\n'
                         'По всем интересующим вопросам обращайтесь к нашему менеджеру:\n'
                         'Контактный телефон: <b>+79965610201</b>\n'
                         'telegram: @manager_podplav', reply_markup=kb_menu_user)

#Кнопка "Таблица размеров"
async def button_size(message: types.Message):
    await bot.send_photo(message.from_user.id, types.InputFile('size_table.jpeg'))
    await message.answer('🚨 <b> ВАЖНО!</b>\n\n'
            '1. Вы можете заказать разный размер брюк и куртки, для этого не забудьте указать нужные размеры '
                    'при оформлении заказа. Данная опция стоит <b>+200 RUB</b> к заказу.\n\n'
            '2. В случае, если Вы ошиблись с размером, мы <b>БЕСПЛАТНО</b> поменяем костюм на аналогичный, с другим размером, '
                    'при условии, что сохранен товарный вид. Пересылка в данном случае оплачивается заказчиком.\n\n'
            '3. 🔄 <b> ВОЗВРАТ</b>. В комплект костюма входит жетон с серийным номером комплекта. Для каждого '
                    'заказа он индивидуален и подтверждает его подлинность, поэтому возврат жетона вместе '
                    'с костюмом <b>ОБЯЗАТЕЛЕН.</b> Возврат денежных средств или обмен без жетона <b>НЕ</b> производится!'
            '4. Если Вы немного ошиблись с ростом и заказали костюм длиннее, перед укорачиванием и подшивом,'
                    'рекомендуем Вам сделать это после первой стирки.\n\n'
            '5. Мы рекомендуем выбирать такой размер, чтобы костюм сидел на вас слегка свободно, не стесняя движений.\n\n'
            '6. Если ты заказал костюм и тебе понравилось, не стоит скрывать эту находку от своих коллег. Даже если '
                    'этот коллега твой злой начальник.\n\n'
            '<B>Вдруг он такой злой, потому, что никогда не носил хорошего костюма?</b>😎', reply_markup=kb_menu_user)

#Кнопка "Доставка"
async def button_delivery(message: types.Message):
        await message.answer('<b> Информация по доставке: </b> \n\n'
                             'Мы осуществляем отправку в двухдневный срок (как правило это происходит в день заказа),'
                             'если выбранный Вами костюм и размер есть в наличии.\n\n'
                            'На данный момент мы можем отправить Вам заказ только почтой России, '
                            'но мы работаем над расширением этого списка.🙄\n\n'
                            '<b> Отправка почтой возможна в следующих вариантах:</b>\n'
                            '- EMS 🚀 6-8 дней;\n'
                            '- 1 класс ✈️ 7-9 дней;\n'
                            '- обычной посылкой 🚊12-14 дней.\n'
                            ' Доставку оплачивает заказчик вместе с оплатой костюма.\n\n'
                             '<b>Информация по оплате:</b>\n'
                             'Мы работаем по <b>100% оплате товара</b>, переводом необходимой суммы на карту💳\n'
                             '2202201904667470\nКирилл Алексеевич Ш\n'
                             'Скрин об оплате необходимо прислать менеджеру после оформления заказа📲'
                             '', reply_markup=kb_menu_user)

#Кнопка "Каталог"
async def button_catalog(message: types.Message):
        await message.answer('Не забудьте оформить заказ на понравившийся комплект 🛒')
        await db_script.sqlDB_catalogRB_read(message)

#Кнопка "Купить"
async def button_buy(message: types.Message):
    await checkout_handler_md.start_buy(message)

# Кнопка "FAQ"
async def button_faq(message: types.Message):
    await message.answer('Важная информация! \n\n'
                         'Подробности <b>‼️акции‼️:</b>\n'
                         'На каждый пятый купленный у нас костюм Вы получите скидку 50% от актуальной цены.\n\n'
                         '<b>Правила ухода за костюмом:</b>\n'
                            '- допускается машинная стирка при температуре не выше 40℃;🧺\n'
                            '- глаженье при максимальной температуре не более 150℃;💨\n'
                            '- возможна барабанная сушка при обычной температуре;\n'
                            '- не отбеливать.🙅\n'
                            '\n'
                        '<b>Информация по внесению изменений:</b>\n'
                        'При заказе партии от 50 штук, Вы можете по согласовании с менеджером внести следующие изменения:\n'
                            '- тип ткани;\n'
                            '- цвет ткани;\n'
                            '- убрать или добавить светоотражающие полосы;\n'
                            '- добавить Ваш герб/логотип/надпись;\n'
                            '- дополнительный внутренний карман или отделения для ручек.\n'
                            '(некоторые изменения платные, конечная цена зависит, от партии)'
                         '', reply_markup=kb_menu_user)

def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(button_main_menu, Text(equals=kb_menu_main.menu_name_btn, ignore_case=True))
    dp.register_message_handler(button_contact, Text(equals=kb_menu_main.contact_name_btn, ignore_case=True))
    dp.register_message_handler(button_size, Text(equals=kb_menu_main.size_name_btn, ignore_case=True))
    dp.register_message_handler(button_delivery, Text(equals=kb_menu_main.delivery_name_btn, ignore_case=True))
    dp.register_message_handler(button_catalog, Text(equals=kb_menu_main.catalog_name_btn, ignore_case=True))
    dp.register_message_handler(button_buy, Text(equals=kb_menu_main.buy_name_btn, ignore_case=True))
    dp.register_message_handler(button_faq, Text(equals=kb_menu_main.info_name_btn, ignore_case=True))