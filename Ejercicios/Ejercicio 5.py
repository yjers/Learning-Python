# Escribe un programa que pregunte al usuario una cantidad a invertir, el interes anual y el numero de años, y muestra por patalla el capital obtenido en la inversion

print("Ejercicio 5:")
capital_inicial = float (input("Ingrese la cantidad a invertir: "))
tasa_interes = float (input("Ingrese el interes anual: "))
periodo_ahorro = float (input("Ingrese el numero de años: "))

capital_final = capital_inicial * (1+tasa_interes) ** periodo_ahorro

print(f"Capital Obtenido de la Inversion: {capital_final}")