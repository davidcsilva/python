# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:56:42 2021

@author: David
"""

valor = float(input('Digite o valor a pagar:'))
moedas = 0
atual = 0.50
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        moedas += 1
    else:
        print('%d moedas de R$%.2f' % (moedas, atual))
        if apagar == 0.00:
            break
        if atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        elif apagar < 0.01:
            print('Valor digitado inválido!')
            break
        
        moedas = 0
