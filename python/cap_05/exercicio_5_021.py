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


cedulas = 0
atual = 50

while True:
    valor = input('Digite o valor a ser pago R$: ')
    valor_e_num = is_int(valor)

    if valor_e_num == True:
        apagar = int(valor)
        valor = int(valor)
        if valor == 0:
            break
        else:
            cedulas = 0
            atual = 50
            while True:
                if atual <= apagar:
                    apagar -= atual
                    cedulas += 1
                else:
                    print('%d cedulas de R$ %d' % (cedulas, atual)) 
                    if apagar == 0:
                        break
                    if atual == 50:
                        atual = 20
                    elif atual == 20:
                        atual = 10
                    elif atual == 10:
                        atual = 5
                    elif atual == 5:
                        atual = 1
                    cedulas = 0
    else:
        print('Valor digitado é inválido!')
        continue

