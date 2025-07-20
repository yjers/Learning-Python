'''
Escriba un programa en Python que implemente el “Juego de las Ruedas”. Para esto genere
aleatoriamente una lista de 15 elementos donde cuatro elementos deben decir “Rueda” y
los otros once, “X”.
Luego el programa deberá pedirle al jugador que ingrese por teclado índices entre 0 y 14
(validar). Asuma que el jugador siempre ingresa índices distintos. Si el índice ingresado por
el usuario corresponde al de una “Rueda”, gana $1000. El jugador tiene siete intentos para
hallar las cuatro “Ruedas”. En cada intento muestre por pantalla el número total de
“Ruedas” encontradas hasta el momento. Si el jugador encuentra las cuatro “Ruedas” se
gana un carro. El juego termina cuando encuentra las cuatro “Ruedas” o ha usado todos los
intentos.
Al final muestre el premio que recibe el jugador (cantidad de dólares o la palabra “carro” si
encontró las cuatro ruedas).
'''
import random as rd # importamos la libreria random
elemList = ['Rueda']*4 + ['X']*11 # ['Rueda', 'Rueda', 'Rueda', 'Rueda', 'X', 'X','X',...]
rd.shuffle(elemList) # Revolver los elementos de la lista
dinero = 0 # primero va empezar con $0
intentos = 7 # numeros intentos
listRueda = [] # lista vacia para almacenar cada vez que el usuario encuentre las 4 ruedas
while intentos != 0 and len(listRueda) != 4:
    indices = input("[-] Ingrese un indices entre 0 y 14: ") # El usuario debe ingresar indices entre 0 y 14
    if indices.isdigit() and 0<=int(indices)<=14: # validar que el indice ingrese por el usuario este entre 0 y 14
        if elemList[int(indices)]  == 'Rueda': # valida si el indice que el usuario ingresa es igual a la posicion donde se encuentra la palabra 'Rueda'
            listRueda.append('Rueda') # Si cumple lo va agregar a la lista de rueda
            print(f"[-] Ruedas encontradas: {len(listRueda)}") # Mostrar la cantidad de rueda que encontro por cada vuelta
            dinero += 1000
            intentos -=1
            print(f"[-] Numeros intentos: {intentos}")
        else:
            print(f"[-] No encontrastes nada | Ruedas encontradas: {len(listRueda)}") # Mostrar que el len de lista  ya que no encontro nada
            intentos -=1
            print(f"[-] Numeros intentos: {intentos}")
    else:
        print("[-] Vuelva a ingresar un indice entre 0 y 14") # valida que debe ingresar de nuevo el indice
if len(listRueda) == 4:
    print(f"[-] Felicidades Ganastes el carro y ${dinero}") # Mostrara que gano el carro ya que el len  de la lista tendra 4 elementos
else:
    if dinero == 0: # Mostrara que no gano nada ya que adivino 0 ruedas
        print("[-] Perdiste!")
    else:
        print(f"[-] Encontraste {len(listRueda)} ruedas, por lo tanto te llevas ${dinero} ") # Con las ruedas que encontrar gano cierta gana de dolares
