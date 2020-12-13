# -*-encoding: utf-8 -*-
##############################################################################
# Programa: Gato                                                             #
# Proposito: Juego del gato                                                  #
# Autor: Mauricio Roman Ruiz bárcenas                                        #
# Fecha: 15/07/2019                                                          #
# Correo: mauro_ruiz2001@hotmail.com                                         #
#         crostow.ewinkeiton@gmail.com                                       #
##############################################################################


# Importamos metodos necesarios para la ejecucion del programa
import time
import sys
import os
# declaramos las variablea y listas para el funcionamiento del programa
datos = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
ficha = 0
jugadas = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
tiradas = 0


# Metodo que da la bienvenida y permite la eleccion de la ficha
def Bienvenida():
    global ficha
    print("""*****************************************
             *   Bienvenido al juego del gato        *
             *   con que ficha deseas jugar          *
             *          X       0                    *
             *****************************************""")
    ficha = input('''
          preciona 1 si quieres jugar con X
          preciona 2 si quieres jugar con 0
          ''')
    if ficha == "1":
        ficha = "X"
    elif ficha == "2":
        ficha = "0"
    else:
        print("No elegiste correctamente vualve a intentarlo")
        time.sleep(2)
        os.system("clear")
        Bienvenida()


# Mandamos a imprimir el tablero en la terminal y le pasamos como parametro
# la lista en la cual se van guardando las tiradas
def tablero(tirada):
    print(str(tirada[0][0])+"|"+str(tirada[0][1])+"|"+str(tirada[0][2]))
    print("-----")
    print(str(tirada[1][0])+"|"+str(tirada[1][1])+"|"+str(tirada[1][2]))
    print("-----")
    print(str(tirada[2][0])+"|"+str(tirada[2][1])+"|"+str(tirada[2][2]))


# Se manda la informacion de como se debe tirar y se verifica que sea correcta
# la informacion que se da
def tirada():
    global tiradas
    print("la judada se da por medio de coordenadas")
    print("tiradas disponibles")
    print(jugadas)
    '''
    00 01 02
    10 11 12
    20 21 22
    '''
    while True:
        try:
            coordenada = input("Tirada: ")
            break
        except:
            print("la cordenada debe ser solo numerica")
            print("intenta de nuevo")
            pass
    verificar_jugada(coordenada)


# Se verifica que la jugada sea permitida en caso contraio se vuelve a mandar
# la informacion para poder tirar correctamente
def verificar_jugada(coordenada):
    coo = str(coordenada)
    if coo in jugadas:
        agregar(coo)
    else:
        print("no es una jugada valida vuelve a tirar")
        tirada()


# Se agrega la tirada a la lista donde se guardan las tiradas
# Cambio de turno de jugador
# Se guarda la tirada y se manda a imprimir el tablero
def agregar(coo):
    global tiradas
    global ficha
    datos[int(coo[0])][int(coo[1])] = ficha
    tablero(datos)
    jugadas.remove(coo)
    if ficha == "X":
        ficha = "0"
    elif ficha == "0":
        ficha = "X"
    tiradas = tiradas + 1
    if tiradas == 9:
        print("juego terminado")
    else:
        verificar_ganador()
        tirada()


# Verificamos si se cumple alguna condicion de ganador
def verificar_ganador():
    for i in range(3):
        if ((datos[0][i] == "X" and
             datos[1][i] == "X" and
             datos[2][i] == "X") or
            (datos[i][0] == "X" and
             datos[i][1] == "X" and
             datos[i][2] == "X")):
            print("gana el jugador con la ficha  \"X\"")
            time.sleep(5)
            sys.exit()
        elif ((datos[0][0] == "X" and
               datos[1][1] == "X" and
               datos[2][2] == "X") or
              (datos[0][2] == "X" and
               datos[1][1] == "X" and
               datos[2][0] == "X")):
            print("gana el jugador con la ficha  \"X\"")
            time.sleep(5)
            sys.exit()

        elif ((datos[0][i] == "0" and
               datos[1][i] == "0" and
               datos[2][i] == "0") or
              (datos[i][0] == "0" and
               datos[i][1] == "0" and
               datos[i][2] == "0")):
            print("gana el jugador con la ficha  \"0\"")
            time.sleep(3)
            sys.exit()
        elif ((datos[0][0] == "0" and
               datos[1][1] == "0" and
               datos[2][2] == "0") or
              (datos[0][2] == "0" and
               datos[1][1] == "0" and
               datos[2][0] == "0")):
            print("gana el jugador con la ficha  \"X\"")
            time.sleep(3)
            sys.exit()


# Iniciamos el programa
Bienvenida()
print("jugaras con: " + ficha)
tablero(datos)
tirada()
