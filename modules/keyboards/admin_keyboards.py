from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

admin_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Посмотреть новые заказы',callback_data='check_orders')],
        [InlineKeyboardButton(text='Мой личный кабинет', callback_data='admin_profile')]
    ]
)

back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Главное меню", callback_data='admin_menu')]
    ]
)