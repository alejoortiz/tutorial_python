### variable type tuple ###

tuple_1 = (1, 10, 9, 8, 3)
tuple_2 = ("manzanas", "peras", "bananos", "fresas")
tuple_3 = (True, False, False)

# Get value
print(tuple_2[1])

# Error change value 
# tuple_2[0] = 10

# erase a tuple
# delete tuple_1

print(type(tuple_1))
print(tuple_1)
print(len(tuple_2))

tuple_4 = tuple_1+tuple_2
print(tuple_4)

print(tuple_4*2)


### SET ####
frutas = {"manzanas", "peras", "bananos", "fresas"}

# check if in set
print("manzanas" in frutas)

# add to set
frutas.add('naranjas')
print(frutas)
frutas.add('naranjas')
print(frutas)

# remove from set
frutas.remove("peras")
print(frutas)

# clear set
frutas.clear()
print(frutas)

# delete
del frutas
# print(frutas)
