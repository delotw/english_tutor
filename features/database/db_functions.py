import aiosqlite
from settings import DB
from datetime import datetime
from loguru import logger


async def get_random_task(type: str) -> dict:
    db = await aiosqlite.connect(DB)
    cur = await db.cursor()

    await cur.execute('''
    SELECT * FROM tasks 
    WHERE type = ?
    ORDER BY RANDOM()
    LIMIT 1
    ''', (type,))
    res = list(await cur.fetchone())
    await db.commit()
    await db.close()

    data = {
        "id": res[0],
        "type": res[1],
        "descr": res[2],
        "descr_url": res[3],
        "ans": res[4],
        "exp": res[5],
        "exp_url": res[6]
    }

    return data


async def create_user(uid: int, name: str, grade: int, sex: str):
    db = await aiosqlite.connect(DB)
    cur = await db.cursor()

    # * проверка существувет ли пользователь
    await cur.execute('''SELECT * FROM users WHERE uid = ?''', (uid,))
    user_check = await cur.fetchone()
    if user_check:
        return

    await cur.execute('INSERT INTO users (uid, name, sex, grade) VALUES (?, ?, ?, ?)', (uid, name, sex, grade,))
    await db.commit()
    await db.close()
    logger.success(f'Добавлен пользователь | UID: {uid} | Имя: {name} | Класс {grade}')


async def check_user_exists(uid: int) -> bool:
    db = await aiosqlite.connect(DB)
    cur = await db.cursor()

    await cur.execute('''SELECT * FROM users WHERE uid = ?''', (uid,))
    user_check = await cur.fetchone()
    await db.close()

    if user_check:
        return True
    else:
        return False


async def get_user(uid: int) -> dict:
    db = await aiosqlite.connect(DB)
    cur = await db.cursor()

    await cur.execute('''
    SELECT * FROM users 
    WHERE uid = ?''', (uid,))
    info = list(await cur.fetchone())
    data = {
        "uid": info[0],
        "name": info[1],
        "balance": info[2],
        "sex": info[3],
        "grade": info[4],
        "solved": info[5],
        "right_solved": info[6]
    }
    await db.close()
    return data


async def get_user_name(uid: int) -> str:
    db = await aiosqlite.connect(DB)
    cur = await db.cursor()

    await cur.execute('''
    SELECT * FROM users 
    WHERE uid = ?''', (uid,))
    user_info = list(await cur.fetchone())
    await db.close()
    return user_info[1]


def get_percentage(right: int, solved: int) -> int:
    try:
        res = right * 100 // solved
        return res
    except ZeroDivisionError:
        return 0


async def insert_ai_mail_check(uid: int, type: str, content: str, score: str, status: int):
    date = datetime.today().strftime('%d-%m-%Y')
    db = await aiosqlite.connect(DB)
    cur = await db.cursor()

    await cur.execute('INSERT INTO mails (uid, type, content, date, score, status) VALUES (?, ?, ?, ?, ?, ?)', (uid, type, content, score, date, status, ))
    await db.commit()
    await db.close()
    logger.success(f'Добавлено письмо | UID: {uid} | Тип: {type}')


async def debit_money(uid: int, amount: int):
    db = await aiosqlite.connect(DB)
    cur = await db.cursor()
    await cur.execute(f'UPDATE users SET balance = balance - {amount} WHERE uid = ?', (uid, ))
    await db.commit()
    await db.close()
    logger.success(f'Оплачена услуга | UID: {uid} | Сумма: {amount}')


async def write_solve(uid: int, solved: int, right_solved: int):
    db = await aiosqlite.connect(DB)
    cur = await db.cursor()
    await cur.execute(f'UPDATE users SET solved = solved + {solved}, right_solved = right_solved + {right_solved} where uid = {uid}')
    await db.commit()
    await db.close()
    logger.info(f'Изменена статистика заданий | UID: {uid} | Решено: {solved} | Верно: {right_solved}')
