# Escriba un programa en el que el usuario una cantidad de segundos y se le impriman en pantalla la cantidad de horas, minutos y segundos

cantidad_segundos = float (input("Ingrese el tiempo en segundos: "))

segundos_horas = cantidad_segundos / 3600
segundos_minutos = (cantidad_segundos % 3600) / 60
segundos = cantidad_segundos % 60

print(f"\nEn horas: {segundos_horas:.2f}h\nEn minutos: {segundos_minutos:.2f}min\nEn segundos: {segundos:.2f}s")