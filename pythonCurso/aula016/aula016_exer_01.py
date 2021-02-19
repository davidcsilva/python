import re


def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False


def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


e_num = False

while e_num != True:
    numero = input('Digite um numero: ')
    e_num = is_int(numero)
    if e_num == False:
        print('Isso não é um numero inteiro')

numero = int(numero)

if numero % 2 != 0:
    print('Este é um numero ímpar!')
else:
    print('Este é um numero par!')
