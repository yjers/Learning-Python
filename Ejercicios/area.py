# Crea un programa que calcule el área de un círculo dado su radio. El radio debe ser una variable. Usa una constante para representar pi y muestra el resultado con dos decimales

print("Calcular el area de un circulo")

numero_radio = float (input("Ingrese el radio del circulo: "))
calculo_area = 3.14 * numero_radio ** 2

print(f"El numero pi es {calculo_area:.2f}")