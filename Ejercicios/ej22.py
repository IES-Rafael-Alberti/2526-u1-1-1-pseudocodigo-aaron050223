'''
Número de teléfono sin prefijo ni extensión
Descripción: Pide un teléfono en formato +34-número-extensión y muestra solo el número central.
Entrada: teléfono en formato indicado (texto).
Salida: número sin prefijo ni extensión.
'''

def pedirTelefono():
    telefono = str(input("Dime tu teléfono en formato +34-número-extensión >> "))
    return telefono

def extraerNumero(telefono):
    partes = telefono.split('-')
    if len(partes) == 3:
        numero = partes[1]
    else:
        numero = "Formato incorrecto"
    return numero

def mostrarResultado(numero):
    print(f"Número sin prefijo ni extensión >> {numero}")

def main():
    telefono = pedirTelefono()
    numero = extraerNumero(telefono)
    mostrarResultado(numero)
if __name__ == "__main__":
    main()