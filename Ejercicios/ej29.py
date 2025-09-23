'''
Producto, precio y unidades formateado
Descripción: Pide nombre del producto, precio unitario y unidades; muestra también el coste total con formato tabulado/alineado.
Entrada: nombre (texto), precio (número), unidades (entero).
Salida: producto, precio unitario, unidades y coste total formateados.
'''

def pedirNombre():
    return input(str("Introduce el nombre del producto >> "))

def pedirPrecio():
    try:
        blucle = True
        while blucle:
            precio = float(input("Introduce el precio del producto por unidad >> "))
            if precio < 0:
                print("El precio no puede ser negativo. Intentalo de nuevo.")
            else:
                blucle = False
        return precio
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")
        return pedirPrecio()

def pedirUnidades():
    try:
        blucle = True
        while blucle:
            unidades = int(input("Introduce las unidades del producto >> "))
            if unidades < 0:
                print("Las unidades no pueden ser negativas. Inténtalo de nuevo.")
            else:
                blucle = False
        return unidades
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
        return pedirUnidades()

def calcularCoste(precio, unidades):
    return precio * unidades

def mostrarResultado(nombre, precio, unidades, costeTotal):
    print(f"El producto {nombre} tiene un precio de {precio:.2f}€ por unidad.")
    print(f"Comprando {unidades} unidades, el precio total >> {costeTotal:.2f}€")

def main():
    nombre = pedirNombre()
    precio = pedirPrecio()
    unidades = pedirUnidades()
    costeTotal = calcularCoste(precio, unidades)
    mostrarResultado(nombre, precio, unidades, costeTotal)
if __name__ == "__main__":
    main()