'''
Mostrar todos los divisores de un número
Descripción: Pide un número entero y muestra todos sus divisores.
Entrada: número entero.
Salida: lista de divisores.
'''

def pedirNumero():
    try:
        numero = int(input("Introduce un número entero >> "))
        return numero
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
        return pedirNumero()

def encontrarDivisores(numero):
    divisores = 0
    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            divisores += 1
    
    return divisores

def mostrarResultado(numero, divisores):
    print(f"El número {numero} tiene {divisores} divisores")

def main():
    numero = pedirNumero()
    divisores = encontrarDivisores(numero)
    mostrarResultado(numero, divisores)
if __name__ == "__main__":
    main()