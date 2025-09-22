'''
Dado el precio final (con IVA), calcula el precio sin IVA y el IVA pagado (asume 10%).
'''

def quitarIVA(precio):
    precioSinIva = precio - (10 * precio / 100)
    return precioSinIva

def mostrarResultado(precio, precioSinIva):
    print(f"El precio de {precio} € sin IVA es de {precioSinIva} €")

def main():
    precio = float(input("Precio con IVA >> "))
    precioSinIva= quitarIVA(precio)
    mostrarResultado(precio, precioSinIva)
if __name__ == "__main__":
    main()