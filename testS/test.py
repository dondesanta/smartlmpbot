import requests


def test_devices():
    token = 'y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'

    link = 'https://api.iot.yandex.net/v1.0/user/info'
    header = {'Authorization': f'Bearer {token}'}
    responce = requests.get(link, headers=header)
    data = responce.json()

    name = []
    capabilities = []
    for i in data['devices']:
        name.append(i["name"])
        capabilities.append(i['capabilities'])

    brightness = []
    bool_value = []
    for x in capabilities:
        for i in x:
            if i['type'] == 'devices.capabilities.on_off':
                bool_value.append(i['state']['value'])
            elif i['type'] == 'devices.capabilities.range':
                brightness.append(i['state']['value'])

    on_off = []
    for value, bool_check in zip(brightness, bool_value):
        if bool_check:
            if value <= 25:
                on_off.append('🌒')
            elif 25 < value <= 50:
                on_off.append('🌓')
            elif 50 < value <= 75:
                on_off.append('🌔')
            elif 75 < value <= 100:
                on_off.append('🌕')
        else:
            on_off.append('🌑')

    result = []
    num = 0
    for i in range(len(name)):
        num += 1
        print(f'<b>{num}. {name[i]}</b> | {on_off[i]} | <b>{brightness[i]}</b>')
        result.append(f'<b>{num}. {name[i]}</b> | {on_off[i]} | <b>{brightness[i]}</b>')
    result = '\n'.join(result)

    dict_ = {'result_devices': result, 'num_devices': num}

    return dict_
