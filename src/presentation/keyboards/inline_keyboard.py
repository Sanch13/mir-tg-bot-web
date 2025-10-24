from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# def get_main_menu():
#     buttons = [
#         [KeyboardButton(text="🔍🧴 Подбор упаковки")],
#         [KeyboardButton(text="👨‍💼📱 Консультация менеджера")],
#         [KeyboardButton(text="Минимальная партия")],
#         [KeyboardButton(text="О МИРАН"), KeyboardButton(text="FAQ")],
#     ]
#     return ReplyKeyboardMarkup(
#         keyboard=buttons,
#         resize_keyboard=True,   # кнопки подгоняются под ширину экрана
#         one_time_keyboard=False
#     )


def get_main_menu() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="🔎🧴 Подбор упаковки", callback_data="search_packaging"),
        ],
        [
            InlineKeyboardButton(
                text="ㅤ    👨‍💼📱 Консультация менеджера    ㅤ",  # тут стоят не видимые символы
                callback_data="manager_consultation",
            ),
        ],
        [
            InlineKeyboardButton(text="ㅤ   🚚 📦 Минимальная партия    ㅤ", callback_data="min_order"),
        ],
        [
            InlineKeyboardButton(text="📋️ О МИРАН", callback_data="about_miran"),
            InlineKeyboardButton(text="⁉️ FAQ", callback_data="faq"),
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def return_main_menu() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="Меню", callback_data="main_menu"),
        ],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_inline_agree_rules() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(text="Да", callback_data="yes"),
            InlineKeyboardButton(text="Нет", callback_data="no"),
        ]
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
