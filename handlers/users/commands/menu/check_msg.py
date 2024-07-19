from FSMs.fsm_class import ClientStatesGroup

from aiogram import types
from loader import dp


@dp.message_handler(state=ClientStatesGroup.menu)
async def check(message: types.Message):
    await message.delete()
