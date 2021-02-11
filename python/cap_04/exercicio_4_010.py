print('1 - Residencial')
print('2 - Comercial')
print('3 - Industrial')

tipo_consumidor = int(input('Digite o tipo de consumidor: '))
consumo = float(input('Digite o consumo em kWh: '))

if tipo_consumidor == 1:
    if consumo <= 500.0:
        valor_pagar = consumo * 0.40
        print('O valor a pagar é R$: %0.2f' % valor_pagar)
    else:
        if consumo > 500.0:
            valor_pagar = consumo * 0.65
            print('O valor a pagar é R$: %0.2f' % valor_pagar)
else:
    if tipo_consumidor == 2:
        if consumo <= 1000.0:
            valor_pagar = consumo * 0.55
            print('O valor a pagar é R$: %0.2f' % valor_pagar)
        else:
            if consumo > 1000.0:
                valor_pagar = consumo * 0.60
                print('O valor a pagar é R$: %0.2f' % valor_pagar)
    else:
        if tipo_consumidor == 3:
            if consumo <= 5000.0:
                valor_pagar = consumo * 0.55
                print('O valor a pagar é R$: %0.2f' % valor_pagar)
            else:
                if consumo > 5000.0:
                    valor_pagar = consumo * 0.60
                    print('O valor a pagar é R$: %0.2f' % valor_pagar)
        else:
            print('Digite um tipo de consumidor válido!')