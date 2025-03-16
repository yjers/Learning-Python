# Utiizando los datos del Ejercicio 7
# Escriba un programa que solicite una cantidad de euros y la convierta en dolares

print("\nConvertir de Dolares a Euros")
ValorEuro = float (input("Ingrese la cantidad de euros: "))
ValorDolar = ValorEuro / 0.885

print(f"La cantidad de euros {ValorEuro}€ a dolar es: {ValorDolar:.1f}$")
