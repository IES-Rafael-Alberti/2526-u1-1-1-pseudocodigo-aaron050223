'''
Muestra un nombre completo en minúsculas, mayúsculas y con mayúsculas iniciales.
'''

def pedirNombre():
    nombre = str(input("Dime tu nombre >> "))
    return nombre

def pasarAMinusculas(nombre):
    nombreMinusculas = nombre.lower()
    return nombreMinusculas

def pasarAMayusculas(nombre):
    nombreMayusculas = nombre.upper()
    return nombreMayusculas

def pasarAMayusculasIniciales(nombre):
    nombreMayusculasIniciales = nombre.title()
    return nombreMayusculasIniciales

def mostrarInformacion(nombre, nombreMinusculas, nombreMayusculas, nombreMayusculasIniciales):
    print(f"Nombre original >> {nombre}")
    print(f"Nombre en minúsculas >> {nombreMinusculas}")
    print(f"Nombre en mayúsculas >> {nombreMayusculas}")
    print(f"Nombre con mayúscula inicial >> {nombreMayusculasIniciales}")

def main():
    nombre = pedirNombre()
    nombreMinusculas = pasarAMinusculas(nombre)
    nombreMayusculas = pasarAMayusculas(nombre)
    nombreMayusculasIniciales = pasarAMayusculasIniciales(nombre)
    mostrarInformacion(nombre, nombreMinusculas, nombreMayusculas, nombreMayusculasIniciales)
if __name__ == "__main__":
    main()