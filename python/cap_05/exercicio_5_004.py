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
    fim = input('Digite um numero para contagem: ')
    e_num = is_int(fim)
    if e_num != True:
        print('Digite um valor válido!')

fim = int(fim)

x  = 0
while (x <= fim):
    if (x % 2 != 0):
        print(x)
    x = x + 1
