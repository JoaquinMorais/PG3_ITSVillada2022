
class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad}")

class Empleado(Persona):
    def __init__(self,nombre = "Pepe", edad = 0, sueldo = 3000):
        Persona.__init__(self,nombre,edad)
        if sueldo.isnumeric():
            self.sueldo = int(sueldo)
        
    
    def mostrarTodo(self):
        print(f"Nombre: {self.nombre} - Edad: {self.edad} - Sueldo: {self.sueldo}")
    def isImpuestos(self):
        if(self.sueldo > 3000):
            print(f"Tiene impuestos ({self.sueldo} > 3000)")
        else:
            print(f"No tiene impuestos ({self.sueldo} <= 3000)")



persona = Persona(input(">> Dime tu nombre: "),input(">> Dime tu edad: "))
persona.mostrar()

empleado = Empleado(input(">> Dime tu nombre: "),input(">> Dime tu edad: "),input(">> Dime tu sueldo: "))
empleado.mostrar()
empleado.mostrarTodo()
empleado.isImpuestos()