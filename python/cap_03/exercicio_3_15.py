qtde_cigarros_dia = int(input('Digite a quantidade de cigarros fumados por dia:'))
qtde_anos = int(input('Digite a quantidade de anos que você fuma:'))

cigarros_fumados = qtde_anos * 365 * qtde_cigarros_dia

tempo_vida_menos = (cigarros_fumados * 10/60)/24

print('Você perdeu %d dias de vida' % tempo_vida_menos)

