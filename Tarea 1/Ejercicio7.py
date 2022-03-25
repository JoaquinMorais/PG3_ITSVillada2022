from calendar import isleap


def isStep(lista):
    aux = ""
    cont = 0
    valor = True
    for i in lista:
        if cont==0:
            aux = i
            
        else:
            if i == (aux-1) or i == (aux+1):
                aux = i
            else:
                valor = False
        cont+=1
    return valor

lista = 1234567876543210

print(f"La lista {lista}")
if isStep(lista):
    print("Esta Conformada Por Numeros Step")
else:
    print("No Esta Conformada Por Numeros Step")