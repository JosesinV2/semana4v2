#Crea una función que reciba un salario numérico, aumente su parámetro y comprueba si cambió la variable original.
def aumentar_salario(salario):
    salario += 1000
    return salario 

salario_original = float(input("Ingrese el salario original: "))
salario_aumentado = aumentar_salario(salario_original)
print("Salario original:", salario_original)
print("Salario aumentado:", salario_aumentado)