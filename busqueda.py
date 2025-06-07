def busqueda_binaria(valor, lista):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        medio = (inicio + final) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            inicio = medio + 1
        else:
            final = medio - 1
    return None

def realizar_busqueda_binaria(valor, lista):
    busqueda = busqueda_binaria(valor, lista)
    if busqueda is None:
        print(f"El número {valor} no se encuentra en la lista.")
    else:
        print(f"El número {valor} se encuentra en el índice {busqueda}.")

def busqueda_lineal(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return None

def realizar_busqueda_lineal(valor, lista):
    busqueda = busqueda_lineal(valor, lista)
    if busqueda is None:
        print(f"El número {valor} no se encuentra en la lista.")
    else:
        print(f"El número {valor} se encuentra en el índice: {busqueda}.")

def crear_lista():
    nueva_lista = []
    while True:
        i = input("¿Qué número querés agregar? (escribí 'listo' para terminar): ")
        if i.lower() == "listo":
            break
        try:
            nueva_lista.append(int(i))
        except ValueError:
            print("Ingresá solo números o 'listo' para terminar.")
    return nueva_lista

def seleccionar_lista():
    selc = input("1) Crear nueva lista\n2) Usar lista por defecto\nSeleccioná una opción: ")
    if selc == "1":
        return crear_lista()
    elif selc == "2":
        return lista_por_defecto
    else:
        print("Opción no válida. Usando lista por defecto.")
        return lista_por_defecto

lista_por_defecto = [
    47, 3, 89, 15, 62, 23, 78, 1, 34, 56,
    90, 11, 7, 73, 41, 66, 99, 27, 36, 50,
    84, 5, 21, 8, 40, 95, 12, 38, 59, 2,
    31, 68, 13, 18, 44, 10, 25, 92, 4, 77,
    81, 35, 19, 58, 60, 16, 70, 29, 6, 45
]

while True:
    print("\n¿Qué tipo de búsqueda deseas realizar?")
    print("1) Búsqueda lineal")
    print("2) Búsqueda binaria")
    print("0) Salir")
    seleccion = input("Seleccioná una opción: ")

    if seleccion == "0":
        print("Programa finalizado.")
        break

    valor_input = input("¿Qué número querés buscar?: ")
    try:
        valor = int(valor_input)
    except ValueError:
        print("Debés ingresar un número válido.")
        continue

    lista_seleccionada = seleccionar_lista()

    if seleccion == "1":
        realizar_busqueda_lineal(valor, lista_seleccionada)
    elif seleccion == "2":
        lista_ordenada = sorted(lista_seleccionada)
        realizar_busqueda_binaria(valor, lista_ordenada)
    else:
        print("Opción inválida.")