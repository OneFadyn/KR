'''
import telebot
from telebot import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

token = '7191032155:AAFmw9T1Idrj7tzHAOHZfyOauTTp0rdxmPg'

bot = telebot.TeleBot(token)

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='btn1'),
            KeyboardButton(text='btn2')
        ],
        [
            KeyboardButton(text='btn3')
        ]
    ],
    resize_keyboard=True
)


@bot.message_handler(commands=["start"])
def send_mainmenu(message):
    #bot.send_message(message.chat.id, 'Доброе утро!')
    mainmenu = types.InlineKeyboardMarkup()
    study = types.InlineKeyboardButton(text='Учеба', callback_data='study')
    other = types.InlineKeyboardButton(text='Другое', callback_data='other')
    mainmenu.add(study)
    mainmenu.add(other)
    bot.send_message(message.chat.id, 'Здравствуйте! Скоро здесь будет гораздо больше информации!', reply_markup=mainmenu)




@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'study':
        study_menu = types.InlineKeyboardMarkup()
        schedule = types.InlineKeyboardButton(text='Расписание', callback_data='schedule')
        deadlines = types.InlineKeyboardButton(text='Дедлайны на дз', callback_data='deadlines')
        literature = types.InlineKeyboardButton(text='Список литературы', callback_data='literature')
        assistant = types.InlineKeyboardButton(text='Помощник', callback_data='assistant')
        news = types.InlineKeyboardButton(text='Важные новости', callback_data='news')
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        study_menu.add(schedule, deadlines, literature, assistant, news, back)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Меню учебы", reply_markup=study_menu)
    elif call.data == 'schedule':
        schedule_menu = types.InlineKeyboardMarkup()
        day_schedule = types.InlineKeyboardButton(text='На день', callback_data='day_schedule')
        week_schedule = types.InlineKeyboardButton(text='На неделю', callback_data='week_schedule')
        month_schedule = types.InlineKeyboardButton(text='На месяц', callback_data='month_schedule')
        exams_schedule = types.InlineKeyboardButton(text='Расписание экзаменов и зачетов', callback_data='exams_schedule')
        back = types.InlineKeyboardButton(text='Назад', callback_data='back')
        schedule_menu.add(day_schedule, week_schedule, month_schedule, exams_schedule,back)
        #bot.send_message(call.message.chat.id, "Расписание")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Меню расписания", reply_markup=schedule_menu)
    elif call.data == 'deadlines':
        bot.send_message(call.message.chat.id, "Дедлайны на дз")
    elif call.data == 'literature':
        bot.send_message(call.message.chat.id, "Список литературы для каждой из дисциплин в семестре")
    elif call.data == 'assistant':
        bot.send_message(call.message.chat.id, "Помощник")
    elif call.data == 'news':
        bot.send_message(call.message.chat.id, "Важные новости")
    elif call.data == 'back':
        mainmenu = types.InlineKeyboardMarkup()
        study = types.InlineKeyboardButton(text='Учеба', callback_data='study')
        other = types.InlineKeyboardButton(text='Другое', callback_data='other')
        mainmenu.add(study)
        mainmenu.add(other)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Это главное меню!", reply_markup=mainmenu)






bot.polling()
'''