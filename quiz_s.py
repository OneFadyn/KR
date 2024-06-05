"""
import asyncio
from aiogram import Bot, types, Dispatcher
from aiogram.types import message

from config import chat_id, BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


async def quiz_main():
    questions = [
        "Столица России?",
        "Самая высокая гора мира?",
        "Самый длинный океан?",
        "Самый большой остров?",
        "Самое большое животное?",
    ]
    answers = ["Москва", "Эверест", "Тихий океан", "Гренландия", "Синий кит"]

    async def handle_answer(msg: types.Message, i: int):
        if msg.text == answers[i]:
            await bot.send_message(chat_id, "Правильно!")
        else:
            await bot.send_message(chat_id, f"Неправильно! Правильный ответ: {answers[i]}")

    for i in range(len(questions)):
        await bot.send_message(chat_id, questions[i])

        user_answer = None

        async def inner_handler(msg: types.Message):
            nonlocal user_answer
            user_answer = msg
            await handle_answer(msg, i)

        dp.register_message_handler(inner_handler)

        while user_answer is None:
            await asyncio.sleep(30)  # Подождать, пока не будет получен ответ


# Запуск асинхронной функции в основном цикле
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(quiz_main())
    loop.run_forever()



#

from config import BOT_TOKEN
from os import system

from telegram import Update
from telegram.ext import Application, ContextTypes, ConversationHandler, MessageHandler, filters, CommandHandler

(ENTRY_STATE, ANSWER_STATE) = range(2)


def generate_question(q: str):





async def start(update: Update, context: ContextTypes):

from chatbot import start
from config import BOT_TOKEN

Начинаем диалог

    await update.message.reply_text(
        "Начинаем викторину",
    )

    return ANSWER_STATE


# Handling the question
async def pre_query_handler(update: Update, context: ContextTypes):
    Ждём ответ от пользователя

    return ANSWER_STATE


# Handling the answer
async def pre_query_answer_handler(update: Update, context: ContextTypes):
    #Выводим вопрос из викторины

    ans = update.message.text

    if ans == '/stopchat':
        await update.message.reply_text("Диалог завершен. До свидания!")

        system('python main.py')


    ques = generate_question(ans)
    context.user_data['ques'] = ques

    await update.message.reply_text(
        ques,
    )

    return ANSWER_STATE



if __name__ == '__main__':
    application = Application.builder().token(BOT_TOKEN).read_timeout(100).get_updates_read_timeout(100).build()

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.TEXT, start)],
        states={
            ANSWER_STATE: [
                MessageHandler(filters.TEXT, pre_query_answer_handler),
            ],
        },
        fallbacks=[],
    )

    application.add_handler(conv_handler)

    print("Бот запущен...")
    application.run_polling()

"""