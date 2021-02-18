'''
Entrada de dados

'''

nome = input('Qual seu nome? ')
print(f'O usuario digitou {nome} e o tipo da variável '
      f'é {type(nome)}')

idade = input('Qual sua idade? ')
ano_nasc = 2019 - int(idade)
print(f'{nome} tem {idade} anos. '
      f' Nasceu em {ano_nasc}.')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
soma = num1 + num2
print(f'A soma dos dois numeros é {soma}.')