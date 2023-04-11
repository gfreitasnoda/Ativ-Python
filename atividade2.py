a = ""
b = None
c = ""
z = None


a = input("Digite um valor: ")
b = input("Digite outro valor: ")
c = input("Digite um numero real: ")

p = int(a) * 2
print("O dobro do primeiro: " + str(p))

p = int(b) / 2
print("A metade do segundo: "+ str(p))

p = int(a) * 2 + int(b) / 2
print("A soma do dobro do primeiro com a metade do segundo: " + str(p))

p = int(a) * 3 + int(c)
print("A soma do triplo do primeiro com o terceiro: " + str(p))

print("O terceiro elevado ao cubo: "+ str(pow(int(c),3)))
