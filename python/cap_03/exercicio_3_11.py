precoMerc  = float(input("Digite o preço do produto: "))
descMerc = float(input("Digite o valor do desconto: "))

desconto = precoMerc * descMerc/100

print("O valor percentual do desconto é %0.2f ." % desconto)

novoPreco = precoMerc - desconto

print("O valor a pagar é %0.2f reais" % novoPreco)