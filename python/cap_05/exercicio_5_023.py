num = input('Digite um número: ')

e_num = num.isdigit()
e_primo = False
if e_num == True:
    num = int(num)
    if num % 2 == 0:
        e_primo = False
    else:
        for i in range(1, num, 2):
            print(i)
            if num == 2:
                e_primo = True
            if num == 3:
                e_primo = True
            if num % i != 0:
                e_primo = True
            else:
                e_primo = False
        else:
            if e_primo == False:
                print(f'{num} não é primo')
            else:
                print(f'{num} é primo')

else:
    print('Valor digitado é inválido!')