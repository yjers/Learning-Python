# Escriba un programa para validar una cdedula.
# Las condiciones son:
# 1. La cedula debe contener solo números
# 2. La cedula debe tener 10 digitos exactos
# 3. La cedula deber ser de Gye (09), empezar con estos digitos
# 4. Solicite la cédula y presente un mensaje personalizado

print("VALIDAR CEDULA")

numero_cedula = input("Ingrese el numero de cedula: ")
valid_1 = numero_cedula.isdigit()
valid_2 = len(numero_cedula) == 10
valid_3 = numero_cedula.startswith("09")

validacion = valid_1 and valid_2 and valid_3

print("La cedula esta correcta?", validacion)