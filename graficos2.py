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
ruta_txt_imin_36_buck = 'trazas/checkpoint4/Buck_Vin_36_imin.txt'
ruta_txt_imax_36_buck = 'trazas/checkpoint4/Buck_Vin_36_imax.txt'
ruta_txt_imin_12_buck = 'trazas/checkpoint4/Buck_Vin_12_imin.txt'
ruta_txt_imax_12_buck = 'trazas/checkpoint4/Buck_Vin_12_imax.txt'
ruta_txt_corriente_min = 'trazas/checkpoint4/Buck_corriente_caso_min'

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
df_buck_12_imax = leer_txt(ruta_txt_imax_12_buck, nombres_senoidal_txt, 1)
df_buck_12_imin = leer_txt(ruta_txt_imin_12_buck, nombres_senoidal_txt, 1)
df_buck_36_imax = leer_txt(ruta_txt_imax_36_buck, nombres_senoidal_txt, 1)
df_buck_36_imin = leer_txt(ruta_txt_imin_36_buck, nombres_senoidal_txt, 1)
df_buck_corriente_caso_min = leer_txt(ruta_txt_corriente_min, nombres_senoidal_txt, 1)

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 30])
plt.ylabel('Tensión [V]')
plt.xlabel('Tiempo [us]')
plt.plot(df_triangular['time']*10**6, df_triangular['v'])
plt.savefig("triangular.png")

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 30])
plt.ylabel('Tensión [V]')
plt.xlabel('Tiempo [us]')
plt.plot(df_cte['time']*10**6, df_cte['v'])
plt.savefig("salida_duty_cte.png")

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 100])
plt.ylabel('Tensión [V]')
plt.xlabel('Tiempo [us]')
plt.plot(df_duty['time']*10**6, df_duty['v'])
plt.savefig("salida_duty_variando.png")

plt.figure(figsize=(10,8))
plt.grid()
plt.xlim([0, 100])
plt.ylim([4.7, 7.5])
plt.ylabel('Tensión [V]')
plt.xlabel('Tiempo [us]')
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


fig, axs = plt.subplots(1, 2, sharey=True)
axs[0].grid()
axs[1].grid()
axs[0].set_xlabel("Tiempo [ms]")
axs[1].set_xlabel("Tiempo [ms]")
axs[0].set_ylabel("Vo [V]")
axs[0].plot(df_buck_12_imin['time']*10**3, df_buck_12_imin['v'], "-r", label="Tensión de salida con corriente \n"
                                                                             " mínima y Vin 12V")
axs[1].plot(df_buck_12_imax['time']*10**3, df_buck_12_imax['v'], label="Tensión de salida con corriente \n "
                                                                       "máxima y Vin 12V")
fig.legend()
fig.savefig("vo_vin12.png")

fig, axs = plt.subplots(1, 2, sharey=True)
axs[0].grid()
axs[1].grid()
axs[0].set_xlabel("Tiempo [ms]")
axs[1].set_xlabel("Tiempo [ms]")
axs[0].set_ylabel("Vo [V]")
axs[0].plot(df_buck_36_imin['time']*10**3, df_buck_36_imin['v'], "-r",label="Tensión de salida con corriente \n"
                                                                       "mínima y Vin 36V")
axs[1].plot(df_buck_36_imax['time']*10**3, df_buck_36_imax['v'], label="Tensión de salida con corriente \n"
                                                                       "máxima y Vin 36V")
fig.legend()
fig.savefig("vo_vin36.png")

plt.figure()
plt.grid()
plt.ylabel("Corriente [mA]")
plt.xlabel("Tiempo [ms]")
plt.ylim([0,25])
plt.xlim([8,8.05])
plt.plot(df_buck_corriente_caso_min['time']*10**3, df_buck_corriente_caso_min['v']*10**3
         , label="Ripple de corriente del inductor \nen el caso mínima corriente")
plt.legend()
plt.savefig("ripple_corriente_buck.png")

plt.figure()
plt.grid()
plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo [ms]")
plt.ylim([6.15,6.55])
plt.xlim([9.5,9.55])
plt.plot(df_buck_12_imin['time']*10**3, df_buck_12_imin['v'], label="Ripple de Tensión del inductor \n"
                                                                           "en el caso de mínima corriente")
plt.legend()
plt.savefig("ripple_tension_buck.png")