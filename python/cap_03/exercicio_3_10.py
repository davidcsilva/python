salario  = float(input("Digite o valor do salário: "))
aumPercentual = float(input("Digite o valor percentual do aumento: "))

aumento = salario * aumPercentual/100

print("O valor do aumento é %0.2f ." % aumento)

novoSal = salario + aumento

print("O novo salário é %0.2f reais" % novoSal)
