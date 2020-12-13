import random

FIGURAS = ['''
+---+
    |
    |
    |
    ===''', '''
+---+
 O  |
    |
    |
    ===''','''
+---+
 O  |
 |  |
    |
    ===''','''
+---+
 O  |
/|  |
    |
    ===''','''
+---+
 O  |
/|\ |
    |
    ===''','''   
+---+
 O  |
/|\ |
/   |
    ===''','''
+---+
 O  |
/|\ |
/ \ |
    ===''']

Lista_palabras = {
    1:["E","L","E","F","A","N","T","E"],
    2:"CTHULHU",
    3:"AUSTRALOPITHECUS",
    4:"MICROSCOPIO",
    5:"VENTILADOR",
    6:"MONSTER"
}
respuesta = []

def obtener_palabra_aleatoria(listado):
    palabra = Lista_palabras[listado]
    return palabra

def actualiza_tablero(letras_incognitas,letras_adivinadas,palabra_secreta):
    if (letras_adivinadas == len(palabra_secreta)):
        print(f"\n felicitaciones!!! ganaste! la palabra era {palabra_secreta}")
        return 1
    else:
        
        return 0

def preguntar_letra():
    letra = input("Ingrese una letra: ")
    letra = letra.upper()
    print("\n\n")
    return letra

def calcula_puntaje(puntaje):
    puntaje = puntaje-20
    print(f"incorrecto!! te quedan {puntaje} puntos")
    print(f"llevas {letras_adivinadas} y faltan {letras_incognitas} por descubrir")
    return puntaje

ganador = 0
j=0
puntaje = 100

print("""*****************************************
*   Bienvenido al juego del ahorcado    *
*****************************************""")

print("A JUGAR!!!")
#key = random.randint(1,6)
key=1
palabra = obtener_palabra_aleatoria(key)
letras_adivinadas = 0
letras_incognitas = len(palabra)
for i in range (0,len(palabra)):
    respuesta.append("_")

while(ganador == 0):
    contador = 0
    print(FIGURAS[j],end=" ")
    print(" ".join(respuesta), end="")
    letra = preguntar_letra()
    for i in range (0,len(palabra)):
        if(letra == palabra[i])and(letra != respuesta[i]):
            respuesta[i] = letra
            letras_adivinadas = letras_adivinadas+1
            letras_incognitas = letras_incognitas-1
        else:
            contador = contador+1
    if(contador == len(palabra)):
        puntaje = calcula_puntaje(puntaje)       
        i=len(palabra) 
        j=j+1
    ganador = actualiza_tablero(letras_incognitas,letras_adivinadas,palabra)
