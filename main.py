from aiogram import executor, Dispatcher
from handlers import user_main_start
import asyncio
from data.loader import *
from services.api_sqlite import *
from data.config import *
from img import *


if __name__ == '__main__':
    executor.start_polling(dp)