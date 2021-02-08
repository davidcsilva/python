valHoras = int(input("Digite o valor em horas: "))
valMinutos = int(input("Digite o valor em minutos: "))
valSegundos = int(input("Digite o valor em segundos: "))


'''#Calcula a quantidade total de segundos'''

qSegundos = valHoras * 3600 + valMinutos * 60 + valSegundos  

print("O valor total em segundos de %d horas, %d minutos e %d segundos é %d segundos" % (valHoras, valMinutos, valSegundos, qSegundos))