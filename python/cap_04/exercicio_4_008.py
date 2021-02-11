print('+ : Soma')
print('- : Subtração')
print('* : Multiplicação')
print('/ : Divisão')

operacao = input('Digite a operação: ')
num1 = float(input('Digite o 1º numero: '))
num2 = float(input('Digite o 2º numero: '))

if operacao == '+' :
    soma = num1 + num2
    print('A soma dos dois números é %0.2f' % soma)
else:
    if operacao == '-':
        subtracao = num1 - num2
        print('A subtração dos dois números é %0.2f' % subtracao)
    else:
        if operacao == '*':
            multiplicacao = num1 * num2
            print('A multiplicação dos dois números é %0.2f' % multiplicacao)
        else:
            if operacao == '/':
                if num2 == 0:
                    print('Impossível divisão por zero!')
                divisao = num1 / num2
                print('A divisão dos dois números é %0.2f' % divisao)

