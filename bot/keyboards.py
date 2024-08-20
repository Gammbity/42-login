from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_markup = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Kontakt yuborish", request_contact=True)
    ]
],resize_keyboard=True, is_persistent=True)