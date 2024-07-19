import requests
import json


link_data = 'https://api.iot.yandex.net/v1.0/user/info'
link = 'https://api.iot.yandex.net/v1.0/devices/actions'
header = {'Authorization': 'Bearer y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'}
data = {
            "devices": [
                {
                    "id": "b74bdeea-7d00-4906-91d3-bcafe4eabbb1",
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

resp = requests.post(link, json=data, headers=header)
resp_data = requests.get(link_data, headers=header)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(resp_data.json(), f, indent=4, ensure_ascii=False)

print(resp)
