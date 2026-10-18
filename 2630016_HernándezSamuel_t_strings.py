# ==================================================
# PORTADA
# ==================================================
# Nombre: Samuel Hernández Nava
# Matrícula: 2630016
# Grupo: IM-1 TSU 75001



# ==================================================
# RESUMEN EJECUTIVO
# ==================================================
# Un string en Python es una secuencia de caracteres escrita entre comillas.
# Su tipo de dato es str y es inmutable: cualquier cambio crea una nueva
# cadena. Con los strings podemos concatenar, obtener la longitud con len(),
# extraer sub-cadenas con slicing, buscar patrones con in, find() y count(),
# y reemplazar texto con replace().
# Es importante validar y normalizar el texto de entrada (correos, nombres,
# contraseñas) porque los usuarios escriben espacios de más, mezclan
# mayúsculas y minúsculas o usan formatos incorrectos, y eso produce errores
# y datos basura.
# Este documento cubre 6 problemas; cada uno tiene su descripción, entradas,
# salidas, validaciones, métodos de string y 3 casos de prueba, con el código.


# ==================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ==================================================
# - Los strings son inmutables: cualquier cambio genera una nueva cadena.
# - Es buena práctica normalizar la entrada con strip() y lower() antes de
#   compararla.
# - Evitar "números mágicos" en los índices: documentar qué extrae cada slice.
# - Usar métodos de string en lugar de reescribir lógica básica.
# - Diseñar validaciones claras: primero que no esté vacío, luego el formato.
# - Escribir código legible: nombres de variables claros y mensajes de error
#   entendibles.


# ==================================================
# Problem 1: Full name formatter (name + initials)
# ==================================================
# Description:
# The program receives a full name in one string, normalizes it (strip,
# extra spaces, uppercase/lowercase) and shows the name in Title Case
# and the initials (example: J.C.T.).
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Name In Title Case>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - full_name must not be empty after strip() (spaces only is not valid).
# - It must contain at least two words (name and last name).
#
# Test cases:
# 1) Normal: "  samuel hernandez nava " -> Formatted name: Samuel Hernandez Nava
#                                      Initials: S.H.N.
# 2) Border: "  CHaRLY    MERCuRY  "    -> Formatted name: Charly Mercury
#                                      Initials: C.M.
# 3) Error: "Oskar"                   -> Error: invalid input

print("--- Problem 1: Full name formatter ---")

full_name = input("Enter your full name: ").strip()

if full_name == "":
    print("Error: invalid input")
else:
    # split() without arguments also removes the extra spaces between words
    name_words = full_name.split()

    if len(name_words) < 2:
        print("Error: invalid input")
    else:
        # join() puts the words back together with exactly one space
        formatted_name = " ".join(name_words).title()

        initials = ""
        for name_word in name_words:
            # name_word[0] is the first letter of each word
            initials = initials + name_word[0].upper() + "."

        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")

print()

# ==================================================
# Problem 2: Simple email validator (structure + domain)
# ==================================================
# Description:
# The program checks if an email has a basic correct format: exactly one
# '@', at least one '.' after the '@' and no blank spaces.
# If the email is valid, it also shows the domain (the part after '@').
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true" or "Valid email: false"
# - If valid: "Domain: <domain_part>"
#
# Validations:
# - email_text must not be empty after strip().
# - Count how many times '@' appears (it must be exactly 1).
# - There must be no spaces inside email_text.
# - There must be at least one '.' after the '@'.
#
# Test cases:
# 1) Normal: "2630016@upv.edu.mx"  -> Valid email: true
#                                   Domain: upv.edu.mx
# 2) Border: "a@b.c"              -> Valid email: true
#                                   Domain: b.c
# 3) Error: "samuel@@upv.edu.mx"  -> Valid email: false

print("--- Problem 2: Simple email validator ---")

email_text = input("Enter an email: ").strip()

if email_text == "":
    print("Error: invalid input")
elif " " in email_text:
    print("Valid email: false")
elif email_text.count("@") != 1:
    print("Valid email: false")
else:
    # find() returns the position of '@'; the domain starts one position later
    at_position = email_text.find("@")
    domain_part = email_text[at_position + 1:]

    if "." not in domain_part:
        print("Valid email: false")
    else:
        print("Valid email: true")
        print(f"Domain: {domain_part}")

print()

# ==================================================
# Problem 3: Palindrome checker (ignoring spaces and case)
# ==================================================
# Description:
# The program checks if a phrase reads the same from left to right and
# from right to left, ignoring blank spaces and uppercase/lowercase.
# It also shows the normalized version of the phrase.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Normalized: <phrase without spaces and in lowercase>"
# - "Is palindrome: true" or "Is palindrome: false"
#
# Validations:
# - phrase must not be empty after strip().
# - After cleaning the spaces it must have at least MIN_LENGTH characters.
#
# Test cases:
# 1) Normal: Atar a la rata" -> Normalized: ataralarata
#                                    Is palindrome: true
# 2) Border: "A b A"               -> Normalized: aba
#                                    Is palindrome: true
# 3) Error: "   "                  -> Error: invalid input

print("--- Problem 3: Palindrome checker ---")

MIN_LENGTH = 3

phrase = input("Enter a phrase: ").strip()

if phrase == "":
    print("Error: invalid input")
else:
    normalized_phrase = phrase.lower().replace(" ", "")

    if len(normalized_phrase) < MIN_LENGTH:
        print("Error: invalid input")
    else:
        print(f"Normalized: {normalized_phrase}")

        # [::-1] is a slice that reads the whole text backwards
        if normalized_phrase == normalized_phrase[::-1]:
            print("Is palindrome: true")
        else:
            print("Is palindrome: false")

#Examples of normal case for practice: somos o no somos, luz azul, yo hago yoga hoy

print()

# ==================================================
# Problem 4: Sentence word stats (lengths and first/last word)
# ==================================================
# Description:
# The program receives a sentence, removes the spaces at the beginning and
# at the end, and splits it into words. Then it shows the number of words,
# the first and last word, and the shortest and longest word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - sentence must not be empty after strip().
# - It must have at least one valid word after split().
#
# Test cases:
# 1) Normal: "  Charly Mercury is Python Lover " -> Word count: 5
#                                              First word: Charly
#                                              Last word: Lover
#                                              Shortest word: is
#                                              Longest word: Mercury
# 2) Border: "Hello"                          -> Word count: 1 and the first,
#            last, shortest and longest word are all "Hello"
# 3) Error: "     "                           -> Error: invalid input

print("--- Problem 4: Sentence word stats ---")

sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: invalid input")
else:
    sentence_words = sentence.split()

    if len(sentence_words) == 0:
        print("Error: invalid input")
    else:
        # We start with the first word and compare it with all the others
        shortest_word = sentence_words[0]
        longest_word = sentence_words[0]

        for sentence_word in sentence_words:
            if len(sentence_word) < len(shortest_word):
                shortest_word = sentence_word
            if len(sentence_word) > len(longest_word):
                longest_word = sentence_word

        print(f"Word count: {len(sentence_words)}")
        print(f"First word: {sentence_words[0]}")
        print(f"Last word: {sentence_words[-1]}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")

print()

# ==================================================
# Problem 5: Password strength classifier
# ==================================================
# Description:
# The program classifies a password as "weak", "medium" or "strong"
# using the rules written below. It checks the password character by
# character and uses boolean flags to remember what it found.
#
# Rules used:
# - Weak: length < 8, or it does not meet the rules of medium or strong
#   (for example, only lowercase letters).
# - Medium: length >= 8 and it has uppercase AND lowercase letters,
#   or it has at least one digit.
# - Strong: length >= 8 and it has at least one uppercase letter,
#   one lowercase letter, one digit and one symbol (not alphanumeric).
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: weak"
# - "Password strength: medium"
# - "Password strength: strong"
#
# Validations:
# - The password must not be empty (checked with strip()).
# - The length is verified with len().
#
# Test cases:
# 1) Normal: "sancharly2026# -> Password strength: strong
# 2) Border: "Abcdefg1"    -> Password strength: medium
#                             (exactly 8 characters, but without a symbol)
# 3) Error: ""             -> Error: invalid input

print("--- Problem 5: Password strength classifier ---")

MIN_PASSWORD_LENGTH = 8

password_input = input("Enter a password: ")

# strip() is used only to check that it is not empty; the password
# itself is not modified because spaces can be part of a password
if password_input.strip() == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for character in password_input:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        elif not character.isalnum():
            has_symbol = True

    if len(password_input) < MIN_PASSWORD_LENGTH:
        password_strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        password_strength = "strong"
    elif (has_upper and has_lower) or has_digit:
        password_strength = "medium"
    else:
        password_strength = "weak"

    print(f"Password strength: {password_strength}")

print()

# ==================================================
# Problem 6: Product label formatter (fixed-width text)
# ==================================================
# Description:
# The program builds a one-line label with the format
# "Product: <NAME> | Price: $<PRICE>" that has exactly 30 characters.
# If the text is shorter it is filled with spaces at the end, and if it
# is longer it is cut to 30 characters.
#
# Inputs:
# - product_name (string)
# - price_text (string that must be convertible to a positive number)
#
# Outputs:
# - "Label: "<exactly 30 characters>"" (between quotes to see the spaces)
# - "Length: 30"
#
# Validations:
# - product_name must not be empty after strip().
# - price_text must be convertible to a positive number.
#
# Test cases:
# 1) Normal: "Mouse", "15.5"
#            -> Label: "Product: Mouse | Price: $15.5 "
#               (29 characters + 1 space at the end)
# 2) Border: "Mechanical Keyboard", "49.99"
#            -> Label: "Product: Mechanical Keyboard |"
#               (the text was longer than 30, so it was cut)
# 3) Error: "Mouse", "-5" -> Error: invalid input

print("--- Problem 6: Product label formatter ---")

LABEL_LENGTH = 30

product_name = input("Enter the product name: ").strip()
price_text = input("Enter the price: ").strip()

# replace(".", "", 1) removes one decimal point so isdigit() can check the
# rest; a minus sign or a letter makes isdigit() return False
price_is_number = price_text.replace(".", "", 1).isdigit()

if product_name == "" or not price_is_number:
    print("Error: invalid input")
elif float(price_text) <= 0:
    print("Error: invalid input")
else:
    label = f"Product: {product_name} | Price: ${price_text}"

    if len(label) > LABEL_LENGTH:
        label = label[:LABEL_LENGTH]
    else:
        # " " * n repeats the space n times to fill the missing characters
        label = label + " " * (LABEL_LENGTH - len(label))

    print(f'Label: "{label}"')
    print(f"Length: {len(label)}")

print()


# ==================================================
# CONCLUSIONES
# ==================================================
# El manejo de strings es esencial porque la mayoría de los datos de entrada
# y salida de un programa son texto. strip() y lower() sirven para limpiar la
# entrada, split() y join() para trabajar palabra por palabra y reconstruir
# el texto, y los slices como [::-1] o [:30] para leer o cortar texto.
# Normalizar el texto antes de compararlo evita diferencias falsas como
# "Hello" y "hello ". Las validaciones claras (primero vacío, luego formato)
# evitan errores y datos basura. Reforcé la idea que los strings son inmutables:
# los métodos devuelven una cadena nueva, así que hay que guardar el
# resultado en una variable.


# ==================================================
# REFERENCES
# ==================================================
# References:
# 1) Python documentation - Built-in Types: Text Sequence Type - str
# 2) Python documentation - Tutorial: An Informal Introduction to Python
# 3) Matthes, E. Python Crash Course (strings, lists and if statements)
# 4) Real Python - Python Strings and Character Data
# 5) Class notes of the programming course (files understanding_*.py)
