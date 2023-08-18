from multiprocessing.sharedctypes import Value


continuar = True
totalVenta = 0
cantidadVenta = 0

def inputNumber(mensaje, isFloat = False):
    while True:
        try:
            if isFloat:
                return float(input(mensaje))
            return int(input(mensaje))
        except ValueError:
            print("¡¡Ingrese una cantidad válida!!")

while continuar == True:
    cantidad = inputNumber("Ingresa la cantidad de productos: ")
    precio = inputNumber("Ingresa el precio por unidad: ", True)

    totalSinDescuento = cantidad * precio


    if cantidad >= 5 and cantidad <= 10:
        totalVenta += totalSinDescuento - (cantidad * precio * 0.05)
    elif cantidad >= 11 and cantidad <= 20:
        totalVenta += totalSinDescuento - (cantidad * precio * 0.10)
    elif cantidad > 20:
        totalVenta += totalSinDescuento - (cantidad * precio * 0.15)
    else:
        totalVenta += (cantidad * precio)
    
    cantidadVenta += cantidad

    opcion = input("Continuar? S/N ")
    if opcion.upper() == 'N':
        continuar = False
        print("¡Gracias por comprar!")
    
print("Total de la Venta: ${0}".format(totalVenta))
print("Unidades Totales: {0}".format(cantidadVenta))