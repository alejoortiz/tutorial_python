from netmiko import ConnectHandler
import os

my_username = os.environ['CISCO_USERNAME']
my_password =  os.environ['CISCO_PASSWORD']

cisco = {
    "device_type": "cisco_xr",
    "host": "172.18.104.43",
    "username": my_username,
    "password": my_password,
}

with ConnectHandler(**cisco) as net_connect:
    output = net_connect.send_command(
        'show arp', use_textfsm=True)

for search in output:
    if "TenGigE" in search['interface'] and 'Dynamic' in search['state']:
        print(search)
