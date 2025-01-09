from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.enums import ParseMode
from common.filters import IsAdmin

import modules.keyboards.admin_keyboards as akb

admin_router = Router()
admin_router.message.filter(IsAdmin())
mark_down = ParseMode.MARKDOWN

test_text = '''много
букав
блять'''


@admin_router.message(F.text == '/admin')
async def admin_start(message: Message):
    text = ('Выбери интересующий раздел')
    await message.answer(text=text, reply_markup=akb.admin_start)


@admin_router.message(F.text == '/test')
async def reg_first(message: Message):
    text = f'> {test_text}'
    await message.answer(text=text, parse_mode=mark_down)


@admin_router.callback_query(F.data == 'admin_menu')
async def admin_menu(callback: CallbackQuery):
    text = ('Выбери интересующий раздел')
    await callback.message.answer(text=text, reply_markup=akb.admin_start)


@admin_router.callback_query(F.data == 'check_orders')
async def check_orders(callback: CallbackQuery):
    text = ('Вот твои заказы:')
    await callback.message.answer(text=text, reply_markup=akb.back_to_main_menu)


@admin_router.callback_query(F.data == 'admin_profile')
async def admin_profile(callback: CallbackQuery):
    text = ('Твой профиль и статистика:')
    await callback.message.answer(text=text, reply_markup=akb.back_to_main_menu)
