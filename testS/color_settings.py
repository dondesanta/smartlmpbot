import requests


link = 'https://api.iot.yandex.net/v1.0/devices/actions'
header = {'Authorization': 'Bearer y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'}
data = {
            "devices": [
                {
                    "id": "2a6779e5-da84-43e6-a4dd-7450865e805e",
                    "actions": [
                        {
                            "type": "devices.capabilities.color_setting",
                            "state": {
                                "instance": "hsv",
                                "value": {
                                    "h": 244,
                                    "s": 100,
                                    "v": 100
                                }
                            }
                        }
                    ]
                }
            ]
        }

resp = requests.post(link, json=data, headers=header)
print(resp)
