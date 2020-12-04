lista = []
cantidad = 0
numero = int(input("ingrese un numero: "))
lista.append(numero)
cantidad = 1
contador = 0

while(cantidad <15):
    numero = int(input("ingrese un numero: "))
    for i in range (0,cantidad):
        if(numero == lista[i]):
            contador = contador + 1
    if (contador == 0 ):
        lista.append(numero)
        cantidad = cantidad + 1
    else:
        print("dato repetido")
    contador = 0
    print(lista)