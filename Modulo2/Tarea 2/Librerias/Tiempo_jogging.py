## Tiempo total de sesiones de jogging
## en base a la velocidad de 3 fases
def horario_termino(horario_inicio, tiempo_total):
    ''' calcula horario de termino en base a:
            horario_inicio --> (horas, minutos)
            tiempo_total --> horas
        retorna horario_termino
    '''
    hora_inicio = horario_inicio[0]
    minutos_inicio = horario_inicio[1]
    tiempo_total_minutos = 60 * tiempo_total
    dias = tiempo_total_minutos/(1440)
    dias_entero = int(dias)
    minutos_restantes = tiempo_total_minutos - dias_entero *1440
    horas = minutos_restantes/60
    horas_entero = int(horas)
    minutos_restantes = int(minutos_restantes - horas_entero * 60)
    hora_termino = hora_inicio + horas_entero
    minutos_termino = minutos_inicio + minutos_restantes
    dias_adicionales = dias_entero
    print("\nEl horario de inicio es ", str(int(hora_inicio))+":"
                                        +str(int(minutos_inicio)))
    print("El tiempo total es ", str(horas_entero) 
            + ":" + str(minutos_restantes)
            + " +" + str(dias_entero)+ " días" )
    if minutos_termino > 59:
        hora_termino = hora_termino + 1
        minutos_termino = minutos_termino - 60
    if hora_termino > 23:
        dias_adicionales = dias_adicionales + 1
        hora_termino = hora_termino - 24
    return (int(hora_termino), int(minutos_termino), dias_adicionales)

print("Calculo para tiempo total de sesiones de jogging")
print("Ingrese horario de inicio:")
hora_inicio = float(input("Hora:"))
minutos_inicio = float(input("Minutos:"))
velocidad_suave = float(input("Ingrese Velocidad Suave:"))
distancia_tramo_suave = float(input("Ingrese Distancia Tramo Suave:"))
velocidad_intermedia = float(input("Ingrese Velocidad Intermedia:"))
distancia_tramo_intermedio = float(input("Ingrese Distancia Tramo Intermedio:"))
velocidad_alto = float(input("Ingrese Velocidad Alta:"))
distancia_tramo_alto = float(input("Ingrese Distancia Tramo Alto:"))

tiempo_tramo_suave = distancia_tramo_suave / velocidad_suave
tiempo_tramo_intermedio = distancia_tramo_intermedio / velocidad_intermedia
timepo_tramo_alto = distancia_tramo_alto / velocidad_alto

tiempo_total = tiempo_tramo_suave + tiempo_tramo_intermedio + timepo_tramo_alto

print("La distancia total de mi trayecto es: ", 
            distancia_tramo_suave
            + distancia_tramo_intermedio
            + distancia_tramo_alto)
print("El tiempo total de mi trayecto es: ", tiempo_total)

horario_inicio = (hora_inicio, minutos_inicio)

horario_termino = horario_termino(horario_inicio, tiempo_total)

print("El horario de regreso es", str(horario_termino[0])+":"
        + str(horario_termino[1])+ " + "
        + str(horario_termino[2])+ " días adicionales")