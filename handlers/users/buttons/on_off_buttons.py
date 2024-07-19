from FSMs.fsm_class import ClientStatesGroup
from handlers.users.functions.get_menu_devices import get_menu

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import MessageNotModified

from keyboards.ikb_menu import ikb_menu
from loader import dp


@dp.callback_query_handler(Text(startswith='on_off'), state=ClientStatesGroup.menu)
async def on_off(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        token = data['token']
    header = {'Authorization': f'Bearer {token}'}
    lamp_id = callback.data[7:]
    resp = requests.get(f'https://api.iot.yandex.net/v1.0/devices/{lamp_id}', headers=header)
    for i in resp.json()['capabilities']:
        if i['type'] == 'devices.capabilities.on_off':
            if i['state']['value']:
                data = {
                    "devices": [
                        {
                            "id": f"{lamp_id}",
                            "actions": [
                                {
                                    "type": "devices.capabilities.on_off",
                                    "state": {
                                        "instance": "on",
                                        "value": False
                                    }
                                }
                            ]
                        }
                    ]
                }
                resp = requests.post('https://api.iot.yandex.net/v1.0/devices/actions', json=data, headers=header)
            else:
                data = {
                    "devices": [
                        {
                            "id": f"{lamp_id}",
                            "actions": [
                                {
                                    "type": "devices.capabilities.on_off",
                                    "state": {
                                        "instance": "on",
                                        "value": True
                                    }
                                }
                            ]
                        }
                    ]
                }
                resp = requests.post('https://api.iot.yandex.net/v1.0/devices/actions', json=data, headers=header)
            if resp.json()['devices'][0]['capabilities'][0]['state']['action_result']['status'] == 'ERROR':
                if resp.json()['devices'][0]['capabilities'][0]['state']['action_result']['error_message'] == 'device offline':
                    await callback.answer('Устройство выключено!', show_alert=True)
                else:
                    await callback.answer('Произошла какая-то ошибка!', show_alert=True)
            else:
                text = await get_menu(token)
                try:
                    await callback.message.edit_text(text=text['text'],
                                                     reply_markup=ikb_menu(token, text['num']))
                    await callback.answer()
                except MessageNotModified:
                    print('MessageNotModified')
                    await callback.answer('Состояние не изменилось!')
                    pass
