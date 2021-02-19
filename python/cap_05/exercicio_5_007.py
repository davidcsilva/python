fim = input('Digite o valor limite da multiplicação: ')
e_num = fim.isdigit()
if e_num == False:
    print('Valor digitado é inválido!')
else:
    fim = int(fim)

x = 1

if e_num == True:
    while (x <= fim):
        print(f'2 x {x} = {2*x}')
        x = x + 1
        
