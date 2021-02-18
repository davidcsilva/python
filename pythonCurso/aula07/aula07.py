'''
Introdução à formatação de strings

'''

nome = 'David'
idade = 36
altura = 1.67
e_maior = idade >= 18 #booleano
data_1 = True #booleano
data_atual = 2021
peso = 60.0

imc = peso / altura**2

print('%s tem idade de %d anos e IMC %0.2f' % (nome, idade, imc))
print(f'{nome} tem idade de {idade} anos e IMC{imc: .2f}')
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))
