import json

from handlers.users.functions.check_on_off import check_on_off
from handlers.users.functions.get_menu_devices import get_menu

from aiogram import types
from loader import bot
from aiogram.dispatcher import FSMContext
from FSMs.fsm_class import ClientStatesGroup
from keyboards.ikb_menu import ikb_menu


async def menu(message: types.Message, state: FSMContext, token):
    async with state.proxy() as data:
        msg_id = data['msg_id']
        msg1_id = data['msg1_id']
        dict_ = await get_menu(token)
        await bot.edit_message_text(chat_id=message.from_user.id,
                                    message_id=msg1_id,
                                    text='<b>Состояние:</b>')
        await bot.edit_message_text(chat_id=message.from_user.id,
                                    message_id=msg_id,
                                    text=dict_['text'],
                                    reply_markup=ikb_menu(token, dict_['num']))
    await ClientStatesGroup.next()
    with open('handlers/users/commands/menu/flag.json', 'w') as f:
        flag = await check_on_off(token)
        json.dump(flag, f)
