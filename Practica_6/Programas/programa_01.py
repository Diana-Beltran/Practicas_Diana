#Escribir un programa que reciba una cadena de caracteres y 
# devuelva un diccionario con cada palabra que contiene y su frecuencia. 
# Escribir otra función que reciba el diccionario generado con la función anterior y 
# devuelva una tupla con la palabra más repetida y su frecuencia.


def contar_frecuencia_palabras(cadena):
    # replace, hace la funcion de remplazar las comas y puntos por espacios vacios.
    cadena = cadena.replace(",", "").replace(".", "")
    # Convierte el texto a minúsculas
    cadena = cadena.lower()
    # El texto ingresado lo convierte a una lista
    palabras = cadena.split()
    
    # Contar frecuencias
    frecuencias = {}
    for i  in palabras:
        if i in frecuencias:
            frecuencias[i] += 1
        else:
            frecuencias[i] = 1
            
    return frecuencias

def palabra_mas_repetida(diccionario):
    mayor = ""
    frecuencia_mayor = 0

    for palabra in diccionario:
        if diccionario[palabra] > frecuencia_mayor:
            mayor = palabra
            frecuencia_mayor = diccionario[palabra]

    return (mayor, frecuencia_mayor)


# Programa principal

texto = input("Ingresa un texto: ")
frecuencias = contar_frecuencia_palabras(texto)
print("Frecuencias:", frecuencias)

resultado = palabra_mas_repetida(frecuencias)
palabra = resultado[0]
cantidad = resultado[1]

print("Palabra más repetida:", palabra)
print("Frecuencia:", cantidad)




