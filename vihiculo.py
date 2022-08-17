class vehiculo:
        puertas = 4
        ruedas = 4
        color = 'rojo'

class coche(vehiculo):
        velocidad = 200
        puertas = 2
        cilindrada = 160

c = coche()
print(c.puertas, c.color, c.velocidad, c.cilindrada, c.ruedas)
