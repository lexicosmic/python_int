# -*- coding: utf-8 -*-

# # Imprime Olá, Mundo!
# print("Olá, mundo!")

# # Operações matemáticas
# print(2+2)
# print(2**3)
# print(10/3)
# print(10//3)
# print(10 % 3)

# # Variáveis
# minha_variavel = "Olá, mundo!"
# print(minha_variavel)
# inteira = 1  # integer
# real = 1.1  # float
# textual = "Eu sou uma string"  # string
# booleana = True  # bool
# booleana = False  # bool
# print(inteira)
# print(real)
# print(textual)
# print(booleana)

# # Operadores relacionais
# var_x = 4
# var_y = 4
# print(var_x == var_y)
# var_x = 2
# var_y = 3
# print(var_x == var_y)
# print(var_x < var_y)
# soma = var_x + var_y
# print(soma < var_x)

# # Operadores lógicos
# var_x = 3
# var_y = 3
# var_z = 4
# print(var_x == var_y and var_x == var_z)
# print(var_x == var_y or var_x == var_z)
# print(var_x == var_y or var_x == var_z and var_z == var_y)

# # Estruturas condicionais
# var_x = 1
# var_y = 1000000
# if var_x > var_y:
#     print("X é maior que Y")
# elif var_y > var_x:
#     print("Y é maior que X")
# else:
#     print("X é igual a Y")

# var_x = 1
# var_y = 1
# if var_x > var_y:
#     print("X é maior que Y")
# elif var_y > var_x:
#     print("Y é maior que X")
# else:
#     print("X é igual a Y")

# Estruturas de repetição
var_x = 1
while var_x < 10:
    print(var_x, end=" ")
    var_x += 1

lista1 = [1, 2, 3, 4, 5]
lista2 = ["Olá", "Mundo", "!"]
lista3 = [0, "Olá", "biscoito", 9.87, True]

for elem in lista1:
    print(elem, end=" ")
print()

for elem in lista2:
    print(elem, end=" ")
print()

for elem in lista3:
    print(elem, end=" ")
print()

for i in range(10, 20, 2):
    print(i, end=" ")
print()
