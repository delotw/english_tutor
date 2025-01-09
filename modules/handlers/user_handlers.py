from common.states_classes import Reg, CheckMail, SolveTasks
from features.chatgpt.chatgpt_func import get_score_37
from features.database.db_functions import *
import modules.keyboards.user_keyboadrs as kb
from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from loguru import logger


# Переменные
router = Router()
user_router = Router()
mark_down = ParseMode.MARKDOWN


@user_router.message(F.text == '/start')
async def send_welcome(message: Message):
    if await check_user_exists(uid=message.from_user.id):
        text = (f"<b>Привет, {await get_user_name(uid=message.from_user.id)} 👋</b> \nВыбери интересующий тебя раздел ниже:")
        await message.answer(text=text, reply_markup=kb.main_menu)
    else:
        text = ('Привет 👋, меня зовут <b>Тьютор</b>! \nПропиши /reg для регистарции!')
        await message.answer(text=text)


@user_router.message(F.text == '/reg')
async def reg_first(message: Message, state: FSMContext):
    text = ('1️⃣: Как тебя зовут?')
    await state.set_state(Reg.name)
    await message.answer(text=text)


@user_router.message(Reg.name)
async def reg_second(message: Message, state: FSMContext):
    logger.info(f"Получен message | UID: {message.from_user.id} | cb: {message.text} ")
    await state.update_data(name=message.text)
    await state.set_state(Reg.grade)
    text = (f'2️⃣: {message.text}, в каком классе ты учишься?')
    await message.answer(text=text, reply_markup=kb.choice_grade)


@user_router.message(Reg.grade)
async def reg_third(message: Message, state: FSMContext):
    logger.info(f"Получен message | UID: {message.from_user.id} | cb: {message.text} ")
    await state.update_data(grade=message.text)
    await state.set_state(Reg.sex)
    text = (f'3️⃣: Как мне к тебе обращаться?')
    await message.answer(text=text, reply_markup=kb.choice_sex)


@user_router.message(Reg.sex)
async def reg_final(message: Message, state: FSMContext):
    logger.info(f"Получен message | UID: {message.from_user.id} | cb: {message.text} ")
    await state.update_data(sex=message.text)
    data = await state.get_data()
    uid = message.from_user.id
    name = str(data["name"])
    grade = int(data["grade"])
    sex = str(data["sex"])
    await create_user(uid=uid, name=name, grade=grade, sex=sex)
    text = ('🎉 <b>Регистрация успешно окончена, я рад, что мы познакомились поближе.</b> \n В качестве <b>подарка</b> тебе закинул немного баланса, чтобы ты мог протестировать нашу проверку писем нейронкой.\n----------\n➡️ Нажми на кнопку ниже, чтобы перейти в главное меню!')
    await state.clear()
    await message.answer(text=text, reply_markup=kb.from_register_to_main_menu)


@user_router.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.clear()  # сброс состояний пользователя
    text = (f"<b>Привет, {await get_user_name(uid=callback.from_user.id)} 👋</b> \nВыбери интересующий тебя раздел ниже:")
    await callback.message.edit_text(text=text, reply_markup=kb.main_menu)
    await callback.answer()


@user_router.callback_query(F.data == "preparation")
async def menu_preparation(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.clear()
    text = ("Отлично, что же тебя интересует? 🔖")
    await callback.message.edit_text(text=text, reply_markup=kb.preparation)
    await callback.answer()


@user_router.callback_query(F.data == "profile")
async def menu_user_profile(callback: CallbackQuery):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    uid = callback.from_user.id
    user = await get_user(uid=uid)
    temp = get_percentage(right=user["right_solved"], solved=user["solved"])
    text = (
        '<b>Твой профиль</b> 😀 \n'
        '----------\n'
        f'<b>Имя</b>: {user["name"]}\n'
        f'<b>Баланс</b>: {user["balance"]} руб.\n'
        f'<b>Класс</b>: {user["grade"]}\n'
        f'<b>Решено верно</b>: {user["right_solved"]} ({temp}%)\n'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.profile)
    await callback.answer()


@user_router.callback_query(F.data == "support")
async def menu_support(callback: CallbackQuery):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    text = (f"При возникновении проблем обращаться к @delotbtw")
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_main_menu)
    await callback.answer()


@user_router.callback_query(F.data == "choose_exam_variants")
async def menu_exam_variants(callback: CallbackQuery):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    text = ("🎲 Так, ну выбор за тобой!")
    await callback.message.edit_text(text=text, reply_markup=kb.to_variants)
    await callback.answer()


@user_router.callback_query(F.data == "choose_tamplate_tasks")
async def menu_template_tasks(callback: CallbackQuery):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    text = ("⬇️ Часть экзамена")
    await callback.message.edit_text(text=text, reply_markup=kb.to_template_tasks)
    await callback.answer()


@user_router.callback_query(F.data == "choose_essay")
async def menu_check_mail(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.clear()  # отчистка состояния при отмене проверки письма
    text = ("Ух ты, уже есть написанный текст? Круто! \nКакой тип проверки выберешь?")
    await callback.message.edit_text(text=text, reply_markup=kb.choice_check_by)
    await callback.answer()


@user_router.callback_query(F.data == "check_by_ai")
async def check_by_ai(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(CheckMail.check_type)
    await state.update_data(check_type='ai')
    text = ("⬇️ Выбери задание, которое хочешь проверить ")
    await callback.message.edit_text(text=text, reply_markup=kb.choice_check_task_by_ai)
    await callback.answer()


# todo:  Сделать наконец эту проверку эссе
@user_router.callback_query(F.data == 'choice_38_ai')
async def confirm_check_38_ai(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(CheckMail.task_type)
    await state.update_data(task_type='essay')
    text = ('Скоро, пока недоступно 🕓')
    await callback.message.edit_text(text=text, reply_markup=kb.confirm_ai_check_38)
    await callback.answer()


# * Все обработчики, связанные с проверкой 37 задания через CHATGPT
@user_router.callback_query(F.data == 'choice_37_ai')
async def confirm_check_37_ai(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(CheckMail.task_type)
    await state.update_data(task_type='mail')
    text = ('Подтверждай покупки ниже и мы начианем 💥')
    await callback.message.edit_text(text=text, reply_markup=kb.confirm_ai_check_37)
    await callback.answer()


@user_router.callback_query(F.data == 'confirm_ai_37')
async def check_37(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    user = await get_user(uid=callback.from_user.id)
    if int(user["balance"]) > 149:
        await state.set_state(CheckMail.confirmed)
        await state.update_data(confirmed='1')
        await debit_money(uid=callback.from_user.id, amount=149)
        text = ('Окей, деньги с баланса списаны. \nОтправляй мне письмо.')
        await callback.message.answer(text=text)
    else:
        text = (f'❗ <b>Недостаточно средств</b> на балансе: {user["balance"]}\n'
                'Переходи в главное меню, чтобы пополнить баланс в Профиле')
        await callback.message.edit_text(text=text, reply_markup=kb.back_to_main_menu)
    await callback.answer()


@user_router.message(CheckMail.confirmed, F.text)
async def get_ai_score_37(message: Message, state: FSMContext):
    logger.info(f"Получен message | UID: {message.from_user.id} | Письмо на оценку ")

    chatgpt_answer = await get_score_37(mail_text=message.text)
    clear_asnwer = chatgpt_answer.replace('**', '')  # чтобы не потерять форматирование

    text = (f'<b>Оценка твоего письма:</b> ⤵️ \n---------- \n<blockquote>{clear_asnwer}</blockquote> \n')
    text_1 = 'Вернуться в главное меню?'

    await state.set_state(CheckMail.check_done)
    await state.update_data(check_done='1')
    await insert_ai_mail_check(uid=message.from_user.id,
                               type='mail',
                               content=message.text,
                               score=clear_asnwer,
                               status=1)
    await message.answer(text=text)
    await message.answer(text=text_1, reply_markup=kb.check_back_to_main_menu)


# * Обработчики всего, что связано с типовыми заданиями по аудированию
@user_router.callback_query(F.data == 'part_audirovanie')
async def choice_audio_div(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    text = 'Хорошо, выбери конкретное задание:'
    await state.set_state(SolveTasks.solve_audio)
    await callback.message.edit_text(text=text, reply_markup=kb.audio_choice_div)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_main_content)
@user_router.callback_query(F.data == 'audio_main_content')
async def audio_main_content(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_main_content)
    task = await get_random_task(type='main_content')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
        f'<b>Ссылка на аудио:</b> {task["descr_url"]} \n'
        f'<b>Ответ:</b> <tg-spoiler>{task["ans"]}</tg-spoiler>'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.audio_solve_task)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_TFNS_search)
@user_router.callback_query(F.data == 'audio_TFNS_search')
async def audio_TFNS_search(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_TFNS_search)
    task = await get_random_task(type='TFNS_search')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
        f'<b>Ссылка на аудио:</b> {task["descr_url"]} \n'
        f'<b>Ответ:</b> <tg-spoiler>{task["ans"]}</tg-spoiler>'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.audio_solve_task)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_full_understanding)
@user_router.callback_query(F.data == 'audio_full_understanding')
async def audio_full_understanding(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_full_understanding)
    task = await get_random_task(type='full_understanding')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
        f'<b>Ссылка на аудио:</b> {task["descr_url"]} \n'
        f'<b>Ответ:</b> <tg-spoiler>{task["ans"]}</tg-spoiler>'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.audio_solve_task)
    await callback.answer()


# * Обработчики всего, что связано с типовыми заданиями по чтению
@user_router.callback_query(F.data == 'part_reading')
async def choice_reading_div(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    text = 'Хорошо, выбери конкретное задание:'
    await state.set_state(SolveTasks.solve_reading)
    await callback.message.edit_text(text=text, reply_markup=kb.reading_choice_div)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_match)
@user_router.callback_query(F.data == 'reading_match')
async def reading_match(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_match)
    task = await get_random_task(type='match')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
        f'<b>Ответ:</b> <tg-spoiler>{task["ans"]}</tg-spoiler>'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.reading_solve_tasks)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_insert)
@user_router.callback_query(F.data == 'reading_insert')
async def reading_insert(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_insert)
    task = await get_random_task(type='insert')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
        f'<b>Ответ:</b> <tg-spoiler>{task["ans"]}</tg-spoiler>'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.reading_solve_tasks)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_choice_right)
@user_router.callback_query(F.data == 'reading_choice_right')
async def reading_choice_right(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_choice_right)
    task = await get_random_task(type='choice_right')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
        f'<b>Ответ:</b> <tg-spoiler>{task["ans"]}</tg-spoiler>'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.reading_solve_tasks)
    await callback.answer()


# * Обработчики всего, что связано с типовыми заданиями по грамматике
@user_router.callback_query(F.data == 'part_grammar')
async def choice_grammar_div(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    text = 'Хорошо, выбери конкретное задание:'
    await state.set_state(SolveTasks.solve_grammar)
    await callback.message.edit_text(text=text, reply_markup=kb.grammar_choice_div)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_grammar)
@user_router.callback_query(F.data == 'grammar_grammar')
async def grammar_grammar(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_grammar)
    task = await get_random_task(type='grammar')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
        f'<b>Ответ:</b> <tg-spoiler>{task["ans"]}</tg-spoiler>'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.grammar_solve_tasks)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_vocabulary)
@user_router.callback_query(F.data == 'grammar_vocabulary')
async def grammar_vocabulary(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_vocabulary)
    task = await get_random_task(type='vocabulary')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
        f'<b>Ответ:</b> <tg-spoiler>{task["ans"]}</tg-spoiler>'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.grammar_solve_tasks)
    await callback.answer()


# * Обработчики всего, что связано с типовыми заданиями по написанию письма
@user_router.callback_query(F.data == 'part_mail')
async def choice_mail_div(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    text = 'Хорошо, выбери конкретное задание:'
    await state.set_state(SolveTasks.solve_mails)
    await callback.message.edit_text(text=text, reply_markup=kb.mail_choice_div)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_mail)
@user_router.callback_query(F.data == 'mail_mail')
async def mail_mail(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_mail)
    task = await get_random_task(type='mail')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.mail_solve_tasks)
    await callback.answer()


@user_router.callback_query(F.data == 'new', SolveTasks.solve_essay)
@user_router.callback_query(F.data == 'mail_essay')
async def mail_essay(callback: CallbackQuery, state: FSMContext):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await state.set_state(SolveTasks.solve_essay)
    task = await get_random_task(type='essay')
    text = (
        f'<b>Задание {task["id"]}</b> \n'
        '---------- \n'
        f'<blockquote>{task["descr"]}</blockquote>\n'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.mail_solve_tasks)
    await callback.answer()

# * Обработчики верно/неверно решенных заданий


@user_router.callback_query(F.data == 'right')
async def solve_right(callback: CallbackQuery):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await write_solve(uid=callback.from_user.id, solved=1, right_solved=1)
    await callback.answer(text='Записано')


@user_router.callback_query(F.data == 'wrong')
async def solve_wrong(callback: CallbackQuery):
    logger.info(f"Получен callback | UID: {callback.from_user.id} | cb: {callback.data} ")
    await write_solve(uid=callback.from_user.id, solved=1, right_solved=0)
    await callback.answer(text='Записано')


#! Заглушки на кнопки
@user_router.callback_query(F.data == "check_by_expert")
async def check_by_expert(callback: CallbackQuery):
    text = ('Скоро, пока недоступно 🕓')
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_essay)
    await callback.answer()


@user_router.callback_query(F.data == "variant")
async def done_variants(callback: CallbackQuery):
    text = ('Скоро, пока недоступно 🕓')
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_variants)
    await callback.answer()


@user_router.callback_query(F.data == "variant_random")
async def random_variant(callback: CallbackQuery):
    text = ('Скоро, пока недоступно 🕓')
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_variants)
    await callback.answer()


@user_router.callback_query(F.data == "part_audirovanie")
async def part_audio(callback: CallbackQuery):
    text = ('Скоро, пока недоступно 🕓')
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_template_tasks)
    await callback.answer()


@user_router.callback_query(F.data == "part_grammar")
async def part_grammar(callback: CallbackQuery):
    text = ('Скоро, пока недоступно 🕓')
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_template_tasks)
    await callback.answer()


@user_router.callback_query(F.data == "part_mail")
async def part_mail(callback: CallbackQuery):
    text = ('Скоро, пока недоступно 🕓')
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_template_tasks)
    await callback.answer()
