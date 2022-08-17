class alumno:
    def nombre(self,nom):
        self.nombre=nom
    def nota(self,n):
        self.nota=float(n)
    def aprobado(self):
        if self.nota > 4.9:
            print("aprobado")
        else:
            print("No Aprobo")
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("nota: ",self.nota)

alumno1=alumno()
alumno1.nombre("Marcos")
alumno1.nota(9)
alumno1.mostrar()
alumno1.aprobado()
