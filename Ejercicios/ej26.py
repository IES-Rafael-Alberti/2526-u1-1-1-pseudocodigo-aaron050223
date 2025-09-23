'''
Separar euros y céntimos de un precio
Descripción: Separa la parte entera y los céntimos de un precio en euros con dos decimales.
Entrada: precio (número con dos decimales).
Salida: euros (entero), céntimos (entero 0–99).
'''

def pedirPrecio():
    precio = float(input("Introduce un precio en euros (Formato >> 1.80) >> "))
    return precio

def separarPrecio(precio):
    euro = int(precio) # Para quitar los decimales
    centimos = precio - euro
    return euro, centimos

def mostrarResultado(euro, centimos):
    print(f"Euros >> {euro}")
    print(f"Céntimos >> {int(centimos * 100)}")

def main():
    precio = pedirPrecio()
    euro, centimos = separarPrecio(precio)
    mostrarResultado(euro, centimos)
if __name__ == "__main__":
    main()