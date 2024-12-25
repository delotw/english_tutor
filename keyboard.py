from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from aiogram import types

start = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Прогуливаюсь мимо 🚶'), KeyboardButton(text='10'), KeyboardButton(text='11')]],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выбери класс, в котором сейчас учишься:'
)

agree_to_start = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Конечно ✅', callback_data='main_menu')]]
)

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подготовка", callback_data="preparation")],
        [InlineKeyboardButton(text="Личный кабинет", callback_data="user_cabinet")],
        [InlineKeyboardButton(text="Техническая поддержка", callback_data="support")],
    ]
)

preparation = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Готовые варианты 📚", callback_data="choose_exam_variants"
            )
        ],
        [
            InlineKeyboardButton(
                text="Типовые задания 📋", callback_data="choose_tamplate_tasks"
            )
        ],
        [
            InlineKeyboardButton(
                text="Проверить письмо 📝", callback_data="choose_essay"
            )
        ],
        [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")],
    ]
)

back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="main_menu")],
    ]
)

variants = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Вариант 1", callback_data="variant"),
            InlineKeyboardButton(text="Вариант 2", callback_data="variant"),
        ],
        [
            InlineKeyboardButton(text="Вариант 3", callback_data="variant"),
            InlineKeyboardButton(text="Вариант 4", callback_data="variant"),
        ],
        [
            InlineKeyboardButton(
                text="Рандомный вариант", callback_data="variant_random"
            )
        ],
        [InlineKeyboardButton(text="Назад", callback_data="preparation")],
    ]
)

template_tasks = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Аудирование 🎧", callback_data="part_audirovanie"
            ),
            InlineKeyboardButton(text="Чтение 📖", callback_data="part_reading"),
        ],
        [
            InlineKeyboardButton(
                text="Лексика и грамматика 📚", callback_data="part_grammar"
            ),
            InlineKeyboardButton(text="Письмо ✍️", callback_data="part_mail"),
        ],
        [InlineKeyboardButton(text="Назад", callback_data="preparation")],
    ]
)

check_by_choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Проверка нейросетью 🤖", callback_data="check_by_ai"
            )
        ],
        [
            InlineKeyboardButton(
                text="Проверка экспертом 👨‍🏫", callback_data="check_by_expert"
            )
        ],
        [InlineKeyboardButton(text="Назад", callback_data="preparation")],
    ]
)

back_to_essay = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="choose_essay")]
    ]
)

back_to_variants = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="choose_exam_variants")]
    ]
)

back_to_template_tasks = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Назад", callback_data="choose_tamplate_tasks")]
    ]
)
