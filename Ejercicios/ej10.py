'''
Suma de tres números usando solo dos variables
'''

def pedirNumero():
    return int(input("Número >> "))

def mostrarResultado(resultado):
    print(f"El resultado es >> {resultado}")

def main():
    numero = pedirNumero() + pedirNumero() + pedirNumero()
    mostrarResultado(numero)
if __name__ == "__main__":
    main()