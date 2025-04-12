"""Este código resuelve una dinámica en la cual empareja a personas que tienen la menor diferencia
de puntaje en su test de personalidad :)"""

"""Paso 1: importar la biblioteca de numpy e itertools para generar combinaciones"""

import numpy as np # Importamos la biblioteca de numpy
from itertools import combinations # Importar combinaciones

"""Paso 2: Guardar las variables que refieren a los valores mínimo y máximo (no incluído), 
así como el tamaño de la muestra"""

min_value = 0 
high_value = 101
sample_size = 10

"""Paso 3: Crear un generador de números aleatorios"""

generator = np.random.default_rng(1010) # Generador de números aleatorios con una semilla
data = np.round(generator.uniform(low=min_value, high=high_value, size=sample_size)) #Generador de números aleatorios con distribución uniforme

"""Paso 4: Generar una matriz de numpy con las posibles parejas de estos 10 puntajes"""

Parejas = list(combinations(data, 2)) # Combinaciones posibles por pares de los números aleatorios 
Pares = np.array(Parejas) # Hacemos un arreglo 2D con estas posibles parejas

"""Paso 5: Generar un arreglo con la diferencia absoluta de los puntajes de cada pareja"""

Diferencias = np.abs(Pares[:, 0] - Pares[:, 1]) # Toma el primer puntaje de cada pareja y le resta su respectivo segundo puntaje, pero lo expresa en cantidad absoluta
Arreglo = np.array(Diferencias) # Convertimos las diferencias de puntaje de cada pareja en un arreglo de numpy

"""Paso 6: Ordenar el arreglo de diferencias de menor a mayor"""

Índices_ordenados = np.argsort(Arreglo) # Primero ordenamos los índices
Pares_ordenados = Pares[Índices_ordenados] # Después ordenamos los pares
Diferencias_ordenadas = Arreglo[Índices_ordenados] # Finalmente, ordenamos las diferencias de menor a mayor

"""Paso 7: Iterar sobre los pares ordenados para encontrar las parejas con menor diferencia y que no se repita 
una persona en otra pareja"""

Lista_de_parejas = [] # Guardamos una lista de parejas
Índices_visitados = set() # Guardamos un conjunto para evitar que las personas se repitan

for i in range(len(Pares_ordenados)): # Se recorre por las parejas ordenadas
    Par = Pares_ordenados[i]
    Individuo1, Individuo2 = Par # Los dos individuos que forman la pareja

    # Verificamos si ya hemos emparejado a los individuos
    if Individuo1 not in Índices_visitados and Individuo2 not in Índices_visitados:
        Lista_de_parejas.append(Par) # Si no, agregamos a la pareja
        Índices_visitados.add(Individuo1) # Y a los individuos en el set
        Índices_visitados.add(Individuo2)

    # Si ya tenemos 5 parejas (porque son 10 personas, máximo 5 parejas), detenemos la búsqueda
    if len(Lista_de_parejas) == 5:
        break

"""Resultados"""

print("Números aleatorios generados:", data)
print("Arreglo de las diferencias absolutas entre todas las posibles parejas:", Arreglo)
print("Las 5 parejas con la menor diferencia son:")
for idx, Par in enumerate(Lista_de_parejas, 1): # Finalmente una oportunidad para usar enumerate :)
    print(f"Pareja {idx}: {Par[0]} y {Par[1]} ; Diferencia: {np.abs(Par[0] - Par[1])}")








