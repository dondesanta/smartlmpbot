from handlers.users.commands.start.ask_for_calibration import ask_for_calibration
from keyboards.ikb_get_token import ikb_get_token
from data.config import start_text_wrong
from FSMs.fsm_class import ClientStatesGroup

import requests
from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext, filters


@dp.message_handler(filters.Text(startswith='/'), state=ClientStatesGroup.token)
async def token_check_cmd(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        msg_id = data['msg_id']
        await message.delete()
        await bot.edit_message_text(chat_id=message.from_user.id,
                                    message_id=msg_id,
                                    text=start_text_wrong,
                                    reply_markup=ikb_get_token)


@dp.message_handler(state=ClientStatesGroup.token)
async def token_check_valid(message: types.Message, state: FSMContext):
    token = message.text
    link = 'https://api.iot.yandex.net/v1.0/user/info'
    header = {'Authorization': f'Bearer {token}'}
    responce = requests.get(link, headers=header)
    async with state.proxy() as data:
        msg_id = data['msg_id']
        if responce.status_code != 200:
            await message.delete()
            await bot.edit_message_text(chat_id=message.from_user.id,
                                        message_id=msg_id,
                                        text=start_text_wrong,
                                        reply_markup=ikb_get_token)
        else:
            await message.delete()
            data['token'] = message.text
            data['message'] = message
            await ask_for_calibration(message=message, msg_id=msg_id)


@dp.message_handler(content_types=types.ContentType.ANY,  state=ClientStatesGroup.token)
async def token_check_types(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        msg_id = data['msg_id']
        if message.content_type != 'text':
            await message.delete()
            await bot.edit_message_text(chat_id=message.from_user.id,
                                        message_id=msg_id,
                                        text=start_text_wrong,
                                        reply_markup=ikb_get_token)
        else:
            pass
