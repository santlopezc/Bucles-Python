numero = int(input("Ingrese un numero: "))
factorial = 1
if numero < 0:
    print("No se puede calcular el factorial de un numero negativo")
elif numero == 0:
    print("El factorial de 0 es 1")
else:
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es {factorial}")