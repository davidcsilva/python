velocidade = float(input('Digite a velocidade do carro em km/h: '))

if velocidade > 80.0:
    excesso_vel = velocidade - 80
    valor_multa = excesso_vel * 5
    print('Você foi multado no valor de %0.2f reais.' % valor_multa)
    