# %%

import os
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from IPython.display import Audio, display

# Resolución automática de la ruta del archivo

carpeta_local = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
ruta_directa = os.path.join(carpeta_local, 'AnalisisTexto16.wav')

# =====================================================
# PUNTO 4: Carga de datos y visualización de parámetros
# =====================================================

audio, sr = sf.read(ruta_directa)

print("=== DESARROLLO DEL PUNTO 4 =========================")
print("Vector de la señal segmentada:")
print(audio)
print('Largo array:', len(audio))
print('Frecuencia de Muestreo:', sr)
print('Duración:', len(audio) / sr)
print("===================================================\n")

# ==================================================================
# %%PUNTO 5: Impresión de la señal sonora (Gráfico de forma de onda)
# ==================================================================

print("======DESARROLLO DEL PUNTO 5 (Gráfico de forma de onda)======")
plt.plot(audio)
plt.show()

# ==============================================================================
# PUNTO 6: Reproducción de la señal original
# ==============================================================================
print("• Punto 6: Audio Original ( 16 bits)")
display(Audio(audio, rate=sr))

# ==============================================================================
# PUNTO 7: Modificación de la frecuencia de muestreo (Duración y tono)
# ==============================================================================

print("\n• Punto 7a: Mayor duración (Menor velocidad / Tono grave)")
display(Audio(audio, rate=sr * 0.3))

print("\n• Punto 7b: Menor duración (Mayor velocidad / Tono agudo)")
display(Audio(audio, rate=sr * 2))

# ==============================================================================
# PUNTO 8: Modificación de la profundidad de bits (Cuantización)
# ==============================================================================

print("\n• Punto 8: Baja calidad de audio (Conversión a 8 bits)")
y = (audio * 2**3).astype(np.int8)
display(Audio(y, rate=sr))
# %%