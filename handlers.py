from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from db.db_functions import *
import keyboard as kb

# Переменные
# ------------------------------------
p_html = ParseMode.HTML
router = Router()


# Привественное сообщение и получение данных о пользователе
# ------------------------------------
@router.message(F.text == '/start')
async def send_welcome(message: types.Message) -> None:
    # f'<b>Привет, {message.from_user.first_name} </b>👋\n'
    text = (f'Меня зовут <b>Тьютор</b>, я помогу тебе подготовиться к ЕГЭ по английскому!\n'
            f'Выбери класс, в котом ты сейчас учишься:')

    # Запись данных в БД
    create_user(tg_id=message.from_user.id, name=message.from_user.first_name)

    await message.answer(text=text, reply_markup=kb.start, parse_mode=p_html)


# Продолжение первичной регистрации пользователя, запись данных и классе юзера в БД
# ------------------------------------
@router.message(F.text.in_(['10', '11', 'Прогуливаюсь мимо 🚶']))
async def paste_class(message: types.Message) -> None:
    # Запись данных в БД
    paste_grade(tg_id=message.from_user.id, grade=message.text)
    text = (
        'Отлично, я узнал о тебе все, что мне требовалось!\n'
        'Готов приступить к своей лучшей подготовке к ЕГЭ? 🤩'
    )
    await message.delete()
    await message.answer(text=text, reply_markup=kb.agree_to_start, parse_mode=p_html)


# Возвращение в главное меню
# ------------------------------------
@router.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: types.CallbackQuery) -> None:
    text = (
        f"<b>Привет, {callback.from_user.first_name} 👋</b> \nВыбери интересующий тебя раздел ниже:"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.main_menu, parse_mode=p_html)
    await callback.answer()


# Меню "Подготовка"
# ------------------------------------
@router.callback_query(F.data == "preparation")
async def menu_preparation(callback: types.CallbackQuery) -> None:
    text = (
        "Отлично, что же тебя интересует?"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.preparation, parse_mode=p_html)
    await callback.answer()


# Меню личного кабинета пользователя
# ------------------------------------
@router.callback_query(F.data == "user_cabinet")
async def menu_user_profile(callback: types.CallbackQuery) -> None:
    tg_id = callback.from_user.id
    user_info = get_userinfo(tg_id=tg_id)
    name, grade, task_solved, task_solved_right = user_info[1], user_info[3], user_info[4], user_info[5]
    temp = calc_percentage(right=task_solved_right, solved=task_solved)
    text = (
        f'<b>Имя:</b> {name}\n'
        f'<b>Класс:</b> {grade}\n'
        f'<b>Заданий решено:</b> {task_solved}\n'
        f'<b>Решено верно:</b> {task_solved_right} ({temp})'
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_main_menu, parse_mode=p_html)
    await callback.answer()


# Меню с технической поддержкой
# ------------------------------------
@router.callback_query(F.data == "support")
async def menu_support(callback: types.CallbackQuery) -> None:
    text = (
        "При возникновении проблем обращаться: @delotbtw"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_main_menu, parse_mode=p_html)


# Выбор готового варианта
# ------------------------------------
@router.callback_query(F.data == "choose_exam_variants")
async def menu_exam_variants(callback: types.CallbackQuery) -> None:
    text = (
        "Так, ну выбор за тобой!"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.variants, parse_mode=p_html)
    await callback.answer()


# Выбор типовых заданий
# ------------------------------------
@router.callback_query(F.data == "choose_tamplate_tasks")
async def menu_template_tasks(callback: types.CallbackQuery) -> None:
    text = (
        "Часть экзамена:"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.template_tasks, parse_mode=p_html)
    await callback.answer()


# Раздел с проверкой письма
# ------------------------------------
@router.callback_query(F.data == "choose_essay")
async def menu_check_mail(callback: types.CallbackQuery) -> None:
    text = (
        "Ух ты, уже есть написанное письмо? Круто! \nКакой тип проверки выберешь?"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.check_by_choice, parse_mode=p_html)
    await callback.answer()


# !!!!!!!!!!! !!ТУПО ЗАГЛУШКИ ДЛЯ КНОПОК, ПОКА НЕ НАПИШУ ПОД НИХ КОД !!!!!!!!!!!
# ? Заглушка на проверку экспертом
# ------------------------------------
@router.callback_query(F.data == "check_by_expert")
async def check_by_expert(callback: types.CallbackQuery) -> None:
    text = (
        "Пока в разработке, скоро исправим 😆"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_essay, parse_mode=p_html)
    await callback.answer()


# ? Заглушка на проверку нейронкой
# ------------------------------------
@router.callback_query(F.data == "check_by_ai")
async def check_by_ai(callback: types.CallbackQuery) -> None:
    text = (
        "Пока в разработке, скоро исправим 😆"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_essay, parse_mode=p_html)
    await callback.answer()


# ? Заглушка на готовые нумерованные варианты
# ------------------------------------
@router.callback_query(F.data == "variant")
async def done_variants(callback: types.CallbackQuery) -> None:
    text = (
        "Пока в разработке, скоро исправим 😆"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_variants, parse_mode=p_html)
    await callback.answer()


# ? Заглушка на рандомный варинат
# ------------------------------------
@router.callback_query(F.data == "variant_random")
async def random_variant(callback: types.CallbackQuery) -> None:
    text = (
        "Пока в разработке, скоро исправим 😆"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_variants, parse_mode=p_html)
    await callback.answer()


# ? Заглушка на аудирование
# ------------------------------------
@router.callback_query(F.data == "part_audirovanie")
async def part_audio(callback: types.CallbackQuery) -> None:
    text = (
        "Пока в разработке, скоро исправим 😆"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_template_tasks, parse_mode=p_html)
    await callback.answer()


# ? Заглушка на чтение
# ------------------------------------
@router.callback_query(F.data == "part_reading")
async def part_reading(callback: types.CallbackQuery) -> None:
    text = (
        "Пока в разработке, скоро исправим 😆"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_template_tasks, parse_mode=p_html)
    await callback.answer()


# ? Заглушка на чтение
# ------------------------------------
@router.callback_query(F.data == "part_grammar")
async def part_grammar(callback: types.CallbackQuery) -> None:
    text = (
        "Пока в разработке, скоро исправим 😆"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_template_tasks, parse_mode=p_html)
    await callback.answer()


# ? Заглушка на чтение
# ------------------------------------
@router.callback_query(F.data == "part_mail")
async def part_mail(callback: types.CallbackQuery) -> None:
    text = (
        "Пока в разработке, скоро исправим 😆"
    )
    await callback.message.edit_text(text=text, reply_markup=kb.back_to_template_tasks, parse_mode=p_html)
    await callback.answer()
