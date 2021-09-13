### como leer archivos en python ###

file_open = open("lorem_ipsum.txt", "r")
file_read = file_open.read()
file_open.close()
print(file_read)

### como escribir archivos en python ###

file_write = open("demo.txt", "w")
file_write.write(file_read)
file_write.close()

### como utilizar el with en archivos usando python ###

with open("demo.txt", 'a', encoding='utf-8') as f:
   f.write("\nlinea 1\n")
   f.write("linea 2\n")
   f.write("linea 3\n")
