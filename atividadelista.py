z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for x in range(1,10):
    print(x)

for x in range (8,14):
    print(x)

for x in z:
    if(x % 2 ==0):
        print("Numeros pares : " + str(x))

for x in z:
    if(x % 2 != 0):
        print("Numeros Impares: " + str(x))

for x in z:
    if(x % 2 == 0):
        print("Numeros Divisiveis por dois: " + str(x))

for x in z:
    if(x % 3 ==0):
        print("Numeros Divisiveis por três: " + str(x))

for x in z:
    if(x % 4 ==0):
        print("Numeros Divisiveis por quatro: " + str(x))

for x in range (15, -1, -1):
    print(x)
