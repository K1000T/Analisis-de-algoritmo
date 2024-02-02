import random
import string
import time
import matplotlib.pyplot as plt

# Generar datos del censo
census_data = []
ids = set()
for i in range(500000):
    # Generar ID único
    while True:
        id = ''.join(random.choices(string.digits, k=6))
        if id not in ids:
            ids.add(id)
            break
    # Generar nombre
    name = ''.join(random.choices(string.ascii_uppercase, k=5))

    # Generar edad
    age = random.randint(18, 99)

    # Generar paga_impuestos con un 75% de probabilidad de ser True
    pays_taxes = random.choices([True, False], weights=[75, 25], k=1)[0]

    # Agregar datos al objeto censo
    census_data.append([id, name, age, pays_taxes])
    # Imprimir cada 100k entradas creadas
    if (i + 1) % 100000 == 0:
        print(f"{i + 1} datos creados")

# Imprimir última persona
print("Última persona generada: ", census_data[-1])

# Ordenar datos por ID para la búsqueda binaria
census_data.sort(key=lambda x: x[0])

# Búsqueda por nombre con probabilidad de no encontrar
def search_by_name(name_to_find):
    found = False
    for data in census_data:
        if data[1].upper() == name_to_find.upper() and random.random() > 0.1:
            print("Datos encontrados: ", data)
            found = True
            break
    if not found:
        print("Nombre no encontrado.")

# Búsqueda binaria por ID con probabilidad de no encontrar
def binary_search_by_id(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid][0] < x:
            low = mid + 1
        elif arr[mid][0] > x:
            high = mid - 1
        else:
            if random.random() > 0.1:
                print("Datos encontrados: ", arr[mid])
            else:
                print("ID no encontrado.")
            return
    print("ID no encontrado.")

# Menú para buscar por ID o por nombre
while True:
    print("\n1. Buscar por ID\n2. Buscar por Nombre\n3. Salir")
    option = input("Elige una opción: ")
    if option == '1':
        id_to_find = input("Introduce el ID: ")
        binary_search_by_id(census_data, id_to_find)
    elif option == '2':
        name_to_find = input("Introduce el nombre: ")
        search_by_name(name_to_find)
    elif option == '3':
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")

# Visualización del tiempo de ejecución
start_time_seq = time.time()
search_by_name(census_data[random.randint(0, len(census_data) - 1)][1])
end_time_seq = time.time()

census_data.sort(key=lambda x: x[0])  # Ordenar nuevamente para la búsqueda binaria

start_time_bin = time.time()
binary_search_by_id(census_data, census_data[random.randint(0, len(census_data) - 1)][0])
end_time_bin = time.time()

# Visualización del tiempo de ejecución
labels = ['Búsqueda Secuencial', 'Búsqueda Binaria']
times = [end_time_seq - start_time_seq, end_time_bin - start_time_bin]

plt.bar(labels, times)
plt.ylabel('Tiempo de Ejecución (s)')
plt.title('Comparación de Tiempos de Búsqueda')

# Guardar la gráfica como una imagen en el directori
plt.savefig('tiempos_de_busqueda.png')

# Mostrar la gráfica en la ventana
plt.show()



# Menú para buscar por ID o por nombre
menu(census_data)



