'''
Suma de tres números sin variables adicionales
'''

def pedirNumero():
    return int(input("Número >> "))

def mostrarResultado(resultado):
    print(f"El resultado es >> {resultado}")

def main():
    return mostrarResultado(pedirNumero() + pedirNumero() + pedirNumero())
if __name__ == "__main__":
    main()