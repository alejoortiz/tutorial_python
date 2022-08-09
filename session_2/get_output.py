from netmiko import ConnectHandler
from getpass import getpass

my_password = getpass()

cisco1 = {
    "device_type": "cisco_xr",
    "host": "10.192.65.121",
    "username": "htts",
    "password": my_password,
}

with ConnectHandler(**cisco1) as net_connect:
    print(net_connect.find_prompt())
    print(net_connect.send_command('show ip int brief'))


huawei1 = {
    "device_type": "huawei",
    "host": "10.179.0.64",
    "username": "htts",
    "password": my_password,
}

with ConnectHandler(**huawei1) as net_connect:
    print(net_connect.find_prompt())
    print(net_connect.send_command('display interface brief'))

