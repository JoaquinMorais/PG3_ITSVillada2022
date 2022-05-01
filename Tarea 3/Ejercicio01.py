def main():
    while True:
        n1  = getNumber(1)
        if(n1 != False):
            break
    while True:
        n2  = getNumber(2)
        if(n2 != False):
            break

    
    print(n1)
    print(n2)
    suma(n1,n2)

def suma(n1,n2):
    print(f"{n1} + {n2} = {n1+n2}")


def getNumber(pos):
    try:
        n = int(input(f"Ingrese el {pos}° numero:\n>> "))
        return n
    except:
        print("Tienes que ingresar un numero...")
        return False
    

def isContinue():
    print("Desea continuar? (S/N)")
    opc = input(">> ")
    if opc in ["S","s","n","N"]:
        if opc in ["S","s"]:
            return True
        else:
            return False
    else:
        print("Error...")
        return False

while True:
    main()
    continuos = isContinue()
    if not continuos:
        print("Cerrando Programa...")
        break
