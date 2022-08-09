import textfsm
import os

file_path = os.getcwd()+"/show_ipv4_interface_brief_example"
with open(file_path, 'r') as file:
    file_output = file.read()

template_path = os.getcwd()+"/show_ipv4_interface_brief_template"
with open(template_path, 'r') as template:
    template_object = textfsm.TextFSM(template)

output_parse = template_object.ParseText(file_output)

# print(output_parse[0])

for interface in output_parse:
    if interface[3] == 'Down':
        print(interface)
