import random
import time


def bienvenida():
    print("""*****************************************
    *   Bienvenido al juego del gato        *
    *   con que ficha deseas jugar          *
    *          X       O                    *
    *****************************************""")
    ficha = input("Quiere jugar con X o O?: ")
    ficha = ficha.upper()
    while(ficha !="X"):
        print("Esa no es una opcion.\n\n")
        ficha = input("Elija X o O?: ")
        ficha = ficha.upper()
    return ficha

posiciones = {
    1: "1",
    "col1.1": "|",
    2: "2",
    "col1.2": "|",
    3: "3",
    "fila1": "=====",
    4: "4",
    "col2.1": "|",
    5: "5",
    "col2.2": "|",
    6: "6",
    "fila2": "=====",
    7: "7",
    "col3.1": "|",
    8: "8",
    "col3.2": "|",
    9: "9"
}

def tablero ():
    j=0
    for i in posiciones:
        print(posiciones[i],end="")
        if(j==4)or(j==5)or(j==10)or(j==11):
            print("")
        j=j+1
    print("")

def movimiento(jugada,ficha):
    if(ficha=="X"):
        while(posiciones[jugada]=="X")or(posiciones[jugada]=="O"):
            print("ese lugar ya contiene una ficha.")
        else:
            posiciones[jugada]=ficha        
    else:
        while(posiciones[jugada]=="X")or(posiciones[jugada]=="O"):
            #print("ese lugar ya contiene una ficha.")
            jugada = random.randint(1,9)
        posiciones[jugada]=ficha     

def condiciones(n):
    ###Condiciones para ganar
    if(posiciones[1]==posiciones[2]==posiciones[3]=="X"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[4]==posiciones[5]==posiciones[6]=="X"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[7]==posiciones[8]==posiciones[9]=="X"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[1]==posiciones[4]==posiciones[7]=="X"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[2]==posiciones[5]==posiciones[8]=="X"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[3]==posiciones[6]==posiciones[9]=="X"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[1]==posiciones[5]==posiciones[9]=="X"):
        print("GanasTE!!!!!!!!!!!")    
        return(1)
    elif(posiciones[7]==posiciones[5]==posiciones[3]=="X"):
        print("GanasTE!!!!!!!!!!!")
        return(1)

    ###Condiciones para perder
    elif(posiciones[1]==posiciones[2]==posiciones[3]=="O"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[4]==posiciones[5]==posiciones[6]=="O"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[7]==posiciones[8]==posiciones[9]=="O"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[1]==posiciones[4]==posiciones[7]=="O"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[2]==posiciones[5]==posiciones[8]=="O"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[3]==posiciones[6]==posiciones[9]=="O"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    elif(posiciones[1]==posiciones[5]==posiciones[9]=="O"):
        print("GanasTE!!!!!!!!!!!")    
        return(1)
    elif(posiciones[7]==posiciones[5]==posiciones[3]=="O"):
        print("GanasTE!!!!!!!!!!!")
        return(1)
    ##otros##
    elif(n>9):
        print("Empate")
    else:
        return(0)

##################### INICIO DE PROGRAMA ####################

ficha1 = bienvenida()
if(ficha1=="X"):
    ficha2="O"
else:
    ficha2="X"
ganador = 0
jugadas = 1
while(ganador != 1):
    pc = 0
    tablero()
    mov = int(input("En que numero desea jugar?: "))
    print(mov)
    while(mov>10):
        print("movimiento no valido.")
        mov = int(input("En que numero desea jugar?: "))
    movimiento(mov, ficha1)
    tiempo = random.randint(1,3)
    print(".........pensando!!")
    time.sleep(tiempo)
    mov = random.randint(1,9)
    movimiento(mov, ficha2)
    ganador = condiciones(jugadas)
    jugadas= jugadas+1


print("adios")