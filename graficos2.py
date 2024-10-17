import pandas as pd
import matplotlib.pyplot as plt

# Función para leer datos de un archivo Excel
def leer_excel(ruta_excel, nombres, saltar_filas=0):
    """
    Lee un archivo de Excel y devuelve un DataFrame, con opción de saltar filas.

    :param ruta_excel: Ruta del archivo Excel.
    :param saltar_filas: Cantidad de filas a saltar desde el inicio.
    :return: DataFrame con los datos del archivo Excel.
    """
    df_excel = pd.read_excel(ruta_excel, names=nombres, skiprows=saltar_filas)
    return df_excel


# Función para leer datos de un archivo TXT con separador de tabulación (\t)
def leer_txt(ruta_txt, nombres, saltar_filas=0):
    """
    Lee un archivo TXT con separador de tabulación y devuelve un DataFrame, con opción de saltar filas.

    :param ruta_txt: Ruta del archivo TXT.
    :param saltar_filas: Cantidad de filas a saltar desde el inicio.
    :return: DataFrame con los datos del archivo TXT.
    """
    df_txt = pd.read_csv(ruta_txt, sep='\t', names=nombres, skiprows=saltar_filas)
    return df_txt

# Repetir N veces con N cantidad de graficos

# ruta a la carpeta del archivo puede ser relativa (desde la posicion de este archivo) o absoluta
ruta_excel = ''
ruta_txt = ''

# Esta son listas aca pones entre comillas los nombres que van a identificar tus columnas en el dataframe
# los nombres van entre comillas
nombres_excel = []
nombres_txt = []

# Leer archivo Excel y TXT, saltando la primer fila y seteando nombre de cada columna
df_excel = leer_excel(ruta_excel, nombres_excel, saltar_filas=1)
df_txt = leer_txt(ruta_txt, nombres_txt, saltar_filas=1)


# Repetir esta estructura N veces
plt.figure(figsize=(10, 6))
# para agregar otro grafico en el mismo par de ejes  solo hace otro plot
plt.plot(df_excel['nombre col x'], df_excel['nombre col y'], label='aca va la etiqueta', marker='o')
plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.legend()
plt.tight_layout()
plt.show()
# pongan un nombre a la figura y subanla a overleaf
plt.savefig()
