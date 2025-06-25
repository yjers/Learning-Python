# EJERCICIO 1
vocales = ['a', 'e', 'i', 'o', 'u']
consonantes = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ',
    'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
]
def analizar_palabras(frase):
    palabras = frase.split()
    contador_vocales = 0
    contador_consonante=0
    for palabra in palabras:
        primera_letra = palabra[0].lower()
        if primera_letra in vocales:
            contador_vocales +=1
        elif primera_letra in consonantes:
            contador_consonante+=1
    return f"El total de palabra que empieza con una vocal es {contador_vocales}\n El total de palabra que empieza con una consonante es {contador_consonante}"


print(analizar_palabras("A veces, perderse es la mejor manera de encontrarse."))


# EJERCIO 2
def filtra_notas(lst_notas):
    aprobados=[]
    reprobados=[]
    for nota in lst_notas:
        nombre, notas = nota.split("-")
        if int(notas)>=60:
            aprobados.append(f"{nombre}-{nota}")
        else:
            reprobados.append(f"{nombre}-{nota}")
    return f"Lista de aprobados: {aprobados}\nLista de reprobados: {reprobados}"
        
notas = [
    'ana-98', 'carlos-76', 'luisa-88', 'mario-61', 'elena-95',
    'jorge-82', 'valeria-91', 'david-59', 'sofia-100', 'manuel-73',
    'paula-87', 'ricardo-93', 'fernanda-66', 'lucas-90', 'isabel-78',
    'diego-40',
    
]

print(filtra_notas(notas))


    
# EJERCICIO 3
def verificador_codigos(lstcodigos):
    codigos_paises=[]
    for elem in lstcodigos:
        ciudad, codpais = elem.split("-")
        codp=''
        pais=''
        for ch in codpais:
            if ch.isdigit():
                codp+=ch
            elif ch.isalpha():
                pais+=ch
        codigos_paises.append(f"{pais} {codp}")
    return ' '.join(codigos_paises)


l = [
    'GYE-593ECU',   # Guayaquil - Ecuador
    'LIM-51PER',    # Lima - Perú
    'BOG-57COL',    # Bogotá - Colombia
    'MEX-52MEX',    # Ciudad de México - México
    'BUE-54ARG',    # Buenos Aires - Argentina
    'SCL-56CHI',    # Santiago - Chile
    'LPZ-591BOL',   # La Paz - Bolivia
    'MTV-1USA',     # Mountain View - Estados Unidos
    'TOR-1CAN',     # Toronto - Canadá
    'MAD-34ESP',    # Madrid - España
    'PAR-33FRA',    # París - Francia
    'ROM-39ITA',    # Roma - Italia
    'BER-49ALE',    # Berlín - Alemania
    'TKY-81JPN',    # Tokio - Japón
    'SYD-61AUS'     # Sídney - Australia
]

print(verificador_codigos(l))



