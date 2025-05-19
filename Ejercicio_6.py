# Ejercicio 6 - Buscar un número en una lista de 20 números aleatorios
# Autor: Nicolas Moreno

# Este programa genera una lista de 20 números aleatorios entre 1 y 100.
# Luego solicita al usuario un número y busca si está presente en la lista.

import random

# Generar la lista
lista = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", lista)

# Pedir número al usuario
numero = int(input("Ingrese el número a buscar: "))

# Verificar si el número está en la lista
if numero in lista:
    # Mostrar la primera posición donde se encuentra
    print(f"Número encontrado en la posición: {lista.index(numero)}")
else:
    print("Número no encontrado")
