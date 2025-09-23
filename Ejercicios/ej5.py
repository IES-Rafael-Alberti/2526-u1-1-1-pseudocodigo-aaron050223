'''
Calcula el importe total multiplicando horas trabajadas por el precio por hora.
'''

def salario(precio,horas):
    salario = precio * horas
    return salario

def mostrarResultado(salario):
    print(f"El trabajador se lleva {salario} €")
    
def main():
    precio = int(input("Precio por hora >> "))
    horas = int(input("Horas trabajadas >> "))
    salarioGanado = salario(precio,horas)
    mostrarResultado(salarioGanado)
if __name__ == "__main__":
    main()