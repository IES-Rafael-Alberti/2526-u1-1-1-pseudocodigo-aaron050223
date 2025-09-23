'''
Solicita el nombre del usuario y muestra un saludo personalizado.
'''

def pedirNombre():
    nombre = input("Dime tu nombre >> ")
    return nombre

def saludar(nombre):
    print(f"¡Que pasa {nombre}, tu eres mi colega!")

def main():
    nombrePedido = pedirNombre()
    saludar(nombrePedido)
if __name__ == "__main__":
    main()