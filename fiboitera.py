print("Este programa halla la serie de fibonacci de forma iterativa")
print()

n = int(input("Ingrese las veces que quiere hacer la serie:  "))
aux, aux2, aux3 = 1, 1, 0

for i in range(n-2):
    aux3 = aux + aux2
    aux = aux2
    aux2 = aux3
    

print("El resultado da: "+str(aux3))

# 1 1 2 3 5 8 13 21 34 55 89 144
