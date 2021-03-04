N = []
qtde_num = 0
temp = 1
soma = 0.0
media = 0.0

while temp != 0:
    temp = input('Digite um numero inteiro (0 para sair): ')
    temp_e_num = temp.isdigit()
    if (temp_e_num == True):
        temp = int(temp)
        if temp == 0:
            continue
        soma = soma + temp
        N = N + [temp]
        qtde_num += 1
    else:
        print('Valor digitado é invalido!')
else:
    media = soma / qtde_num
    print(f'A quantidade de numeros digitados é {qtde_num}, a soma é {soma} e a média aritmética é {media}.')

for N in N:
    print(N)
