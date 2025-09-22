'''
Convierte una temperatura de Celsius a Fahrenheit.
'''

def calcular(celcius):
    fahrenheit = (celcius * 9/5) + 32
    print(f"En fahrenheit la temperatura sera de {fahrenheit}º")

def main():
    celcius = float(input("Temperatura en Celcius >> "))
    calcular(celcius)
if __name__ == "__main__":
    main()