# ==================================================
# PORTADA
# ==================================================
# Nombre: Samuel Hernández Nava
# Matrícula: 2630016
# Grupo: IM-1 TSU 75001

# ==================================================
# RESUMEN EJECUTIVO
# ==================================================
# Una lista (list) es una colección ordenada y mutable, una tupla (tuple) es
# una colección ordenada e inmutable, y un diccionario (dict) guarda parejas
# clave-valor. Mutable significa que se puede modificar después de crearla
# (agregar, quitar o cambiar elementos); inmutable significa que no se puede.
# Los diccionarios asocian cada clave con un valor y permiten buscar la
# información directamente por la clave, sin recorrer todos los elementos.
# Este documento cubre 2 problemas: cada uno tiene descripción, entradas,
# salidas, validaciones y 3 casos de prueba, usando listas y tuplas.


# ==================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ==================================================
# - Usar listas cuando se necesite agregar o eliminar elementos seguido.
# - Usar tuplas para datos que no deben cambiar (coordenadas, fechas,
#   configuraciones fijas).
# - Usar diccionarios cuando se necesite buscar información por una clave
#   (nombre, id, código).
# - Evitar modificar una lista mientras se recorre con un for, a menos que se
#   sepa exactamente lo que se hace.
# - Usar nombres de claves descriptivos en los diccionarios.
# - Escribir código legible y mensajes claros para el usuario.


# ==================================================
# Problem 1: Shopping list basics (list operations)
# ==================================================
# Description:
# The program builds a list of products from a text separated by commas,
# adds a new product at the end, shows the total number of items and checks
# if a specific product is in the list (boolean is_in_list).
#
# Inputs:
# - initial_items_text (string, for example "grape,mango,pear")
# - new_item (string, product to add)
# - search_item (string, product to search)
#
# Outputs:
# - "Items list: <items_list>"
# - "Total items: <len_list>"
# - "Found item: true" or "Found item: false"
#
# Validations:
# - initial_items_text, new_item and search_item must not be empty after
#   strip().
# - The text is split by commas and each item is cleaned with strip().
# - Decision: empty pieces (like in "grape,,pear") are ignored, and an
#   initial list that ends up empty is not accepted (invalid input).
# - Decision: everything is converted to lowercase to compare it correctly.
#
# Test cases:
# 1) Normal: "grape, mango ,pear", "kiwi", "mango"
#    -> Items list: ['grape', 'mango', 'pear', 'kiwi']
#       Total items: 4
#       Found item: true
# 2) Border: "melon", "melon", "plum"
#    -> Items list: ['melon', 'melon']
#       Total items: 2
#       Found item: false
# 3) Error: "", "kiwi", "grape" -> Error: invalid input

print("--- Problem 1: Shopping list basics ---")

initial_items_text = input("Enter the initial items separated by commas: ").strip()
new_item = input("Enter the item to add: ").strip().lower()
search_item = input("Enter the item to search: ").strip().lower()

if initial_items_text == "" or new_item == "" or search_item == "":
    print("Error: invalid input")
else:
    items_list = []

    # split(",") cuts the text at every comma and gives a list of pieces
    for piece in initial_items_text.split(","):
        clean_piece = piece.strip().lower()
        if clean_piece != "":
            items_list.append(clean_piece)

    if len(items_list) == 0:
        print("Error: invalid input")
    else:
        items_list.append(new_item)
        is_in_list = search_item in items_list

        print(f"Items list: {items_list}")
        print(f"Total items: {len(items_list)}")
        if is_in_list:
            print("Found item: true")
        else:
            print("Found item: false")

print()

# ==================================================
# Problem 2: Points and distances with tuples
# ==================================================
# Description:
# The program creates two tuples point_a and point_b with the coordinates
# of two points in a 2D plane. Then it calculates the Euclidean distance
# between them and creates a new tuple midpoint with the middle point.
#
# Inputs:
# - x1, y1, x2, y2 (float, coordinates of the points)
#
# Outputs:
# - "Point A: (x1, y1)"
# - "Point B: (x2, y2)"
# - "Distance: <distance>"
# - "Midpoint: (mx, my)"
#
# Validations:
# - The 4 inputs must be convertible to float (negative numbers and
#   decimals are allowed).
# - No additional restrictions in the range.
#
# Test cases:
# 1) Normal: -1, -2, 2, 2 -> Point A: (-1.0, -2.0)
#                            Point B: (2.0, 2.0)
#                            Distance: 5.0
#                            Midpoint: (0.5, 0.0)
# 2) Border: 7, 7, 7, 7 -> Point A and Point B: (7.0, 7.0)
#                          Distance: 0.0 (same point)
#                          Midpoint: (7.0, 7.0)
# 3) Error: "xyz", 1, 2, 3 -> Error: invalid input

print("--- Problem 2: Points and distances with tuples ---")

x1_text = input("Enter x1: ").strip()
y1_text = input("Enter y1: ").strip()
x2_text = input("Enter x2: ").strip()
y2_text = input("Enter y2: ").strip()

coordinate_texts = [x1_text, y1_text, x2_text, y2_text]
all_numbers = True

for coordinate_text in coordinate_texts:
    check_text = coordinate_text

    # A minus sign is only accepted at the beginning of the number
    if check_text.startswith("-"):
        check_text = check_text[1:]

    # replace(".", "", 1) removes one decimal point so isdigit() can check
    if not check_text.replace(".", "", 1).isdigit():
        all_numbers = False

if not all_numbers:
    print("Error: invalid input")
else:
    x1 = float(x1_text)
    y1 = float(y1_text)
    x2 = float(x2_text)
    y2 = float(y2_text)

    point_a = (x1, y1)
    point_b = (x2, y2)

    # Index 0 is the x coordinate and index 1 is the y coordinate
    x_difference = point_b[0] - point_a[0]
    y_difference = point_b[1] - point_a[1]
    distance = (x_difference ** 2 + y_difference ** 2) ** 0.5

    midpoint = ((point_a[0] + point_b[0]) / 2, (point_a[1] + point_b[1]) / 2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, 2)}")
    print(f"Midpoint: {midpoint}")

print()


# ==================================================
# CONCLUSIONES HASTA EL MOMENTO
# ==================================================
# Las listas conviene usarlas cuando los datos cambian seguido, porque se
# pueden agregar y eliminar elementos de forma flexible con append() y pop().
# Las tuplas son útiles para datos que no deben cambiar, como las coordenadas
# de un punto, porque al ser inmutables evitan modificaciones por error.
# En mi investigación sobre Los diccionarios llegué a la conclusión que 
# facilitan las búsquedas rápidas por clave, como encontrar el precio de un producto 
# o el teléfono de un contacto sin recorrer todo.
# Elegir bien la estructura hace el código más simple y claro.
 
 
# ==================================================
# REFERENCES
# ==================================================
# References:
# 1) Python documentation - Built-in Types: list, tuple, dict
# 2) Python documentation - Tutorial: Data Structures
# 3) Matthes, E. Python Crash Course (lists, tuples and dictionaries)
# 4) Real Python - Dictionaries in Python
# 5) Class notes of the programming course (files understanding_*.py)
