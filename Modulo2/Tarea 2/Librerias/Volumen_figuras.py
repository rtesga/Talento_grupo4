import utils

def Volumen_esfera(radio):
    volumen = 4*utils.pi*radio**3
    print(volumen)

#perimetro triangulo equilatero
def Volumen_piramide(area_base, altura):
    volumen = area_base*altura/3
    print(volumen)

def Volumen_cubo(lado_A):
    volumen = lado_A**3
    print(volumen)

def Volumen_paralelepipedo(lado_A, lado_B, lado_C):
    volumen = lado_A*lado_B*lado_C
    print(volumen)


     