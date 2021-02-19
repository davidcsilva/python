'''
Pass e Ellipsis como placeholders
'''

valor = True

if valor:
    print('oi')
else:
    print('Tchau')

if valor:
    pass # PASS como placeholder
else:
    print('Tchau')

if valor:
    ... # Ellipsis como placeholder
else:
    print('Tchau')