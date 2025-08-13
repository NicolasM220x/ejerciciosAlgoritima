# Ejercicio 1 - Saber si un número es par o impar
# Autor: Laura Marin y Nicolas Moreno

# Función para solicitar un número entero al usuario
def ingresarNumero():
    while True:
        try:
            num = int(input("Ingrese el número: "))
            break
        except:
            print("Número no válido")
    return num  

# Función para decidir si el número es par o impar
def decidirPar(n):
    if n % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

# Programa principal
n = ingresarNumero()
decidirPar(n)

