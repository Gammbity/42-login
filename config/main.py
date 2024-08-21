from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import BotCommand
from asyncio import run
from functions import send_password, get_contact, start_command, recovery_password
import states

dp = Dispatcher()

async def startup_answer(bot:Bot):
    await bot.send_message(6089066974, 'Bot ishga tushdi')

async def shutdown_answer(bot:Bot):
    await bot.send_message(6089066974, 'Bot ishdan to\'xtadi')

async def start():
    # dp.startup.register(startup_answer)
    # dp.shutdown.register(shutdown_answer)


    dp.message.register(start_command, CommandStart())
    dp.message.register(send_password, states.NewMember.login)
    dp.message.register(get_contact, states.NewMember.phone)
    dp.callback_query.register(recovery_password, F.data == 'password_recovery')
    
    dp.message.register(send_password, Command('login'))


    bot = Bot('7528133763:AAGc4JIHlBBK2JfdelzK9FazU5IYuzkP-F0')
    
    await bot.set_my_commands([
        BotCommand(command='/login', description='Kirish uchun kod')
    ])

    await dp.start_polling(bot)

run(start())