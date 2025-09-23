def calcularImc(peso, altura):
    imc = peso / (altura * altura)
    return imc

def mostrarInfo(imc):
    print(f'Tu índice de masa corporal (IMC) es: {imc:.2f}') # 2 Decimales

def main():
    peso = float(input("Introduce tu peso en kilogramos (Ejemplo >> 90) >> "))
    altura = float(input("Introduce tu altura en metros (Ejemplo >> 1.90) >> "))
    imc = calcularImc(peso, altura)
    mostrarInfo(imc)
if __name__ == '__main__':
    main()