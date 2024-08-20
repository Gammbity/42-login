from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

password_recovery = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Password Recovery", callback_data='password_recovery')
    ]
])

contact_markup = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Kontakt yuborish", request_contact=True)
    ]
],resize_keyboard=True, is_persistent=True)