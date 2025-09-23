'''
Genera la tabla de multiplicar del número introducido, desde 1 hasta 10.
'''

def tabla(numero):
    for i in range(1, 11):
        reultado = numero * i
        print(f"{numero} x {i} = {reultado}")

def main():
    numero = int(input("Número >> "))
    tabla(numero)
if __name__ == "__main__":
    main()