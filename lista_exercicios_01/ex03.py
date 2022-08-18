# -*- coding: utf-8 -*-

coef0 = float(input("Digite o coeficiente de grau 0: "))
coef1 = float(input("Digite o coeficiente de grau 1: "))
x1 = float(input("Digite a variável de grau 1: "))
coef2 = float(input("Digite o coeficiente de grau 2: "))
x2 = float(input("Digite a variável de grau 2: "))

resultado = coef2 * (x2 ** 2) + coef1 * x1 + coef0

print(f"Reultado: {resultado}")
# 2*3^2 + 0*9 + -2 = 16
