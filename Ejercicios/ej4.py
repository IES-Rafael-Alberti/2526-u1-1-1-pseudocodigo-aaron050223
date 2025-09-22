'''
Solicita el nombre del usuario y muestra un saludo personalizado.
'''

def saludo(nombre):
    print(f"¡Que pasa {nombre}, tu eres mi colega!")

def main():
    nombre = input("Dime tu nombre >> ")
    saludo(nombre)
if __name__ == "__main__":
    main()