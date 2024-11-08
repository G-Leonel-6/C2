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
ruta_txt_vo_buck = 'trazas/checkpoint4/buck_vo.txt'
ruta_txt_il_buck = 'trazas/checkpoint4/buck_il.txt'

# Esta son listas aca pones entre comillas los nombres que van a identificar tus columnas en el dataframe
# los nombres van entre comillas
nombres_senoidal_txt = ['time', 'v']
nombres_pot_3_3_txt = ['time',  'v']

# Leer archivo Excel y TXT, saltando la primer fila y seteando nombre de cada columna
df_senoidal = leer_txt(ruta_txt_senoidal, nombres_senoidal_txt, 1)
df_triangular = leer_txt(ruta_txt_triangular, nombres_senoidal_txt, 1)
df_cte = leer_txt(ruta_txt_cte, nombres_senoidal_txt, 1)
df_duty = leer_txt(ruta_txt_duty, nombres_senoidal_txt, 1)
df_buck_vo = leer_txt(ruta_txt_vo_buck, nombres_senoidal_txt, 1)
df_buck_il = leer_txt(ruta_txt_il_buck, nombres_senoidal_txt, 1)


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
plt.xlim([0, 100])
plt.ylabel('V')
plt.xlabel('us')
plt.plot(df_duty['time']*10**6, df_duty['v'])
plt.savefig("salida_duty_variando.png")

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 100])
plt.ylim([4.7, 7.5])
plt.ylabel('V')
plt.xlabel('us')
plt.plot(df_triangular['time']*10**6, df_triangular['v'], label='Señal triangular generada')
plt.plot(df_senoidal['time']*10**6, df_senoidal['v'], label="Señal senoidal de referencia")
plt.legend()
plt.savefig("triangular_senoidal.png")


plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 9])
plt.ylabel('V')
plt.xlabel('ms')
plt.plot(df_buck_vo['time']*10**3, df_buck_vo['v'])
plt.savefig("buck_vo_transitorio.png")

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([7.5, 7.55])
plt.ylabel('V')
plt.xlabel('ms')
plt.plot(df_buck_vo['time'][300000:]*10**3, df_buck_vo['v'][300000:])
plt.savefig("ripple_tension_buck.png")

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([7.5, 7.55])
plt.ylabel('mA')
plt.xlabel('ms')
plt.plot(df_buck_il['time'][300000:]*10**3, df_buck_il['v'][300000:]*10**3)
plt.savefig("ripple_corriente_buck.png")

plt.ylabel('V')
plt.xlabel('us')
plt.plot(df_triangular['time']*10**6, df_triangular['v'])
plt.plot(df_senoidal['time']*10**6, df_senoidal['v'])
plt.savefig("triangular_senoidal.png")
