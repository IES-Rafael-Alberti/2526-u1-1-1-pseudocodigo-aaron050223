'''
Pide dos enteros y muestra el cociente y el resto de su división entera.
'''

def pedirEnteros():
    numero1 = int(input("Número 1 >> "))
    numero2 = int(input("Número 2 >> "))
    return numero1, numero2

def dividir(numero1, numero2):
    cociente = numero1 // numero2
    resto = numero1 % numero2
    return cociente, resto

def mostrarResultado(cociente, resto):
    print(f"El cociente es {cociente} y el resto es {resto}")

def main():
    numero1, numero2 = pedirEnteros()
    cociente, resto = dividir(numero1, numero2)
    mostrarResultado(cociente, resto)
if __name__ == "__main__":
    main()