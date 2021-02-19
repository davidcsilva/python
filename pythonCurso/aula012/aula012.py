'''
Operadores Lógicos:
And, Or, Not, In e Not in

'''

a = 2
b = 2
c = 3
valor1 = a == b and b < c
print(valor1)
valor2 = a == b or b < c
print(valor2)

c = 2
d = 3

if c < d:
    print('D é maior que C.')
else:
    print('C é maior que D')

if not c < d:
    print('C é maior que D')
else:
    print('D é maior que C')

nome = 'David Silva'
if 'D' in nome:
    print(f'Existe a letra D em {nome}')
else:
    print('Não existe')

if 'O' not in nome:
    print(f'Não existe a letra O em {nome}')
else:
    print('Existe')

usuario = input('Nome de usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = 'David'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce esta logado no sistema')
else:
    print('Usuario ou senha invalidos')