# ==================================================
# PORTADA
# ==================================================
# Nombre: Samuel Hernández Nava
# Matrícula: 2630016
# Grupo: IM-1 TSU 75001

# ==================================================
# RESUMEN EJECUTIVO
# ==================================================
# Un entero (int) es un número sin parte decimal, como 5 o -3, y un flotante
# (float) es un número con parte decimal, como 3.14. La diferencia es que los
# float permiten representar cantidades fraccionarias, aunque pueden tener
# pequeños errores de precisión. Un booleano (bool) solo puede ser True o
# False, y se obtiene al comparar valores con operadores como >=, == o !=.
# Es importante validar rangos y evitar la división entre cero porque datos
# fuera de lo razonable (horas negativas, ingresos en 0) producen resultados
# sin sentido o hacen que el programa se detenga con un error.
# Este documento cubre 6 problemas con descripción, entradas, salidas,
# validaciones y 3 casos de prueba, usando int, float y bool para decidir.


# ==================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# ==================================================
# - Usar tipos apropiados: int para contadores, float para cantidades con
#   decimales.
# - Evitar duplicar expresiones complejas: guardar los resultados
#   intermedios en variables.
# - Validar los datos antes de operar (por ejemplo, que las horas y los
#   salarios no sean negativos).
# - Usar nombres de variables descriptivos y mensajes claros para el usuario.
# - Documentar cómo se interpretan los booleanos: en todos los problemas,
#   true significa que la condición se cumple y false que no se cumple.


# ==================================================
# Problem 1: Temperature converter and range flag
# ==================================================
# Description:
# The program converts a temperature in Celsius to Fahrenheit and Kelvin.
# It also creates the boolean is_high_temperature, which is true when the
# temperature in Celsius is greater than or equal to 30.0.
#
# Inputs:
# - temp_c (float, temperature in Celsius)
#
# Outputs:
# - "Fahrenheit: <temp_f>"
# - "Kelvin: <temp_k>"
# - "High temperature: true" or "High temperature: false"
#
# Validations:
# - temp_c must be convertible to float (negative numbers are allowed).
# - Kelvin cannot be negative (temp_k < 0.0 is physically impossible).
#
# Test cases:
# 1) Normal: "36.6"    -> Fahrenheit: 97.88
#                         Kelvin: 309.75
#                         High temperature: true
# 2) Border: "-273.15" -> Fahrenheit: -459.67
#                         Kelvin: 0.0  (absolute zero, the lowest valid value)
#                         High temperature: false
# 3) Error: "-300"     -> Error: invalid input (Kelvin would be negative)

print("--- Problem 1: Temperature converter and range flag ---")

HIGH_TEMPERATURE_LIMIT = 30.0

temp_text = input("Enter the temperature in Celsius: ").strip()

# A minus sign is only accepted at the beginning of the number
check_text = temp_text
if check_text.startswith("-"):
    check_text = check_text[1:]

# replace(".", "", 1) removes one decimal point so isdigit() can check
if not check_text.replace(".", "", 1).isdigit():
    print("Error: invalid input")
else:
    temp_c = float(temp_text)
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        is_high_temperature = temp_c >= HIGH_TEMPERATURE_LIMIT

        print(f"Fahrenheit: {round(temp_f, 2)}")
        print(f"Kelvin: {round(temp_k, 2)}")
        # str(True) is "True" and lower() makes it "true"
        print(f"High temperature: {str(is_high_temperature).lower()}")

print()


# ==================================================
# Problem 2: Work hours and overtime payment
# ==================================================
# Description:
# The program calculates the weekly pay of a worker. Up to 40 hours are
# paid at hourly_rate and the extra hours are paid at 150% of that rate.
# It also creates the boolean has_overtime.
#
# Inputs:
# - hours_worked (float, hours worked in the week)
# - hourly_rate (float, pay per hour)
#
# Outputs:
# - "Regular pay: <regular_pay>"
# - "Overtime pay: <overtime_pay>"
# - "Total pay: <total_pay>"
# - "Has overtime: true" or "Has overtime: false"
#
# Validations:
# - hours_worked >= 0 (the format check rejects negative numbers).
# - hourly_rate > 0.
# - If one of them is not valid, "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: "45", "120"   -> Regular pay: 4800.0
#                             Overtime pay: 900.0
#                             Total pay: 5700.0
#                             Has overtime: true
# 2) Border: "40", "95.5"  -> Regular pay: 3820.0
#                             Overtime pay: 0.0
#                             Total pay: 3820.0
#                             Has overtime: false (exactly 40 hours)
# 3) Error: "-5", "100"    -> Error: invalid input

print("--- Problem 2: Work hours and overtime payment ---")

REGULAR_HOURS_LIMIT = 40.0
OVERTIME_MULTIPLIER = 1.5

hours_text = input("Enter the hours worked: ").strip()
rate_text = input("Enter the hourly rate: ").strip()

# isdigit() is False for a minus sign, so negative hours are rejected here
hours_is_number = hours_text.replace(".", "", 1).isdigit()
rate_is_number = rate_text.replace(".", "", 1).isdigit()

if not hours_is_number or not rate_is_number:
    print("Error: invalid input")
elif float(rate_text) <= 0.0:
    print("Error: invalid input")
else:
    hours_worked = float(hours_text)
    hourly_rate = float(rate_text)

    # min() keeps at most 40 regular hours; max() never gives a negative number
    regular_hours = min(hours_worked, REGULAR_HOURS_LIMIT)
    overtime_hours = max(hours_worked - REGULAR_HOURS_LIMIT, 0.0)

    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > REGULAR_HOURS_LIMIT

    print(f"Regular pay: {round(regular_pay, 2)}")
    print(f"Overtime pay: {round(overtime_pay, 2)}")
    print(f"Total pay: {round(total_pay, 2)}")
    print(f"Has overtime: {str(has_overtime).lower()}")

print()
# ==================================================
# Problem 3: Discount eligibility with booleans
# ==================================================
# Description:
# The program decides if a customer gets a discount. The customer is
# eligible if is_student is true OR is_senior is true OR the purchase total
# is at least 1000.0. If eligible, a 10% discount is applied to the total.
#
# Inputs:
# - purchase_total (float, total of the purchase)
# - is_student_text (string, "YES" or "NO")
# - is_senior_text (string, "YES" or "NO")
#
# Outputs:
# - "Discount eligible: true" or "Discount eligible: false"
# - "Final total: <final_total>"
#
# Validations:
# - purchase_total >= 0.0 (the format check rejects negative numbers).
# - The texts are normalized to uppercase and must be "YES" or "NO".
# - If any input is not valid, "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: "450", "yes", "no"  -> Discount eligible: true (student)
#                                   Final total: 405.0
# 2) Border: "1000", "no", "no"  -> Discount eligible: true (exactly 1000.0)
#                                   Final total: 900.0
# 3) Error: "300", "maybe", "no" -> Error: invalid input

print("--- Problem 3: Discount eligibility with booleans ---")

DISCOUNT_MIN_TOTAL = 1000.0
DISCOUNT_FACTOR = 0.9
YES_NO_OPTIONS = ["YES", "NO"]

purchase_text = input("Enter the purchase total: ").strip()
student_text = input("Are you a student? (YES or NO): ").strip().upper()
senior_text = input("Are you a senior? (YES or NO): ").strip().upper()

total_is_number = purchase_text.replace(".", "", 1).isdigit()

if not total_is_number:
    print("Error: invalid input")
elif student_text not in YES_NO_OPTIONS or senior_text not in YES_NO_OPTIONS:
    print("Error: invalid input")
else:
    purchase_total = float(purchase_text)

    # Comparing the text with "YES" gives us the boolean directly
    is_student = student_text == "YES"
    is_senior = senior_text == "YES"

    discount_eligible = is_student or is_senior or (purchase_total >= DISCOUNT_MIN_TOTAL)

    if discount_eligible:
        final_total = purchase_total * DISCOUNT_FACTOR
    else:
        final_total = purchase_total

    print(f"Discount eligible: {str(discount_eligible).lower()}")
    print(f"Final total: {round(final_total, 2)}")

print()


# ==================================================
# Problem 4: Basic statistics of three integers
# ==================================================
# Description:
# The program reads three integers and calculates their sum, average
# (float), maximum and minimum. It also creates the boolean all_even, which
# is true when the three numbers are even.
#
# Inputs:
# - n1 (int)
# - n2 (int)
# - n3 (int)
#
# Outputs:
# - "Sum: <sum_value>"
# - "Average: <average_value>"
# - "Max: <max_value>"
# - "Min: <min_value>"
# - "All even: true" or "All even: false"
#
# Validations:
# - The three values must be convertible to int.
# - No additional restrictions (negative numbers are allowed).
#
# Test cases:
# 1) Normal: 7, 12, -2   -> Sum: 17
#                           Average: 5.67
#                           Max: 12
#                           Min: -2
#                           All even: false
# 2) Border: 0, 0, 0     -> Sum: 0
#                           Average: 0.0
#                           Max: 0
#                           Min: 0
#                           All even: true (zero is an even number)
# 3) Error: 5, "x", 3    -> Error: invalid input

print("--- Problem 4: Basic statistics of three integers ---")

n1_text = input("Enter the first integer: ").strip()
n2_text = input("Enter the second integer: ").strip()
n3_text = input("Enter the third integer: ").strip()

number_texts = [n1_text, n2_text, n3_text]
all_integers = True

for number_text in number_texts:
    check_text = number_text

    # A minus sign is only accepted at the beginning of the number
    if check_text.startswith("-"):
        check_text = check_text[1:]

    if not check_text.isdigit():
        all_integers = False

if not all_integers:
    print("Error: invalid input")
else:
    n1 = int(n1_text)
    n2 = int(n2_text)
    n3 = int(n3_text)

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")

print()


# ==================================================
# Problem 5: Loan eligibility (income and debt ratio)
# ==================================================
# Description:
# The program decides if a person is eligible for a loan using the monthly
# income, the monthly debt and the credit score. It calculates the debt
# ratio (debt divided by income) and applies the three rules below.
#
# Rule: eligible is true only if ALL these conditions are true:
# - monthly_income >= 8000.0
# - debt_ratio <= 0.4
# - credit_score >= 650
#
# Inputs:
# - monthly_income (float, monthly income)
# - monthly_debt (float, monthly debt payments)
# - credit_score (int, credit score)
#
# Outputs:
# - "Debt ratio: <debt_ratio>"
# - "Eligible: true" or "Eligible: false"
#
# Validations:
# - monthly_income > 0.0 (this avoids a division by zero).
# - monthly_debt >= 0.0 and credit_score >= 0 (the format check rejects
#   negative numbers).
# - If one of them is not valid, "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: "15000", "3000", "720" -> Debt ratio: 0.2
#                                      Eligible: true
# 2) Border: "10000", "4000", "650" -> Debt ratio: 0.4
#                                      Eligible: true (all limits exact)
# 3) Error: "0", "500", "700"       -> Error: invalid input (income is 0)

print("--- Problem 5: Loan eligibility ---")

MIN_INCOME = 8000.0
MAX_DEBT_RATIO = 0.4
MIN_CREDIT_SCORE = 650

income_text = input("Enter the monthly income: ").strip()
debt_text = input("Enter the monthly debt: ").strip()
score_text = input("Enter the credit score: ").strip()

income_is_number = income_text.replace(".", "", 1).isdigit()
debt_is_number = debt_text.replace(".", "", 1).isdigit()
score_is_number = score_text.isdigit()

if not income_is_number or not debt_is_number or not score_is_number:
    print("Error: invalid input")
elif float(income_text) <= 0.0:
    print("Error: invalid input")
else:
    monthly_income = float(income_text)
    monthly_debt = float(debt_text)
    credit_score = int(score_text)

    # The income is greater than 0 here, so the division is safe
    debt_ratio = monthly_debt / monthly_income

    eligible = (
        monthly_income >= MIN_INCOME
        and debt_ratio <= MAX_DEBT_RATIO
        and credit_score >= MIN_CREDIT_SCORE
    )

    print(f"Debt ratio: {round(debt_ratio, 2)}")
    print(f"Eligible: {str(eligible).lower()}")

print()


# ==================================================
# Problem 6: Body Mass Index (BMI) and category flag
# ==================================================
# Description:
# The program calculates the BMI with weight_kg / (height_m * height_m)
# and creates three booleans to show the category: is_underweight,
# is_normal and is_overweight.
#
# Inputs:
# - weight_kg (float, weight in kilograms)
# - height_m (float, height in meters)
#
# Outputs:
# - "BMI: <rounded_bmi>"
# - "Underweight: true" or "Underweight: false"
# - "Normal: true" or "Normal: false"
# - "Overweight: true" or "Overweight: false"
#
# Validations:
# - weight_kg > 0.0
# - height_m > 0.0
# - If one of them is not valid, "Error: invalid input" is shown.
#
# Test cases:
# 1) Normal: "70", "1.75" -> BMI: 22.86
#                            Underweight: false
#                            Normal: true
#                            Overweight: false
# 2) Border: "74", "2"    -> BMI: 18.5
#                            Underweight: false
#                            Normal: true  (18.5 is the lower limit)
#                            Overweight: false
# 3) Error: "60", "0"     -> Error: invalid input

print("--- Problem 6: Body Mass Index (BMI) ---")

UNDERWEIGHT_LIMIT = 18.5
OVERWEIGHT_LIMIT = 25.0

weight_text = input("Enter the weight in kilograms: ").strip()
height_text = input("Enter the height in meters: ").strip()

weight_is_number = weight_text.replace(".", "", 1).isdigit()
height_is_number = height_text.replace(".", "", 1).isdigit()

if not weight_is_number or not height_is_number:
    print("Error: invalid input")
elif float(weight_text) <= 0.0 or float(height_text) <= 0.0:
    print("Error: invalid input")
else:
    weight_kg = float(weight_text)
    height_m = float(height_text)

    bmi = weight_kg / (height_m * height_m)

    # The categories use the real BMI, not the rounded one
    is_underweight = bmi < UNDERWEIGHT_LIMIT
    is_normal = UNDERWEIGHT_LIMIT <= bmi < OVERWEIGHT_LIMIT
    is_overweight = bmi >= OVERWEIGHT_LIMIT

    print(f"BMI: {round(bmi, 2)}")
    print(f"Underweight: {str(is_underweight).lower()}")
    print(f"Normal: {str(is_normal).lower()}")
    print(f"Overweight: {str(is_overweight).lower()}")

print()


# ==================================================
# CONCLUSIONES
# ==================================================
# Los enteros y los flotantes se usan juntos en cálculos reales, como pagar
# horas trabajadas (float) o contar números (int). Las comparaciones generan
# booleanos, y esos booleanos permiten tomar decisiones con if. Validar los
# rangos y evitar las divisiones entre cero previene resultados sin sentido
# y errores en el programa. Aprendí a combinar condiciones con and, or y not,
# y a guardar el resultado en una variable booleana antes de usarlo. Estos
# patrones se repiten en problemas de nómina, descuentos y préstamos.


# ==================================================
# REFERENCES
# ==================================================
# References:
# 1) Python documentation - Built-in Types: Numeric Types - int, float, complex
# 2) Python documentation - Boolean type - bool
# 3) Matthes, E. Python Crash Course (numbers and if statements)
# 4) Real Python - Numbers in Python
# 5) Class notes of the programming course (understanding_numbers.py and
#    understanding_if_statements.py).
