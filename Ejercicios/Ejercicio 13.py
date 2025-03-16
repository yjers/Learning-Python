import random
participantes = ["Luis", "Rafael", "Diego", "Carlos", "Rodrigo", "Steven", "Jose", "Miguel", "Luka", "Jorge", "Mike"]

primer_ganador = random.choice(participantes)
segundo_ganador = random.choice(participantes)
tercer_ganador = random.choice(participantes)

print(f"El primer ganador {primer_ganador} y se lleva una licuadora")
print(f"El segundo ganador {segundo_ganador} y se lleva una freidora de aire")
print(f"El tercer y ultimo ganador {tercer_ganador} y se lleva una refrigeradora")


