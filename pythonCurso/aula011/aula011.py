'''
Opereadores Relacionais
== > >= < <= !=

'''

print(2 == 2)
print(2 == 1)
print(2 == '2')

num1 = 2
num2 = 2

expressao = (num1 == num2)
print(expressao)

num1 = 3
num2 = 2

expressao = (num1 > num2)
print(expressao)

num1 = 2
num2 = 2

expressao = (num1 >= num2)
print(expressao)

num1 = 3
num2 = 2

expressao = (num2 < num1)
print(expressao)

num1 = 3
num2 = 2

expressao = (num2 <= num1)
print(expressao)

num1 = 3
num2 = 2

expressao = (num2 != num1)
print(expressao)

nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

idade_limite = 18
idade_menor = 20
idade_maior = 30


if idade >= idade_limite:
    print(f'{nome} pode pegar emprestimo.')
else:
    print(f'{nome} não pode pegar emprestimo.')


nome = input('Qual o seu nome: ')
idade = int(input('Qual a sua idade: '))

idade_menor = 20
idade_maior = 30


if (idade >= idade_menor) and (idade <= idade_maior):
    print(f'{nome} pode pegar emprestimo.')
else:
    print(f'{nome} não pode pegar emprestimo.')