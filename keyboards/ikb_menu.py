from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import json


def ikb_menu(token, row_width):
    link = 'https://api.iot.yandex.net/v1.0/user/info'
    header = {'Authorization': f'Bearer {token}'}
    resp = requests.get(link, headers=header)
    data = json.loads(resp.text)

    ikb = InlineKeyboardMarkup(row_width=row_width)
    num = 0
    for x in data['devices']:
        num += 1
        id_lamps = str(x['id'])
        ikb.insert(InlineKeyboardButton(str(num), callback_data=f'on_off_{id_lamps}'))

    for i in data['devices']:
        id_lamps = str(i['id'])
        ikb.insert(InlineKeyboardButton('⚙', callback_data=f'settings_{id_lamps}'))
    ikb.add(InlineKeyboardButton('Перезагрузить', callback_data='reload_button'))
    ikb.add(InlineKeyboardButton('Калибровка', callback_data='calibration_button'))
    return ikb

