from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#Вернуться из любого действия в ПОИТ - 5 курс
ikb_midoPoit5CourseSchedule = InlineKeyboardMarkup(row_width=2)
ib_mido_poit_5course_schedule_backOne = [InlineKeyboardButton(text='Вернуться на один шаг назад', callback_data='mido_poit_5course_schedule_backOne')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back2')]
ikb_midoPoit5CourseSchedule.add(*ib_mido_poit_5course_schedule_backOne)
ikb_midoPoit5CourseSchedule.add(*ib_mido_back)
