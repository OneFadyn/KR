from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData





mainMenuKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Расписание'),
            KeyboardButton(text='Сроки сдачи работ')
        ],
        [
            KeyboardButton(text='Список литературы'),
            KeyboardButton(text='Важные новости')
        ],
        [
            KeyboardButton(text='Помощник'),
            KeyboardButton(text='Другое')
        ]
    ],
    resize_keyboard=True
)

scheduleMenuKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Расписание на сегодня'),
            KeyboardButton(text='Расписание на неделю')
        ],
        [
            KeyboardButton(text='Расписание на завтра'),
            KeyboardButton(text='Расписание сессии')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)

otherMenuKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рекомендации по организации учебного процесса')
        ],
        [
            KeyboardButton(text='Рекомендация литературы'),
            KeyboardButton(text='Анонс мероприятий'),
        ],
        [
            KeyboardButton(text='Викторины')
        ]
    ],
    resize_keyboard=True
)
