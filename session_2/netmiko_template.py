from netmiko import ConnectHandler
import os

my_password = os.environ['SSH_PASSWORD']

cisco = {
    "device_type": "cisco_xr",
    "host": "10.192.65.121",
    "username": "htts",
    "password": my_password,
}

with ConnectHandler(**cisco) as net_connect:
    output = net_connect.send_command(
        'show arp', use_textfsm=True)

for search in output:
    if "Hundred" in search['interface'] and 'Dynamic' in search['state']:
        print(search)
