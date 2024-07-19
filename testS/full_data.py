import requests
import json


header = {'Authorization': 'Bearer y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'}

link = 'https://api.iot.yandex.net/v1.0/user/info'
resp = requests.get(link, headers=header)


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(resp.json(), f, indent=4, ensure_ascii=False)
