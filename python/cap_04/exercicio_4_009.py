valor_casa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o valor do salário R$: '))
prazo = int(input('Digite o prazo em anos: '))

prestacao = valor_casa / (prazo * 12)

if prestacao > (salario * 0.3):
    print('O emprestimo deve ser negado')
else:
    print('O emprestimo deve ser aprovado com valor de prestação R$: %0.2f' % prestacao)

