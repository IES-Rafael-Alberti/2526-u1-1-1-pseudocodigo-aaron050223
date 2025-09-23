'''
Calcula el precio final sumando al precio sin IVA el porcentaje de IVA indicado.
'''

# Teniendo en cuenta que el IVA en España es del 21%

def quitarIVA(precio):
    precioSinIva = precio - (21 * precio / 100)
    return precioSinIva

def mostrarResultado(precio, precioSinIva):
    print(f"El precio de {precio} € sin IVA es de {precioSinIva} €")

def main():
    precio = float(input("Precio con IVA >> "))
    precioSinIva= quitarIVA(precio)
    mostrarResultado(precio, precioSinIva)
if __name__ == "__main__":
    main()