'''
Calcula el importe total multiplicando horas trabajadas por el precio por hora.
'''

def salario(precio,horas):
    salario = precio * horas
    print(f"El trabajador se lleva {salario} €")
    
def main():
    precio = int(input("Precio por hora >> "))
    horas = int(input("Horas trabajadas >> "))
    salario(precio,horas)
if __name__ == "__main__":
    main()