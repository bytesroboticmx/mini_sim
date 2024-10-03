#Descripcion: Simulador de partículas en 2D con rebote en las paredes
#Autor: Dr. Aldo Gonzalez Vazquez
#Version: 1.0
#Licencia: MIT
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definimos algunas constantes
NUM_PARTICULAS = 10  # Número de partículas
ANCHO = 10           # Ancho del área de simulación
ALTO = 10            # Alto del área de simulación
RADIO = 0.5          # Radio de cada partícula
VELOCIDAD_MAX = 0.1  # Velocidad máxima

# Creamos un estado inicial para las partículas
np.random.seed(42)  # Para reproducibilidad
posiciones = np.random.rand(NUM_PARTICULAS, 2) * [ANCHO, ALTO]
velocidades = (np.random.rand(NUM_PARTICULAS, 2) - 0.5) * VELOCIDAD_MAX * 2

# Función para actualizar la posición de las partículas
def actualizar(frame):
    global posiciones, velocidades
    posiciones += velocidades

    # Comprobar colisiones con las paredes y rebotar
    for i in range(NUM_PARTICULAS):
        if posiciones[i, 0] - RADIO < 0 or posiciones[i, 0] + RADIO > ANCHO:
            velocidades[i, 0] *= -1
        if posiciones[i, 1] - RADIO < 0 or posiciones[i, 1] + RADIO > ALTO:
            velocidades[i, 1] *= -1

    # Actualizar posiciones de los puntos en la animación
    scatter.set_offsets(posiciones)

# Configurar la figura para la animación
fig, ax = plt.subplots()
ax.set_xlim(0, ANCHO)
ax.set_ylim(0, ALTO)
ax.set_aspect('equal')
scatter = ax.scatter(posiciones[:, 0], posiciones[:, 1], s=100 * RADIO, c='blue')

# Crear la animación
ani = FuncAnimation(fig, actualizar, frames=200, interval=50)

# Mostrar la animación
plt.show()
