'''
Voltar mais tarde

'''

a = int(input('Digite o 1º numero: '))
b = int(input('Digite o 2º numero: '))
c = int(input('Digite o 3º numero: '))

if (a > b):
    if (b > c):
        print('O 1º valor é o maior e o 3º valor é o menor')
    if (b == c):
        print('O 1º valor é o maior e o 3º e 2º valores são os menores')
    if (b < c):
        print('O 1º valor é o maior e o 2º valor é o menor')

if (c > a):
    if (b > a):
        print('O 3º valor é o maior e o 1º valor é o menor')
    if (b == a):
        print('O 3º valor é o maior e o 1º e 2º valores são os menores')
    if (b < a):
        print('O 3º valor é o maior e o 2º valor é o menor')

if (b > a):
    if (c > a):
        print('O 2º valor é o maior e o 1º valor é o menor')
    if (c == a):
        print('O 2º valor é o maior e o 1º e 3º valores são os menores')
    if (c < a):
        print('O 2º valor é o maior e o 3º valor é o menor')

if (a == b == c):
    print('Todos os valores são iguais')

