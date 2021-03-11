# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 14:44:41 2021

@author: David
"""

valor = int(input('Digite o valor a pagar:'))
cedulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print('%d cedulas de R$%d' % (cedulas, atual))
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
