from netmiko import ConnectHandler
import os

my_username = os.environ['CISCO_USERNAME']
my_password =  os.environ['CISCO_PASSWORD']

my_network = [
    {
        "device_type": "cisco_xr",
        "host": "172.18.104.43",
        "username": my_username,
        "password": my_password,
    },
    {
        "device_type": "cisco_xr",
        "host": "172.18.104.58",
        "username": my_username,
        "password": my_password,
    }
]

def write_output_file(name,output):
    with open(f"{name}.txt", 'w', encoding='utf-8') as f:
        f.write(output)

for device in my_network:
    with ConnectHandler(**device) as net_connect:
        net_connect.find_prompt()
        output = net_connect.send_command('show ipv4 int brief')
        write_output_file(device["host"], output)
