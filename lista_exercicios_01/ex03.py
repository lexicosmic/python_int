# -*- coding: utf-8 -*-

from cmath import sqrt

a = float(input("Digite o coeficiente A: "))
b = float(input("Digite o coeficiente B: "))
c = float(input("Digite o coeficiente C: "))

delta = (b**2) - 4 * a * c

if (delta < 0):
    print("Equação sem raízes reais")
elif (delta == 0):
    resultado = (-b) / 2 * a
    print(f"A raíz da equação é: {resultado}")
else:
    res1 = (-b + sqrt(delta)) / 2 * a
    res2 = (-b - sqrt(delta)) / 2 * a
    print(f"As raízes da equação são: {res1} e {res2}")
