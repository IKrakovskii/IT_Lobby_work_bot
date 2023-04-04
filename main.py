import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from loguru import logger

logger.add(
    'LOGS.log',
    format='{time} {level} {message}',
    level='DEBUG'
)
logger.info('Бот запущен')
CATEGORIES = ['backend', 'frontend', 'fullstack', 'teamlead']
API_TOKEN = '5723423980:AAF64f_gK7hgYZ7kjNyEz9Y0MBnB5u5ZOE8'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class DataBase:
    pass


@logger.catch
@dp.message_handler(commands=['start', 'help', 'restart'])
async def welcome(message: types.Message):
    # rq = InlineKeyboardMarkup(row_width=2)
    rq = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    rq.add(*CATEGORIES)
    await bot.send_message(chat_id=message.chat.id,
                           text='Привет, этот бот создан, чтобы отправлять тебе новые вакансии, основанные на твоих '
                                'интересах')
    await bot.send_message(chat_id=message.chat.id,
                           text='Выбери, интересующие тебя категории', reply_markup=rq)


@logger.catch()
def main():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
