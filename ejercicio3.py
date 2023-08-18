pares = []
impares = []
lista = [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8]
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print("Serie: {0}".format(lista))
print("Pares: {0}".format(pares))
print("Impares: {0}".format(impares))