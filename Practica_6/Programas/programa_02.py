#Escribir un programa con funciones que convierta un número decimal en binario y de binario a decimal.

def decimal_a_binario(decimal):
    binario = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal //= 2
    return binario

def binario_a_decimal(binario):
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[-(i + 1)]) * (2 ** i)
    return decimal

def mostrar_menu():
    print("\n--- Convertidor ---")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")

# Programa principal
opcion = ''
while opcion != '3':
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == '1':
        num = int(input("Ingresa un número decimal: "))
        print("En binario es:", decimal_a_binario(num))

    elif opcion == '2':
        num = input("Ingresa un número binario: ")
        print("En decimal es:", binario_a_decimal(num))

    elif opcion == '3':
        print("Adios")

    else:
        print("Opción ivalida. Intenta de nuevo.")
