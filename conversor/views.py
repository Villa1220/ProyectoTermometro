from django.shortcuts import render
import tensorflow as tf
import numpy as np
import os

# --- CONFIGURACIÓN DE LA IA ---

# 1. Construimos la ruta donde está guardado el modelo
# Esto busca la carpeta 'modelos' dentro de la carpeta actual 'conversor'
ruta_modelo = os.path.join(os.path.dirname(__file__), 'modelos/modelo.keras')

# 2. Cargamos el modelo UNA SOLA VEZ al iniciar el servidor
# Esto evita que la web sea lenta recargando la IA en cada clic
print("Cargando Inteligencia Artificial desde:", ruta_modelo)
try:
    modelo = tf.keras.models.load_model(ruta_modelo)
    print("¡Modelo cargado y listo para usar!")
except Exception as e:
    print(f"Error cargando el modelo (Revisa que ejecutaste entrenar.py): {e}")
    modelo = None

# --- VISTA (LÓGICA DE LA PÁGINA) ---

def index(request):
    resultado = None
    celsius = "" # Para guardar lo que escribió el usuario
    
    # Si el usuario envió el formulario (dio clic al botón)
    if request.method == 'POST':
        celsius = request.POST.get('celsius')
        
        if modelo is not None:
            try:
                # 1. Convertir texto a número decimal
                val_c = float(celsius)
                
                # 2. Preparar el dato para TensorFlow (necesita un arreglo)
                entrada = np.array([val_c])
                
                # 3. PREDECIR
                prediccion = modelo.predict(entrada)
                
                # 4. Extraer el valor numérico del resultado
                resultado = float(prediccion[0][0])
                
            except ValueError:
                resultado = "Error: Debes ingresar un número válido."
        else:
            resultado = "Error: El modelo de IA no se cargó correctamente."

    # Enviamos los datos al HTML para que los muestre
    return render(request, 'index.html', {'resultado': resultado, 'celsius': celsius})