print("Este programa divide dos números de forma iterativa")
print()

a = int(input("Ingrese el dividendo:  "))
b = int(input("Ingrese el divisor:  "))
aux=0
cont=0

while aux<a:
    aux += b
    cont=cont+1

print("La división da: "+str(cont))
