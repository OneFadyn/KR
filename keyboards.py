from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from config import URL_VK, URL_MOODLE



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
            KeyboardButton(text='Расписание на день'),
            KeyboardButton(text='Расписание на неделю')
        ],
        [
            KeyboardButton(text='Расписание на месяц'),
            KeyboardButton(text='Расписание сессии')
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)

#todayMenuKeyboard =





"""

cb = CallbackData('open', 'id', 'name', 'price')

keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Moodle', callback_data='Open:1:site1:1'),
            InlineKeyboardButton(text='VK', callback_data='Open:2:site2:1')
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

moodle_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Открыть', url=URL_MOODLE)
        ]
    ]
)
"""

"""
vk_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Открыть', url=URL_VK)
        ]
    ]
)
"""