'''

* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseadona idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (baseado no peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-strings (com as chaves)
'''

nome = 'David'
idade = 36
altura = 1.67
e_maior = idade >= 18 #booleano
data_1 = True #booleano
data_atual = 2021
peso = 60.0
ano_nasc = data_atual - idade

imc = peso / altura**2
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.')
print(f'O IMC de {nome} e {imc: .2f}')
print(f'{nome} nasceu em {ano_nasc}.')