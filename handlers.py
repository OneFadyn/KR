import asyncio
from asyncore import loop
from os import system
import datetime

from aiogram import Dispatcher, Bot
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, update
from aiogram.dispatcher.filters import Text, Command
from keyboards import mainMenuKeyboard, scheduleMenuKeyboard, otherMenuKeyboard

from config import chat_id, BOT_TOKEN


bot = Bot(BOT_TOKEN, parse_mode='HTML')

dp = Dispatcher(bot, loop=loop)

async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='Здравствуйте! Нажмите /menu, чтобы начать работу бота')

@dp.message_handler(Command('quiz'))
async def quiz(message: Message):
    """await bot.send_message(chat_id=chat_id, text='Добро пожаловать в режим викторины!', reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=chat_id,
                           text='На данный момент доступны 3 викторины:')
    await bot.send_message(chat_id=chat_id,
                           text='№1 - Викторина на эрудицию. Нажмите /start, чтобы начать игру')
    await bot.send_message(chat_id=chat_id,
                           text='№2 - Викторина 2. Нажмите /start_2, чтобы начать игру')
    await bot.send_message(chat_id=chat_id,
                           text='№3 - Викторина 3. Нажмите /start_3, чтобы начать игру')
"""
    """Переход в режим викторины"""

    # Запускаем викторину в отдельном процессе
    system('python quiz.py')


@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Главное меню', reply_markup=mainMenuKeyboard)


# Переход на уровень расписания

@dp.message_handler(Text(equals=['Расписание']))
async def schedule_menu(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Меню расписания",
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры
    await bot.send_message(message.chat.id, 'Выберите нужный раздел', reply_markup=scheduleMenuKeyboard)


# handlers для блока меню с расписаниями
@dp.message_handler(Text(equals=['Расписание на сегодня']))
async def schedule_for_today(message: Message):
    current_day = datetime.datetime.today().weekday()  # Получаем номер текущего дня недели (0 - понедельник, 1 - вторник и т.д.)
    days_of_week = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
    day_filename = days_of_week[current_day] + '.png'  # Формируем имя файла на основе текущего дня недели

    await bot.send_message(chat_id=message.chat.id, text=f"Расписание на {days_of_week[current_day]}",
                           reply_markup=ReplyKeyboardRemove())  # Удаление предыдущей клавиатуры

    with open(f'data/{day_filename}', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo.read())

    await message.answer('Menu', reply_markup=mainMenuKeyboard)

async def get_schedule_for_today():
    current_day = datetime.datetime.today().weekday()  # Получаем номер текущего дня недели (0 - понедельник, 1 - вторник и т.д.)
    days_of_week = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
    day_filename = days_of_week[current_day] + '.png'  # Формируем имя файла на основе текущего дня недели

    schedule_text = f"Расписание на {days_of_week[current_day]}\n"
    with open(f'data/{day_filename}', 'rb') as photo:
        photo_data = photo.read()

    return photo_data
async def get_deadlines():
    deadlines_text = "Ближайшие дедлайны:\n"
    with open('data/deadlines.txt', 'r', encoding='utf-8') as file:
        deadlines_text += file.read()
    return deadlines_text


@dp.message_handler(Text(equals=['Расписание на завтра']))
async def schedule_for_tomorrow(message: Message):
    current_day = datetime.datetime.today().weekday()  # Получаем номер текущего дня недели (0 - понедельник, 1 - вторник и т.д.)
    days_of_week = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу', 'воскресенье']
    day_filename = days_of_week[current_day+1] + '.png'  # Формируем имя файла на основе текущего дня недели

    await bot.send_message(chat_id=message.chat.id, text=f"Расписание на завтра (на {days_of_week[current_day+1]})",
                           reply_markup=ReplyKeyboardRemove())  # Удаление предыдущей клавиатуры

    with open(f'data/{day_filename}', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo.read())

    await message.answer('Menu', reply_markup=mainMenuKeyboard)



@dp.message_handler(Text(equals=['Расписание на неделю']))
async def schedule_for_week(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Расписание групп ИТ-3 на неделю",
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры
    with open('data/schedule_week.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo.read())


@dp.message_handler(Text(equals=['Расписание сессии']))
async def schedule_exams(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Расписание сессии",
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры
    with open('data/schedule_exams.png', 'rb') as photo:
        await bot.send_photo(chat_id=message.chat.id, photo=photo.read())


# Список литературы
@dp.message_handler(Text(equals=['Список литературы']))
async def literature(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Нажмите на необходимую ссылку",
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры
    with open('data/List of literature.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=ReplyKeyboardRemove())


# Помощник
@dp.message_handler(Text(equals=['Помощник']))
async def helper_start(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='Переход в режим помощника... Для выхода из режима помощника '
                                                         'нажмите /stopchat или выберите эту команду в меню',
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры

    """Переход в чат-бот"""

    # Запускаем чат-бота в отдельном процессе
    system('python chatbot.py')


@dp.message_handler(Text(equals=['Важные новости']))
async def news(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Новости",
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры
    with open('data/news.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=ReplyKeyboardRemove())

async def get_news():
    news_text = "Важные новости:\n"
    with open('data/news.txt', 'r', encoding='utf-8') as file:
        news_text += file.read()
    return news_text

@dp.message_handler(Text(equals=['Сроки сдачи работ']))
async def deadlines(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Новости",
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры
    with open('data/deadlines.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=['Другое']))
async def other(message: Message):
    await bot.send_message(message.chat.id, 'Выберите нужный раздел', reply_markup=otherMenuKeyboard)


# handlers для блока меню "Другое"
@dp.message_handler(Text(equals=['Викторины']))
async def quiz(message: Message):
    await bot.send_message(chat_id=chat_id, text='Добро пожаловать в режим викторины!', reply_markup=ReplyKeyboardRemove())
    await bot.send_message(chat_id=chat_id,
                           text='На данный момент доступны 3 викторины:')
    await bot.send_message(chat_id=chat_id,
                           text='№1 - Викторина на эрудицию. Нажмите /start_1, чтобы начать игру')
    await bot.send_message(chat_id=chat_id,
                           text='№2 - Викторина на знание физики. Нажмите /start_2, чтобы начать игру')
    await bot.send_message(chat_id=chat_id,
                           text='№3 - Викторина по программированию. Нажмите /start_3, чтобы начать игру')

    """Переход в режим викторины"""

    # Запускаем викторину в отдельном процессе
    system('python quiz.py')


@dp.message_handler(Text(equals=['Рекомендации по организации учебного процесса']))
async def rec(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Рекомендации по организации учебного процесса",
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры
    # можно предложить сайты или уже готовую информацию

@dp.message_handler(Text(equals=['Рекомендация литературы']))
async def rec_lit(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Рекомендуемая литература",
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры
    with open('data/rec_lit.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=ReplyKeyboardRemove())

    # можно разделы сделать

@dp.message_handler(Text(equals=['Анонс мероприятий']))
async def events(message: Message):
    await bot.send_message(chat_id=message.chat.id, text="Анонс мероприятий",
                           reply_markup=ReplyKeyboardRemove())  # удаление предыдущей клавиатуры
    with open('data/events.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    await bot.send_message(chat_id=message.chat.id, text=text, reply_markup=ReplyKeyboardRemove())

'''
функция эхо ответы
@dp.message_handler()
async def send_answer(message: Message):
    text = message.text
    await message.answer(text=text)
'''
