import sqlite3

db = sqlite3.connect('./features/database/english_tutor.db')
c = db.cursor()

# создание таблицы пользователей
c.execute('''
CREATE TABLE IF NOT EXISTS users (
uid INTEGER PRIMARY KEY,
name TEXT,
balance INTEGER NOT NULL DEFAULT 149,
sex TEXT,
grade INTEGER DEFAULT 10,
solved INTEGER DEFAULT 0,
right_solved INTERGER DEFAULT 0
)''')

# создание таблицы заданий
c.execute('''
CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY AUTOINCREMENT,
type TEXT,
description TEXT,
description_url TEXT,
answer TEXT,
explanation TEXT,
explanation_url TEXT
)''')

# создание таблицы со всеми письмами пользователей
c.execute('''
CREATE TABLE IF NOT EXISTS mails (
id INTEGER PRIMARY KEY AUTOINCREMENT,
uid INTEGER,
type TEXT,
content TEXT,
date TEXT,
score TEXT,
status INTEGER DEFAULT 0,
notified INTEGER DEFAULT 0,
FOREIGN KEY (uid) REFERENCES users (uid)
)''')

c.execute('''
CREATE TABLE IF NOT EXISTS deposits (
uid INTEGER,
amount INTEGER,
date TEXT,
status INTEGER DEFAULT 0,
notified INTEGER DEFAULT 0,
FOREIGN KEY (uid) REFERENCES users (uid)
)''')


# создание таблицы с платежными операциями
c.execute('''
CREATE TABLE IF NOT EXISTS billings_operation (
billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
uid INTEGER,
type INTEGER,
check_type TEXT,
price INTEGER,
date TEXT,
FOREIGN KEY (uid) REFERENCES users (uid),
FOREIGN KEY (type) REFERENCES tasks (id)
)''')

db.commit()
db.close()
