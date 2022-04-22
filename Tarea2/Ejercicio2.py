import random

class Alumno():
    def __init__(self):
        self.nombre = ""
        self.nota = random.randint(1,10)

    def setNombre(self, nombre):
        self.nombre = nombre
    def setNota(self, nota):
        self.nota = nota
    
    def mostrar(self):
        print(f"Alumno: {self.nombre} - Nota: {self.nota}")
        self.promedio()

    def promedio(self):
        if(self.nota > 6):
            print("Aprobado!!")
        if(self.nota == 6):
            print("Regular... pero aprovaste :)")
        if(self.nota == 5):
            print("Desaprobaste, pero falto muy poco... mayor suerte la proxima vez!!")
        if (self.nota < 5):
            print("Desaprobado :'(")
        

alumno1 = Alumno()
alumno1.setNombre("Juan")
alumno1.mostrar()

alumno2 = Alumno()
alumno2.setNombre("Pedro")
alumno2.setNota(9)
alumno2.mostrar()