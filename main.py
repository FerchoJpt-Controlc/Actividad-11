def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


cantidad = int(input("¿Cuántos nombres desea ingresar? "))

nombres = []
for i in range(cantidad):
    nombre = input(f"Ingrese el nombre #{i + 1}: ")
    nombres.append(nombre)

nombres_ordenados = quick_sort(nombres)

print("\nLista ordenada alfabéticamente:")
for nombre in nombres_ordenados:
    print(nombre)

"""""
estudiantes = [6, 3, 9, 2]
resultado = quick_sort(estudiantes)
print(resultado)
"""

