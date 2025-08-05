def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

estudiantes = {}
cantidad = int(input("\nIngrese cuantos estudiantes decea ingresar:"))

for i in range(cantidad):
    print(f"\nEstudiante #{i + 1}")
    carnet = input("Ingrese el número de carnet: ")
    nombre = input("Ingrese el nombre: ")
    carrera = input("Ingrese la carrera: ")

    estudiantes[carnet] = {
        "nombre": nombre,
        "carrera": carrera,

    }

carnet_ordenado = quick_sort(list(estudiantes.keys()))

print("\nEstudiantes ordenados por carnet:")
for carnet in carnet_ordenado:
    datos = estudiantes[carnet]
    print(f"\nCarnet: {carnet}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Carrera: {datos['carrera']}")

