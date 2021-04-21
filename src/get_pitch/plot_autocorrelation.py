import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

signal, fm = sf.read('') #falta grabar y añadir la señal sonora
t = np.arange(0, len(signal)) /fm

plt.figure()

#Plot de la señal temporal del segmento de voz
plt.subplot(211)
plt.plot(t, signal)
plt.title('Señal temporal')
plt.xlabel("t(s)")
plt.grid()

#Plot de la autocorrelación del segmento de voz
#Utilizamos la funcion plt.acorr de la bibiloteca malplotlib.pyplot
#Nos devuelve una grafica de la autocorrelación de la señal
plt.subplot(212)
plt.acorr(signal, maxlags = 20) #maxlags = len(signal)-1 ??
plt.title('Autocorrelación')
plt.xlabel("\tau(s)")
plt.grid()

plt.show()