divida_inicial = input('Digite o valor da dívida R$: ')
e_num_divida = divida_inicial.isnumeric()

tx_juros = input('Digite a taxa de juros em %: ')
e_num_juros = tx_juros.isnumeric()

parcela = input('Digite o valor da parcela mensal R$: ')
e_num_parcela = parcela.isnumeric()

if e_num_divida and e_num_juros and e_num_parcela:
    divida_inicial = float(divida_inicial)
    tx_juros = float(tx_juros)
    parcela = float(parcela)
    divida = divida_inicial
    mes = 0
    total_pago = 0
    while divida > 0:
        if mes == 0:
            divida = divida * ((100 + tx_juros)/100)
            mes += 1
        else:
            if divida >= parcela:
                divida = divida - parcela
                total_pago = total_pago + parcela
                divida = divida * ((100 + tx_juros)/100)
                mes += 1
            else:
                total_pago = total_pago + divida
                divida = divida - divida
    else:
        print(f'A divida será paga em {mes} meses e o total pago sera R$: {total_pago: .2f}')
else:
    print('Valores digitados inválidos!')
