contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0
cadena = input("Ingresa una cadena: ")
for i in cadena:
    if i.lower() == 'a':
        contadorA += 1
    elif i.lower() == 'e':
        contadorE += 1
    elif i.lower() == 'i':
        contadorI += 1
    elif i.lower() == 'o':
        contadorO += 1
    elif i.lower() == 'u':
        contadorU += 1

print("A: {0}".format(contadorA))
print("E: {0}".format(contadorE))
print("I: {0}".format(contadorI))
print("O: {0}".format(contadorO))
print("U: {0}".format(contadorU))