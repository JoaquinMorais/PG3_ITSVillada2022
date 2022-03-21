def invertir(palabra):
    aux = ""
    for i in range(len(palabra)):
        aux = palabra[i] + aux
    return aux

def palindromo(palabra):
    if palabra == invertir(palabra):
        return True
    else:
        return False

print("Dime Una Palabra:")
palabra = input(">> ")
if palindromo(palabra):
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")
