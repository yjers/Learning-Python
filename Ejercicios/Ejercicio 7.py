# Escriba un programa que solicite al usuario una cantidad de dolares y la convierta en euros
# Utilice la relación ValorEuro = (0.885)ValorDolar

print("\n----Conversion de Dolar a Euros----")

# asignar las variables para la solucion del ejercicio
ValorDolar = float (input("Ingrese la cantidad de dolares: "))
ValorEuro = 0.885 * ValorDolar


print(f"La cantidad de {ValorDolar}$ a euro es {ValorEuro}€")