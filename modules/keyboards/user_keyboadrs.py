from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from annotated_types import T

choice_grade = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Прогуливаюсь мимо 🚶'),
         KeyboardButton(text='10'),
         KeyboardButton(text='11')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)


choice_sex = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Господин 🤵‍♂️'),
         KeyboardButton(text='Госпожа 🤵‍♀️')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


agree_to_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Конечно ✅', callback_data='main_menu')]
    ]
)


from_register_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="В главное меню ✅", callback_data='main_menu')]
    ]
)

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Подготовка 🎯", callback_data="preparation")],
        [InlineKeyboardButton(text="Профиль ℹ️", callback_data="profile")],
        [InlineKeyboardButton(text="Поддержка ☎️", callback_data="support")],
    ]
)

preparation = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Готовые варианты 📚", callback_data="choose_exam_variants")],
        [InlineKeyboardButton(text="Типовые задания 📋", callback_data="choose_tamplate_tasks")],
        [InlineKeyboardButton(text="Проверить письмо 📝", callback_data="choose_essay")],
        [InlineKeyboardButton(text="⬅️ Главное меню", callback_data="main_menu")],
    ]
)

back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Главное меню", callback_data="main_menu")],
    ]
)

to_variants = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Вариант 1", callback_data="variant"),
         InlineKeyboardButton(text="Вариант 2", callback_data="variant"), ],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="preparation")],
    ]
)

to_template_tasks = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Аудирование 🎧", callback_data="part_audirovanie"),
         InlineKeyboardButton(text="Чтение 📖", callback_data="part_reading"), ],
        [InlineKeyboardButton(text="Лексика и грамматика 📚", callback_data="part_grammar"),
         InlineKeyboardButton(text="Письмо ✍️", callback_data="part_mail"), ],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="preparation")],
    ]
)

choice_check_by = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Проверка нейросетью 🤖", callback_data="check_by_ai")],
        [InlineKeyboardButton(text="Проверка экспертом 👨‍🏫", callback_data="check_by_expert")],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="preparation")],
    ]
)

back_to_essay = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="choose_essay")]
    ]
)

back_to_variants = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="⬅️ Назад", callback_data="choose_exam_variants")]
    ]
)

back_to_template_tasks = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(
            text="⬅️ Назад", callback_data="choose_tamplate_tasks")]
    ]
)

choice_check_task_by_ai = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='37', callback_data='choice_37_ai'),
         InlineKeyboardButton(text='38', callback_data='choice_38_ai')],
        [InlineKeyboardButton(text='Назад', callback_data='choose_essay')]
    ]
)

choice_check_task_by_expert = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='37', callback_data='choice_37_expert'),
         InlineKeyboardButton(text='38', callback_data='choice_38_expert')]
    ]
)

profile = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пополнить баланс 💰', callback_data='deposit')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='main_menu')],
    ]
)

confirm_deny_deposit = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Подтверждаю ✅', callback_data='confirm_deposit')],
        [InlineKeyboardButton(text='Отмена, в главное меню ❌', callback_data='main_menu')]
    ]
)

confirm_ai_check_37 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Подтверждаю ✅', callback_data='confirm_ai_37')],
        [InlineKeyboardButton(text='Отмена ❌', callback_data='choose_essay')]
    ]
)

confirm_ai_check_38 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='check_by_ai')],
    ]
)

check_back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Главное меню', callback_data='main_menu')]
    ]
)

audio_choice_div = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Понимание основного содержания (1)', callback_data='audio_main_content')],
        [InlineKeyboardButton(text='True, false, not stated (2)', callback_data='audio_TFNS_search')],
        [InlineKeyboardButton(text='Полное понимание речи (3-9)', callback_data='audio_full_understanding')],
        [InlineKeyboardButton(text='Назад', callback_data='choose_tamplate_tasks')]
    ]
)

reading_choice_div = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Соответствие заголовок-текст (10)', callback_data='reading_match')],
        [InlineKeyboardButton(text='Вставка конструкций в текст (11)', callback_data='reading_insert')],
        [InlineKeyboardButton(text='Текст и 1 правильный овтет из 4 (12-18)', callback_data='reading_choice_right')],
        [InlineKeyboardButton(text='Назад', callback_data='choose_tamplate_tasks')]
    ]
)
grammar_choice_div = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Грамматика слов (19-24)', callback_data='grammar_grammar')],
        [InlineKeyboardButton(text='Грамматика и лексика слов (25-36)', callback_data='grammar_vocabulary')],
        [InlineKeyboardButton(text='Назад', callback_data='choose_tamplate_tasks')]
    ]
)

mail_choice_div = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Письмо (37)', callback_data='mail_mail')],
        [InlineKeyboardButton(text='Эссе (38)', callback_data='mail_essay')],
        [InlineKeyboardButton(text='Назад', callback_data='choose_tamplate_tasks')]
    ]
)

audio_solve_task = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅', callback_data='right'),
         InlineKeyboardButton(text='❌', callback_data='wrong')],
        [InlineKeyboardButton(text='Новое задание 🆕', callback_data='new')],
        [InlineKeyboardButton(text='Назад', callback_data='part_audirovanie')]

    ]
)

reading_solve_tasks = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅', callback_data='right'),
         InlineKeyboardButton(text='❌', callback_data='wrong')],
        [InlineKeyboardButton(text='Новое задание 🆕', callback_data='new')],
        [InlineKeyboardButton(text='Назад', callback_data='part_reading')]

    ]
)

grammar_solve_tasks = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='✅', callback_data='right'),
         InlineKeyboardButton(text='❌', callback_data='wrong')],
        [InlineKeyboardButton(text='Новое задание 🆕', callback_data='new')],
        [InlineKeyboardButton(text='Назад', callback_data='part_grammar')]

    ]
)


mail_solve_tasks = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Новое задание 🆕', callback_data='new')],
        [InlineKeyboardButton(text='Назад', callback_data='part_mail')]
    ]
)
