import tensorflow as tf
import numpy as np
import os

# 1. Datos de entrenamiento
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# 2. Crear el modelo
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=600, verbose=False)
print("Modelo entrenado!")

# 3. Guardar el modelo
if not os.path.exists('conversor/modelos'):
    os.makedirs('conversor/modelos')

modelo.save('conversor/modelos/modelo.keras')
print("Red neuronal guardada en conversor/modelos/modelo.keras")