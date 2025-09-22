'''
Calcula el precio final sumando al precio sin IVA el porcentaje de IVA indicado.
'''

# Teniendo en cuenta que el IVA en España es del 21%

def quitarIVA(precio):
    precioSinIva = precio - (21 * precio / 100)
    print(f"El precio de {precio} € sin IVA es de {precioSinIva} €")

def main():
    precio = int(input("Precio con IVA >> "))
    quitarIVA(precio)
if __name__ == "__main__":
    main()