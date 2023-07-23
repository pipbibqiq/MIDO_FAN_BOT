from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#Выбор курса ПОИТ
ikb_midoPoitCourse = InlineKeyboardMarkup(row_width=2)
ib_mido_poit_1course = [InlineKeyboardButton(text='1 курс', callback_data='mido_poit_1course')]
ib_mido_poit_2course = [InlineKeyboardButton(text='2 курс', callback_data='mido_poit_2course')]
ib_mido_poit_3course = [InlineKeyboardButton(text='3 курс', callback_data='mido_poit_3course')]
ib_mido_poit_4course = [InlineKeyboardButton(text='4 курс', callback_data='mido_poit_4course')]
ib_mido_poit_5course = [InlineKeyboardButton(text='5 курс', callback_data='mido_poit_5course')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back1')]
ikb_midoPoitCourse.add(*ib_mido_poit_1course)
ikb_midoPoitCourse.add(*ib_mido_poit_2course)
ikb_midoPoitCourse.add(*ib_mido_poit_3course)
ikb_midoPoitCourse.add(*ib_mido_poit_4course)
ikb_midoPoitCourse.add(*ib_mido_poit_5course)
ikb_midoPoitCourse.add(*ib_mido_back)

#1 курс ПОИТ
ikb_poit_1course = InlineKeyboardMarkup(row_width=2)
ib_poit_1course_generalScheduleSheet = [InlineKeyboardButton(text='Расписание', callback_data='poit_1course_gss')]
ib_poit_1course_sessionSchedule = [InlineKeyboardButton(text='График проведения сессий', callback_data='poit_1course_ss')]
ib_poit_1course_interSessionSchedule = [InlineKeyboardButton(text='Расписание межсессионных занятий', callback_data='poit_1course_iss')]
ib_poit_1course_listOfTeachers = [InlineKeyboardButton(text='Контакты преподавателей', callback_data='poit_1course_lot')]
ib_poit_1course_deans = [InlineKeyboardButton(text='Деканат', callback_data='poit_1course_deans')]
ib_poit_1course_liquidationOfDebts = [InlineKeyboardButton(text='Ликвидация долгов', callback_data='poit_1course_lod')]
ib_poit_1course_paymentSchedule = [InlineKeyboardButton(text='График оплат', callback_data='poit_1course_ps')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back1')]
ikb_poit_1course.add(*ib_poit_1course_generalScheduleSheet)
ikb_poit_1course.add(*ib_poit_1course_sessionSchedule)
ikb_poit_1course.add(*ib_poit_1course_interSessionSchedule)
ikb_poit_1course.add(*ib_poit_1course_listOfTeachers)
ikb_poit_1course.add(*ib_poit_1course_deans)
ikb_poit_1course.add(*ib_poit_1course_liquidationOfDebts)
ikb_poit_1course.add(*ib_poit_1course_paymentSchedule)
ikb_poit_1course.add(*ib_mido_back)

#2 курс ПОИТ
ikb_poit_2course = InlineKeyboardMarkup(row_width=2)
ib_poit_2course_generalScheduleSheet = [InlineKeyboardButton(text='Расписание', callback_data='poit_2course_gss')]
ib_poit_2course_sessionSchedule = [InlineKeyboardButton(text='График проведения сессий', callback_data='poit_2course_ss')]
ib_poit_2course_interSessionSchedule = [InlineKeyboardButton(text='Расписание межсессионных занятий', callback_data='poit_2course_iss')]
ib_poit_2course_listOfTeachers = [InlineKeyboardButton(text='Контакты преподавателей', callback_data='poit_2course_lot')]
ib_poit_2course_deans = [InlineKeyboardButton(text='Деканат', callback_data='poit_2course_deans')]
ib_poit_2course_liquidationOfDebts = [InlineKeyboardButton(text='Ликвидация долгов', callback_data='poit_2course_lod')]
ib_poit_2course_paymentSchedule = [InlineKeyboardButton(text='График оплат', callback_data='poit_2course_ps')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back1')]
ikb_poit_2course.add(*ib_poit_2course_generalScheduleSheet)
ikb_poit_2course.add(*ib_poit_2course_sessionSchedule)
ikb_poit_2course.add(*ib_poit_2course_interSessionSchedule)
ikb_poit_2course.add(*ib_poit_2course_listOfTeachers)
ikb_poit_2course.add(*ib_poit_2course_deans)
ikb_poit_2course.add(*ib_poit_2course_liquidationOfDebts)
ikb_poit_2course.add(*ib_poit_2course_paymentSchedule)
ikb_poit_2course.add(*ib_mido_back)

#3 курс ПОИТ
ikb_poit_3course = InlineKeyboardMarkup(row_width=2)
ib_poit_3course_generalScheduleSheet = [InlineKeyboardButton(text='Расписание', callback_data='poit_3course_gss')]
ib_poit_3course_sessionSchedule = [InlineKeyboardButton(text='График проведения сессий', callback_data='poit_3course_ss')]
ib_poit_3course_interSessionSchedule = [InlineKeyboardButton(text='Расписание межсессионных занятий', callback_data='poit_3course_iss')]
ib_poit_3course_listOfTeachers = [InlineKeyboardButton(text='Контакты преподавателей', callback_data='poit_3course_lot')]
ib_poit_3course_deans = [InlineKeyboardButton(text='Деканат', callback_data='poit_3course_deans')]
ib_poit_3course_liquidationOfDebts = [InlineKeyboardButton(text='Ликвидация долгов', callback_data='poit_3course_lod')]
ib_poit_3course_paymentSchedule = [InlineKeyboardButton(text='График оплат', callback_data='poit_3course_ps')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back1')]
ikb_poit_3course.add(*ib_poit_3course_generalScheduleSheet)
ikb_poit_3course.add(*ib_poit_3course_sessionSchedule)
ikb_poit_3course.add(*ib_poit_3course_interSessionSchedule)
ikb_poit_3course.add(*ib_poit_3course_listOfTeachers)
ikb_poit_3course.add(*ib_poit_3course_deans)
ikb_poit_3course.add(*ib_poit_3course_liquidationOfDebts)
ikb_poit_3course.add(*ib_poit_3course_paymentSchedule)
ikb_poit_3course.add(*ib_mido_back)

#4 курс ПОИТ
ikb_poit_4course = InlineKeyboardMarkup(row_width=2)
ib_poit_4course_generalScheduleSheet = [InlineKeyboardButton(text='Расписание', callback_data='poit_4course_gss')]
ib_poit_4course_sessionSchedule = [InlineKeyboardButton(text='График проведения сессий', callback_data='poit_4course_ss')]
ib_poit_4course_interSessionSchedule = [InlineKeyboardButton(text='Расписание межсессионных занятий', callback_data='poit_4course_iss')]
ib_poit_4course_listOfTeachers = [InlineKeyboardButton(text='Контакты преподавателей', callback_data='poit_4course_lot')]
ib_poit_4course_deans = [InlineKeyboardButton(text='Деканат', callback_data='poit_4course_deans')]
ib_poit_4course_liquidationOfDebts = [InlineKeyboardButton(text='Ликвидация долгов', callback_data='poit_4course_lod')]
ib_poit_4course_paymentSchedule = [InlineKeyboardButton(text='График оплат', callback_data='poit_4course_ps')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back1')]
ikb_poit_4course.add(*ib_poit_4course_generalScheduleSheet)
ikb_poit_4course.add(*ib_poit_4course_sessionSchedule)
ikb_poit_4course.add(*ib_poit_4course_interSessionSchedule)
ikb_poit_4course.add(*ib_poit_4course_listOfTeachers)
ikb_poit_4course.add(*ib_poit_4course_deans)
ikb_poit_4course.add(*ib_poit_4course_liquidationOfDebts)
ikb_poit_4course.add(*ib_poit_4course_paymentSchedule)
ikb_poit_4course.add(*ib_mido_back)

#5 курс ПОИТ
ikb_poit_5course = InlineKeyboardMarkup(row_width=2)
ib_poit_5course_generalScheduleSheet = [InlineKeyboardButton(text='Расписание', callback_data='poit_5course_gss')]
ib_poit_5course_sessionSchedule = [InlineKeyboardButton(text='График проведения сессий', callback_data='poit_5course_ss')]
ib_poit_5course_interSessionSchedule = [InlineKeyboardButton(text='Расписание межсессионных занятий', callback_data='poit_5course_iss')]
ib_poit_5course_listOfTeachers = [InlineKeyboardButton(text='Контакты преподавателей', callback_data='poit_5course_lot')]
ib_poit_5course_deans = [InlineKeyboardButton(text='Деканат', callback_data='poit_5course_deans')]
ib_poit_5course_liquidationOfDebts = [InlineKeyboardButton(text='Ликвидация долгов', callback_data='poit_5course_lod')]
ib_poit_5course_paymentSchedule = [InlineKeyboardButton(text='График оплат', callback_data='poit_5course_ps')]
ib_mido_back = [InlineKeyboardButton(text='Вернуться в начало', callback_data='back1')]
ikb_poit_5course.add(*ib_poit_5course_generalScheduleSheet)
ikb_poit_5course.add(*ib_poit_5course_sessionSchedule)
ikb_poit_5course.add(*ib_poit_5course_interSessionSchedule)
ikb_poit_5course.add(*ib_poit_5course_listOfTeachers)
ikb_poit_5course.add(*ib_poit_5course_deans)
ikb_poit_5course.add(*ib_poit_5course_liquidationOfDebts)
ikb_poit_5course.add(*ib_poit_5course_paymentSchedule)
ikb_poit_5course.add(*ib_mido_back)
