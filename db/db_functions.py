import sqlite3
from configuration import DB_PATH

db = sqlite3.connect(DB_PATH)
cur = db.cursor()


# ? Фукнция для получения случайного задания определенного типа
# --------
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


# ? Функция для записи данных и пользователе в базу данных
# ------------
def create_paste_user_id(tg_id: int, name: str) -> None:
    # * проверка существувет ли пользователь
    cur.execute('''SELECT * FROM users WHERE tg_id = ?''', (tg_id,))
    user_check = cur.fetchone()

    if user_check:
        return

    try:
        cur.execute('''
        INSERT INTO users (tg_id, name) VALUES (?, ?)''', (tg_id, name,))
        db.commit()
        print(f'Пользователь с ID {tg_id} по имени {name} был добавлен в базу данных')
    except Exception as err:
        print(f'Не вышло добавить пользователя из-за {err}')


def paste_user_class(tg_id: int, grade: int) -> None:
    try:
        cur.execute('''
        UPDATE users 
        SET class = ?
        WHERE tg_id = ?''', (grade, tg_id))
        db.commit()
        print(f'Пользователю с ID {tg_id} был присвоен {grade} класс')
    except Exception as err:
        print(f'Не вышло присвоить класс пользователю из-за {err}')
