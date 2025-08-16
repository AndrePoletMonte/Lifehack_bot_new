from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура выбора языка
language_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")
        ],
        [
            InlineKeyboardButton(text="🇷🇸 Српски", callback_data="lang_sr")
        ]
    ]
)

# Главное меню
main_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📚 Получить лайфхак", callback_data="get_hack")
        ],
        [
            InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")
        ]
    ]
)
