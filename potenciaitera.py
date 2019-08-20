print("Este programa halla la potencia de un número de forma iterativa")
print()

base = int(input("Ingrese la base:  "))
exp = int(input("Ingrese el exponente:  "))
aux = 1

for i in range(exp):
    aux = aux*base
    

print("El resultado da: "+str(aux))
