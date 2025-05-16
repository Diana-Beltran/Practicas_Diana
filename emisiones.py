import pandas as pd
""" Leemos los archivos y las comas la cambiamos por un separador"""
emision_2016 = pd.read_csv('emisiones-2016.csv', sep=';')
emision_2017 = pd.read_csv('emisiones-2017.csv', sep=';')
emision_2018 = pd.read_csv('emisiones-2018.csv', sep=';')
emision_2019 = pd.read_csv('emisiones-2019.csv', sep=';')
#Formamos un DataFrame de los 4 archivos 
emisiones_df = pd.concat([emision_2016, emision_2017, emision_2018, emision_2019], ignore_index=True)
#print(emisiones_df.columns)  # Para verificar que las columnas están correctas


# Lista con las columnas de los días
dias = [f'D{str(d).zfill(2)}' for d in range(1, 32)]

# Columnas que deseamos 
columnas_filtradas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES'] + dias

# Filtrar el DataFrame
emisiones_filtrado = emisiones_df[columnas_filtradas]
#print(emisiones_filtrado)



emisiones_restructurado = pd.melt(
    emisiones_filtrado,
    id_vars=['ESTACION', 'MAGNITUD', 'ANO', 'MES'],
    value_vars=dias,
    var_name='DIA',
    value_name='VALOR'
)

emisiones_restructurado['DIA_NUM'] = emisiones_restructurado['DIA'].str.extract('D(\d{2})').astype(int)
"""Eliminamos la columna que tenia los valores de los dias con el formato D00"""
emisiones_restructurado.drop(columns=['DIA'], inplace=True)
emisiones_restructurado.rename(columns={'DIA_NUM': 'DIA'}, inplace=True)

#emisiones_restructurado['FECHA'] = pd.to_datetime(emisiones_restructurado[['ANO', 'MES', 'DIA']])
print(emisiones_restructurado[['ANO', 'MES', 'DIA']].dtypes)

print(emisiones_restructurado)
