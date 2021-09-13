from netmiko import ConnectHandler
import os

my_password = os.environ['SSH_PASSWORD']
my_network = [
    {
        "device_type": "cisco_xr",
        "host": "10.192.65.121",
        "username": "htts",
        "password": my_password,
    },
    {
        "device_type": "cisco_xr",
        "host": "10.192.65.122",
        "username": "htts",
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
