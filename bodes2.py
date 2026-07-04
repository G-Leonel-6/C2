import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ruta = "trazas/vref_B.txt"
valor_1 = np.loadtxt(ruta, delimiter='\t', skiprows=1)

tiempo_1 = valor_1[:, 0]
amplitud_1 = valor_1[:, 1]

plt.figure()
plt.grid()
#plt.xlim([4.2, 4.25])
plt.ylim([0, 1.4])

plt.ylabel("Tensión [V]")
plt.xlabel("Tiempo [ms]")
plt.plot(tiempo_1*1000, amplitud_1, label=f"Señal de referencia empleada")
#plt.plot(tiempo_2*1000, amplitud_2, label=f"Transitorio de corriente del inductor \npara una RLOAD de 635$\Omega$ ")
plt.legend()
plt.show()
