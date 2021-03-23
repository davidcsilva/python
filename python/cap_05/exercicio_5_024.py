n = int(input("Digite N: "))

lista =[]
divisores =[]
for i in range(2, n+1):
    for j in range(1, i+1):
        if i >= j:
            if i % j == 0:
                divisores.append(j)
                print("divisores",divisores)
    if len(divisores) == 2:
        lista.append(i)
    divisores = []

print("primos",lista)