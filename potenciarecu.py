def potencia(base,exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return potencia(base,exp-1)*base

print("Este programa halla la potencia de un número de forma recursiva")
print()

base = int(input("Ingrese la base:  "))
exp = int(input("Ingrese el exponente:  "))
aux = 1

print("El resultado da: "+str(potencia(base,exp)))
