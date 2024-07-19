import requests


async def check_on_off(token):
    header = {'Authorization': f'Bearer {token}'}
    resp = requests.get('https://api.iot.yandex.net/v1.0/user/info', headers=header)
    data = resp.json()
    IDs = []
    for i in data['devices']:
        IDs.append(i['id'])

    data_check = []
    for i in IDs:
        resp_check = requests.get(f'https://api.iot.yandex.net/v1.0/devices/{i}', headers=header)
        data_check.append(resp_check.json()['capabilities'])

    booltype = []
    for i in data_check:
        for x in i:
            if x['type'] == 'devices.capabilities.on_off':
                booltype.append(x['state']['value'])

    flag = {}
    for x, y in zip(IDs, booltype):
        flag[f'{x}'] = y
    return flag
