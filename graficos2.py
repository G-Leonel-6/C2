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
ruta_excel_1 = 'trazas/checkpoint3/foldback_3_3.xlsx'
ruta_excel_2 = 'trazas/checkpoint3/foldback_3_3_discretas.xlsx'
ruta_txt_I_3_3 = 'trazas/checkpoint1/I_RL_3_3_B.txt'
ruta_txt_V_3_3 = 'trazas/checkpoint1/V03_3B.txt'

ruta_excel_3 = 'trazas/checkpoint3/foldback_5.xlsx'
ruta_excel_4 = 'trazas/checkpoint3/foldback_5_discretas.xlsx'
ruta_txt_V_5 = 'trazas/checkpoint3/vo5.txt'
ruta_txt_I_5 = 'trazas/checkpoint3/I_Rl_5.txt'

ruta_excel_5 = 'trazas/checkpoint3/Libro1.xlsx'
ruta_excel_6 = 'trazas/checkpoint3/Libro2.xlsx'
ruta_txt_pot_5 = 'trazas/checkpoint2/potencia_B_5.txt'
ruta_txt_pot_3 = 'trazas/checkpoint2/potencia_B_3_3.txt'

# Esta son listas aca pones entre comillas los nombres que van a identificar tus columnas en el dataframe
# los nombres van entre comillas
nombres_excel_3_3 = ['Vo(V)', 'I(A)']
nombres_excel_3_3_discretas = ['I(A)', 'Vo(V)']
nombres_txt_I = ['time', 'I(A)']
nombres_txt_V = ['time', 'V(V)']

nombres_excel_5 = ['Vo(V)', 'I(A)']
nombres_excel_5_discretas = ['I(A)', 'Vo(V)', '']
nombres_txt_I_5 = ['time', 'I(A)']
nombres_txt_V_5 = ['time', 'V(V)']

nombres_pot_5 = ['Vo', 'pot']
nombres_pot_3 = ['Vo', 'pot']
nombres_pot_5_txt = ['time', 'pot', 'vo']
nombres_pot_3_3_txt = ['time', 'pot', 'vo']

# Leer archivo Excel y TXT, saltando la primer fila y seteando nombre de cada columna
df_excel_3_3 = leer_excel(ruta_excel_1, nombres_excel_3_3, saltar_filas=0)
df_excel_3_3_discretas = leer_excel(ruta_excel_2, nombres_excel_3_3_discretas, saltar_filas=0)
df_txt_I = leer_txt(ruta_txt_I_3_3, nombres_txt_I, saltar_filas=1)
df_txt_V = leer_txt(ruta_txt_V_3_3, nombres_txt_V, saltar_filas=1)

df_excel_5 = leer_excel(ruta_excel_3, nombres_excel_5, saltar_filas=0)
df_excel_5_discretas = leer_excel(ruta_excel_4, nombres_excel_5_discretas, saltar_filas=0)
df_txt_I_5 = leer_txt(ruta_txt_I_5, nombres_txt_I, saltar_filas=1)
df_txt_V_5 = leer_txt(ruta_txt_V_5, nombres_txt_V, saltar_filas=1)

df_excel_pot5 = leer_excel(ruta_excel_5, nombres_pot_5, saltar_filas=1)
df_excel_pot3 = leer_excel(ruta_excel_6, nombres_pot_3, saltar_filas=1)
df_txt_pot_5 = leer_txt(ruta_txt_pot_5, nombres_pot_5_txt, saltar_filas=1)
df_txt_pot_3_3 = leer_txt(ruta_txt_pot_3, nombres_pot_3_3_txt, saltar_filas=1)

# Repetir esta estructura N veces
plt.figure(figsize=(10, 6))
plt.grid()
# para agregar otro grafico en el mismo par de ejes  solo hace otro plot
plt.plot(df_excel_3_3['I(A)'], df_excel_3_3['Vo(V)'], label='Medición con reostato', marker='o')
plt.plot(df_excel_3_3_discretas['I(A)'], df_excel_3_3_discretas['Vo(V)'], label='Medición resistencias\n discretas', marker='o')
plt.plot(df_txt_I['I(A)'], df_txt_V['V(V)'], label='Simulación')
plt.title('Comparación simulación con mediciones a 3,3V')
plt.xlabel('Corriente [A]')
plt.ylabel('Tensión [V]')
plt.legend()
plt.tight_layout()
# pongan un nombre a la figura y subanla a overleaf
plt.savefig('Foldback_3_3.png')

plt.figure(figsize=(10, 6))
plt.grid()
# para agregar otro grafico en el mismo par de ejes  solo hace otro plot
plt.plot(df_excel_5['I(A)'], df_excel_5['Vo(V)'], label='Medición con reostato', marker='o')
plt.plot(df_excel_5_discretas['I(A)'], df_excel_5_discretas['Vo(V)'], label='Medición resistencias\n discretas', marker='o')
plt.plot(df_txt_I_5['I(A)'], df_txt_V_5['V(V)'], label='Simulación')
plt.title('Comparación simulación con mediciones a 5V')
plt.xlabel('Corriente [A]')
plt.ylabel('Tensión [V]')
plt.legend()
plt.tight_layout()
# pongan un nombre a la figura y subanla a overleaf
plt.savefig('Foldback_5.png')

plt.figure(figsize=(10, 6))
plt.grid()
# para agregar otro grafico en el mismo par de ejes  solo hace otro plot
plt.plot(df_excel_pot5['Vo'], df_excel_pot5['pot'], label='Potencia disipada en la medición', marker='o')
plt.plot(df_txt_pot_5['vo'], df_txt_pot_5['pot'], label='Simulación')
plt.title('Comparación simulación con mediciones a 5V')
plt.xlabel('Vo [V]')
plt.ylabel('Potencia disipada [W]')
plt.legend()
plt.tight_layout()
# pongan un nombre a la figura y subanla a overleaf
plt.savefig('potencia_5.png')

plt.figure(figsize=(10, 6))
plt.grid()
# para agregar otro grafico en el mismo par de ejes  solo hace otro plot
plt.plot(df_excel_pot3['Vo'], df_excel_pot3['pot'], label='Potencia disipada en la medición', marker='o')
plt.plot(df_txt_pot_3_3['vo'], df_txt_pot_3_3['pot'], label='Simulación')
plt.title('Comparación simulación con mediciones a 3,3V')
plt.xlabel('Vo [V]')
plt.ylabel('Potencia disipada [W]')
plt.legend()
plt.tight_layout()
# pongan un nombre a la figura y subanla a overleaf
plt.savefig('potencia_3.png')