'''
Calcula el precio de barras con 60% de descuento sobre el precio habitual de 3,49€.
'''

def calcularPrecio():
    precioHabitual = 3.49
    descuento = 60
    precioFinal = precioHabitual - (descuento * precioHabitual / 100)
    return precioFinal

def mostrarResultado(precioFinal):
    print(f"El precio final es >> {precioFinal:.2f} €")

def main():
    precioFinal = calcularPrecio()
    mostrarResultado(precioFinal)
if __name__ == "__main__":
    main()