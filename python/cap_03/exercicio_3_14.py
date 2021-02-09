km_percorrido = float(input('Digite a quantidade de km percorridos: '))
dias_alugado = float(input('Digite a quantidade de dias alugado: '))

valor_dias = dias_alugado * 60
valor_km = km_percorrido * 0.15

valor_total = valor_dias + valor_km

print('O valor total a pagar pelo aluguel é: %0.2f' % valor_total)