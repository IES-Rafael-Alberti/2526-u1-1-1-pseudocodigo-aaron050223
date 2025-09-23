'''
Convierte una temperatura de Celsius a Fahrenheit.
'''

def calcular(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def mostrarResultado(fahrenheit):
    print(f"En fahrenheit la temperatura sera de {fahrenheit}º")

def main():
    celcius = float(input("Temperatura en Celcius >> "))
    fahrenheit = calcular(celcius)
    mostrarResultado(fahrenheit)
if __name__ == "__main__":
    main()