"""El código determina cuáles peces sobreviven dado un arreglo numpy de sus ubicaciones en un espacio 3D y
considerando que el pez más grande se come al más chico, si es que están en el mismo espacio."""

"""Paso 1: # Establecer el arreglo de numpy de las posiciones de los 10 peces"""

import numpy as np
locs = np . array ([
[0 ,0 ,0] ,
[1 ,1 ,2] ,
[0 ,0 ,0] ,
[2 ,1 ,3] ,
[5 ,5 ,4] ,
[5 ,0 ,0] ,
[5 ,0 ,0] ,
[0 ,0 ,0] ,
[2 ,1 ,3] ,
[1 ,3 ,1]
])
print("Ubicación de los 10 peces:", locs)

"""Paso 2: Crear un generador de números random para tener los pesos de los peces"""

generator = np.random.default_rng(1010)
weights = abs(generator.normal(size = 10)) # Solo se agregó "abs" al código dado para tener valores absolutos, ya que hablamos de pesos.
print ("Pesos de los 10 peces:", weights )

"""Paso 3: Descartar peces fuera de rango"""
#Hay peces fuera del rango de la pecera 5x5x5. Esos peces se considerarán como muertos por estar fuera de agua
#solo se trabajará con los peces dentro del cubo

Peces_en_pecera = np.all((locs >= 0) & (locs < 5), axis=1) # Se descartan a los peces que están fuera de la pecera
locs_válidas = locs[Peces_en_pecera] # Nos quedamos solo con las ubicaciones de peces dentro para compararlos
weights_válidos = weights[Peces_en_pecera] # Nos quedamos con los pesos de los peces dentro
Índices_válidos = np.where(Peces_en_pecera)[0] # Y con sus respectivos índices

"""Paso 4: Buscar los peces en la misma locación y comparar sus pesos, el de mayor peso sobrevive."""

locs_tuplas = [tuple(loc) for loc in locs_válidas] # Convertimos las locaciones válidas en tuplas
Peces_sobrevivientes = {} # Generamos un diccionario vacío para ir guardando a los peces sobrevivientes por locación (llave) e índice (valor)

for i, loc in enumerate(locs_tuplas): # Itera todas las locaciones válidas convertidas en tuplas
    weight = weights_válidos[i] # Guadamos el peso de esa iteración
    Índices_originales = Índices_válidos[i] # Y el índice para comparar adelante 
    if loc not in Peces_sobrevivientes: # Si esa locación no está en el diccionario de peces sobrevivientes...
        Peces_sobrevivientes[loc] = Índices_originales # Se agrega junto con su índice del arreglo original
    else: # Pero si esa locación ya está, entonces hay dos peces ahí y deben competir
        Índice_existente = Peces_sobrevivientes[loc] # Obtenemos el índice del pez que ya estaba en esa locación 
        if weights[Índices_originales] > weights[Índice_existente]: # Y comparamos el que acabamos de encontrar con el que ya estaba. Usamos el arreglo weights porque usamos los índices originales 
            Peces_sobrevivientes[loc] = Índices_originales # Si el que acabamos de encontrar tiene un peso mayor, lo reemplazamos y este es el nuevo pez sobreviviente.

"""Paso 5: Tomar los índices originales de los peces sobrevivientes e imprimir los resultados."""

Índices = sorted(Peces_sobrevivientes.values()) # Tomamos los índices (valores) del diccionario Peces_sobrevivientes y los ordenamos

print("Los peces sobrevivientes son los número:", Índices)
print("Ubicados en las locaciones:", locs[Índices])
print("Y sus respectivos pesos son:", weights[Índices])





        