#grupo: Jose Adan Solorzano y Javier Isaac Suazo
#requerimientos:
"""Solicitar el nombre del producto, precio y cantidad.
Crear una función que calcule el subtotal.
Crear una función que aplique 8 % de descuento cuando el subtotal sea mayor o igual a C$ 3,000.
Crear una función que calcule el IVA del 15 % después del descuento.
Crear un procedimiento que muestre producto, subtotal, descuento, IVA y total.
Utilizar variables locales dentro de las funciones.
Probar el programa con una compra que reciba descuento y otra que no lo reciba.
Explicar qué parámetros presentan comportamiento similar al paso por valor."""


def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad
    return subtotal


def calcular_descuento(subtotal):
    descuento = 0

    if subtotal >= 3000:
        descuento = subtotal * 0.08

    return descuento


def calcular_iva(subtotal, descuento):
    subtotal_descuento = subtotal - descuento
    iva = subtotal_descuento * 0.15

    return iva

def mostrar_compra(producto, subtotal, descuento, iva, total):
    print("Producto:", producto)
    print("Subtotal: C$", subtotal)
    print("Descuento: C$", descuento)
    print("IVA: C$", iva)
    print("Total: C$", total)


producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: C$ "))
cantidad = int(input("Ingrese la cantidad: "))

subtotal = calcular_subtotal(precio, cantidad)
descuento = calcular_descuento(subtotal)
iva = calcular_iva(subtotal, descuento)
total = subtotal - descuento + iva

mostrar_compra(producto, subtotal, descuento, iva, total)


