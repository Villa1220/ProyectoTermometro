import tensorflow as tf
import numpy as np
import os

# 1. DATOS
celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

# 2. ARQUITECTURA (4 neuronas x 3 capas)
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=4, input_shape=[1]),
    tf.keras.layers.Dense(units=4),
    tf.keras.layers.Dense(units=1)
])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

# 3. ENTRENAMIENTO 
print("Entrenando (3500 épocas)...")
historial = modelo.fit(celsius, fahrenheit, epochs=3500, verbose=False)
print("¡Entrenamiento finalizado!")

# 4. GUARDAR EL MODELO
if not os.path.exists('conversor/modelos'):
    os.makedirs('conversor/modelos')

modelo.save('conversor/modelos/modelo.keras')
print("✅ Modelo final guardado en conversor/modelos/modelo.keras")