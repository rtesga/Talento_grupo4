"""
Si tienes un archivo llamado mi_modulo.py, si lo ejecutamos como programa principal el
atributo __name__ será '__main__', si lo usamos importándolo desde otro módulo (import mi_modulo)
el atributo __name__ será igual a 'mi_modulo'.

Básicamente, lo que haces usando if __name__ == “__main__”: es ver si el módulo ha sido ejecutado 
directamente o no (importado). Si se ha ejecutado como programa principal se ejecuta el código
dentro del condicional.

"""

def area_circulo(int radio)
    area=3.1415926*pow(radio,2)
    return(area)

def perimetro_circulo(int radio)
    perimetro = 2*3.1415926*radio
    return(perimetro)

def area_triangulo(int base, int altura)
    area = base*altura/2
    return(area)

def perimetro_triangulo_equilatero(int base, int altura)
    perimetro = 3*base
    return(perimetro)

def area_recgantuclo(int a,int b)
    area = a*b
    return(area)

def perimetro_recgantuclo(int a,int b)
    perimetro =2*a+2*b
    return(perimetro)

def distancia_recorrida(int tiempo, int velocidad)
