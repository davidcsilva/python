num1 = input('Digite o 1º numero: ')
num2 = input('Digite o 2º numero: ')

e_num1 = num1.isdigit()
e_num2 = num2.isdigit()

if (e_num1 == True and e_num2 == True):
    num1 = int(num1)
    num2 = int(num2)
    x = 1
    soma = 0

    while x <= num2 :
        soma = soma + num1
        x = x + 1
    
    print(f'O resultado da multiplicação é: {soma}')
else:
    print('Pelo menos um dos valores digitados é inválido.')
    
