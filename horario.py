import time

def main():
    tiempo_segundos = time.time()
    tiempo_cadena = time.ctime(tiempo_segundos) # 1488651001.7188754 seg
    print("Hoy es: ", tiempo_cadena)
    tiempo_st = time.gmtime(tiempo_segundos)
    hora = int(tiempo_st.tm_hour - 3)
    minutos = int(tiempo_st.tm_min)
    minutosquefaltan = 60 - minutos
    horasquefaltan = 19 - hora
    if hora >= 19:
        print("Hora de ir a casa")
    elif hora < 19:
        print("Faltan: ", horasquefaltan, 'horas', minutosquefaltan, 'minutos')

main()
