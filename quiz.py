from os import system
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN, chat_id
class QuizStates(StatesGroup):
    quiz_1 = State()
    quiz_2 = State()
    quiz_3 = State()

questions_1 = [
    "Столица России?",
    "Самая высокая гора мира?",
    "Самый большой океан?",
    "Самый большой остров?",
    "Самое большое животное?",
]

answers_1 = ["Москва", "Эверест", "Тихий океан", "Гренландия", "Синий кит"]

questions_2 = [
    "Как называется единица измерения силы тока?",
    "Какой закон физики описывает сохранение энергии в замкнутой системе?",
    "Как называется наука, изучающая движение тел и силы, вызывающие это движение?",
    "Какой закон физики устанавливает, что каждое действие вызывает равное по величине и противоположно направленное противодействие?",
    "Как называется наука, изучающая свет и его взаимодействие с веществом?",
]

answers_2 = ["Ампер", "Закон сохранения энергии", "Механика", "Закон Ньютона", "Оптика"]

questions_3 = [
    "Какой язык программирования используется для разработки Android-приложений?",
    "Как называется операция объединения двух строк в Python?",
    "Что обозначает аббревиатура HTML?",
    "Какая структура данных используется для хранения элементов в виде ключ-значение?",
    "Какой оператор используется для проверки равенства значений в JavaScript?",
]

answers_3 = ["Java", "concatenate", "HyperText Markup Language", "Словарь", "=="]

async def start(message: Message):
    await message.answer("Добро пожаловать в режим викторины!", reply_markup=types.ReplyKeyboardRemove())
    await message.answer("На данный момент доступны 3 викторины:")
    await message.answer("№1 - Викторина на эрудицию. Нажмите /start_1, чтобы начать игру")
    await message.answer("№2 - Викторина 2. Нажмите /start_2, чтобы начать игру")
    await message.answer("№3 - Викторина 3. Нажмите /start_3, чтобы начать игру")

async def start_quiz_1(message: Message, state: FSMContext):
    await state.update_data(score=0, current_question_index=0)
    await message.answer("Начинаем викторину 1")
    await message.answer(questions_1[0])
    await QuizStates.quiz_1.set()

async def start_quiz_2(message: Message, state: FSMContext):
    await state.update_data(score=0, current_question_index=0)
    await message.answer("Начинаем викторину 2")
    await message.answer(questions_2[0])
    await QuizStates.quiz_2.set()

async def start_quiz_3(message: Message, state: FSMContext):
    await state.update_data(score=0, current_question_index=0)
    await message.answer("Начинаем викторину 3")
    await message.answer(questions_3[0])
    await QuizStates.quiz_3.set()

async def handle_answer_quiz_1(message: Message, state: FSMContext):
    state_data = await state.get_data()
    score = state_data['score']
    current_question_index = state_data['current_question_index']

    if message.text.lower() == answers_1[current_question_index].lower():
        score += 1

    current_question_index += 1

    if current_question_index < len(questions_1):
        await state.update_data(score=score, current_question_index=current_question_index)
        await message.answer(questions_1[current_question_index])
    else:
        await message.answer(f"Ваш результат: {score}/{len(questions_1)}")
        await message.answer("Викторина 1 закончена, спасибо за участие!")
        await state.finish()

async def handle_answer_quiz_2(message: Message, state: FSMContext):
    state_data = await state.get_data()
    score = state_data['score']
    current_question_index = state_data['current_question_index']

    if message.text.lower() == answers_2[current_question_index].lower():
        score += 1

    current_question_index += 1

    if current_question_index < len(questions_2):
        await state.update_data(score=score, current_question_index=current_question_index)
        await message.answer(questions_2[current_question_index])
    else:
        await message.answer(f"Ваш результат: {score}/{len(questions_2)}")
        await message.answer("Викторина 2 закончена, спасибо за участие!")
        await state.finish()

async def handle_answer_quiz_3(message: Message, state: FSMContext):
    state_data = await state.get_data()
    score = state_data['score']
    current_question_index = state_data['current_question_index']

    if message.text.lower() == answers_3[current_question_index].lower():
        score += 1

    current_question_index += 1

    if current_question_index < len(questions_3):
        await state.update_data(score=score, current_question_index=current_question_index)
        await message.answer(questions_3[current_question_index])
    else:
        await message.answer(f"Ваш результат: {score}/{len(questions_3)}")
        await message.answer("Викторина 3 закончена, спасибо за участие!")
        await state.finish()

if __name__ == '__main__':
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    dp.middleware.setup(LoggingMiddleware())

    dp.register_message_handler(start, commands="quiz", state="*")
    dp.register_message_handler(start_quiz_1, commands="start_1", state="*")
    dp.register_message_handler(start_quiz_2, commands="start_2", state="*")
    dp.register_message_handler(start_quiz_3, commands="start_3", state="*")

    dp.register_message_handler(handle_answer_quiz_1, state=QuizStates.quiz_1)
    dp.register_message_handler(handle_answer_quiz_2, state=QuizStates.quiz_2)
    dp.register_message_handler(handle_answer_quiz_3, state=QuizStates.quiz_3)

    executor.start_polling(dp, skip_updates=True)
