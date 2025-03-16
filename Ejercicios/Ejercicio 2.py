user_name = str (input("Ingrese el nombre del usuario: "))

start_a = user_name.lower().startswith('a')
if start_a:
    print("Tu nombre empieza con la letra A")
else:
    print("Tu nombre no empieza con la letra A")

