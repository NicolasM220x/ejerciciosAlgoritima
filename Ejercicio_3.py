# Ejercicio 3 - Mostrar los números pares del 100 al 1000
# Autor: Nicolas Moreno

# Este programa imprime todos los números pares del 100 al 1000 y cuenta cuántos hay

suma = 0  # Contador de pares

for i in range(100, 1000):
    if i % 2 == 0:
        print(i)
        suma += 1

print(f"Total de números pares entre 100 y 1000: {suma}")
