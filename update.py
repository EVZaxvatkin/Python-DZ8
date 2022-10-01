import sqlite3
con = sqlite3.connect('schooldatabase.db')
cursorObj = con.cursor()
from sqlite3 import Error


def update_data():

    print('1. День недели')
    print('2. Номер урока')
    print('3. Время начала урока')
    print('4. Предмет')
    print('5. Школьный класс')
    print('6. Номер кабинета')
    print('7. Фамилию и инициалы учителя')
    var = input('Укажите какие данные необходимо изменить: ')

    if var == '1':
        weekday = input('Введите новое значение дня недели: ')
        n = int(input('Введите идентификатор для изменения записи: '))
        data = (weekday)
        ins = f'UPDATE schedule SET weekday = "{data}" where id = {n}'
        table = cursorObj.execute(ins)
        con.commit()

    if var =='2':
        number_lesson = input('Введите новое значение номера урока: ')
        n = int(input('Введите идентификатор для изменения записи: '))
        data = (number_lesson)
        ins = f'UPDATE schedule SET number_lesson = "{data}" where id = {n}'
        table = cursorObj.execute(ins)
        con.commit()

    if var =='3':
        time_lesson = input('Введите новое время начала урока: ')
        n = int(input('Введите идентификатор для изменения записи: '))
        data = (time_lesson)
        ins = f'UPDATE schedule SET time_lesson = "{data}" where id = {n}'
        table = cursorObj.execute(ins)
        con.commit()


    if var == '4':
        lesson = input('Введите название другого предмета: ')
        n = int(input('Введите идентификатор для изменения записи: '))
        data = (lesson)
        ins = f'UPDATE schedule SET lesson = "{data}" where id = {n}'
        table = cursorObj.execute(ins)
        con.commit()

    if var =='5':
        name_class = input('Введите новые данные класса: ')
        n = int(input('Введите идентификатор для изменения записи: '))
        data = (name_class)
        ins = f'UPDATE schedule SET name_class = "{data}" where id = {n}'
        table = cursorObj.execute(ins)
        con.commit()

    if var == '6':
        number_cabinet = input('Введите другой номер кабинета: ')
        n = int(input('Введите идентификатор для изменения записи: '))
        data = (number_cabinet)
        ins = f'UPDATE schedule SET number_cabinet = "{data}" where id = {n}'
        table = cursorObj.execute(ins)
        con.commit()

    if var == '7':
        name_teacher = input('Введите фамилию и инициалы нового учителя: ')
        n = int(input('Введите идентификатор для изменения записи: '))
        data = (name_teacher)
        ins = f'UPDATE schedule SET teacher = "{data}" where id = {n}'
        table = cursorObj.execute(ins)
        con.commit()





