'''
Calcula el peso total de un pedido (112 g por payaso, 75 g por muñeca).
'''

def productosPedidos():
    payasos = int(input("Número de payasos >> "))
    muniecas = int(input("Número de muñecas >> "))
    return payasos, muniecas

def pesoTotal(payasos, muniecas):
    pesoPayasos = payasos * 112
    pesoMuniecas = muniecas * 75
    pesoTotal = pesoPayasos + pesoMuniecas
    return pesoTotal

def mostrarResultado(pesoTotal):
    print(f"El peso total del pedido es {pesoTotal} g")

def main():
    payasos, muniecas = productosPedidos()
    pesoTotalPedido = pesoTotal(payasos, muniecas)
    mostrarResultado(pesoTotalPedido)
if __name__ == "__main__":
    main()