archivo = open("./Tarea 3/Texto.txt","w")



def getText():
    text = input("Ingrese el texto para ingresar en txt: ")
    return text
def getNumber():
    while True:
        n = input("Ingrese el numero para ingresar en txt: ")
        if n.isnumeric():
            break
        else:
            print("Tienes que ingresar un numero...")
    return int(n)
    
def main():
    archivo.write(getText())
    print("Texto ingresado en txt...")
    archivo.write("\n")
    num = getNumber()
    try:
        
        archivo.write(num)
    except TypeError:
        print("Error no puede entrar un numero entero a un text, primero deberia convertrlo a un string con la funcion str()")
        archivo.write(str(num))
        print(f"Numero {num} añadido al txt")



main()


archivo.close()