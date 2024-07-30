import pandas as pd
import numpy as np

# Crear un DataFrame a partir de los datos del archivo datos_meteorologicos.csv

df = pd.read_csv("datos_meteorologicos.csv")

# Realizar observaciones iniciales de los datos con Pandas

head = df.head() 

tail = df.tail() 

tendencia = df.describe()

columnas = df.columns

nulos = df.isnull().sum()

# Convertir las columnas del DataFrame en arrays de NumPy

temperatura = df["Temperatura"].to_numpy()

precipitacion = df["Precipitación"].to_numpy()

humedad = df["Humedad"].to_numpy()

# Identificar los datos faltantes en los arrays, y reemplazarlos por el promedio de los valores del respectivo array

# Datos faltantes isnan()

temp_nulo = np.isnan(temperatura)

precip_nulo = np.isnan(precipitacion)

humedad_nulo = np.isnan(humedad)

# Identificar el promedio de cada array

temp_promedio = np.nanmean(temperatura)

precip_promedio = np.nanmean(precipitacion)

humedad_promedio = np.nanmean(humedad)

# Remplazar valores nulos por promedios

temperatura[temp_nulo] = temp_promedio

precipitacion[precip_nulo] = precip_promedio

humedad[precip_nulo] = humedad_promedio

# Realizar análisis estadísticos básicos

temperatura_promedio = np.nanmean(temperatura)
print("El promedio de temperatura es:", temperatura_promedio)

precipitacion_total = np.sum(precipitacion)
print("Precipitacion total: ", precipitacion_total)

humedad_maxima = np.max(humedad)
print("Humedad maxima es:", humedad_maxima)

# Fecha mas calurosa

mas_calor = np.max(temperatura)
print("El dia que mas temperatura hubo fueron: ", mas_calor)

# Registro correspondiente a la temperatura más alta
registro_mas_caluroso = np.where(temperatura == mas_calor)[0][0]
print("registro numero: ",registro_mas_caluroso)

# Fecha correspondiente al registro más caluroso
fecha_mas_calurosa = df.iloc[registro_mas_caluroso]['Fecha']
print("la fecha mas calurosa es el: ", fecha_mas_calurosa)

# Fecha mas fria

fecha_mas_fria = df.iloc[np.where(temperatura == np.min(temperatura))[0][0]]['Fecha']
print("la fecha mas fria fue: ", fecha_mas_fria)

# Crear un DataFrame con los resultados
resultados = pd.DataFrame({
    'Metrica': ['Temperatura Promedio', 'Precipitación Total', 'Humedad Máxima', 'Día Más Caluroso', 'Día Más Frío'],
    'Valor': [temp_promedio, precipitacion_total, humedad_maxima, fecha_mas_calurosa, fecha_mas_fria]
})

# Guardar los resultados en un nuevo archivo CSV
resultados.to_csv('Resultados análisis meteorológico.csv', index=False)