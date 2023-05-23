from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

user_start = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton('🧬 Алгоритм действий', callback_data='algoritm'))

instruction_user = InlineKeyboardMarkup(row_width=1).add(
    InlineKeyboardButton('📲 Регистрация', callback_data='https://1wiuup.top/casino/list?open=register&sub1='),
    InlineKeyboardButton('🔍 Проверить регистрацию', callback_data='check'))
