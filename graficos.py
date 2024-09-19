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
def graficar(data1, data2, color='b', xlabel='', ylabel='', title='', label='', semilogx=False):
    plt.figure(figsize=(10, 6))
    if semilogx:
        plt.semilogx(data1, data2, linestyle='-', color=color, label=label)
    else:
        plt.plot(data1, data2, linestyle='-', color=color, label=label)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(title)


# Ruta del archivo .txt
# regulacion de carga

vo_5_B_txt = 'Vo5_A.txt'
vo_3_3_B_txt = 'Vo_3_3A.txt'
irl_3_3_B_txt = 'I_RL_3_3_A.txt'
irl_5_B_txt = 'I_RL_5_A.txt'
eficiencia_3_3_B_txt = 'eficiencia3_3A.txt'
eficiencia_5_B_txt = 'eficiencia5A.txt'
regulacion_linea_3_3B_txt = 'regulacion_linea_3_3A.txt'
regulacion_linea_5B_txt = 'regulacion_linea_5A.txt'
ganancia_lazo_5B_txt = 'ganancia_de_lazo_5_B.txt'
ganancia_lazo_3_3B_txt = 'ganancia_de_lazo_3_3_B.txt'
a_modificado_3_3B_txt = 'a_modificado_3_3B.txt'
a_modificado_5B_txt = 'a_modificado_5B.txt'
ganancia_d = 'ganancia_d.txt'
ganancia_c = 'ganancia_c.txt'

# Leer los datos del archivo
tiempo1, Vo_5 = leer_datos(vo_5_B_txt)
tiempo2, Vo_3_3 = leer_datos(vo_3_3_B_txt)
tiempo3, irl_5_B = leer_datos(irl_5_B_txt)
tiempo4, irl_3_3_B = leer_datos(irl_3_3_B_txt)
vin1, eficiencia_3_3B = leer_datos(eficiencia_3_3_B_txt)
vin2, eficiencia_5_B = leer_datos(eficiencia_5_B_txt)
vin3, regulacion_linea_3_3B = leer_datos(regulacion_linea_3_3B_txt)
vin4, regulacion_linea_5B = leer_datos(regulacion_linea_5B_txt)
freq1, ganancia_lazo_5B = leer_datos(ganancia_lazo_5B_txt)
freq2, ganancia_lazo_3_3B = leer_datos(ganancia_lazo_3_3B_txt)
freq3, a_modificado_5B = leer_datos(a_modificado_5B_txt)
freq4, a_modificado_3_3B = leer_datos(a_modificado_3_3B_txt)
freq5, gd = leer_datos(ganancia_d)
freq6, gc = leer_datos(ganancia_c)

# Graficar los datos
graficar(irl_5_B, Vo_5, 'g',
         r'$I_RL$ [A]', r'V_o [V]',
         'Limitador de corriente del regulador A a 5,5V',
         'Proteccion foldback a 5,5V')

graficar(irl_3_3_B, Vo_3_3, 'g',
         r'$I_{RL} [A]$', r'V_o [V]',
         'Limitador de corriente del regulador A a 3,3V',
         'Proteccion foldback a 3,3V')

graficar(vin1, eficiencia_3_3B, 'g',
         r'$V_{in} [V]$', r'Eficiencia [/%]',
         'Eficiencia del regulador A a 3,3V',
         'Eficiencia a 3,3V')

graficar(vin2, eficiencia_5_B, 'g',
         r'$V_{in} [V]$', r'Eficiencia [/%]',
         'Eficiencia del regulador A a 5V',
         'Eficiencia a 5V')

graficar(vin3, regulacion_linea_3_3B, 'g',
         r'$V_{in} [V]$', r'V_o [V]',
         'Regulación de linea del regulador A a 3,3V',
         'Regulación de linea')

graficar(vin4, regulacion_linea_5B, 'b',
         r'$V_{in} [V]$', r'V_o [V]',
         'Regulación de linea del regulador A 5V',
         'Regulación de linea')

graficar(freq1, ganancia_lazo_5B, 'b',
         'Frecuencia [Hz]', 'af [dB]',
         'Ganancia de lazo a 5V regulador B',
         'Ganancia de lazo ', True)

graficar(freq2, ganancia_lazo_3_3B, 'b',
         'Frecuencia [Hz]', 'af [dB]',
         'Ganancia de lazo a 3,3V regulador B',
         'Ganancia de lazo ', True)

graficar(freq3, a_modificado_5B, 'b',
         'Frecuencia [Hz]', 'a modificado [dB]',
         'Ganancia de amplificador modificado a 5V regulador B',
         'Ganancia del amplificador modificado', True)

graficar(freq4, ganancia_lazo_3_3B, 'b',
         'Frecuencia [Hz]', 'a modificado [dB]',
         'Ganancia del amplificador modificado 3,3V regulador B',
         'Ganancia del amplificador modificado', True)


graficar(freq5, gd, 'b',
         'Frecuencia [Hz]', r'A$_{vd}$ [dB]',
         'Ganancia diferencial del par diferencial',
         'Ganancia diferencial', True)

graficar(freq6, gc, 'b',
         'Frecuencia [Hz]', r'A$_{vc}$ [dB]',
         'Ganancia de modo comun del par diferencial',
         'Ganancia de modo comun', True)