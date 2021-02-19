'''
Obtendo tamanho de strings com len()

'''

usuario = input('Digite seu usuario: ')

qtde_caracteres = len(usuario)
print(usuario, qtde_caracteres, type(qtde_caracteres))

if qtde_caracteres < 6:
    print('Voce precisa digitar pelo menos 6 caracteres.')
else:
    print('Voce foi cadastrado no sistema')

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')

