'''
Calcula el saldo tras 1, 2 y 3 años aplicando un 4% de interés compuesto anual.
'''

def pedirSueldo():
    sueldo = float(input("Sueldo inicial >> "))
    return sueldo

def calcularInteres(sueldo, anios):
    for anios in range(anios):
        sueldo = sueldo + (sueldo * 4 / 100)
        print(f"Tras {anios + 1} año(s) >> Tu saldo es de {sueldo:.2f} €")
    return sueldo

def main():
    sueldo = pedirSueldo()
    calcularInteres(sueldo, 3)
if __name__ == "__main__":
    main()