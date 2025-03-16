import math

pi = math.pi

print("Calcular el area de un circulo y el volumen de una esfera")

circulo_radio = float (input("Ingreso el radio del circulo: "))
esfera_radio = float (input("Ingreso el radio de la esfera: "))

circulo_area = pi * circulo_radio ** 2
esfera_volumen = (4 * pi * esfera_radio ** 3)/3

print(f"El Area del circulo es igual a: {circulo_area:.2f} ")
print(f"El Volumen de la esfera es igual a: {esfera_volumen:.3f}")
