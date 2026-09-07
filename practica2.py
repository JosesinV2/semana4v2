#Crea una función que reciba una lista de ventas y agregue una nueva venta mediante append().
lista_ventas = [100, 200, 300, 400, 500]

def agregar_venta(venta):
    lista_ventas.append(venta)
    print("Venta agregada:", venta)

agregar_venta(600)
print("Lista de ventas:", lista_ventas)