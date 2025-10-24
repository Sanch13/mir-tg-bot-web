from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from src.presentation.keyboards.inline_keyboard import get_main_menu, return_main_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = get_main_menu()
    await message.answer(
        text="ㅤㅤㅤㅤㅤㅤ       Меню       ㅤㅤㅤ",
        reply_markup=keyboard,
    )


@router.callback_query(F.data == "search_packaging")
async def process_search_packaging(callback_query: CallbackQuery):
    await callback_query.message.answer(
        text="Нажата кнопка 🔍🧴 Подбор упаковки",
    )
    await callback_query.answer()


@router.callback_query(F.data == "manager_consultation")
async def process_manager_consultation(callback_query: CallbackQuery):
    await callback_query.message.answer(
        text="Нажата кнопка 👨‍💼📱 Консультация менеджера",
    )
    await callback_query.answer()


@router.callback_query(F.data == "min_order")
async def process_min_order(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="🚚 📦 Минимальная партия\n\nИнформация о минимальных партиях заказа...",
        reply_markup=return_main_menu(),
    )
    await callback_query.answer()


@router.callback_query(F.data == "about_miran")
async def process_about_miran(callback_query: CallbackQuery):
    # Редактируем существующее сообщение (меняем меню на описание)
    await callback_query.message.edit_text(
        text="📋 О компании МИРАН\n\n"
        "Здесь будет ваше описание компании...\n"
        "Подробная информация о деятельности, "
        "истории и преимуществах компании МИРАН.",
        reply_markup=return_main_menu(),
    )
    await callback_query.answer()


@router.callback_query(F.data == "faq")
async def process_faq(callback_query: CallbackQuery):
    await callback_query.message.answer(
        text="Нажата кнопка ⁉️ FAQ",
    )
    await callback_query.answer()


@router.callback_query(F.data == "main_menu")
async def process_return_main_menu(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text="ㅤㅤㅤㅤㅤㅤ       Меню       ㅤㅤㅤ", reply_markup=get_main_menu())
    await callback_query.answer()


@router.message(Command("menu"))
async def cmd_menu(message: Message):
    keyboard = get_main_menu()
    await message.answer(text="ㅤㅤㅤㅤㅤㅤ       Меню       ㅤㅤㅤ", reply_markup=keyboard)
