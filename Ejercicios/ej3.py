'''
Indica si un número entero es primo (solo divisible entre 1 y él mismo).
'''

def pedirNumero():
    numero = int(input("Número >> "))
    return numero

def numeroPrimo(numero):
    contador = 0
    if numero <= 1:
        print("El número no es primo")
    else:
        for i in range(1, numero + 1):
            if numero % i == 0:
                contador += 1
        if contador > 2:
            print("El número no es primo")
        else:
            print("El número es primo")

def main():
    numero = pedirNumero()
    numeroPrimo(numero) 
if __name__ == "__main__":
    main()