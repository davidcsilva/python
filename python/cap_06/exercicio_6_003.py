lista1 = [1, 2, 3]
lista2 = [1, 1, 4]
lista1 = lista1 + lista2
lista3 = []
i = 0
j = 0
for i in lista1:
    if i not in lista3:
        lista3.append(i)
else:
    print(lista3)