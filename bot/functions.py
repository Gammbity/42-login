from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from . import states
from . import keyboards
import random
import psycopg2
from datetime import datetime
from django.utils.timezone import now
import html
import markdown

db_name = "42"
db_user = "postgres"
db_password = "Qwerty123$"
db_host = "localhost"
db_port = "5432"

try:
    # PostgreSQL-ga ulanish
    connection= psycopg2.connect(
        database=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )

    cursor = connection.cursor()
    print("PostgreSQL-ga muvaffaqiyatli ulandik")

except (Exception, psycopg2.Error) as error:
    print("PostgreSQL-ga ulanishda xatolik:", error)

async def start_command(message:Message, state:FSMContext):
    user_id = message.from_user.id
    cursor.execute("SELECT * FROM user_user WHERE telegram_id = %s", (user_id,))
    user = cursor.fetchone()
    if user:
        return await send_password(message)
    await message.answer("Kantaktingizni pastdagi tugma orqali kiriting ⬇️", reply_markup=keyboards.contact_markup)
    await state.set_state(states.NewMember.phone)


async def get_contact(message:Message, state:FSMContext):
    cursor.execute("INSERT INTO user_user(password, last_login, telegram_id, full_name, username, phone, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (123, datetime.now(), message.from_user.id, f"{message.from_user.last_name} {message.from_user.first_name}", message.from_user.username, message.contact.phone_number, datetime.now(), datetime.now()))
    connection.commit()
    await state.set_state(states.NewMember.login)


async def send_password(message:Message):
    raqam = random.randint(100000, 999999)
    time = datetime.now()
    cursor.execute("SELECT id FROM user_user WHERE telegram_id=%s", (message.from_user.id,))
    user_id = cursor.fetchall()
    cursor.execute("INSERT INTO user_generatepassword(password, time, user_id) VALUES (%s, %s, %s)", (raqam, time, user_id[0][0]))
    connection.commit()
    await message.answer(str(raqam), reply_markup=keyboards.password_recovery)


async def recovery_password(callback_data:CallbackQuery, state:FSMContext):
    cursor.execute("SELECT id FROM user_user WHERE telegram_id=%s", (callback_data.from_user.id,))
    user_id = cursor.fetchall()
    cursor.execute("SELECT time FROM user_generatepassword WHERE user_id=%s ORDER BY time DESC", (user_id[0][0],))
    time = cursor.fetchone()
    if (now() - time[0]).total_seconds() < 60:
        return await callback_data.answer("Parolingiz hali kuchda! ☝️")
    await callback_data.message.delete()
    raqam = random.randint(100000, 999999)
    time = datetime.now()
    cursor.execute("SELECT * FROM user_user WHERE telegram_id=%s", (callback_data.from_user.id,))
    user = cursor.fetchall()
    user_id = user[0][0]
    cursor.execute("INSERT INTO user_generatepassword(password, time, user_id) VALUES (%s, %s, %s)", (raqam, time, user_id))
    connection.commit()
    await callback_data.message.answer(str(raqam), reply_markup=keyboards.password_recovery)
