import random
a = [["","",""],["","",""],["","",""]]
for i in range (0,3):
    print(a[i])
movimientos = 0
ganador = 0
print("Usted es el X")

while((movimientos<=9)or(ganador == 0)):
    coordenada_x = int(input("Ingrese columna: "))
    coordenada_y = int(input("Ingrese fila: "))
    if (a[coordenada_x][coordenada_y]==""):
        a[coordenada_x][coordenada_y]="X"
    coordenada_x = random.randint(0,2)
    coordenada_y = random.randint(0,2)
    while(a[coordenada_x][coordenada_y]!=""):
        coordenada_x = random.randint(0,2)
        coordenada_y = random.randint(0,2)
    a[coordenada_x][coordenada_y]="0"
    for i in range (0,3):
        print(a[i])
    movimientos = movimientos + 1
    
    #Evaluacion de X
    x="X"
    if((a[0][0]==x)and(a[0][1]==x)and(a[0][2]==x)):
        print("GANASTE!!!!!!")
        ganador = 1
    elif((a[1][0]==x)and(a[1][1]==x)and(a[1][2]==x)):
        print("GANASTE!!!!!!")
        ganador = 1
    elif((a[2][0]==x)and(a[2][1]==x)and(a[2][2]==x)):
        print("GANASTE!!!!!!")
        ganador = 1
    elif((a[0][0]==x)and(a[1][0]==x)and(a[2][0]==x)):
        print("GANASTE!!!!!!")
        ganador = 1
    elif((a[0][1]==x)and(a[1][1]==x)and(a[2][1]==x)):
        print("GANASTE!!!!!!")
        ganador = 1
    elif((a[0][2]==x)and(a[1][2]==x)and(a[2][2]==x)):
        print("GANASTE!!!!!!")
        ganador = 1
    elif((a[0][0]==x)and(a[1][1]==x)and(a[2][2]==x)):
        print("GANASTE!!!!!!")
        ganador = 1   
    elif((a[0][2]==x)and(a[1][1]==x)and(a[2][0]==x)):
        print("GANASTE!!!!!!")
        ganador = 1
        
    #Evaluacion de Y
    if((a[0][0]=="0")and(a[0][1]=="0")and(a[0][2]=="0")):
        print("PERDEDOR!!!!!")
        ganador = 1
    elif((a[1][0]=="0")and(a[1][1]=="0")and(a[1][2]=="0")):
        print("PERDEDOR!!!!!")
        ganador = 1
    elif((a[2][0]=="0")and(a[2][1]=="0")and(a[2][2]=="0")):
        print("PERDEDOR!!!!!")
        ganador = 1
    elif((a[0][0]=="0")and(a[1][0]=="0")and(a[2][0]=="0")):
        print("PERDEDOR!!!!!")
        ganador = 1
    elif((a[0][1]=="0")and(a[1][1]=="0")and(a[2][1]=="0")):
        print("PERDEDOR!!!!!")
        ganador = 1
    elif((a[0][2]=="0")and(a[1][2]=="0")and(a[2][2]=="0")):
        print("PERDEDOR!!!!!")
        ganador = 1
    elif((a[0][0]=="0")and(a[1][1]=="0")and(a[2][2]=="0")):
        print("GANASTE!!!!!!")
        ganador = 1   
    elif((a[0][2]=="0")and(a[1][1]=="0")and(a[2][0]=="0")):
        print("GANASTE!!!!!!")
        ganador = 1