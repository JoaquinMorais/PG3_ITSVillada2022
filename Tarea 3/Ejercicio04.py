
def divicion(n1,n2):

    try:
        print(f"{n1} / {n2} = {int(n1)/int(n2)}")
        
    
    except (ZeroDivisionError, ValueError, TypeError):
        print("Error Intente Nuevamente...")
        
        

def main():
    
    while True:
        n1 = input("Ingrese el primer numero:\n>> ")
        n2 = input("Ingrese el segundo numero:\n>> ")
        divicion(n1,n2)

        print("Desea continuar? (S/N)")
        opc = input(">> ")
        if opc in ['S','s']:
            continue
        else:
            print("Cerrando Programa...")
            break
    


main()