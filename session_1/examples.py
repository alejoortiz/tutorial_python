### example age ### 

age = int(input("¿Cuál es tu edad? "))
if age < 18: 
	print ("Eres menor de edad.")
else:
	print("Eres mayor de edad.")


### Examples functions ###

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        array = []
        n1 = 0
        n2 = 1
        count = 0
        while count < n:
            array.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
        return array


print(fibonacci(10))


### numeros primos ###

num = 1
while num <= 30:
    check = True
    i = 2
    while i <= num//2:
        if num % i == 0:
            check = False
            break
        i = i + 1
    if check == True and num != 1:
        print(num)
    num = num + 1

### bubble sort ###

array = [69,  7, 12, 11, 83]

n = len(array)
for i in range(n):
    sorted = True
    for j in range(n - i - 1):
        print("i="+str(i)+" "+"j="+str(j),array)
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            sorted = False
    if sorted:
        break
