import matplotlib.pyplot as plt
import numpy as np

file1 = "trazas/checkpoint5/bode_sin_compensar.txt"
GananciaLazo = np.loadtxt(file1, delimiter='\t', skiprows=2, dtype=str, max_rows=2101)
GananciaLazo2 = np.loadtxt(file1, delimiter='\t', skiprows=2104, dtype=str)

frecuencia = GananciaLazo[:, 0].astype(float)  # Convertir frecuencia a float
modulo_fase = GananciaLazo[:, 1]  # Extraer la columna de (módulo, fase)
frecuencia2 = GananciaLazo2[:, 0].astype(float)  # Convertir frecuencia a float
modulo_fase2 = GananciaLazo2[:, 1]  # Extraer la columna de (módulo, fase)

# Función para limpiar y extraer módulo y fase
def extraer_valores(val):
    try:
        modulo_str, fase_str = val.split(',')
        modulo = float(modulo_str[1:].replace('dB', '').strip())  # Limpiar y convertir módulo
        fase = float(fase_str.replace('°', '').replace(')', '').strip())  # Limpiar y convertir fase
        return modulo, fase
    except ValueError:
        print(f"Error al procesar el valor: {val}")
        return None, None  # Devuelve None si hay un error

# Aplicar la función para extraer valores de módulo y fase
modulo_fase_limpios = [extraer_valores(val) for val in modulo_fase]
modulo_fase_limpios2 = [extraer_valores(val) for val in modulo_fase2]

# Filtrar los valores válidos (donde no hubo errores)
modulo_fase_limpios = [val for val in modulo_fase_limpios if val[0] is not None]
modulo_fase_limpios2 = [val for val in modulo_fase_limpios2 if val[0] is not None]

# Separar los módulos y fases en arrays
modulo = np.array([val[0] for val in modulo_fase_limpios])
fase = np.array([val[1] for val in modulo_fase_limpios])
modulo2 = np.array([val[0] for val in modulo_fase_limpios2])
fase2 = np.array([val[1] for val in modulo_fase_limpios2])
fig, ax1 = plt.subplots()

# Graficar el módulo en el eje Y izquierdo
ax1.semilogx(frecuencia[:len(modulo)], modulo, label='Ganancia de la respuesta en \nfrecuencia para 8 Ohms', color='brown')
ax1.semilogx(frecuencia2[:len(modulo2)], modulo2, label='Ganancia de la respuesta en \nfrecuencia para 635 Ohms', color='red')
ax1.set_xlabel('f [Hz]')
ax1.set_ylabel('Ganancia [dB]', color='brown')
ax1.tick_params(axis='y', labelcolor='brown')
ax1.grid()
plt.legend(loc="lower left")

# Crear un segundo eje Y para la fase

fase = np.unwrap(np.radians(fase))  # Desenvuelve la fase
fase = np.degrees(fase)
fase2 = np.unwrap(np.radians(fase2))  # Desenvuelve la fase
fase2 = np.degrees(fase2)

ax2 = ax1.twinx()
ax2.semilogx(frecuencia[:len(fase)], fase, "--", label='Fase del circuito compensado', color='b')
ax2.semilogx(frecuencia2[:len(fase2)], fase2, "--", label='Fase del circuito compensado', color='g')
ax2.set_ylabel('Fase [°]', color='b')
ax2.tick_params(axis='y', labelcolor='b')
plt.legend(loc="center left")

# Limitar el rango de frecuencias hasta 10^5 Hz
#ax1.set_ylim([-50,80])
ax1.set_xlim([frecuencia[0], 1e6])
"""
# Buscar la frecuencia donde la ganancia cruza 0 dB
indices_cercanos_0dB = np.where(np.abs(modulo) < 0.5)[0]  # Buscar los índices donde la ganancia está cerca de 0 dB
if len(indices_cercanos_0dB) > 0:
    cruce_ganancia_0dB = frecuencia[indices_cercanos_0dB[0]]  # Frecuencia donde la ganancia cruza 0 dB
    fase_en_cruce_0dB = fase[indices_cercanos_0dB[0]]  # Fase en esa frecuencia
    margen_de_fase =fase_en_cruce_0dB  # Margen de fase

    # Marcar el cruce de 0 dB y el margen de fase
    ax2.axhline(y=fase_en_cruce_0dB, color='black', linestyle='--', label=f'Margen de fase: {margen_de_fase:.2f}°')
    plt.legend()
    ax1.axvline(x=cruce_ganancia_0dB, color='black', linestyle='--', label=f'Cruce 0dB: {cruce_ganancia_0dB:.2f} Hz')

"""

plt.tight_layout()  # Asegurarse de que todo quede bien distribuido
plt.show()