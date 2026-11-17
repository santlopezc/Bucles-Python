cantidad = int(input("Cuantos numeros multiplicaras?"))
producto = 1
for i in range(cantidad):
    numero = float(input("Ingrese un numero: "))
    producto *= numero
print(f"El producto total es: {producto}")