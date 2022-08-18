# -*- coding: utf-8 -*-

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
sinal = input("Digite a operação: ")

resultado = 0

if sinal == "+":
    resultado = num1 + num2
elif sinal == "-":
    resultado = num1 - num2
elif sinal == "*":
    resultado = num1 * num2
elif sinal == "/":
    try:
        resultado = num1 / num2
    except:
        print("Não é permitido dividir por zero!")
        exit()
elif sinal == "**":
    resultado = num1 ** num2
else:
    print("Sinal inválido")
    exit()

print(f"Reultado: {resultado}")
