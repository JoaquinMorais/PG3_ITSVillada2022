def contVocales(palabra):
    cont = 0
    for i in palabra:
        if i.casefold() in 'aeiou': 
            cont += 1
    return cont

print("Dime Una Oracion:")
oracion = input(">> ")
print(f"La oracion tiene {contVocales(oracion)} vocales")
