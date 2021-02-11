distacia_km = float(input('Digite a distância da viagem em km: '))

if (distacia_km <= 200):
    preco_passagem = distacia_km * 0.50
    print('O preço da passagem é %0.2f reais.' % preco_passagem)
else:
    preco_passagem = distacia_km * 0.45
    print('O preço da passagem é %0.2f reais.' % preco_passagem)
