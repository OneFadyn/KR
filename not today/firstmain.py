import telebot

# Создаем экземпляр бота
bot = telebot.TeleBot('7191032155:AAFmw9T1Idrj7tzHAOHZfyOauTTp0rdxmPg')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


# Запускаем бота
bot.polling(none_stop=True, interval=0)



"""import telebot
import random
from telebot import types
# Загружаем список интересных фактов
f = open('data/facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()
# Загружаем список поговорок
f = open('data/thinks.txt', 'r', encoding='UTF-8')
thinks  = f.read().split('\n')
f.close()
# Создаем бота
bot = telebot.TeleBot('7191032155:AAFmw9T1Idrj7tzHAOHZfyOauTTp0rdxmPg')
# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        item2=types.KeyboardButton("Поговорка")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ',  reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    # Если юзер прислал 1, выдаем ему случайный факт
    if message.text.strip() == 'Факт' :
            answer = random.choice(facts)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'Поговорка':
            answer = random.choice(thinks)
    # Отсылаем юзеру сообщение в его чат
    bot.send_message(message.chat.id, answer)
# Запускаем бота
bot.polling(none_stop=True, interval=0)"""


'''
one more huynya



import telebot
from telebot import types

token = '7191032155:AAFmw9T1Idrj7tzHAOHZfyOauTTp0rdxmPg'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def inline_key(a):
    mainmenu = types.InlineKeyboardMarkup()
    study = types.InlineKeyboardButton(text='Учеба', callback_data='study')
    other = types.InlineKeyboardButton(text='Другое', callback_data='other')
    schedule = types.InlineKeyboardButton(text='Расписание', callback_data='schedule')
    mainmenu.add(study)
    mainmenu.add(schedule)
    mainmenu.add(other)
    bot.send_message(a.chat.id, 'Это главное меню!', reply_markup=mainmenu)

# Добавим обработчик для нажатия кнопки "Расписание"
@bot.callback_query_handler(func=lambda call: call.data == 'schedule')
def view_schedule(call):
    photo = open('data/schedule.jpg', 'rb')
    bot.send_photo(call.message.chat.id, photo, caption='Расписание на день')

    back_menu = types.InlineKeyboardMarkup()
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    back_menu.add(back)
    bot.send_message(call.message.chat.id, 'Чтобы вернуться в главное меню, нажмите "Назад"', reply_markup=back_menu)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":
        mainmenu = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='key1')
        key2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='key2')
        mainmenu.add(key1, key2)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    elif call.data == "key1":
        next_menu = types.InlineKeyboardMarkup()
        key3 = types.InlineKeyboardButton(text='Кнопка 3', callback_data='key3')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu.add(key3, back)
        bot.edit_message_text('Это меню уровня 2, для кнопки1!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu)
    elif call.data == "key2":
        next_menu2 = types.InlineKeyboardMarkup()
        key4 = types.InlineKeyboardButton(text='Кнопка 4', callback_data='key4')
        back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
        next_menu2.add(key4, back)
        bot.edit_message_text('Это меню уровня 2, для кнопки2!', call.message.chat.id, call.message.message_id,
                              reply_markup=next_menu2)

bot.polling()

'''