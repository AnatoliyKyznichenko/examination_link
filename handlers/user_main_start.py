import asyncio
from os import path
from data.loader import *
from aiogram import types
from keyboards.user_keyboards import *
from urllib.parse import urlparse
from pyrogram import Client

channel_id = ''

api_id = 0
api_hash = ''


async def get_channel_history():
    async with Client("my_session", api_id, api_hash) as app:
        async for message in app.get_chat_history(chat_id=""):
            id_users = str(message.text).split(':')[1]
            #id_balances = str(message.text).split(':')[2]
            return id_users


async def get_balance():
    async with Client("my_session", api_id, api_hash) as app:
        async for message in app.get_chat_history(chat_id=""):
            id_balances = str(message.text).split(':')[-1]
            if len(message.text.split(':')) != 3:
                return None
            return id_balances


@dp.message_handler(commands='start')
async def main(message: types.Message):
    await message.answer_photo(caption='Добро пожаловать, Вы уже в шаге от своего выигрыша😉!\n\n'
                         'Для того чтобы подвязать свой аккаунт к нашему софту и получить доступ к закрытому сообществу\n'
                         'с победными сигналами, тебе необходимо выполнить определенный алгоритм действий.\n\n'
                         '🔹 Нажимай на кнопку "🧬 Алгоритм действий" для продолжения.',reply_markup=user_start,
                            photo=types.InputFile(path.join('img', 'e9521353-1484-4273-9f96-9471325064a5.jpg'),))


@dp.callback_query_handler(text='algoritm')
async def instruction(call: types.CallbackQuery):
    chat_id = call.from_user.id
    chat_id_fstring = f'https://1w.top/casino/list?open=register&sub1={chat_id}'
    parsed_url = urlparse(chat_id_fstring)
    sub1_value = parsed_url.query.split('sub1=')[1]
    print(sub1_value)
    await call.message.answer_photo(caption='📲 Шаг 1 - Пройти регистрацию \n\n'
                              '🔹 Процесс регистрации связующее звено между двумя точками которая запускает процесс.\n'
                              'Где "а" это Ваш аккаунт, и "б" наш софт который в свою очередь подвязан к структуре сайта.\n\n'
                              '🔹 Аккаунт должен быть НОВЫЙ, без единого депозита и испорченной истории игр,\n'
                              'т. к. софт разрабатывался обходя свежую систему отслеживания действий потенциально носящих финансовый ущерб компании.\n'
                              'В случае того, если у Вас был когда либо аккаунт на данном сайте,\n'
                              'рекомендуем заходить и регистрировать новый во вкладке инкогнито используя новый номер\n'
                              'телефона который не был зарегистрирован ранее. \n\n'
                              '🔹 Если у Вас не работает сайт, попытайтесь зайти на него используя VPN. Все ровно не работает?\n'
                              'В таком случае напишите в поддержку, где менеджер постарается решить вашу проблему в кротчайшие сроки. \n\n'
                              'Техническая поддержка - \n\n'
                              '🔹 После регистрации, нажмите кнопку "🔍 Проверить регистрацию".',
                              reply_markup=InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('📲 Регистрация', url=chat_id_fstring),
    InlineKeyboardButton('🔍 Проверить регистрацию', callback_data='check')),
                                    photo=types.InputFile(path.join('img', '317976e3-ba7e-4c95-80c8-3f9e8a9b6e26.jpg')))


@dp.callback_query_handler(text='check')
async def check_register(call: types.CallbackQuery):
    user_id_check = call.from_user.id
    chat_id_fstring = f'https://1w.top/casino/list?open=register&sub1={user_id_check}'
    channel_history = await get_channel_history()
    #check_chanel_id = await bot.get_chat_history(chat_id=channel_id, limit=10)
    #for check_id_chanell in check_chanel_id:
    #check_id_chanell = check_id_chanell.text.split(':')[1]
    if str(user_id_check) == channel_history:
            await call.message.answer('✅ Вы успешно зарегистрировались на сайте! Переходим к Шагу 2')
            await asyncio.sleep(2)
            await call.message.answer_photo(caption='📲 Шаг 2 - Сделать первый депозит от 1000 Рублей, 500 Гривен, или же 15 долларов.\n\n'
                                      '● Это сумма с которой можно выйти в отличный плюс за короткий срок и\n'
                                      'это часто встречающейся депозит который не должен вызывать никаких подозрений,\n'
                                      'поскольку Ваш аккаунт, а конкретно Вы, будете выигрывать\n'
                                      'намного чаще и больше чем все остальные игроки.\n\n'
                                      '● Данные действия необходимы дабы система отслеживания\n'
                                      'Вас не заподозрила и не удалила аккаунт.\n'
                                      'Таким образом Ваши транзакции смешаются с остальными и вас невозможно будет отследить.\n'
                                      'После нескольких дней адаптации Вашего аккаунта,\n'
                                      'Вы сможете вносить депозиты любого размера в удобное для Вас время,\n'
                                      'без беспокойства о том, что Ваш аккаунт может быть заподозрен или удален.\n\n'
                                      '● После пополнения первого депозита, нажмите кнопку "🔍 Проверить депозит".',
                                      reply_markup=InlineKeyboardMarkup(row_width=1).
                                      add(InlineKeyboardButton("🔍 Проверить депозит", callback_data='check_depozit')),
                                            photo=types.InputFile(path.join('img', 'ed409b6d-3383-433d-933d-ce99ded166bd.jpg')))
            return
    else:
        await call.message.answer('❌ К сожалению система вас не видит в базе! \n'
                            'Проблема может быть в том, что вы не вышли со старого аккаунта,\n'
                            'или не зарегистрировались через бот. Напишите нам в поддержку или попробуйте снова.')
        await asyncio.sleep(4)


@dp.callback_query_handler(text='check_depozit')
async def check_deposit(call: types.CallbackQuery):
    summa_depozita = await get_balance()
    print(summa_depozita)
    if summa_depozita is None:
        await call.message.answer('❌Пополнение не было совершено!\n\n'
                                  'Пополните баланс на сумму , 500 гривен или\n 13$, и нажмите «🔎Проверить депозит»')
    if float(summa_depozita) < 13:
        await call.message.answer('❌Сумма пополнения меньше требуемой! \n'
                                  'Пополните баланс на сумму, 500 гривен или 13$, и нажмите «🔎Проверить депозит»')
        return
    await call.message.answer('✅ Поздравляю! Вы успешно прошли синхронизацию,\n'
                              'теперь ваш аккаунт числиться в базе софта и будет\n'
                              'выдавать вам максимально точные сигналы.\n\n'
                              'Ждем тебя в VIP Чате!👇', reply_markup=InlineKeyboardMarkup(row_width=1).
                                      add(InlineKeyboardButton("VIP 🎉", url='')))



