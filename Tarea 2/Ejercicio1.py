class Persona:
    def __init__(self):
        self.nombre = ""
    
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def saludar(self):
        print("Hola, soy " + self.getNombre() + "!! Mucho gusto!!")

persona1 = Persona()
persona1.setNombre("Juan")
persona1.saludar()

persona2 = Persona()
persona2.setNombre("Pedro")
persona2.saludar()