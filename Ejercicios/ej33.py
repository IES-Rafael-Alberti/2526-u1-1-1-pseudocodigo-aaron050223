'''
Serie de Fibonacci hasta n términos
Descripción: Genera y muestra los primeros n términos de la serie de Fibonacci (empezando en 0 y 1).
Entrada: n (entero ≥ 1).
Salida: términos de la serie hasta n.
'''

def pedirNumero():
    try:
        bucle = True
        while bucle:
            numero =  int(input("Introduce el número >> "))
            if numero > 0:
                bucle = False
            else:
                print("El número debe ser positivo")
        return numero
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número entero.")
        return pedirNumero()
    
def serieFibonacci(numero):
    fibonacci = 1
    fibonacci2 = 0
    resultadoFibonacci = 0

    for ordenFibonacci in range(1, numero + 1):
        if ordenFibonacci == 1:
            resultadoFibonacci = 0 
        elif ordenFibonacci == 2:
            resultadoFibonacci = 1 
        else:
            resultadoFibonacci = fibonacci + fibonacci2
            fibonacci2 = fibonacci
            fibonacci = resultadoFibonacci

    return resultadoFibonacci

def mostrarResultado(numero, resultadoFibonacci):
    print(f"El resultado de la serie Fibonacci hasta el número {numero} es >> {resultadoFibonacci}")

def main():
    numero = pedirNumero()
    resultadoFibonacci = serieFibonacci(numero)
    mostrarResultado(numero, resultadoFibonacci)
if __name__ == "__main__":
    main()