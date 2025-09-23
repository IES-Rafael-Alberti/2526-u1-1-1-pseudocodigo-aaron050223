'''
Invertir una frase
Descripción: Muestra una frase escrita por el usuario invertida (de atrás hacia adelante).
Entrada: frase (texto).
Salida: frase invertida.
'''

def pedirFrase():
    frase = str(input("Dime una frase >> "))
    return frase

def invertirFrase(frase):
    fraseInvertida = frase[::-1]
    return fraseInvertida

def mostrarResultado(fraseInvertida):
    print(f"Frase invertida >> {fraseInvertida}")

def main():
    frase = pedirFrase()
    fraseInvertida = invertirFrase(frase)
    mostrarResultado(fraseInvertida)
if __name__ == "__main__":
    main()