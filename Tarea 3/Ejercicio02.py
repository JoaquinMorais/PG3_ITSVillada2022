def main():
    n1  = getNumber(1)
    n2  = getNumber(2)
    
    divicion(n1,n2)

def divicion(n1,n2):
    try:
        print(f"{n1} / {n2} = {n1/n2}")
    except ZeroDivisionError:
        print("No se puede dividir entre 0...")
        

def getNumber(pos):
    while True:
        n = input(f"Ingrese el {pos}° numero:\n>> ")
        if n.isnumeric():
            break
        else:
            print("Tienes que ingresar un numero...")
    return int(n)
main()