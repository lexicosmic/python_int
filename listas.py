# -*- coding: utf-8 -*-

# # Básico
# minha_lista = ["Mamão", "Melancia", "Açaí"]
# minha_lista2 = [1, 4, 2, 6, 3]
# minha_lista3 = ["Ana", 78, "Banana", 87.7]
# minha_lista4 = []

# print(len(minha_lista))

# for item in minha_lista2:
#     print(item, end=" ")
# print()

# minha_lista.append("Banana")
# print(minha_lista)

# if 78 in minha_lista3:
#     print("Minha lista 2 possui o número 78")

# del (minha_lista2[2:4])
# print(minha_lista2)

# minha_lista4.append(57)
# print(minha_lista4)

# Ordenação
lista = [4, 67, 78, 3, -5, 0, -23]
print(sorted(lista))
print(lista)

lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

lista.reverse()
print(lista)

lista_textual = ["Mamão", "Melancia", "Açaí"]
print(lista_textual)
lista_textual.reverse()
print(lista_textual)
