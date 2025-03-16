# Escriba un programa en el que el usuario ingrese la temperatura en Fahrenheit y haga la conversion de grados Fahrenheit a grados centigrados.

grados_fahrenheit = float (input("Ingrese la temperatura en Fahrenheit: "))
fahrenheit_centigrados = (5 * (grados_fahrenheit - 32))/9

print(f"Resultado de la conversion de grados Fahrenheit a grados Centigrados es igual a: {fahrenheit_centigrados:.2f} ")