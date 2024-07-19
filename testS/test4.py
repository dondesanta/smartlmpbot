import requests

link_info = 'https://api.iot.yandex.net/v1.0/user/info'
header_info = {'Authorization': f'Bearer y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'}
responce_info = requests.get(link_info, headers=header_info)
data_info = responce_info.json()

text = []
for i in data_info['devices']:
    print(i['id'])
    data = {
        "devices": [
            {
                "id": f"{i['id']}",
                "actions": [
                    {
                        "type": "devices.capabilities.on_off",
                        "state": {
                            "instance": "on",
                            "value": True
                        }
                    },
                    {
                        "type": "devices.capabilities.range",
                        "state": {
                            "instance": "brightness",
                            "value": 100
                        }
                    }
                ]
            }
        ]
    }

    off = {
        "devices": [
            {
                "id": f"{i['id']}",
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

    link = 'https://api.iot.yandex.net/v1.0/devices/actions'
    link_info = f'https://api.iot.yandex.net/v1.0/devices/{i["id"]}'
    header = {'Authorization': f'Bearer y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'}
    resp = requests.post(link, json=data, headers=header)
    resp_off = requests.post(link, json=off, headers=header)
    resp_info = requests.get(link_info, headers=header)
    if resp.json()['devices'][0]['capabilities'][0]['state']['action_result']['status'] == 'ERROR':
        text.append(f"{resp_info.json()['name']} | Устройство выключено")
    else:
        text.append(f"{resp_info.json()['name']} | DONE")
    print(f'{resp} | resp')
    print(f'{resp_off} | OFF')

text = '\n'.join(text)
print(text)
