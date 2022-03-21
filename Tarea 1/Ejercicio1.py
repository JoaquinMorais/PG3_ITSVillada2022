igualdades = []
lista = ["a","b","c","d","a","b","c","d","e","b","b","b"]


print("Dime Que Buscar")
variable = input(">> ")



def buscarDentroDeLista(lista,parametro):
    cont = 0
    for i in lista:
        if i==parametro:
            igualdades.append(cont)
        cont += 1
    
    if igualdades == []:
        print("El parametro que desea buscar no esta dentro de la lista")
    else:
        print(f"El parametro aparece en la posicion {igualdades}") 
    


    
            

buscarDentroDeLista(lista,variable)