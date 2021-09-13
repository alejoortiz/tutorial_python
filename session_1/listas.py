### variable type list ###

list_1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
list_2 = ['h', 'e', 'l', 'l', '0']


print(type(list_1))
print(list_1)
print(list_2)
print(list_1[5:9])

### list operations ###

print(list_1)
list_1.append(10)
print(list_1)
list_1.pop(0)
print(list_1)
list_1.remove(5)
print(list_1)
list_1.sort()
print(list_1)


### list Comprehension ###

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in fruits if "a" in x]

print(newlist)
