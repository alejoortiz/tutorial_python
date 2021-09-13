import os
import json

current_path = os.getcwd()
file_path = current_path+'/example.json'

print(file_path)

### como leer archivos json en python ###

# get json file
with open(file_path) as file_in:
    data_input = json.loads(file_in.read())
    print(data_input)

# ### como escribir archivos json en python ###

data_output = {
    "tipo": "gato",
    "nombre": "tito",
    "edad": "6",
    "peso": "5kg"
}

with open(f"{current_path}/test.json", 'w') as file_out:
    json.dump(data_output, file_out, indent=1)
