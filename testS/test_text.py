from testS.test import test_devices
from testS.test2 import test_groups

dict_devices = test_devices()
dict_groups = test_groups()

text = f'<b>Устройства:</b>\n' \
       f'{dict_devices["result_devices"]}\n' \
       f'\n' \
       f'<b>Группы:</b>\n' \
       f'{dict_groups}'

print(text)
