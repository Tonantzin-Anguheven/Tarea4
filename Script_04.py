"""Dado un arreglo de 10x10x10 de ceros, establece (i, j, k) = 1 sí, i es impar, j es par y k es primo"""

import numpy as np

"""Paso 1: Definir la función para saber si un número es primo"""

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

"""Paso 2: Crear el arreglo 10x10x10 lleno de ceros"""

Arreglo = np.zeros((10, 10, 10), dtype=int)

"""Paso 3: Crear los índices i, j, k de cada posición del arreglo"""

I, J, K = np.indices((10, 10, 10))

"""Paso 4: Crear máscaras para cada condición"""

I_impar = I % 2 == 1 # Máscara para I
J_par = J % 2 == 0 # Máscara para J
primos = np.array([es_primo(x) for x in range(10)]) # Lista de los primos entre 0 y 9
K_primo = primos[K]  # Máscara para K

"""Paso 5: Combinar todas las máscaras"""

Mascara_Total = I_impar & J_par & K_primo

"""Paso 6: Asignar 1 a las posiciones que cumplen la condición"""

Arreglo[Mascara_Total] = 1

"""Paso 7: Obtener los índices donde se cumple la condición"""

indices = np.array(np.nonzero(Arreglo)).T # Usamos .T para tener cada tupla (i, j, k) en una fila

"""Paso 8: Imprimir resultados"""

print("Coordenadas que cumplen con la condición:")
for indice in indices:
    print(f"{tuple(indice)} = {Arreglo[tuple(indice)]}")

