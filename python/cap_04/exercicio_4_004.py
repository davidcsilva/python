salario_atual = float(input('Digite o salário atual: '))
if (salario_atual >= 1250.00):
    aumento = salario_atual * 10 / 100
    salario_novo = salario_atual + aumento
    print('O novo salario é %0.2f reais' % salario_novo)

if (salario_atual < 1250.00):
    aumento = salario_atual * 15 / 100
    salario_novo = salario_atual + aumento
    print('O novo salario é %0.2f reais' % salario_novo)

