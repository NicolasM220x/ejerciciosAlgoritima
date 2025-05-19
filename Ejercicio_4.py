# Ejercicio 4 - Calcular la suma de los números pares entre dos números dados
# Autor: Nicolas Moreno

# Función para ingresar un número entero
def ingresarNumero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            return num
        except:
            print("Número no válido. Intente de nuevo.")

# Función para calcular la suma de los números pares entre dos números dados
def sumarPares(ini, fin):
    suma = 0
    for i in range(ini, fin + 1):
        if i % 2 == 0:
            suma += i
    return suma

# Programa principal
print("Cálculo de la suma de pares entre dos números dados")

# Se piden los dos números
inicio = ingresarNumero("Ingrese el primer número: ")
fin = ingresarNumero("Ingrese el segundo número: ")

# Asegurarse que inicio sea menor que fin
if inicio > fin:
    inicio, fin = fin, inicio  # intercambia los valores

# Se llama a la función y se muestra el resultado
resultado = sumarPares(inicio, fin)
print(f"La suma de los números pares entre {inicio} y {fin} es: {resultado}")
