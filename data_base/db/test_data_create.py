import sqlite3
from random import randint
from itertools import permutations

db = sqlite3.connect('test_eng_tasks.db')
c = db.cursor()

'''
#создание случайных ответов
random_answers = []
for x in permutations('0123456789',5):
    a = ''.join(x)
    random_answers.append(a)

#создание случайных номеров на каком-либо сайте-сборнике заданий (сдам-гиа, как пример)
random_nums = []
for x in permutations('0123456789',3):
    a = ''.join(x)
    random_nums.append(a)

#создание списки с рандомными данными для 10 задания
reshu = []
kim = [10] * 20
content_task = []
otvet = []

#добавляем всякую инфу в списки
for i in range(1, 21):
    t_reshu = random_nums[randint(1, 100)]
    t_content_task = f'Установите соответсвие. Номер задания: {randint(1, 100)}'
    t_otvet = random_answers[randint(1, 100)]

    reshu.append(t_reshu)
    content_task.append(t_content_task)
    otvet.append(str(t_otvet))

#дебаг, выводим залупу эту
print(reshu[6])
print(kim[6])
print(content_task[6])
print(otvet[6])

#добавляем данные для 10 задания из КИМ
for i in range(10):
    c.execute('INSERT INTO zadania (site_number, kim_number, task_content, task_answer) VALUES (?, ?, ?, ?)', (reshu[i], kim[i], content_task[i], otvet[i]))
'''


# функция, которая генерирует и вставляет данные для 11 задание КИМ
def generator_kim_task_10_11(num_of_kim, count):
    pp_num = []

    for x in permutations('0123456789', 3):
        a = ''.join(x)
        pp_num.append(int(a))

    for i in range(count + 1):
        answer = randint(100000, 999999)
        content = f'Условие задания {num_of_kim}. Номер этого условия: {pp_num[randint(1, 700)]}'
        c.execute('INSERT INTO zadania (site_number, kim_number, task_content, task_answer) VALUES (?, ?, ?, ?)',
                  (pp_num[i], num_of_kim, content, answer))


def generator_kim_task_12_18_and_25_36(num_of_kim, count):
    pp_num = []
    answer = []

    for x in range(count + 1):
        answer.append(randint(1, 10))
    for x in permutations('0123456789', 3):
        a = ''.join(x)
        pp_num.append(int(a))
    for i in range(count + 1):
        content = f'Условие задания {num_of_kim}. Номер этого условия: {pp_num[randint(1, 700)]}'
        c.execute('INSERT INTO zadania (site_number, kim_number, task_content, task_answer) VALUES (?, ?, ?, ?)',
                  (pp_num[i], num_of_kim, content, answer[i]))


def generator_kim_task_19_24(num_of_kim, count):
    pp_num = []
    answer = [
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

    for x in permutations('0123456789', 3):
        a = ''.join(x)
        pp_num.append(int(a))

    t_pp_num = pp_num[randint(1, 700)]

    for i in range(count + 1):
        content = f'Условие задания {num_of_kim}. Номер этого условия: {t_pp_num}'
        c.execute('INSERT INTO zadania (site_number, kim_number, task_content, task_answer) VALUES (?, ?, ?, ?)',
                  (t_pp_num, num_of_kim, content, answer[randint(1, 78)]))


for i in range(10, 12):
    generator_kim_task_10_11(i, 20)

for i in range(12, 19):
    generator_kim_task_12_18_and_25_36(i, 20)

for i in range(19, 25):
    generator_kim_task_19_24(i, 20)

for i in range(25, 37):
    generator_kim_task_12_18_and_25_36(i, 20)

# сохранение изменений в бд и закрытие соединения
db.commit()
db.close()
