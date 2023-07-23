from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#Вернуться из любого действия в ПОИТ - 1 курс
ikb_midoPoit1CourseSchedule = InlineKeyboardMarkup(row_width=2)
ib_mido_poit_1course_schedule_backOne = [InlineKeyboardButton(text='Вернуться на один шаг назад', callback_data='mido_poit_1course_schedule_backOne')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back2')]
ikb_midoPoit1CourseSchedule.add(*ib_mido_poit_1course_schedule_backOne)
ikb_midoPoit1CourseSchedule.add(*ib_mido_back)
