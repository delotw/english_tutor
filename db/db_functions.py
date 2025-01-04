import sqlite3
from paths import DB_PATH
from datetime import datetime

db = sqlite3.connect(DB_PATH)
cur = db.cursor()


# Получение случайного задания определенного типа
def get_random_task(kim_id: int) -> list:
    cur.execute('''
    SELECT * FROM tasks 
    WHERE kim_id = ?
    ORDER BY RANDOM()
    LIMIT 1
    ''', (kim_id,))
    result_list = list(cur.fetchone())
    db.commit()

    return result_list


# Функция записи uid и имени пользователя в БД
def create_user(tg_id: int, name: str):
    # * проверка существувет ли пользователь
    cur.execute('''SELECT * FROM users WHERE tg_id = ?''', (tg_id,))
    user_check = cur.fetchone()
    if user_check:
        return

    cur.execute('''
    INSERT INTO users (tg_id, name) VALUES (?, ?)''', (tg_id, name,))
    db.commit()
    print(f'Пользователь с ID {tg_id} по имени {
          name} был добавлен в базу данных')


# Функция записи данных о классе пользователя в БД
def paste_grade(tg_id: int, grade: int):
    cur.execute('''
    UPDATE users 
    SET class = ?
    WHERE tg_id = ?''', (grade, tg_id))
    db.commit()
    print(f'Пользователю {tg_id} был присвоен {grade} класс')


# Геттер данных о пользователе
def get_userinfo(tg_id: int) -> list:
    cur.execute('''
    SELECT * FROM users 
    WHERE tg_id = ?''', (tg_id,))
    user_info = list(cur.fetchone())

    return user_info


# Для подсчета процента верно выполненных заданий
def calc_percentage(right: int, solved: int) -> int:
    try:
        temp = right * 100 // solved
        return temp
    except ZeroDivisionError:
        return 0


# Запись текста письма в БД для статистики
def write_text_mail(tg_id: int, mail_text: str, kim_num: int):
    date = datetime.today().strftime('%d-%m-%Y')
    cur.execute('''INSERT INTO mails (tg_id, id, mail_text, date) VALUES (?, ?, ?, ?)''',
                (tg_id, kim_num, mail_text, date,))
    print(f'Текст письма {kim_num} пользователя {tg_id} было записано в БД')
