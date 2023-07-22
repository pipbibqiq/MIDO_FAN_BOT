from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN_API
import poit_buttons
import text_messages

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

# Словарь для хранения информации о фото для каждого пользователя
user_photo_data = {}


async def on_startup(_):
    print('The bot has been successfully launched!')


#Выбор специальности МИДО
ikb_mido = InlineKeyboardMarkup(row_width=2)
ib_mido_poit = [InlineKeyboardButton(text='ПОИТ', callback_data='mido_poit')]
ikb_mido.add(*ib_mido_poit)


#Выбор курса ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit')
async def handle_button(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали ПОИТ!\nВыберите какой у вас курс:', reply_markup=poit_buttons.ikb_midoPoitCourse)


#1 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_1course')
async def handle_button_1course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 1 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_1course)


#2 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_2course')
async def handle_button_2course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 2 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_2course)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2course_gss')
async def handle_button_2course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    # Отправка фото из папки poit_2course
    photo_path = "poit/poit_2course/poit_2course_schedule.jpg"  # Путь к вашему фото в папке poit_2course
    with open(photo_path, "rb") as photo_file:
        await bot.send_photo(callback_query.from_user.id, photo_file, caption="Расписание для групп 41702122, 41702222, 41702322")
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit2CourseSchedule)

#Вернуться из расписания 2 курс ПОИТ
ikb_midoPoit2CourseSchedule = InlineKeyboardMarkup(row_width=2)
ib_mido_poit_2course_schedule_backOne = [InlineKeyboardButton(text='Вернуться на один шаг назад', callback_data='mido_poit_2course_schedule_backOne')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back2')]
ikb_midoPoit2CourseSchedule.add(*ib_mido_poit_2course_schedule_backOne)
ikb_midoPoit2CourseSchedule.add(*ib_mido_back)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_2course_schedule_backOne')
async def handle_button_2course_schedule(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id-1)  # Удалить старое сообщение с кнопками
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 2 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_2course)


#3 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_3course')
async def handle_button_3course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 3 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_3course)


#4 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_4course')
async def handle_button_4course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 4 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_4course)


#5 курс ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_5course')
async def handle_button_5course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 5 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_5course)


#Возврат в начало #1
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'back1')
async def handle_button_back(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, text=text_messages.START_COMMAND, reply_markup=ikb_mido)  # Отправляем команду /start


#Возврат в начало #2
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'back2')
async def handle_button_back(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id-1)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, text=text_messages.START_COMMAND, reply_markup=ikb_mido)  # Отправляем команду /start


# Обработчик всех текстовых сообщений (удаляет любые сообщения, кроме команды /start)
@dp.message_handler(content_types=types.ContentType.TEXT)
async def handle_text_messages(message: types.Message):
    if message.text.strip().lower() == "/start":
        await message.answer(text=text_messages.START_COMMAND, reply_markup=ikb_mido)
        await message.delete()
    else:
        await message.delete()


# Обработчик всех медиафайлов (фото, стикеры, GIF и т.д.) (удаляет все медиа типы)
@dp.message_handler(content_types=[
    types.ContentType.PHOTO,
    types.ContentType.STICKER,
    types.ContentType.ANIMATION,
    types.ContentType.VIDEO,
    types.ContentType.DOCUMENT,
    types.ContentType.AUDIO,
    types.ContentType.VOICE,
])
async def handle_media_messages(message: types.Message):
    await message.delete()


#Команда /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=text_messages.HELP_COMMAND)


#Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text=text_messages.START_COMMAND, reply_markup=ikb_mido)
    await bot.delete_message(message.chat.id, message.message_id)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
