
class Triangulo():
    def __init__(self):
        self.lados = ['1','1','1']
    
    def setLados(self, lado1, lado2, lado3):
        if (lado1 < 0 or lado2 < 0 and lado3 < 0):
            print("ERROR: Index Out of Range")
        else:
            self.lados[0] = lado1
            self.lados[1] = lado2
            self.lados[2] = lado3
    
    def ladoMayor(self):
        valorMayor = self.lados[0]
        for i in self.lados:
            if(i > valorMayor):
                valorMayor = i
        print(f"El lado mas grande mide {valorMayor}")
    
    def tipoTriangulo(self):
        if(self.lados[0] == self.lados[1] and self.lados[1] == self.lados[2]):
            print("Equilatero")
        elif(self.lados[0] == self.lados[1] or self.lados[1] == self.lados[2] or self.lados[0] == self.lados[2]):
            print("Isosceles")
        else:
            print("Escaleno")

triangulo = Triangulo()
triangulo.setLados(6,6,6)
triangulo.ladoMayor()
triangulo.tipoTriangulo()