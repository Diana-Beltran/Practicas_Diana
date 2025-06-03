"""
2. Escriba un programa Python utilizando funciones, que genere una lista de n número aleatorios
(en cualquier rango) y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado (n),
y los valores sean los cuadrados de los números aleatorios generados.
Al final imprima el contenido de la lista de aleatorios y los valores del diccionario.

"""

import random 

def generar_lista(n):
    lista = []  
    for _ in range(n):
        numero = random.randint(1, 100)  # Número aleatorio entre 1 y 100
        lista.append(numero)  # Agregamos el número a la lista
    return lista


def crear_diccionario(lista):
    diccionario = {}  # Diccionario vacío
    for i in range(len(lista)):
        diccionario[i + 1] = lista[i] ** 2  
    return diccionario


def funcion_principal():
    n = int(input("¿Cuántos números aleatorios deseas generar? "))
    numeros = generar_lista(n)  # Generamos la lista
    diccionario = crear_diccionario(numeros)  # Creamos el diccionario

    # Mostramos los resultados
    print("\nLista de números aleatorios:")
    print(numeros)

    print("\nDiccionario con los cuadrados:")
    print(diccionario)


funcion_principal()
