'''
Programa que pide un número entero y determina si es par (divisible entre 2) o impar.
'''

def paroimpar(numero):
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"
    
def main():
    numero = int(input("Número >> "))
    resultado = paroimpar(numero)
    print(resultado)
if __name__ == "__main__":
    main()