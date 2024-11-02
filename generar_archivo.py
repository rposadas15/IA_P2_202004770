import pandas as pd
import numpy as np

# Generar un arreglo con 1000 valores aleatorios entre -50 y 50
arreglo_aleatorio = np.random.randint(-50, 51, size=1000)  # Incluye 50

# Crear un DataFrame
df = pd.DataFrame(arreglo_aleatorio, columns=["valores"])

# Guardar el DataFrame en un archivo CSV
csv_file_path = 'kmeans.csv'
df.to_csv(csv_file_path, index=False)

print(f'Archivo CSV guardado en: {csv_file_path}')
