import requests


link = 'https://api.iot.yandex.net/v1.0/devices/actions'
header = {'Authorization': 'Bearer y0_AgAAAABUuaiYAAorAAAAAADoViVANjWoqQgsRxa4WKDLkrQNdcK7S04'}
data = {
            "devices": [
                {
                    "id": "aac8be68-fc8c-40fd-b820-e4d5b15aabb3",
                    "actions": [
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

resp = requests.post(link, json=data, headers=header)
print(resp)
