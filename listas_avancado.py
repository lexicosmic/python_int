# -*- coding: utf-8 -*-

# #  List comprehension
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [i**2 for i in lista1]
# lista3 = [i for i in lista1 if i % 2 != 0]

# print("Usando list comprehension")
# print(lista1)
# print(lista2)
# print(lista3)

# # Função enumerate
# lista1 = ["abacate", "bola", "cachorro"]
# for i, nome in enumerate(lista1):
#     print(f"{i}: {nome}")


# # Função map
# def dobro(x):
#     return x * 2


# valores = [1, 2, 3, 4, 5]
# valoresDobrados = map(dobro, valores)
# valoresDobrados = list(valoresDobrados)
# print(valoresDobrados)


# # Função reduce
# from functools import reduce


# def soma(x, y):
#     return x + y


# lista = [1, 3, 5, 10, 20]

# soma = reduce(soma, lista)
# print(soma)


# Função zip
lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$2,00", "R$5,00", "Não tem preço",
          "Não tem preço", "Não tem preço"]

for numero, nome, preco in zip(lista1, lista2, lista3):
    print(f"{numero}: {nome} - {preco}")
