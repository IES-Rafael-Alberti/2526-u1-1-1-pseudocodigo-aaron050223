'''
Calcula la suma de los n primeros enteros positivos usando la fórmula n(n+1)/2.
'''

# Este ejercicio no lo entendia, pero consultandolo con IA me ha dado esta formula

def suma(numero):
    resultado = (numero * (numero + 1)) // 2
    print(f'La suma de los {numero} primeros enteros positivos es: {resultado}')

def main():
    n = int(input('Introduce un número entero positivo: '))
    if n < 1:
        print('Por favor, introduce un número entero positivo mayor que 0.')
    else:
        suma(n)
if __name__ == '__main__':
    main()