import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def graficar(x, y, xlabel='', ylabel='', title='', ruta_salida=''):

    plt.figure()
    plt.grid()
    # Asumiendo que el archivo tiene columnas llamadas 'dato1', 'dato2', etc.
    plt.plot(x, y)

    # Configuraciones del gráfico
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(ruta_salida)


def graficar_subplots(x, y1, y2, xlabel='', ylabel1='', ylabel2='', title='', ruta_salida=''):
    fig, axs = plt.subplots(1, 2, sharex=True, figsize=(10, 6))

    fig.suptitle(title,  fontsize=16)
    axs[0].grid()
    axs[0].set_xlim([1, 1*10**7])
    axs[0].semilogx(x, y1, 'r')
    axs[0].set_xlabel(xlabel)
    axs[0].set_ylabel(ylabel1)

    axs[1].grid()
    axs[1].set_xlim([1, 1 * 10 ** 7])
    axs[1].semilogx(x, y2, 'b')
    axs[1].set_xlabel(xlabel)
    axs[1].set_ylabel(ylabel2)

    fig.savefig(ruta_salida)


carpeta = 'trazas/checkpoint2'
carpeta_salida = 'imagenes/checkpoint2'

# Cargar los datos desde un archivo de texto, saltando la primera línea
nombres1 = ['time', 'potencia a 3,3', 'vo_3_3']
nombres2 = ['time', 'potencia a 5', 'vo_5']
nombres3 = ['freq', 'magnitud tension', 'fase tension']
nombres4 = ['freq', 'magnitud corriente', 'fase corriente']
nombres5 = ['time', 'respuesta transitoria V']
nombres6 = ['time', 'corriente estabilizada']
nombres7 = ['freq', 'magnitud V sin estabilizar', 'fase V sin estabilizar']
nombres8 = ['freq', 'magnitud I sin estabilizar', 'fase I sin estabilizar']
nombres9 = ['time', 'tension inestable']
nombres10 = ['freq', 'magnitud', 'fase']
nombres11 = ['freq', 'magnitud', 'fase']
nombres12 = ['time', 'Vo']
nombres13 = ['time', 'potencia 3,3', 'tension salida']
nombres14 = ['time', 'potencia 5', 'tension salida']

potencia_B_3_3 = f'{carpeta}/potencia_B_3_3.txt'  # Reemplaza con la ruta de tu archivo
potencia_B_5 = f'{carpeta}/potencia_B_5.txt'
lazo_estabilizado_B_corriente = f'{carpeta}/lazo_estabilizado_B_corriente.txt'
lazo_estabilizado_B_tension = f'{carpeta}/lazo_estabilizado_B_tension.txt'
respuesta_transitoria = f'{carpeta}/respuesta_transitoria_B.txt'
corriente_estabilizada = f'{carpeta}/corriente_transitoria.txt'
lazo_V_sin_estabilizar = f'{carpeta}/lazo_V_sin_estabilizar.txt'
lazo_I_sin_estabilizar = f'{carpeta}/lazo_I_sin_estabilizar.txt'
transtorio_inestable = f'{carpeta}/transitorio_inestable.txt'
ganancia_lazo_tension_A = f'{carpeta}/ganancia_lazo_tension_regA.txt'
lazo_corriente_A = f'{carpeta}/lazo_corriente_regA.txt'
tension_transitoria_A = f'{carpeta}/tensiion_transitoria_regA.txt'
potencia_A_3_3 = f'{carpeta}/potencia_A_3_3.txt'
potencia_A_5 = f'{carpeta}/potencia_A_5.txt'

datos1 = pd.read_csv(potencia_B_3_3, sep='\t', skiprows=1, names=nombres1)
datos2 = pd.read_csv(potencia_B_5, sep='\t', skiprows=1, names=nombres2)
datos3 = pd.read_csv(lazo_estabilizado_B_tension, sep='\t', skiprows=1, names=nombres3)
datos4 = pd.read_csv(lazo_estabilizado_B_corriente, sep='\t', skiprows=1, names=nombres4)
datos5 = pd.read_csv(respuesta_transitoria, sep='\t', skiprows=1, names=nombres5)
datos6 = pd.read_csv(corriente_estabilizada, sep='\t', skiprows=1, names=nombres6)
datos7 = pd.read_csv(lazo_V_sin_estabilizar, sep='\t', skiprows=1, names=nombres7)
datos8 = pd.read_csv(lazo_I_sin_estabilizar, sep='\t', skiprows=1, names=nombres8)
datos9 = pd.read_csv(transtorio_inestable, sep='\t', skiprows=1, names=nombres9)
datos10 = pd.read_csv(ganancia_lazo_tension_A, sep='\t', skiprows=1, names=nombres10)
datos11 = pd.read_csv(lazo_corriente_A, sep='\t', skiprows=1, names=nombres11)
datos12 = pd.read_csv(tension_transitoria_A, sep='\t', skiprows=1, names=nombres12)
datos13 = pd.read_csv(potencia_A_3_3, sep='\t', skiprows=1, names=nombres13)
datos14 = pd.read_csv(potencia_A_5, sep='\t', skiprows=1, names=nombres14)

fase3_unwrap = np.unwrap(np.radians(datos3[nombres3[2]]))
fase3_unwrap = np.degrees(fase3_unwrap)

fase4_unwrap = np.unwrap(np.radians(datos4[nombres4[2]]))
fase4_unwrap = np.degrees(fase4_unwrap)

fase7_unwrap = np.unwrap(np.radians(datos7[nombres7[2]]))
fase7_unwrap = np.degrees(fase7_unwrap)

fase8_unwrap = np.unwrap(np.radians(datos8[nombres8[2]]))
fase8_unwrap = np.degrees(fase8_unwrap)

fase10_unwrap = np.unwrap(np.radians(datos10[nombres10[2]]))
fase10_unwrap = np.degrees(fase10_unwrap)

fase11_unwrap = np.unwrap(np.radians(datos11[nombres11[2]]))
fase11_unwrap = np.degrees(fase11_unwrap)

graficar_subplots(datos3[nombres3[0]], datos3[nombres3[1]], fase3_unwrap, 'Hz', 'dB',
                  'fase ', 'Lazo de tensión estabilizado', f'{carpeta_salida}/lazo_V_B_estabilizado.png')

graficar_subplots(datos4[nombres4[0]], datos4[nombres4[1]], fase4_unwrap, 'Hz', 'dB',
                  'fase ', 'Lazo de corriente estabilizado', f'{carpeta_salida}/lazo_I_B_estabilizado.png')


graficar_subplots(datos7[nombres7[0]], datos7[nombres7[1]], fase7_unwrap, 'Hz', 'dB',
                  'fase ', 'Lazo de tensión sin estabilizar', f'{carpeta_salida}/lazo_V_B_sin_estabilizar.png')

graficar_subplots(datos8[nombres8[0]], datos8[nombres8[1]], fase8_unwrap, 'Hz', 'dB',
                  'fase ', 'Lazo de corriente sin estabilizar', f'{carpeta_salida}/lazo_I_B_sin_estabilizar.png')

graficar_subplots(datos10[nombres10[0]], datos10[nombres10[1]], fase10_unwrap, 'Hz', 'dB',
                  'fase ', 'Lazo de tensión sin estabilizar', f'{carpeta_salida}/lazo_V_A_estabilizado.png')

graficar_subplots(datos11[nombres11[0]], datos11[nombres11[1]], fase11_unwrap, 'Hz', 'dB',
                  'fase ', 'Lazo de corriente sin estabilizar', f'{carpeta_salida}/lazo_I_A_estabilizado.png')


graficar(datos1[nombres1[2]], datos1[nombres1[1]], 'Vo [V]', 'P [W]', 'Potencia disipada por el transistor de paso',
         f'{carpeta_salida}/potencia_B_3_3')

graficar(datos2[nombres2[2]], datos2[nombres2[1]], 'Vo [V]', 'P [W]', 'Potencia disipada por el transistor de paso',
         f'{carpeta_salida}/potencia_B_5')

graficar(10**3*datos5[nombres5[0]], datos5[nombres5[1]], 'Tiempo [ms]', 'Vo [V]', 'Respuesta transitoria de la tensión',
         f'{carpeta_salida}/transitorio_tension')

graficar(10**3*datos6[nombres6[0]], datos6[nombres6[1]], 'Tiempo [ms]', 'I [A]', 'Respuesta transitoria de la corriente',
         f'{carpeta_salida}/transitorio_corriente')

graficar(10**3*datos12[nombres12[0]], datos12[nombres12[1]], 'Tiempo [ms]', 'I [A]',
         'Respuesta transitoria de la tension',
         f'{carpeta_salida}/transitorio_tension_reg_a')

graficar(datos13[nombres13[2]], datos13[nombres13[1]], 'Vo [V]', 'P [W]',
         'Potencia disipada por el transistor de paso', f'{carpeta_salida}/potencia_3_3_A')

graficar(datos14[nombres14[2]], datos14[nombres14[1]], 'Vo [V]', 'P [W]',
         'Potencia disipada por el transistor de paso', f'{carpeta_salida}/potencia_5_A')

plt.figure()
plt.grid()
# Asumiendo que el archivo tiene columnas llamadas 'dato1', 'dato2', etc.
plt.plot(10**3*datos9[nombres9[0]], datos9[nombres9[1]])

# Configuraciones del gráfico
plt.title('Respuesta transitoria inestable')
plt.xlabel('Tiempo [ms]')
plt.ylabel('Vo [V]')
plt.xlim([0, 5])

plt.savefig(f'{carpeta_salida}/transitorio_inestable')