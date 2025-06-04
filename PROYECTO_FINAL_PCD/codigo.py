#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

""" 
               CARGAMOS NUESTRO ARCHIVO CSV A UN DATAFRAME CON EL METODO READ  DE PANDAS


"""
spotify_df = pd.read_csv('spotify_top_1000_tracks.csv')

""" 
               LIMPIEZA DE NUESTROS DATOS
"""

spotify_df.drop(columns=['id', 'spotify_url'], inplace=True) # Eliminamos las columnas 'id' y 'spotify_url'

"""
               FORMATO DATETIME
"""
# Convertimos la fecha en formato datetime
spotify_df['release_date'] = pd.to_datetime(spotify_df['release_date'], errors='coerce')

# Creamos las nuevas columnas , year, month, day 
spotify_df['year'] = spotify_df['release_date'].dt.year
spotify_df['month'] = spotify_df['release_date'].dt.month
spotify_df['day'] = spotify_df['release_date'].dt.day

# Convertimos  las columnas a enteros, para que se vea mas estetico
spotify_df['year'] = spotify_df['year'].astype('Int64')   
spotify_df['month'] = spotify_df['month'].astype('Int64')
spotify_df['day'] = spotify_df['day'].astype('Int64')



"""     PREGUNTA # 1
                          ¿CUALES SON LOS ARTISTAS CON MAS CANCIONES EN EL TOP 1000
"""

top_artistas = spotify_df['artist'].value_counts().head(10)
sns.set_style("whitegrid")
plt.figure(figsize=(10,6))
sns.barplot(x=top_artistas.values, y=top_artistas.index, palette="crest")
plt.title("Artistas con más canciones en el Top 1000")
plt.xlabel("Número de canciones")
plt.ylabel("Artista")
plt.tight_layout()
plt.show()


"""     PREGUNTA # 2
                          ¿Cómo ha cambiado la popularidad de la música a lo largo del tiempo?

"""


# Agrupar por año  y con el metodo mean de Pandas calculamos la popularidad promedio

popularidad_por_año = spotify_df.groupby('year')['popularity'].mean().reset_index() 

# Ordenarmos los datos por año 
popularidad_por_año = popularidad_por_año.sort_values('year')

# Gráfica de línea
plt.figure(figsize=(10,6))
sns.lineplot(data=popularidad_por_año, x='year', y='popularity', marker='o', color='red')
plt.title("Evolución de la popularidad musical a lo largo del tiempo")
plt.xlabel("Año")
plt.ylabel("Popularidad promedio")
plt.grid(True)
plt.tight_layout()
plt.show()



"""  PREGUNTA # 3
                      ¿Qué décadas están mejor representadas en el Top 1000?

"""

#  Creamos una nueva columna  de decada   

spotify_df['decada'] = (spotify_df['year'] // 10) * 10  

# Contamos las canciones que hay por decada y las ordenamos cronologicamente

canciones_por_decada = spotify_df['decada'].value_counts().sort_index()

#print (canciones_por_decada)       # Imprime el numero total de canciones que hay por decada

# Convertirmos los datos que obtuvimos anteriormente a un DataFrame para graficar, de esta manera es mas sencillo graficar. 
#  
canciones_por_decada_df = canciones_por_decada.reset_index()   # Creamos nuevos indices 
canciones_por_decada_df.columns = ['Decada', 'Cantidad de Canciones']  # Nombramos los indices 
#print(canciones_por_decada_df)     # Imprime el indice, la decada y la cantidad de canciones que hay por decada 

#Gráfica de barras
plt.figure(figsize=(10,6))
sns.set_style("whitegrid")
sns.barplot(data=canciones_por_decada_df, x='Decada', y='Cantidad de Canciones', palette='crest')
plt.title("Canciones por década en el Top 1000 de Spotify")
plt.xlabel("Década")
plt.ylabel("Número de canciones")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


"""   PREGUNTA # 4
                            ¿Existe una duración ideal para una canción popular?

"""


sns.set_style("whitegrid")  # Estilo de la cuadricula 
plt.figure(figsize=(10,6))
sns.scatterplot(data=spotify_df, x='duration_min', y='popularity', alpha=0.6)
plt.title('Relación entre duración de la canción y popularidad')
plt.xlabel('Duración (minutos)')
plt.ylabel('Popularidad')
plt.show()

#   Nos muestra cual es la cancion de duracion maxima 
max_duration = spotify_df['duration_min'].max()
cancion_mas_larga = spotify_df[spotify_df['duration_min'] == max_duration]
#print(cancion_mas_larga[['artist','track_name', 'duration_min', 'popularity']])

#  Nos muestra cual es la cancion con una duracion minima
min_duration = spotify_df['duration_min'].min()
cancion_mas_larga = spotify_df[spotify_df['duration_min'] == min_duration]
#print(cancion_mas_larga[['artist','track_name', 'duration_min', 'popularity']])

# Mostrar las 10 canciones con mayor duración
top_10_largas = spotify_df.sort_values(by='duration_min', ascending=False).head(10)
print(top_10_largas[['artist', 'track_name', 'duration_min', 'popularity']])




"""  PREGUNTA # 5 
                 ¿Qué artistas tienen la mayor popularidad promedio en sus canciones?

"""


# Número mínimo de canciones para filtrar
min_canciones = 5

# Agrupamos por artista, calcular cantidad y popularidad promedio

artistas_pop = spotify_df.groupby('artist').agg(
    canciones=('track_name', 'count'),
    popularidad_promedio=('popularity', 'mean')
).reset_index()

# Filtramos los  artistas con al menos min_canciones canciones
artistas_filtrados = artistas_pop[artistas_pop['canciones'] >= min_canciones]

# Ordenamos  por popularidad promedio descendente y tomar top 10
top10_artistas = artistas_filtrados.sort_values('popularidad_promedio', ascending=False).head(10)

# Gráfica de barras

plt.figure(figsize=(12,6))
sns.barplot(data=top10_artistas, x='popularidad_promedio', y='artist', palette="crest")
plt.title(f'Top 10 artistas con mayor popularidad promedio (min {min_canciones} canciones)', fontsize=16)
plt.xlabel('Popularidad promedio')
plt.ylabel('Artista')
plt.xlim(0, 100)  # popularidad está en rango 0-100
plt.show() 


"""  PREGUNTA # 6 
                ¿Cuáles son los álbumes con más canciones en el top 1000?

"""



# Agrupamos correctamente por álbum y artista
albumes_artistas = spotify_df.groupby(['album', 'artist']).size().reset_index(name='num_canciones')

# Ordenamos  por número de canciones y tomar el top 10
# Utilizamos el by para indicar que columna deseo ordenar
top10_albumes = albumes_artistas.sort_values(by='num_canciones', ascending=False).head(10)  

# Grafica de barras
sns.set_theme(style="whitegrid")  # Estilo cuadricula 
plt.figure(figsize=(12,6))
sns.barplot(data=top10_albumes, x='num_canciones', y='album', palette='crest')
plt.title('Top 10 álbumes con más canciones en el Top 1000 ')
plt.xlabel('Número de canciones')
plt.ylabel('Álbum ')
plt.tight_layout()
plt.show()




""" PREGUNTA # 7 

        ¿Cómo ha cambiado la duración de las canciones a lo largo de los años?
    
"""


# Agrupamos  por año y calculamos la  duración promedio
duracion_por_ano = spotify_df.groupby('year')['duration_min'].mean().reset_index()

# Grafica de linea 
plt.figure(figsize=(12,6))
sns.lineplot(data=duracion_por_ano, x='year', y='duration_min', marker='o', color='teal')
plt.title('Duración promedio de las canciones a lo largo de los años', fontsize=16)
plt.xlabel('Año de lanzamiento')
plt.ylabel('Duración promedio (minutos)')
plt.grid(True)
plt.tight_layout()
plt.show()





"""   PREGUNTA # 8 
                          ¿Hay relación entre el número de canciones de un artista y su popularidad promedio?

"""



# Agrupamos  por artista y calculamos  
artistas_stats = spotify_df.groupby('artist').agg(
    num_canciones=('track_name', 'count'),
    popularidad_promedio=('popularity', 'mean')
).reset_index()

# Grafica de dispersion 
plt.figure(figsize=(10,6))
sns.scatterplot(data=artistas_stats, x='num_canciones', y='popularidad_promedio', alpha=0.6, color='royalblue')
plt.title('Relación entre número de canciones y popularidad promedio por artista', fontsize=14)
plt.xlabel('Número de canciones')
plt.ylabel('Popularidad promedio')
plt.grid(True)
plt.tight_layout()
plt.show()






