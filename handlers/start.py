from aiogram import Router
from aiogram.types import Message, CallbackQuery
from keyboards.inline import language_keyboard, main_menu_keyboard

router = Router()

@router.message(commands=["start"])
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Выберите язык / Choose your language / Изаберите језик:",
        reply_markup=language_keyboard
    )

@router.callback_query(lambda c: c.data and c.data.startswith("lang_"))
async def process_language(callback_query: CallbackQuery):
    lang_code = callback_query.data.split("_")[1]
    
    text = {
        "ru": "Язык выбран: Русский ✅",
        "en": "Language selected: English ✅",
        "sr": "Изабран језик: Српски ✅"
    }.get(lang_code, "Язык выбран ✅")
    
    await callback_query.answer(text=text, show_alert=True)
    await callback_query.message.edit_text(
        "Главное меню:",
        reply_markup=main_menu_keyboard
    )
