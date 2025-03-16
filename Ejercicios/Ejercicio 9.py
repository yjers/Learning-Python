# Escriba un programa que permita ver a los estudiantes de la ESPOL si reprobaron una materia o no (en una materia donde la ponderación es 70% teórico y 30% práctico).
# El programa pedirá al usuario ingresar sus notas de primer parcial, sus notas de segundo parcial, su nota de mejoramiento y su nota práctica, todas sobre 100 (como se muestra en el sistema académico).
# Además, pedirá ingresar su numero de faltas y su número total de clases. Recodemos que aquel estudiante que tenga menos de 60/100 de promedio académico o menos 60% de asistencia a clases están quedado.

print("\nCalcular tu nota final:")

primer_parcial = float (input("Ingresa tu nota de primer parcial: "))
segundo_parcial = float (input("Ingresa tu nota de segundo parcial: "))
mejoramiento = float (input("Ingresa tu nota de mejoramiento: "))
practico = float (input("Ingresa tu nota del practico: "))
numero_faltas = int (input("Ingrese su numero total de faltas: "))
total_clases = int (input("Ingrese su numero total de clases: "))


# Operaciones para calcular su nota final
promedio_parcial = max(
    ((primer_parcial + segundo_parcial)/2),
    ((mejoramiento + primer_parcial)/2),
    ((mejoramiento + segundo_parcial)/2)
)

# Asistencia de clases
asistencia = (1- (numero_faltas / total_clases)) * 100

# Porcentaje de cada componente
promedio_porcentaje = promedio_parcial * 0.70
practico_porcentaje = practico * 0.30

# nota final
notafinal = promedio_porcentaje + practico_porcentaje

aprobo_materia = notafinal >= 60 and asistencia >=60
print(f"Realmente aprobo? Su promedio es de {notafinal}", aprobo_materia)
