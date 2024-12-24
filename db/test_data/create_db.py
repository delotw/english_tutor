import sqlite3

db = sqlite3.connect('../english_tutor.db')
c = db.cursor()

# создание таблицы пользователей
c.execute('''
CREATE TABLE IF NOT EXISTS users (
tg_id INTEGER PRIMARY KEY,
name TEXT,
sex TEXT,
class INTEGER DEFAULT 10,
tasks_solved INTEGER DEFAULT 0,
tasks_solved_right INTERGER DEFAULT 0
)''')

# создание таблицы заданий
c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
kim_id INTEGER,
task_id INTEGER PRIMARY KEY AUTOINCREMENT,
description TEXT,
answer TEXT,
decision TEXT,
decision_link TEXT
)''')

# создание таблицы со всеми письмами пользователей
c.execute('''
CREATE TABLE IF NOT EXISTS mails (
mail_id INTEGER PRIMARY KEY AUTOINCREMENT,
tg_id INTEGER,
id INTEGER,
mail_text TEXT,
date TEXT,
FOREIGN KEY (tg_id) REFERENCES users (tg_id)
)''')

# создание таблицы с платежными операциями
c.execute('''
CREATE TABLE IF NOT EXISTS billings_operation (
billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
tg_id INTEGER,
task_id INTEGER,
mail_id INTEGER,
check_type TEXT,
price INTEGER,
payment_system TEXT,
date TEXT,
FOREIGN KEY (mail_id) REFERENCES mails (mail_id),
FOREIGN KEY (tg_id) REFERENCES users (tg_id),
FOREIGN KEY (task_id) REFERENCES tasks (id)
)''')

db.commit()
db.close()
