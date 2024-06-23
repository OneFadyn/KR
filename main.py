import asyncio
from datetime import datetime, timedelta
from os import system
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, chat_id

from keyboards import mainMenuKeyboard


from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, update
from aiogram.dispatcher.filters import Text, Command
from keyboards import mainMenuKeyboard, scheduleMenuKeyboard

# Создаем цикл событий
loop = asyncio.new_event_loop()



bot = Bot(BOT_TOKEN, parse_mode='HTML')

dp = Dispatcher(bot, loop=loop)

@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Главное меню', reply_markup=mainMenuKeyboard)

@dp.message_handler(Command('startchat'))
async def start_chatbot(message: Message):
    """Переход в чат-бот"""

    # Запускаем чат-бота в отдельном процессе
    system('python chatbot.py')


async def send_everyday_message():
    while True:
        moscow_time = datetime.utcnow() + timedelta(hours=3)

        if moscow_time.hour == 8 and moscow_time.minute == 00:
            schedule_photo = await get_schedule_for_today()
            deadlines_text = await get_deadlines()
            news_text = await get_news()

            await bot.send_photo(chat_id, schedule_photo, caption=f"{deadlines_text}\n\n{news_text}")

        # Ожидаем одну минуту перед следующей проверкой
        await asyncio.sleep(60)


if __name__ == '__main__':
    async def main():
        task_send_message = asyncio.create_task(send_everyday_message())
        await asyncio.gather(task_send_message, send_hello(dp))

    loop = asyncio.get_event_loop()
    loop.create_task(main())

    from handlers import send_hello, dp, schedule_for_today, deadlines, news, get_schedule_for_today, get_deadlines, \
    get_news

    print("Бот запущен...")
    executor.start_polling(dp)
