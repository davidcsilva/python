codigo = 10
valor_total = 0
valor = 0

while codigo != 0:
    codigo = input('Digite o codigo do produto (0 para sair): ')
    codigo_e_num = codigo.isdigit()
    if codigo_e_num == True:
        codigo = int(codigo)
        if codigo == 0:
            continue
        else:
            if codigo == 1:
                qtd_produto = input('Digite a quantidade do produto: ')
                qtd_produto_e_num = qtd_produto.isdigit()
                if qtd_produto_e_num == True:
                    qtd_produto = int(qtd_produto)
                    valor_total = valor_total + qtd_produto * 0.5
                else:
                    print('Quantidade de produto digitada é invalida!')
            else:
                if codigo == 2:
                    qtd_produto = input('Digite a quantidade do produto: ')
                    qtd_produto_e_num = qtd_produto.isdigit()
                    if qtd_produto_e_num == True:
                        qtd_produto = int(qtd_produto)
                        valor_total = valor_total + qtd_produto * 1.00
                    else:
                        print('Quantidade de produto digitada é invalida!')
                else:
                    if codigo == 3:
                        qtd_produto = input('Digite a quantidade do produto: ')
                        qtd_produto_e_num = qtd_produto.isdigit()
                        if qtd_produto_e_num == True:
                            qtd_produto = int(qtd_produto)
                            valor_total = valor_total + qtd_produto * 4.00
                        else:
                            print('Quantidade de produto digitada é invalida!')
                    else:
                        if codigo == 5:
                            qtd_produto = input('Digite a quantidade do produto: ')
                            qtd_produto_e_num = qtd_produto.isdigit()
                            if qtd_produto_e_num == True:
                                qtd_produto = int(qtd_produto)
                                valor_total = valor_total + qtd_produto * 7.00
                            else:
                                print('Quantidade de produto digitada é invalida!')
                        else:
                            if codigo == 9:
                                qtd_produto = input('Digite a quantidade do produto: ')
                                qtd_produto_e_num = qtd_produto.isdigit()
                                if qtd_produto_e_num == True:
                                    qtd_produto = int(qtd_produto)
                                    valor_total = valor_total + qtd_produto * 8.00
                                else:
                                    print('Quantidade de produto digitada é invalida!')
                            else:
                                print('O código do produto digitado é invalido')
    else:
        print('O código do produto digitado é invalido')
else:
    print(f'O valor total das compras é R$: {valor_total: .2f}')
