def division(a,b):
    if a < b:
        return 0
    else:
        return 1 + division(a-b,b)

print("Este programa divide dos números de forma recursiva")
print()

a = int(input("Ingrese el dividendo:  "))
b = int(input("Ingrese el divisor:  "))

print(division(a,b))
