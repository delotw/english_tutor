import sqlite3
from itertools import permutations
import random

db = sqlite3.connect('../english_tutor.db')
c = db.cursor()
dec = 'no decision or decision link'


def gen_10_18_and_25_36(kim_num: int, count: int) -> None:
    desc = f'СОДЕРЖАНИЕ {kim_num}'
    ans = [''.join(x) for x in permutations('123456789', r=5)]
    dec = f'РЕШЕНИЕ {kim_num}'
    dec_link = 'ССЫЛКА НА РЕШЕНИЕ'

    for i in range(count):
        r = random.choice(ans)
        c.execute(
            'INSERT INTO tasks (kim_id, description, answer, decision, decision_link) VALUES (?, ?, ?, ?, ?)',
            (kim_num, desc, r, dec, dec_link)
        )


def gen_19_24(kim_num: int, count: int) -> None:
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
    dec = f'РЕШЕНИЕ {kim_num}'
    dec_link = 'ССЫЛКА НА РЕШЕНИЕ'
    desc = f'СОДЕРЖАНИЕ {kim_num}'

    for i in range(count):
        r = random.choice(ans)
        c.execute(
            'INSERT INTO tasks (kim_id, description, answer, decision, decision_link) VALUES (?, ?, ?, ?, ?)',
            (kim_num, desc, r, dec, dec_link)
        )


for i in range(10, 18):
    gen_10_18_and_25_36(i, 20)
for i in range(25, 37):
    gen_10_18_and_25_36(i, 20)
for i in range(19, 25):
    gen_19_24(i, 20)

db.commit()
db.close()
