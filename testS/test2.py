import requests


def test_groups():
    token = 'y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'
    header = {'Authorization': f'Bearer {token}'}

    responce_groups = requests.get(f'https://api.iot.yandex.net/v1.0/user/info', headers=header)
    data_groups = responce_groups.json()

    name_groups = []
    capabilities_groups = []
    for i in data_groups['groups']:
        name_groups.append(i['name'])
        capabilities_groups.append(i['capabilities'])

    bool_value_groups = []
    brightness_groups = []
    for x in capabilities_groups:
        for i in x:
            if i['type'] == 'devices.capabilities.on_off':
                bool_value_groups.append(i['state']['value'])
            elif i['type'] == 'devices.capabilities.range':
                brightness_groups.append(i['state']['value'])

    on_off = []
    for value_groups, bool_check_groups in zip(brightness_groups, bool_value_groups):
        if bool_check_groups:
            if value_groups <= 25:
                on_off.append('🌒')
            elif 25 < value_groups <= 50:
                on_off.append('🌓')
            elif 50 < value_groups <= 75:
                on_off.append('🌔')
            elif 75 < value_groups <= 100:
                on_off.append('🌕')
        else:
            on_off.append('🌑')

    devices_id = []
    test = []
    for i in data_groups['groups']:
        responce = requests.get(f'https://api.iot.yandex.net/v1.0/groups/{i["id"]}', headers=header)
        data = responce.json()
        test.append(i)
        for x in data['devices']:
            devices_id.append(x['id'])

    test1 = {}
    for i in test:
        test1.update({i['name']: i['id']})
        # print(i['id'])
    # print(test1)

    test2 = {}
    for i in test1.values():
        print(i)
        responce = requests.get(f'https://api.iot.yandex.net/v1.0/groups/{i}', headers=header)
        data = responce.json()
        # print(data['devices'])
        for x in data['devices']:
            test1 = {}

    # name_devices = []
    # for i in devices_id:
    #     responce_devices = requests.get(f'https://api.iot.yandex.net/v1.0/devices/{i}', headers=header)
    #     data_devices = responce_devices.json()
    #     name_devices.append(data_devices['name'])
    #
    # result_groups = []
    # num_groups = 0
    # for i in range(len(name_groups)):
    #     num_groups += 1
    #     result_groups.append(f'<b>{num_groups}. {name_groups[i]}</b> | {on_off[i]} | <b>{brightness_groups[i]}</b>')
    # print(result_groups)
    # # result_groups = '\n'.join(result_groups)
    #
    # result_devices = []
    # num_devices = 0
    # for i in range(len(name_devices)):
    #     num_devices += 1
    #     result_devices.append(f'├ {num_devices}. {name_devices[i]}')
    # print(result_devices)
    # result_devices = '\n'.join(result_devices)
    #
    # text = f'{result_groups}\n' \
    #        f'{result_devices}'
    #
    # text = []
    # num_test = 0
    # print(text)
    # list_ = [result_groups, result_devices]
    # dict_ = {'result_groups': list_, 'num_groups': num_groups}
    #
    # print(dict_['result_groups'])
    # text = []
    # num_test = 1
    # while True:
    #     num_test += 1
    #     print(num_test)
    #     text.append(f'{result_groups[num_test]}\n' + f'{result_devices[num_test]}\n')
    #     if len(name_groups) < num_test:
    #         break
    # print(text)
    # return text


test_groups()
