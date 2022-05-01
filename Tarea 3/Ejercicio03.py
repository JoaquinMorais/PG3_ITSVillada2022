meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')



def getNumber():
    while True:
        n = input("Ingrese el numero del mes:\n>> ")
        if n.isnumeric():
            break
        else:
            print("Tienes que ingresar un numero del 1 al 12...")
    return int(n)

def main():
    mes = getNumber()
       
    try:
        print(f"El mes es {meses[mes-1]}")
    except IndexError:
        print("El mes ingresado no existe...")

main()