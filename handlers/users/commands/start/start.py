from FSMs.fsm_class import ClientStatesGroup
from keyboards.ikb_get_token import ikb_get_token
from data.config import start_text

from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import bot, dp


@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message, state: FSMContext):
    await ClientStatesGroup.token.set()
    await message.delete()
    msg1 = await bot.send_message(chat_id=message.from_user.id,
                                  text='<b>Приветствую!</b>')
    msg = await bot.send_message(chat_id=message.from_user.id,
                                 text=start_text,
                                 reply_markup=ikb_get_token)
    async with state.proxy() as data:
        data['msg_id'] = msg.message_id
        data['msg1_id'] = msg1.message_id
