# Escriba un programa que compruebe si un numero ingreso por teclado es par o impar
num = float (input("Ingrese un numero: "))

if num % 2 == 0:
    print("El numero es par")
elif num % 2 == 1:
    print("El numero es impar")
else:
    print("El numero no es par")