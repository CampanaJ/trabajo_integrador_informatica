# Función que implementa búsqueda binaria sobre una lista ordenada
def busqueda_binaria(valor, lista):
    inicio = 0                      # Índice inicial del segmento a buscar
    final = len(lista) - 1         # Índice final del segmento a buscar
    while inicio <= final:         # Mientras el segmento sea válido
        medio = (inicio + final) // 2  # Calcula el punto medio
        if lista[medio] == valor:      # Si encontró el valor, retorna el índice
            return medio
        elif lista[medio] < valor:     # Si el valor está a la derecha
            inicio = medio + 1
        else:                          # Si el valor está a la izquierda
            final = medio - 1
    return None                    # Si no se encuentra, retorna None


# Función que realiza la búsqueda binaria e informa el resultado al usuario
def realizar_busqueda_binaria(valor, lista):
    busqueda = busqueda_binaria(valor, lista)
    if busqueda is None:
        print(f"El número {valor} no se encuentra en la lista.")
    else:
        print(f"El número {valor} se encuentra en el índice {busqueda}.")

# Función que implementa búsqueda lineal recorriendo la lista secuencialmente
def busqueda_lineal(valor, lista):
    for i in range(len(lista)):
        if lista[i] == valor:      # Si encuentra el valor, retorna el índice
            return i
    return None                    # Si no lo encuentra, retorna None

# Función que realiza la búsqueda lineal e informa el resultado al usuario
def realizar_busqueda_lineal(valor, lista):
    busqueda = busqueda_lineal(valor, lista)
    if busqueda is None:
        print(f"El número {valor} no se encuentra en la lista.")
    else:
        print(f"El número {valor} se encuentra en el índice: {busqueda}.")

# Función que permite al usuario crear su propia lista ingresando números
def crear_lista():
    nueva_lista = []
    while True:
        i = input("¿Qué número querés agregar? (escribí 'listo' para terminar): ")
        if i.lower() == "listo":   # Finaliza si el usuario escribe 'listo'
            break
        try:
            nueva_lista.append(int(i))   # Intenta convertir y agregar el número
        except ValueError:
            print("Ingresá solo números o 'listo' para terminar.")
    return nueva_lista

# Función que permite al usuario elegir entre crear una lista o usar una por defecto
def seleccionar_lista():
    selc = input("1) Crear nueva lista\n2) Usar lista por defecto\nSeleccioná una opción: ")
    if selc == "1":
        return crear_lista()            # Llama a la función para crear lista
    elif selc == "2":
        return lista_por_defecto        # Devuelve la lista predefinida
    else:
        print("Opción no válida. Usando lista por defecto.")
        return lista_por_defecto

# Lista de números usada como valor por defecto
lista_por_defecto = [
    47, 3, 89, 15, 62, 23, 78, 1, 34, 56,
    90, 11, 7, 73, 41, 66, 99, 27, 36, 50,
    84, 5, 21, 8, 40, 95, 12, 38, 59, 2,
    31, 68, 13, 18, 44, 10, 25, 92, 4, 77,
    81, 35, 19, 58, 60, 16, 70, 29, 6, 45
]

# Bucle principal del programa
while True:
    # Menú principal de selección
    print("\n¿Qué tipo de búsqueda deseas realizar?")
    print("1) Búsqueda lineal")
    print("2) Búsqueda binaria")
    print("0) Salir")
    seleccion = input("Seleccioná una opción: ")

    if seleccion == "0":
        print("Programa finalizado.")  # Salida del programa
        break

    # Solicita al usuario el número a buscar
    valor_input = input("¿Qué número querés buscar?: ")
    try:
        valor = int(valor_input)       # Intenta convertir a entero
    except ValueError:
        print("Debés ingresar un número válido.")
        continue                       # Vuelve al menú principal

    # Permite seleccionar la lista a utilizar
    lista_seleccionada = seleccionar_lista()

    # Ejecuta la búsqueda según la opción seleccionada
    if seleccion == "1":
        realizar_busqueda_lineal(valor, lista_seleccionada)
    elif seleccion == "2":
        lista_ordenada = sorted(lista_seleccionada)  # Ordena la lista para búsqueda binaria
        realizar_busqueda_binaria(valor, lista_ordenada)
    else:
        print("Opción inválida.")