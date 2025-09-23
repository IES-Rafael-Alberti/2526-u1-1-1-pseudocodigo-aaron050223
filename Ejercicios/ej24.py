'''
Reemplazar una vocal en una frase
Descripción: Pide una frase y una vocal, y sustituye todas sus apariciones por esa vocal en mayúscula.
Entrada: frase (texto), vocal (carácter).
Salida: frase modificada.
'''

def pedirFrase():
    frase = str(input("Dime una frase >> "))
    return frase

def pedirVocal():
    vocal = str(input("Dime una vocal >> "))
    return vocal

def reemplazarVocal(frase, vocal):
    if vocal.lower() in 'aeiou':
        fraseModificada = frase.replace(vocal.lower(), vocal.upper()) # En el replace primero se pone la que quiero cambiar y luego la que quiero poner
    else:
        fraseModificada = "No es una vocal válida"
    return fraseModificada

def mostrarResultado(fraseModificada):
    print(f"Frase modificada >> {fraseModificada}")

def main():
    frase = pedirFrase()
    vocal = pedirVocal()
    fraseModificada = reemplazarVocal(frase, vocal)
    mostrarResultado(fraseModificada)
if __name__ == "__main__":
    main()