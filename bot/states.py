from aiogram.fsm.state import State, StatesGroup

class NewMember(StatesGroup):
    login = State()
    phone = State()