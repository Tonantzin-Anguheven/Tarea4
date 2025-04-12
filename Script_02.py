"""El programa asigna ceros a los tres primeros estudiantes que saquen menos de 60 puntos"""

"""Paso 1: Importar numpy y generar un arreglo de puntajes"""

import numpy as np
Puntajes = np.array([35, 50, 60, 58, 72, 99, 85, 69, 73, 56]) # Puntajes en el orden en que entregaron el examen

"""Paso 2: Buscar los primeros 3 puntajes que cumplen la condición Puntajes < 60"""

Puntajes_Menores_60 = np.where(Puntajes < 60)[0] # Ubica los índices donde se cumple la condición Puntajes < 60
Puntajes_Menores = Puntajes_Menores_60[:3] # Extrae los primeros 3 índices que cumplen con la condición

"""Paso 3: Sustituir los primeros 3 puntajes < 60 por 0"""

Puntajes[Puntajes_Menores] = 0 # Indica sustituir el valor posicionado en esos índices por el 0 

"""Resultado"""

print("Lista de calificaciones según el orden en que entregaron el examen", Puntajes)


