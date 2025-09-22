'''
Imprime el nombre del usuario tantas veces como indique un entero n.
'''

def pedirDatos():
    nombre = str(input("Dime tu nombre >> "))
    numero = int(input("Dime un número entero >> "))
    return nombre, numero

def imprimirNombre(nombre, numero):
    for i in range(numero):
        print(f"{i + 1} >> {nombre}")

def main():
    nombre, numero = pedirDatos()
    imprimirNombre(nombre, numero)
if __name__ == "__main__":
    main()