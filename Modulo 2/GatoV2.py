import time
import sys
import os
import random

cuadrantes = {
    1 : "_|", 
    2 : "_", 
    3 : "|_", 
    4 : "_|", 
    5 : "_", 
    6 : "|_", 
    7 : " |", 
    8 : " ",
    9 : "| "
}

cuadrantes2 = {
    1 : "1|", 
    2 : "2", 
    3 : "|3", 
    4 : "4|", 
    5 : "5", 
    6 : "|6", 
    7 : "7|", 
    8 : "8",
    9 : "|9 "
}

def Bienvenida():
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
        return ficha
    elif ficha == "2":
        ficha = "0"
        return ficha
    else:
        print("No elegiste correctamente vualve a intentarlo")
        time.sleep(2)
        os.system("clear")
        Bienvenida()



def fichas (valor):
    if valor == "X":
        print("\ / ")
        print(" X ")
        print("/ \ ")
    else:
        print(" __")
        print("|  |")
        print("|__|") 
    return ""

def tablero ():
    for i in range (1,10):
        if(i%3==0):
            print(cuadrantes2[i])
        else:
            print(cuadrantes2[i],end="")

def jugadas(dato,x):
    if (x=="X"):
        while(cuadrantes2[dato]=="X")or(cuadrantes2[dato]=="0"):
            print("esa posicion ya esta ocupada, intente con otra")
            dato = int(input("ingrese la coordenada en la que desea jugar: "))
        cuadrantes2[dato] = "X"
    else:
        while(cuadrantes2[dato]=="X")or(cuadrantes2[dato]=="0"):
            dato = random.randint(1,9)
        cuadrantes2[dato] = "0"
        

"""
def tablero (posicion):
    for i in range (1,10):
        if(cuadrantes[i] == "X")or(cuadrantes[i] == "0"):
            print("esa posicion ya esta ocupada, intente con otra.")
        else:
            cuadrantes[i] = "X"
   """ 

ficha = Bienvenida()
ganador = 0
tablero()
while(ganador == 0):
    jugada = int(input("ingrese la coordenada en la que desea jugar: "))
    jugadas(jugada,"X")
    time.sleep(2)
    jugadas(jugada,"0")
    tablero()
