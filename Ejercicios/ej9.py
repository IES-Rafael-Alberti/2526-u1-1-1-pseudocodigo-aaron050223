'''
Solicita tres números y muestra su suma.
'''

def suma(numero1,numero2,numero3):
    resultado = numero1 + numero2 + numero3
    print(f"La suma de {numero1}, {numero2} y {numero3} es {resultado}")

def main():
    numero1 = int(input("Número 1 >> "))
    numero2 = int(input("Número 2 >> "))
    numero3 = int(input("Número 3 >> "))
    suma(numero1,numero2,numero3)
if __name__ == "__main__":
    main()