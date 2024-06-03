from config import BOT_TOKEN
from copilot import Copilot
from os import system

from telegram import Update
from telegram.ext import Application, ContextTypes, ConversationHandler, MessageHandler, filters, CommandHandler

(ENTRY_STATE, QUESTION_STATE) = range(2)


def generate_copilot(prompt: str):
    """Запрос и ответ от нейросети по запросу prompt"""

    copilot = Copilot()
    c = copilot.get_answer(prompt)

    return c


async def start(update: Update, context: ContextTypes):
    """Начинаем диалог"""

    await update.message.reply_text(
        "Привет, напиши мне что-нибудь и я обязательно тебе отвечу",
    )

    return QUESTION_STATE


# Handling the question
async def pre_query_handler(update: Update, context: ContextTypes):
    """Ждём запрос от пользователя"""

    return QUESTION_STATE


# Handling the answer
async def pre_query_answer_handler(update: Update, context: ContextTypes):
    """Выводим пользователю ответ от нейросети"""

    question = update.message.text

    if question == '/stopchat':
        await update.message.reply_text("Диалог завершен. До свидания!")

        system('python main.py')


    answer = generate_copilot(question)
    context.user_data['answer'] = answer

    await update.message.reply_text(
        answer,
    )

    return QUESTION_STATE



if __name__ == '__main__':
    application = Application.builder().token(BOT_TOKEN).read_timeout(100).get_updates_read_timeout(100).build()

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.TEXT, start)],
        states={
            QUESTION_STATE: [
                MessageHandler(filters.TEXT, pre_query_answer_handler),
            ],
        },
        fallbacks=[],
    )

    application.add_handler(conv_handler)

    print("Бот запущен...")
    application.run_polling()
