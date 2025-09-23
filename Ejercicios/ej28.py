'''
Mostrar productos de la cesta
Descripción: Pide productos separados por comas y los muestra en líneas separadas.
Entrada: cadena con productos separados por comas.
Salida: un producto por línea.
'''

def pedirProductos():
    productos = str(input("Introduce los productos de la cesta separados por comas >> "))
    return productos

def separarProductos(productos):
    listaProductos = productos.split(",")
    return listaProductos

def mostrarProductos(listaProductos):
    print("Productos en la cesta:")
    for producto in listaProductos:
        print(producto)

def main():
    productos = pedirProductos()
    listaProductos = separarProductos(productos)
    mostrarProductos(listaProductos)
if __name__ == "__main__":
    main()