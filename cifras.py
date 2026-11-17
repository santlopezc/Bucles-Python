
numero = int(input("Escriba un número entero: "))

if numero > 0:
    copianumero = numero
    contadorcifras = 0
    sumacifras = 0

    while copianumero > 0:
        cifra = copianumero % 10
        copianumero = copianumero // 10
        sumacifras = sumacifras + cifra
        contadorcifras = contadorcifras + 1

    print("La cantidad de cifras de:", numero)
    print("Son:", contadorcifras)
    print("La sumatoria es:", sumacifras)

else:
    print("No es un número entero positivo")
