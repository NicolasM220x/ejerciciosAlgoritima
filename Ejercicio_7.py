# Ejercicio 7 - Buscar un número en la lista y contar cuántas veces aparece
# Autor: Nicolas Moreno

# Este programa genera una lista de 20 números aleatorios.
# Solicita un número al usuario y muestra cuántas veces aparece en la lista.

import random

# Generar la lista
lista = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", lista)

# Solicitar el número a buscar
numero = int(input("Ingrese el número a buscar: "))

# Contar cuántas veces aparece
veces = lista.count(numero)

# Mostrar resultado
if veces > 0:
    print(f"El número aparece {veces} veces")
else:
    print("Número no encontrado")
