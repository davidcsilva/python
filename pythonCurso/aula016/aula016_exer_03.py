nome = input('Digite o seu nome: ')

qtd_caracteres = len(nome)

if qtd_caracteres <= 4:
    print('Seu nome é curto.')
else:
    if 4 < qtd_caracteres <= 6:
        print('Seu nome é normal.')
    else:
        if 6 < qtd_caracteres:
            print('Seu nome é muito grande.')
