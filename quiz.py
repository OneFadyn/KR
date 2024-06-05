from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN

score = 0

# Ваш код с вопросами и ответами здесь
questions = [
    "Столица России?",
    "Самая высокая гора мира?",
    "Самый длинный океан?",
    "Самый большой остров?",
    "Самое большое животное?",
]

answers = ["Москва", "Эверест", "Тихий океан", "Гренландия", "Синий кит"]

current_question_index = 0  # начинаем с первого вопроса

async def start(message: types.Message):
    global current_question_index  # используем global, чтобы изменить значение переменной вне функции
    current_question_index = 0  # сбрасываем индекс текущего вопроса
    await message.answer("Начинаем викторину")
    await message.answer(questions[current_question_index])

async def pre_query_answer_handler(message: types.Message):
    global current_question_index
    global score

    user_answer = message.text

    if user_answer.lower() == answers[current_question_index].lower():
        score += 1

    current_question_index += 1
    if current_question_index < len(questions):
        next_question = questions[current_question_index]
        await message.answer(next_question)
    else:
        await message.answer(f"Ваш результат: {score}/{len(questions)}")

if __name__ == '__main__':
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)

    dp.register_message_handler(start, commands="start")
    dp.register_message_handler(pre_query_answer_handler, content_types=types.ContentType.TEXT)

    executor.start_polling(dp, skip_updates=True)

