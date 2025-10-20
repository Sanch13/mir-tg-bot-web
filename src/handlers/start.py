from aiogram import types, Router
from aiogram.filters import CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        text=f"Добро пожаловать"
    )
