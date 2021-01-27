import math

def area_circulo(radio):
    area = math.pi*radio**2
    return area

def perimetro_circulo(radio):
    perimetro = 2*math.pi*radio
    return perimetro

def area_triangulo(base, altura):
    area = base*altura/2
    return area

#perimetro triangulo equilatero
def perimetro_triangulo(base):
    perimetro = base*3
    return perimetro

def area_rectangulo(lado_A, lado_B):
    area = lado_A*lado_B
    return area

def perimetro_rectangulo(lado_A, lado_B):
    perimetro = lado_A*2+lado_B*2
    return perimetro

def distancia_recorrida(tiempo, velocidad):
    distancia = tiempo*velocidad
    return distancia