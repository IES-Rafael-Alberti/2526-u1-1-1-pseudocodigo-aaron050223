'''
Número aleatorio entre dos valores
Descripción: Genera un número aleatorio entre un valor mínimo y máximo (incluidos o según se defina).
Entrada: min (número), max (número).
Salida: número aleatorio generado.
'''

import random
def pedirValores():
    try:
        bucle = True
        while bucle:
            numeroMinimo = int(input("Introduce el valor mínimo >> "))
            numeroMaximo = int(input("Introduce el valor máximo >> "))
            if numeroMinimo > numeroMaximo:
                print("El valor mínimo debe ser menor que el valor máximo. Inténtalo de nuevo.")
            else:
                bucle = False
        return numeroMinimo, numeroMaximo
    except ValueError:
        print("Entrada no válida. Por favor, introduce números enteros.")
        return pedirValores()
    
def generarNumeroAleatorio(min_val, max_val):
    return random.randint(min_val, max_val)

def mostrarResultado(numero):
    print(f"Número aleatorio generado >> {numero}")

def main():
    numeroMinimo, numeroMaximo = pedirValores()
    numero_aleatorio = generarNumeroAleatorio(numeroMinimo, numeroMaximo)
    mostrarResultado(numero_aleatorio)
if __name__ == "__main__":
    main()