dep_inicial = input('Digite o deposito inicial: ')
e_num = dep_inicial.isnumeric()

if e_num == True:
    dep_inicial = float(dep_inicial)
else:
    print('Valor digitado é invalido!')

tx_juros = input('Digite a taxa de juros em %: ')

e_num = tx_juros.isnumeric()

if e_num == True:
    tx_juros = float(tx_juros)
else:
    print('Valor digitado é invalido!')

mes = 1
while mes <= 24:
    saldo = dep_inicial * ((100 + tx_juros)/100) ** mes
    print(f'O saldo do mês {mes} é R$: {saldo: .2f}')
    mes = mes + 1

ganho_jrs = saldo - dep_inicial
print(f'O total ganho com juros é R$: {ganho_jrs: .2f}')
