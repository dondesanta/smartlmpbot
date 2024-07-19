import json

import requests


token = 'y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'
link = 'https://api.iot.yandex.net/v1.0/user/info'
header = {'Authorization': f'Bearer {token}'}
resp = requests.get(link, headers=header)
data = json.loads(resp.text)

num = 0
for i in data['groups']:
    num += 1
    id_groups = i['id']
    ikb.insert(InlineKeyboardButton(str(num), callback_data=f'on_off_groups{id_groups}'))
#
# print(groups_id)`
# ikb = InlineKeyboardMarkup(row_width=row_width)
num = 0
for i in data['devices']:
    num += 1
    id_lamps = i['id']
    print(id_lamps)
    # ikb.insert(InlineKeyboardButton(str(num), callback_data=f'on_off_{id_lamps}'))

# for i in data['devices']:
#     id_lamps = str(i['id'])
#     ikb.insert(InlineKeyboardButton('⚙', callback_data=f'settings_{id_lamps}'))
# ikb.add(InlineKeyboardButton('Перезагрузить', callback_data='reload_button'))
# ikb.add(InlineKeyboardButton('Калибровка', callback_data='calibration_button'))