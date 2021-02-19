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
    valor_hora= input('Digite um valor para a hora: ')
    e_num = is_int(valor_hora)
    if e_num == False:
        print('Isso não é um numero inteiro')

valor_hora = int(valor_hora)

if 0 <= valor_hora < 12:
    print('Bom dia')
else:
    if 12 <= valor_hora < 18:
        print('Boa Tarde')
    else:
        if 18 <= valor_hora <= 23:
            print('Boa Noite')
        else:
            print('O valor digitado é inválido!')