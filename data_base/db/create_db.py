import sqlite3

db = sqlite3.connect('test_eng_tasks.db')
c = db.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS zadania (
site_number INTEGER,
kim_number INTEGER,
task_content TEXT,
task_answer TEXT  
)''')

db.commit()
db.close()