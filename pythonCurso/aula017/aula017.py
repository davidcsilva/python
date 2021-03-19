"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
def Cumprimentar (saudacao, nome):
    print(f'{saudacao} {nome}')

Cumprimentar('Olá', 'David')


"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
def Adicao (val1, val2, val3):
    return (val1 + val2 + val3)

soma = Adicao(1, 2, 3)
print(soma)


"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
def Aumento(sal, taxa):
    return sal * (100 + taxa )/100

newsal = Aumento(1000, 10)
print(newsal)

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""

def FizzBuzz (valor):
    if valor%3 == 0:
        print('Fizz')
    if valor%5 == 0:
        print('Buzz')
    if (valor%3 == 0) and (valor%5 == 0):
        print('FizzBuzz')

FizzBuzz(5)