def fibonacci(n):
    if n < 2:
        return 1
    if n >= 2:
        return fibonacci(n-1) + fibonacci (n-2)

print("Este programa halla la serie de fibonacci de forma recursiva")
print()

n = int(input("Ingrese las veces que quiere hacer la serie:  "))

print("El resultado da: "+str(fibonacci(n-1)))
 
# 1 1 2 3 5
