from aiogram.dispatcher.filters.state import StatesGroup, State


class ClientStatesGroup(StatesGroup):
    token = State()
    menu = State()

