from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import BotCommand
from asyncio import run
from . import functions
from . import states
import asyncio


dp = Dispatcher()

async def start():

    dp.message.register(functions.start_command, CommandStart())
    dp.message.register(functions.send_password, states.NewMember.login)
    dp.message.register(functions.get_contact, states.NewMember.phone)

    dp.callback_query.register(functions.recovery_password, F.data == 'password_recovery')
    
    dp.message.register(functions.recovery_password, Command('login'))

    bot = Bot('7528133763:AAGc4JIHlBBK2JfdelzK9FazU5IYuzkP-F0')
    
    await bot.set_my_commands([
        BotCommand(command='/login', description='Kirish uchun kod')
    ])

    await dp.start_polling(bot)

run(start())