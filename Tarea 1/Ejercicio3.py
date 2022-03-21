import string


def pintar(caracter,alto,ancho):
    for i in range(alto):
        print(str(caracter)*ancho)
    
car = input("Ingrese un caracter: ")
alto = int(input("Ingrese la altura: "))
ancho = int(input("Ingrese el ancho: "))

pintar(car,alto,ancho)
