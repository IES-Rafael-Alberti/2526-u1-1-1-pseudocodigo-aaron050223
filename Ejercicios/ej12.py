'''
Operación aritmética compleja
'''

def operacion():
    resultado = (3 + 5) * 2 - (8 / 4) ** 2 + 7
    return resultado

def mostarResultado(resultado):
    print(f"El resultado de la operación es {resultado}")

def main():
    resultado = operacion()
    mostarResultado(resultado)
if __name__ == "__main__":
    main()