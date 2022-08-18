import pickle


class vehiculo:
    puertas = 4
    color = ""

    def __init__(self, color, puertas):
        self.puertas = puertas
        self.color = color

    def getColor(self):
        return self.color

v1 = vehiculo("rojo", 5)

f = open ('datos.bin', 'wb')
pickle.dump(v1,f)
f.close()


f = open('datos.bin', 'rb')
rojo =pickle.load(f)
f.close()

print(type(rojo))
print(rojo.getColor())
