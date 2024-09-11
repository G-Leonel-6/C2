import numpy as np
import matplotlib.pyplot as plt


# Función para leer los datos del archivo usando numpy.loadtxt
def leer_datos(archivo):
    # Utilizamos numpy.loadtxt para leer los datos, saltando la primera línea
    data = np.loadtxt(archivo, delimiter='\t', skiprows=1)

    # Dividimos las dos columnas en data1 y data2
    data1 = data[:, 0]  # Primera columna
    data2 = data[:, 1]  # Segunda columna

    return data1, data2


# Función para graficar los datos
def graficar(data1, data2, color='b', xlabel='', ylabel='', title='', label=''):
    plt.figure(figsize=(10, 6))
    plt.plot(data1, data2, linestyle='-', color=color, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(title)


# Ruta del archivo .txt
# regulacion de carga

vo_5_B_txt = 'Vo5_B.txt'
vo_3_3_B_txt = 'V03_3B.txt'
irl_3_3_B_txt = 'I_RL_3_3_B.txt'
irl_5_B_txt = 'I_RL_5_B.txt'
eficiencia_3_3_B_txt = 'eficiencia3_3B.txt'
eficiencia_5_B_txt = 'eficiencia5B.txt'
regulacion_linea_3_3B_txt = 'regulacion_linea_3_3B.txt'
regulacion_linea_5B_txt = 'regulacion_linea_5B.txt'


# Leer los datos del archivo
tiempo1, Vo_5 = leer_datos(vo_5_B_txt)
tiempo2, Vo_3_3 = leer_datos(vo_3_3_B_txt)
tiempo3, irl_5_B = leer_datos(irl_5_B_txt)
tiempo4, irl_3_3_B = leer_datos(irl_3_3_B_txt)
vin1, eficiencia_3_3B = leer_datos(eficiencia_3_3_B_txt)
vin2, eficiencia_5_B = leer_datos(eficiencia_5_B_txt)
vin3, regulacion_linea_3_3B = leer_datos(regulacion_linea_3_3B_txt)
vin4, regulacion_linea_5B = leer_datos(regulacion_linea_5B_txt)

# Graficar los datos
graficar(irl_5_B, Vo_5, 'b',
         r'$I_RL$ [A]', r'V_o [V]',
         'Limitador de corriente del regulador B a 5,5V',
         'Proteccion foldback a 5,5V')

graficar(irl_3_3_B, Vo_3_3, 'b',
         r'$I_{RL} [A]$', r'V_o [V]',
         'Limitador de corriente del regulador B a 3,3V',
         'Proteccion foldback a 3,3V')

graficar(vin1, eficiencia_3_3B, 'b',
         r'$V_{in} [V]$', r'Eficiencia [/%]',
         'Eficiencia del regulador B a 3,3V',
         'Eficiencia a 3,3V')

graficar(vin2, eficiencia_5_B, 'b',
         r'$V_{in} [V]$', r'Eficiencia [/%]',
         'Eficiencia del regulador B a 5V',
         'Eficiencia a 5V')

graficar(vin3, regulacion_linea_3_3B, 'b',
         r'$V_{in} [V]$', r'V_o [V]',
         'Regulación de linea del regulador B a 3,3V',
         'Regulación de linea')

graficar(vin4, regulacion_linea_5B, 'b',
         r'$V_{in} [V]$', r'V_o [V]',
         'Regulación de linea del regulador B 5V',
         'Regulación de linea')
