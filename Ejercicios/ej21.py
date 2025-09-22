'''
Contar letras del nombre
Descripción: Convierte el nombre a mayúsculas y muestra cuántas letras tiene.
Entrada: nombre (texto).
Salida: nombre en mayúsculas y número de letras.
'''

def pedirNombre():
    nombre = str(input("Dime tu nombre >> "))
    return nombre

def convertirAMayusculas(nombre):
    nombreMayusculas = nombre.upper()
    return nombreMayusculas

def contarLetras(nombre):
    numeroLetras = len(nombre)
    return numeroLetras

def mostrarResultado(nombreMayusculas, numeroLetras):
    print(f"Nombre en mayúsculas >> {nombreMayusculas}")
    print(f"Número de letras >> {numeroLetras}")

def main():
    nombre = pedirNombre()
    nombreMayusculas = convertirAMayusculas(nombre)
    numeroLetras = contarLetras(nombre)
    mostrarResultado(nombreMayusculas, numeroLetras)
if __name__ == "__main__":
    main()