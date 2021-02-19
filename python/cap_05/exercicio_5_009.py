num1 = input('Digite o 1º numero: ')
num2 = input('Digite o 2º numero: ')

e_num1 = num1.isdigit()
e_num2 = num2.isdigit()

if (e_num1 == True and e_num2 == True):
    num1 = int(num1)
    num2 = int(num2)
    quociente = 0
    dividendo = 0
    if num1 < num2:
        print(f'O quociente é 0 e o resto é {num1}')
    else:
        while num1 >= num2:
            dividendo = num1 - num2
            num1 = num1 - num2
            quociente = quociente + 1
        print(f'O quociente é {quociente} e o resto é {num1}')
    
else:
    print('Pelo menos um dos valores digitados é inválido.')
    
