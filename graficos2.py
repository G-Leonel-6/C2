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


# ruta a la carpeta del archivo puede ser relativa (desde la posicion de este archivo) o absoluta
ruta_txt_senoidal = 'trazas/checkpoint4/senoidal.txt'
ruta_txt_triangular = 'trazas/checkpoint4/triangular.txt'
ruta_txt_duty = 'trazas/checkpoint4/variacion_duty.txt'
ruta_txt_cte = 'trazas/checkpoint4/pwm_salida_a_entrada_cte.txt'
# Esta son listas aca pones entre comillas los nombres que van a identificar tus columnas en el dataframe
# los nombres van entre comillas
nombres_senoidal_txt = ['time', 'v']
nombres_pot_3_3_txt = ['time',  'v']

# Leer archivo Excel y TXT, saltando la primer fila y seteando nombre de cada columna
df_senoidal = leer_txt(ruta_txt_senoidal, nombres_senoidal_txt, 1)
df_triangular = leer_txt(ruta_txt_triangular, nombres_senoidal_txt, 1)
df_cte = leer_txt(ruta_txt_cte, nombres_senoidal_txt, 1)
df_duty = leer_txt(ruta_txt_duty, nombres_senoidal_txt, 1)

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 30])
plt.ylabel('V')
plt.xlabel('us')
plt.plot(df_triangular['time']*10**6, df_triangular['v'])
plt.savefig("triangular.png")

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 30])
plt.ylabel('V')
plt.xlabel('us')
plt.plot(df_cte['time']*10**6, df_cte['v'])
plt.savefig("salida_duty_cte.png")

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 60])
plt.ylabel('V')
plt.xlabel('us')
plt.plot(df_duty['time']*10**6, df_duty['v'])
plt.savefig("salida_duty_variando.png")

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 60])
plt.ylabel('V')
plt.xlabel('us')
plt.plot(df_triangular['time']*10**6, df_triangular['v'])
plt.plot(df_senoidal['time']*10**6, df_senoidal['v'])
plt.savefig("triangular_senoidal.png")