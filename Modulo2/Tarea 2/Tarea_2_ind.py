###programa que utiliza el paquete cientific
###con datos entregados por el usuario
###a travez del comando input()
import Librerias

presentacion = ['''         #####Opciones: ##### 
        1) Volumen de figuras geometricas 
        2) Costo de productos
        3) Tiempo total de jogging
        0) Salir del programa ''']

opcion = 1
while(opcion != 0):
    print(presentacion[0])
    opcion = int(input("Que desea hacer: "))
    if (opcion == 1):
        Librerias.Volumen_figuras.Volumen_esfera(5)
        radio = int(input("Ingrese el radio de una esfera: "))
        Librerias.Volumen_figuras.Volumen_esfera(radio)
    elif(opcion == 2):
        Librerias.Costo_de_pedidos
    elif(opcion == 3):
        Librerias.Tiempo_jogging
    else:
        print("opcion erronea, ingrese otro valor")