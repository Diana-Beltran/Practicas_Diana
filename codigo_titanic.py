import pandas as pd 
titanic_df = pd.read_csv('titanic.csv')

""" Dimensiones del DataFrame """

#print("Dimensiones del DataFrame :",titanic_df.shape)
#print("Nombres de columnas: ", titanic_df.columns) 
#print("El numero total de datos que contiene es: ", titanic_df.size)
#print("Índices de las filas:", titanic_df.index.tolist())
#print("El tipo de datos de las columnas es: ", type(titanic_df.columns))
'''Las primeras 10 columans'''
#print(titanic_df.head(10))
"""Las ultimas 10 columnas"""
#print(titanic_df.tail(10))
pasajero_148= titanic_df[titanic_df['PassengerId']== 148]
#print(pasajero_148)
filas_pares = titanic_df[titanic_df.index % 2 == 0 ]
#print(filas_pares)
nombres_primera_clase = titanic_df[titanic_df['Pclass'] ==1] ['Name'].sort_values()
#print(nombres_primera_clase)
#print(titanic_df.columns)

total_pasajeros = titanic_df.shape[0]
sobrevivientes = (titanic_df['Survived'] == 1).sum() / total_pasajeros * 100
no_sobrevientes = 100 - sobrevivientes
#print(f"El porcentaje de sobrevivientes es: {sobrevivientes:.2f}%")
#print(f"El porcentaje de no sobrevivientes es: {no_sobrevientes:.2f}%")
#print(titanic_df.Age)
porcentaje_por_clase = titanic_df.groupby('Pclass')['Survived'].mean() * 100
#print(porcentaje_por_clase)
#print(titanic_df.Age)

titanic_df = titanic_df.dropna(subset=['Age'])
#print(titanic_df.Age)

""" Filtramos en puras mujeres"""
mujeres = titanic_df[titanic_df['Sex'] == 'female'] 
""" Con el metodo mean, encontramos la media """
edad_media_mujeres_por_clase = mujeres.groupby('Pclass')['Age'].mean()
#print("La edad media de las mujeres por claes es:" )
#print(edad_media_mujeres_por_clase)

titanic_df['MenorEdad'] = titanic_df['Age'] < 18 
#print(titanic_df.MenorEdad)



# Agrupamos por clase y condición de edad, y calculamos porcentaje de sobrevivencia
porcentaje = titanic_df.groupby(['Pclass', 'MenorEdad'])['Survived'].mean() * 100
print(porcentaje)

