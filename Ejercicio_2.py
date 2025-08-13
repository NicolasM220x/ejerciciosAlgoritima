# Ejercicio 2 - Sumar los números del 1 al n
# Autor: Laura Marin y Nicolas Moreno

# Función para ingresar un número entero
def ingresarNumero():
    while True:
        try:
            num = int(input("Ingrese el número: "))
            break
        except:
            print("Número no válido")
    return num  

# Función para calcular la suma desde 1 hasta n
def sumar(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i  
    return suma

# Programa principal
n = ingresarNumero()
resultado = sumar(n)
print(f"La suma de los números del 1 al {n} es {resultado}")

