"""
1. Escriba un programa Python, donde declare un diccionario para guardar los nombres
y precios de las distintas frutas (al menos 5).
El programa pedirá el nombre de la fruta y la cantidad que el cliente desea comprar y 
nos mostrará el precio final del pedido a partir de los datos guardados en el diccionario.  
Si la fruta no existe nos dará un error.
Tras cada consulta el programa nos preguntará si queremos hacer otra consulta
"""
# Diccionario con frutas y sus precios por kilo
frutas = {
    'manzana': 20,
    'pera': 30,
    'toronja': 10,
    'fresa': 5,
    'papaya': 2,
}

# Función principal 
def calcular_precio(frutas):
    while True:
        # Pedimos el nombre de la fruta y lo convertimos a minúsculas
        fruta = input("¿Qué fruta deseas comprar? ").lower()

        # Verificamos si la fruta está en el diccionario
        if fruta in frutas:
            # Pedimos la cantidad de kilos que desea comprar
            cantidad = float(input("¿Cuántos kilos deseas comprar? "))
            # Calculamos el precio total
            precio = frutas[fruta] * cantidad
            # Mostramos el precio final
            print(f"El precio total por {cantidad} kg de {fruta} es: ${precio}")
        else:
            
            print("Lo siento, esa fruta no está disponible.")

        # Preguntamos si desea hacer otra consulta
        continuar = input("¿Deseas hacer otra consulta? (s/n): ").lower()
        if continuar != 's':
            # Si responde algo diferente a 's', salimos del bucle
            break
calcular_precio(frutas)


