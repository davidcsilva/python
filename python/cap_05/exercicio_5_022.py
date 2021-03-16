import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)

operacao = 5

while operacao != '0':
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('0 - Sair')
    print('')

    operacao = input('Digite a operação desejada: ')

    if operacao == '0':
        break
    elif operacao == '1':
        num1 = input('Digite o 1º numero: ')
        enum1 = is_number(num1)
        num2 = input('Digite o 2º numero: ')
        enum2 = is_number(num2)
        if enum1 == True and enum2 == True:
            num1 = float(num1)
            num2 = float(num2)
            soma = num1 + num2
            print('')
            print(f'A soma de {num1: .2f} e {num2: .2f} é igual a {soma: .2f}')
            print('')
        else:
            print('')
            print('Valores digitados inválidos!')
            print('')
    elif operacao == '2':
        num1 = input('Digite o 1º numero: ')
        enum1 = is_number(num1)
        num2 = input('Digite o 2º numero: ')
        enum2 = is_number(num2)
        if enum1 == True and enum2 == True:
            num1 = float(num1)
            num2 = float(num2)
            subtracao = num1 - num2
            print('')
            print(f'A subtração de {num1: .2f} e {num2: .2f} é igual a {subtracao: .2f}')
            print('')
        else:
            print('')
            print('Valores digitados inválidos!')
            print('')
    elif operacao == '3':
        num1 = input('Digite o 1º numero: ')
        enum1 = is_number(num1)
        num2 = input('Digite o 2º numero: ')
        enum2 = is_number(num2)
        if enum1 == True and enum2 == True:
            num1 = float(num1)
            num2 = float(num2)
            multiplicacao = num1 * num2
            print('')
            print(f'A multiplicação de {num1: .2f} por {num2: .2f} é igual a {multiplicacao: .2f}')
            print('')
        else:
            print('')
            print('Valores digitados inválidos!')
            print('')
    elif operacao == '4':
        num1 = input('Digite o 1º numero: ')
        enum1 = is_number(num1)
        num2 = input('Digite o 2º numero: ')
        enum2 = is_number(num2)
        if enum1 == True and enum2 == True:
            num1 = float(num1)
            num2 = float(num2)
            if num2 != 0:
                divisao = num1 / num2
                print('')
                print(f'A divisão de {num1: .2f} por {num2: .2f} é igual a {divisao: .2f}')
                print('')
            else:
                print('')
                print('A divisão por 0 é impossível!')
                print('')
        else:
            print('')
            print('Valores digitados inválidos!')
            print('')
            