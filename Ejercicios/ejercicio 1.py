# Ejercicio 1

print("\nIngresa los siguientes datos del usuario:")
nombre_usuario = str (input("Ingrese el nombre del usuario: "))
edad_usuario = float (input("Ingrese la edad del usuario: "))
peso_usuario = float (input("Ingrese el peso del usuario en kg: "))
altura_usuario = float (input("Ingrese la altura del usuario en m: "))

imc = (peso_usuario / altura_usuario ** 2)
if imc < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc < 25:
    clasificacion = "Peso normal"
elif 25 <= imc < 30:
    clasificacion = "Sobrepeso"

else:
    clasificacion = "Obesidad"

nombre_mayus = nombre_usuario.upper()
cantidad_a = nombre_usuario.lower().count('a')

print("\n-----Resultados-----")
print(f"\nHola! {nombre_mayus}\nTienes {edad_usuario} años\nPesas un total de: {peso_usuario}\nAltura: {altura_usuario}\nTu masa corporal es de {imc:.2f} ({clasificacion})")

