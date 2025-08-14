# Ejercicio 5 - Ordenar cinco números de mayor a menor
# Autor: Laura Marin y Nicolas Moreno

# Este programa solicita cinco números al usuario y luego los ordena de mayor a menor

numeros = []
print("Ingrese 5 números:")
for _ in range(5):
    num = int(input("Número: "))
    numeros.append(num)

# Ordenamos la lista en orden descendente
numeros.sort(reverse=True)

# Mostramos el resultado
print("Números ordenados de mayor a menor:", numeros)

