from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN_API
from poit.poit_1course.poit_1course_buttons import ikb_midoPoit1CourseSchedule
from poit.poit_2course.poit_2course_buttons import ikb_midoPoit2CourseSchedule
from poit.poit_3course.poit_3course_buttons import ikb_midoPoit3CourseSchedule
from poit.poit_4course.poit_4course_buttons import ikb_midoPoit4CourseSchedule
from poit.poit_5course.poit_5course_buttons import ikb_midoPoit5CourseSchedule
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


#Функции к специальности ПОИТ
#------------------------------------------------------------------------------------------------------------------------------


#Выбор курса ПОИТ
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit')
async def handle_button(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали ПОИТ!\nВыберите какой у вас курс:', reply_markup=poit_buttons.ikb_midoPoitCourse)


#1 курс ПОИТ-------------------------------------------------------------------------------------------------------------------
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_1course')
async def handle_button_1course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 1 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_1course)


#1.1 Функция отправки фотографии .jpg с информацие о расписании занятий(ПОИТ - 1 курс)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_1course_gss')
async def handle_button_1course_gss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    # Отправка фото из папки poit_1course
    photo_path = "poit/poit_1course/poit_1course_schedule.jpg"  # Путь к вашему фото в папке poit_1course
    with open(photo_path, "rb") as photo_file:
        await bot.send_photo(callback_query.from_user.id, photo_file, caption="Общий лист расписания для 1 курса ПОИТ")
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit1CourseSchedule)


#1.2 Функция обработки график сессий 1 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_1course_ss')
async def handle_button_1course_ss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График проведения сессий 1 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit1CourseSchedule)


#1.3 Функция обработки межсессионного расписания 1 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_1course_iss')
async def handle_button_1course_iss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Расписание межсессионных занятий 1 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit1CourseSchedule)


#1.4 Функция обработки контактов преподавателей 1 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_1course_lot')
async def handle_button_1course_lot(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Контакты преподавателей 1 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit1CourseSchedule)


#1.5 Функция обработки ликвидации долгов 1 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_1course_lod')
async def handle_button_1course_lod(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Ликвидация долгов 1 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit1CourseSchedule)


#1.6 Функция обработки графика оплат 1 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_1course_ps')
async def handle_button_1course_ps(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График оплат 1 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit1CourseSchedule)


#Функция выхода из всех предложенных действий в ПОИТ - 1 курс с удалением высланной информации
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_1course_schedule_backOne')
async def handle_button_1course_back_or_back(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id-1)  # Удалить старое сообщение с кнопками
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 1 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_1course)


#2 курс ПОИТ-------------------------------------------------------------------------------------------------------------------
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_2course')
async def handle_button_2course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 2 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_2course)


#2.1 Функция отправки фотографии .jpg с информацие о расписании занятий(ПОИТ - 2 курс)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2course_gss')
async def handle_button_2course_gss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    # Отправка фото из папки poit_2course
    photo_path = "poit/poit_2course/poit_2course_schedule.jpg"  # Путь к вашему фото в папке poit_2course
    with open(photo_path, "rb") as photo_file:
        await bot.send_photo(callback_query.from_user.id, photo_file, caption="Общий лист расписания для 2 курса ПОИТ")
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit2CourseSchedule)


#2.2 Функция обработки график сессий 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2course_ss')
async def handle_button_2course_ss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График проведения сессий 2 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit2CourseSchedule)


#2.3 Функция обработки межсессионного расписания 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2course_iss')
async def handle_button_2course_iss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Расписание межсессионных занятий 2 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit2CourseSchedule)


#2.4 Функция обработки контактов преподавателей 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2course_lot')
async def handle_button_2course_lot(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Контакты преподавателей 2 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit2CourseSchedule)


#2.5 Функция обработки ликвидации долгов 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2course_lod')
async def handle_button_2course_lod(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Ликвидация долгов 2 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit2CourseSchedule)


#2.6 Функция обработки графика оплат 2 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_2course_ps')
async def handle_button_2course_ps(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График оплат 2 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit2CourseSchedule)


#Функция выхода из всех предложенных действий в ПОИТ - 2 курс с удалением высланной информации
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_2course_schedule_backOne')
async def handle_button_2course_back_or_back(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id-1)  # Удалить старое сообщение с кнопками
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 2 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_2course)


#3 курс ПОИТ-------------------------------------------------------------------------------------------------------------------
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_3course')
async def handle_button_3course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 3 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_3course)


#3.1 Функция отправки фотографии .jpg с информацие о расписании занятий(ПОИТ - 3 курс)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_3course_gss')
async def handle_button_3course_schedule(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    # Отправка фото из папки poit_3course
    photo_path = "poit/poit_3course/poit_3course_schedule.jpg"  # Путь к вашему фото в папке poit_1course
    with open(photo_path, "rb") as photo_file:
        await bot.send_photo(callback_query.from_user.id, photo_file, caption="Общий лист расписания для 3 курса ПОИТ")
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit3CourseSchedule)


#3.2 Функция обработки график сессий 3 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_3course_ss')
async def handle_button_3course_ss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График проведения сессий 3 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit3CourseSchedule)


#3.3 Функция обработки межсессионного расписания 3 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_3course_iss')
async def handle_button_3course_iss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Расписание межсессионных занятий 3 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit3CourseSchedule)


#3.4 Функция обработки контактов преподавателей 3 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_3course_lot')
async def handle_button_3course_lot(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Контакты преподавателей 3 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit3CourseSchedule)


#3.5 Функция обработки ликвидации долгов 3 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_3course_lod')
async def handle_button_3course_lod(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Ликвидация долгов 3 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit3CourseSchedule)


#3.6 Функция обработки графика оплат 3 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_3course_ps')
async def handle_button_3course_ps(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График оплат 3 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit3CourseSchedule)


#Функция выхода из всех предложенных действий в ПОИТ - 3 курс с удалением высланной информации
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_3course_schedule_backOne')
async def handle_button_3course_back_or_back(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id-1)  # Удалить старое сообщение с кнопками
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 3 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_3course)


#4 курс ПОИТ-------------------------------------------------------------------------------------------------------------------
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_4course')
async def handle_button_4course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 4 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_4course)


#4.1 Функция отправки фотографии .jpg с информацие о расписании занятий(ПОИТ - 4 курс)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_4course_gss')
async def handle_button_4course_schedule(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    # Отправка фото из папки poit_1course
    photo_path = "poit/poit_4course/poit_4course_schedule.jpg"  # Путь к вашему фото в папке poit_1course
    with open(photo_path, "rb") as photo_file:
        await bot.send_photo(callback_query.from_user.id, photo_file, caption="Общий лист расписания для 4 курса ПОИТ")
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit4CourseSchedule)


#4.2 Функция обработки график сессий 4 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_4course_ss')
async def handle_button_4course_ss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График проведения сессий 4 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit4CourseSchedule)


#4.3 Функция обработки межсессионного расписания 4 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_4course_iss')
async def handle_button_4course_iss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Расписание межсессионных занятий 4 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit4CourseSchedule)


#4.4 Функция обработки контактов преподавателей 4 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_4course_lot')
async def handle_button_4course_lot(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Контакты преподавателей 4 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit4CourseSchedule)


#4.5 Функция обработки ликвидации долгов 4 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_4course_lod')
async def handle_button_4course_lod(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Ликвидация долгов 4 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit4CourseSchedule)


#4.6 Функция обработки графика оплат 4 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_4course_ps')
async def handle_button_4course_ps(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График оплат 4 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit4CourseSchedule)


#Функция выхода из всех предложенных действий в ПОИТ - 4 курс с удалением высланной информации
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_4course_schedule_backOne')
async def handle_button_4course_back_or_back(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id-1)  # Удалить старое сообщение с кнопками
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 4 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_4course)


#5 курс ПОИТ-------------------------------------------------------------------------------------------------------------------
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_5course')
async def handle_button_5course(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 5 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_5course)


#5.1 Функция отправки фотографии .jpg с информацие о расписании занятий(ПОИТ - 5 курс)
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_5course_gss')
async def handle_button_5course_schedule(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    # Отправка фото из папки poit_1course
    photo_path = "poit/poit_5course/poit_5course_schedule.jpg"  # Путь к вашему фото в папке poit_1course
    with open(photo_path, "rb") as photo_file:
        await bot.send_photo(callback_query.from_user.id, photo_file, caption="Общий лист расписания для 5 курса ПОИТ")
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit5CourseSchedule)


#5.2 Функция обработки график сессий 5 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_5course_ss')
async def handle_button_5course_ss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График проведения сессий 5 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit5CourseSchedule)


#5.3 Функция обработки межсессионного расписания 5 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_5course_iss')
async def handle_button_5course_iss(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Расписание межсессионных занятий 5 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit5CourseSchedule)


#5.4 Функция обработки контактов преподавателей 5 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_5course_lot')
async def handle_button_5course_lot(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Контакты преподавателей 5 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit5CourseSchedule)


#5.5 Функция обработки ликвидации долгов 5 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_5course_lod')
async def handle_button_5course_lod(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='Ликвидация долгов 5 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit5CourseSchedule)


#5.6 Функция обработки графика оплат 5 курс
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'poit_5course_ps')
async def handle_button_5course_ps(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)  # Удалить старое сообщение с кнопками
    await bot.send_message(callback_query.from_user.id, text='График оплат 5 курс ПОИТ.\n' + text_messages.NO_DATA)
    await bot.send_message(callback_query.from_user.id, 'Выберите следующее действие:', reply_markup=ikb_midoPoit5CourseSchedule)


#Функция выхода из всех предложенных действий в ПОИТ - 5 курс с удалением высланной информации
@dp.callback_query_handler(lambda callback_query: callback_query.data == 'mido_poit_5course_schedule_backOne')
async def handle_button_5course_back_or_back(callback_query: types.CallbackQuery):
    await callback_query.answer()  # Ответить на запрос обратного вызова, чтобы убрать "часики" у кнопки
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id-1)  # Удалить старое сообщение с кнопками
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    await bot.send_message(callback_query.from_user.id, 'Вы выбрали 5 курс ПОИТ!\nВыберите, что Вас интересует:', reply_markup=poit_buttons.ikb_poit_5course)


#Общие функции
#------------------------------------------------------------------------------------------------------------------------------

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
