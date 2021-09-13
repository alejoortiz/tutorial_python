# example while loop

print("\nExample While loop \n")

words = ['cat', 'window', 'defenestrate']

a = 0
while a < len(words):
    print(words[a], len(words[a]))
    a += 1


i =0
while True:
    i+=1
    print(i)
    if i==13:
        break


i=0
while i<10:
    i+=1
    if i==7:
        continue
    print(i)
