from webbrowser import Opera


class Operacion:
    def __init__(self,n1 = 1,n2 = 1):
        self.n1 = n1
        self.n2 = n2
        self.main()


    def sumar(self):
        print(f"{self.n1} + {self.n2} = {self.n1 + self.n2}")

    def restar(self):
        print(f"{self.n1} - {self.n2} = {self.n1 - self.n2}")
    
    def multiplicar(self):
        print(f"{self.n1} * {self.n2} = {self.n1 * self.n2}")
    
    def dividir(self):
        if(self.n2 == 0):
            print("No se puede dividir por 0")
        else:
            print(f"{self.n1} / {self.n2} = {self.n1 / self.n2}")
    
    def mostrarNumeros(self):
        print(f"N1: {self.n1} - N2: {self.n2}")
    
    def main(self):
        self.mostrarNumeros()
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()


operacion = Operacion(input(">> Dime el primer numero"),input(">> Dime el segundo numero"))
