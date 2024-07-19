import json

import requests

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def ikb_menu_groups(token, row_width):
    link = 'https://api.iot.yandex.net/v1.0/user/info'
    header = {'Authorization': f'Bearer {token}'}
    resp = requests.get(link, headers=header)
    data = json.loads(resp.text)

    ikb = InlineKeyboardMarkup(row_width=row_width)
    num = 0
    for i in data['groups']:
        num += 1
        id_groups = i['id']
        ikb.insert(InlineKeyboardButton(str(num), callback_data=f'on_off_groups{id_groups}'))

    for i in data['groups']:
        id_groups = i['id']
        ikb.insert(InlineKeyboardButton('⚙', callback_data=f'settings_groups_{id_groups}'))
    ikb.add(InlineKeyboardButton('Перезагрузить', callback_data='reload_button_groups'))
    ikb.add(InlineKeyboardButton('Калибровка', callback_data='calibration_button_groups'))
    return ikb
