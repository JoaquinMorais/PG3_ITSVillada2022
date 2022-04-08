def pintarCuadrado(caracter,alto,ancho):
    for i in range(alto):
        print(str(caracter)*ancho)

def pintarTriangulo(caracter,alto):
    largo = len(str(caracter)*alto)

    for i in range(alto):
        aux = (str(caracter)*i).center(largo)
        print(aux)
    


def main():
    print("Elige Que Realizar:\n1) Cuadrado \n2) Triangulo")
    opcion = int(input("Ingrese la opcion: "))

    caracter = input("Ingrese un caracter: ")
    alto = int(input("Ingrese la altura: "))

    if opcion == 1:
        ancho = int(input("Ingrese el ancho: "))
        pintarCuadrado(caracter,alto,ancho)
    else:
        pintarTriangulo(caracter,alto)
main()
