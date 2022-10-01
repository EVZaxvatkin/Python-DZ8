import sqlite3
con = sqlite3.connect('schooldatabase.db')
cursorObj = con.cursor()
from sqlite3 import Error
from update import *

def new_table():


    cursorObj.execute("CREATE TABLE schedule (id integer PRIMARY KEY, weekday text, number_lesson integer, time_lesson text, lesson text, name_class text, number_cabinet integere, teacher text)")

    con.commit()
    print('Форма для заполнения расписания создана')

def insert_table():
    id = input('Ведите порядковый номер записи: ')
    weekday = input('Введите день недели: ')
    number_lesson = input('Введите номер урока: ')
    time_lesson = input('Введите время начала урока: ')
    lesson = input('Введите название предмета: ')
    name_class = input('Введите школьный класс: ')
    number_cabinet = input('Введите номер кабинета: ')
    name_teacher = input('Введите фамилию и инициалы учителя: ')

    data = (id, weekday, number_lesson, time_lesson,lesson, name_class,number_cabinet, name_teacher)

    ins = f'INSERT INTO schedule(id, weekday, number_lesson, time_lesson, lesson, name_class, number_cabinet, teacher) VALUES {data}'
    table = cursorObj.execute(ins)
    con.commit()
    print('Новые данные внесены в расписание')

def correction_table():
    print('Что необходимо сделать: ')
    print('1. Получение данных таблицы.')
    print('2. Изменить данные.')
    print('3. Удалить данные.')
    var = input('Выберете действие: ')

    if var == '1':
        cursorObj.execute("SELECT * FROM schedule;")
        result = cursorObj.fetchall()
        print(result)

    if var == '2':
        update_data()
        print('Изменение данных произведено')


    if var == '3':

        cursorObj.execute('DROP table if exists schedule')
        con.commit()
        print('Таблица удалена')
