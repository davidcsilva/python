lista1 = [1, 2, 3]
lista2 = [1, 1, 4]
lista3 = []
i = 0
j = 0
for i in range(0, 3, 1):
    contador = 0
    for j in range(0, 3, 1):
        if lista1[i] == lista2[j] and contador < 1:
            lista3.append(lista1[i])
            contador += 1
        elif lista1[i] == lista2[j] and contador >= 1:
            continue
        elif lista1[i] != lista2[j] :
            lista3.append(lista1[i])
            lista3.append(lista2[j])
            contador += 1

else:
    print(lista3)