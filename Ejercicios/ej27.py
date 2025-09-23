'''
Mostrar día, mes y año de una fecha
Descripción: Pide la fecha de nacimiento en formato dd/mm/aaaa y muestra día, mes y año por separado.
Entrada: fecha (texto dd/mm/aaaa).
Salida: día, mes, año.
'''

def pedirFecha():
    fecha = str(input("Introduce tu fecha de nacimiento (Formato >> dd/mm/aaaa) >> "))
    return fecha

def separarFecha(fecha):
    fechaSeparada = fecha.split("/")
    return fechaSeparada

def validar(fechaComprobar):
    if len(fechaComprobar) == 3:
        return True
    else:
        return False

def mostrarResultado(fechaSeparada):
    if validar(fechaSeparada):
        dia = fechaSeparada[0]
        mes = fechaSeparada[1]
        anio = fechaSeparada[2]
        print(f"Día >> {dia}")
        print(f"Mes >> {mes}")
        print(f"Año >> {anio}")
    else:
        print("La fecha introducida no es válida.")

def main():
    fecha = pedirFecha()
    fechaSeparada = separarFecha(fecha)
    mostrarResultado(fechaSeparada)
if __name__ == "__main__":
    main()