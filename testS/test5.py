import requests

link_info = f'https://api.iot.yandex.net/v1.0/devices/329dcb5d-1ff7-4037-a790-9079321c7780'
header = {'Authorization': f'Bearer y0_AgAAAAA67E_nAAorAAAAAADniPKpcyX8SrKRTnevADhz37a8Puopre4'}
resp_info = requests.get(link_info, headers=header)

print(resp_info.json()['name'])
