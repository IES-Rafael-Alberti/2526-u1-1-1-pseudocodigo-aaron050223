'''
Área de un triángulo (fórmula de Herón)
Descripción: Calcula el área de un triángulo dados los tres lados a, b y c.
Entrada: a, b, c (números positivos).
Salida: área del triángulo.
'''

# He tenido que mirar la formula en ChatGPT, no tenia ni idea

def pedirLados():
    try:
        bucle = True
        while bucle:
            a = float(input("Introduce el lado A >> "))
            b = float(input("Introduce el lado B >> "))
            c = float(input("Introduce el lado C >> "))
            if a > 0 and b > 0 and c > 0:
                bucle = False
            else:
                print("Los lados deben ser números positivos. Inténtalo de nuevo.")
        return a, b, c
    except ValueError:
        print("Entrada no válida. Por favor, introduce números.")
        return pedirLados()

def calcularSemiperimetro(a, b, c):
    return (a + b + c) / 2

def calcularArea(a, b, c, s):
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def mostrarResultado(area):
    print(f"El área del triángulo es >> {area}")

def main():
    a, b, c = pedirLados()
    semiperimetro = calcularSemiperimetro(a, b, c)
    area = calcularArea(a, b, c, semiperimetro)
    mostrarResultado(area)
if __name__ == "__main__":
    main()