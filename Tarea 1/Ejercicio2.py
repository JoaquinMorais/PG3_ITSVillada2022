from calendar import isleap


def añoBisiesto(año):
    if isleap(año):
         return True
    else:
        return False

print("Dime un año")
año = int(input(">> "))
if añoBisiesto(año):
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")



