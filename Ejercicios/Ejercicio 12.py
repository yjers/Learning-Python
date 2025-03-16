from traceback import print_tb

user_correo = input("Ingrese el correo ESPOL: ")
valid_1 = user_correo.endswith("espol.edu.ec")
valid_2 = user_correo[0].isalpha()
valid_3 = user_correo.count("@")==1
nombre_usuario = user_correo.split('@')[1]
valid_4 = nombre_usuario.lower() != "espol"


print(nombre_usuario)

validacion = valid_1 and valid_2 and valid_3 and valid_4
print(f"El correo {user_correo} pertence a la Espol", validacion)