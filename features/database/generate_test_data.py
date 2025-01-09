import sqlite3
from itertools import permutations
import random

db = sqlite3.connect('./features/database/english_tutor.db')
c = db.cursor()
dec = 'no decision or decision link'
desc_url = 'ССЫЛКА НА ФАЙЛ'

def gen_num_ans(type: str, count: int) -> None:
    desc = f'СОДЕРЖАНИЕ {type}'
    ans = [''.join(x) for x in permutations('123456789', r=5)]
    dec = f'РЕШЕНИЕ {type}'
    dec_link = 'ССЫЛКА НА РЕШЕНИЕ'

    for i in range(count):
        r = random.choice(ans)
        c.execute(
            'INSERT INTO tasks (type, description, description_url, answer, decision, decision_url) VALUES (?, ?, ?, ?, ?, ?)',
            (type, desc, desc_url, r, dec, dec_link, )
        )


def gen_text_ans(type: str, count: int) -> None:
    ans = [
        "was", "were", "became", "began", "broke", "brought", "built", "bought", "caught",
        "chose", "came", "did", "drew", "drank", "drove", "ate", "fell", "felt", "found",
        "flew", "forgot", "got", "gave", "went", "grew", "had", "heard", "hid", "hit",
        "held", "kept", "knew", "laid", "led", "left", "lent", "let", "lay", "lost",
        "made", "meant", "met", "paid", "put", "read", "rode", "rang", "rose", "ran",
        "said", "saw", "sold", "sent", "set", "shook", "shone", "shot", "showed",
        "sang", "sat", "slept", "spoke", "spent", "stood", "stole", "stuck", "struck",
        "swam", "took", "taught", "tore", "told", "thought", "threw", "understood",
        "woke", "wore", "won", "wrote"
    ]
    dec = f'РЕШЕНИЕ {type}'
    dec_link = 'ССЫЛКА НА РЕШЕНИЕ'
    desc = f'СОДЕРЖАНИЕ {type}'

    for i in range(count):
        r = random.choice(ans)
        c.execute(
            'INSERT INTO tasks (type, description, description_url, answer, decision, decision_url) VALUES (?, ?, ?, ?, ?, ?)',
            (type, desc, desc_url, r, dec, dec_link, )
        )


task_types_nums = ['main_content', 'TFNS_search', 'full_understanding', 'match', 'insert', 'choice_right']
task_types_words = ['grammar', 'vocabulary', 'mail', 'essay']

for type in task_types_nums:
    gen_num_ans(type=type, count=50)

for type in task_types_words:
    gen_text_ans(type=type, count=50)


db.commit()
db.close()
