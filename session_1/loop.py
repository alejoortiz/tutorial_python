### Examples For and While ###

print("Example For loop \n")

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

### recorriendo un diccionario ###

routers = {
    'asr920': 1000,
    'asr9000': 50, 
    'crs': 5
}
sum_routers = 0
for key, values in routers.items():
    sum_routers+= values
    print(key, values)
    print("suma", sum_routers)
