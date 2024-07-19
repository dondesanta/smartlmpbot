import requests
import json


link_data = 'https://api.iot.yandex.net/v1.0/user/info'
link = 'https://api.iot.yandex.net/v1.0/devices/actions'
header = {'Authorization': 'Bearer y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'}
data = {
            "devices": [
                {
                    "id": "329dcb5d-1ff7-4037-a790-9079321c7780",
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

resp = requests.post(link, json=data, headers=header)
resp_data = requests.get(link_data, headers=header)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(resp_data.json(), f, indent=4, ensure_ascii=False)

print(resp)
print(resp.text)
