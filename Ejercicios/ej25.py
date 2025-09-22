'''
Cambiar el dominio de un correo
Descripción: Cambia el dominio de un correo dado por @ceu.es.
Entrada: correo electrónico (texto).
Salida: nuevo correo con dominio @ceu.es.
'''

def pedirCorreo():
    correo = str(input("Introduce tu correo electrónico >> "))
    return correo

def comprobarCorreo(correo):
    contadorArrobas = correo.count("@")
    if "@" in correo and contadorArrobas == 1:
        return True
    else:
        return False
    
def cambiarDominio(correo):
    usuario = correo.split("@")[0]
    nuevoCorreo = usuario + "@ceu.es"
    return nuevoCorreo

def main():
    correo = pedirCorreo()
    if comprobarCorreo(correo):
        nuevoCorreo = cambiarDominio(correo)
        print(f"Tu nuevo correo es >> {nuevoCorreo}")
    else:
        print("El correo introducido no es válido.")
if __name__ == "__main__":
    main()

