import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
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
""" Informacion del pasajero 148 """
pasajero_148= titanic_df[titanic_df['PassengerId']== 148]
#print(pasajero_148)
""" Las filas pares """
filas_pares = titanic_df[titanic_df.index % 2 == 0 ]
#print(filas_pares)


""" Los nombres de las personas que iban en primera clase """
nombres_primera_clase = titanic_df[titanic_df['Pclass'] ==1] ['Name'].sort_values()
#print(nombres_primera_clase)


#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

titanic_df = pd.read_csv('titanic.csv')

""" Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron"""
total_pasajeros = titanic_df.shape[0]
sobrevivientes = (titanic_df['Survived'] == 1).sum() / total_pasajeros * 100
no_sobrevientes = 100 - sobrevivientes
#print(f"El porcentaje de sobrevivientes es: {sobrevivientes:.2f}%")
#print(f"El porcentaje de no sobrevivientes es: {no_sobrevientes:.2f}%")

""" CODIGO DE LA GRAFICA DE BARRAS """

estado = ['Sobrevivientes', 'No sobrevivientes']
porcentajes = [sobrevivientes, no_sobrevientes]

plt.figure(figsize=(12,6))
plt.bar(estado, porcentajes ,width=0.4, color=['pink','brown'])
plt.title("Porcentaje de Sobrevivientes y No Sobrevivientes")
plt.xlabel('Estado')
plt.ylabel('Porcentaje (%)')
plt.ylim(0,100)
plt.show()
#%%

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
titanic_df = pd.read_csv('titanic.csv')
""" Mostrar por pantalla el porcenjate de personas que sobrevivieron en cada clase """
porcentaje_por_clase = titanic_df.groupby('Pclass')['Survived'].mean() * 100
#print(porcentaje_por_clase)

""" CODIGO DE LA GRAFICA"""

sns.barplot(x=porcentaje_por_clase.index, y=porcentaje_por_clase.values, palette='pastel')
plt.title("Porcentaje de Sobrevivientes por Clase")
plt.xlabel("Clase")
plt.ylabel("Porcentaje de Sobrevivientes (%)")
plt.ylim(0, 100)
plt.show()
#%%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
titanic_df = pd.read_csv('titanic.csv')

""" Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase"""
titanic_df = titanic_df.dropna(subset=['Age'])
#print(titanic_df.Age)

""" Filtramos en puras mujeres"""
mujeres = titanic_df[titanic_df['Sex'] == 'female'] 
""" Con el metodo mean, encontramos la media """
edad_media_mujeres_por_clase = mujeres.groupby('Pclass')['Age'].mean()
#print("La edad media de las mujeres por claes es:" )
#print(edad_media_mujeres_por_clase)


""" CODIGO DE LA GRAFICA"""

sns.barplot(x=edad_media_mujeres_por_clase.index, y=edad_media_mujeres_por_clase.values, palette='pastel')
plt.title("Edad Media de Mujeres por Clase")
plt.xlabel("Clase")
plt.ylabel("Edad Media")
plt.ylim(0, titanic_df['Age'].max()) 
plt.show()

#%%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
titanic_df = pd.read_csv('titanic.csv')
titanic_df['MenorEdad'] = titanic_df['Age'] < 18 
#print(titanic_df.MenorEdad)


""" Mostrar por pantalla el porcentaje de menores y mayores de edad que
sobrevivieron en cada clase."""
# Agrupamos por clase y condición de edad, y calculamos porcentaje de sobrevivencia
porcentaje = titanic_df.groupby(['Pclass', 'MenorEdad'])['Survived'].mean() * 100
#print(porcentaje)

""" CODIGO DE LA GRAFICA """

# Convertimos 'porcentaje' a DataFrame para que Seaborn pueda graficar
porcentaje = porcentaje.reset_index()
sns.barplot(data=porcentaje, x='Pclass', y='Survived', hue='MenorEdad', palette='pastel')
plt.title("Porcentaje de Sobrevivientes por Clase y Edad")
plt.xlabel("Clase")
plt.ylabel("Porcentaje de Sobrevivientes (%)")
plt.ylim(0, 100)
plt.legend(title="¿Menor de edad?")
plt.show()
