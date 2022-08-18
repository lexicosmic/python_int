# -*- coding: utf-8 -*-

#  List comprehension
lista1 = [1, 2, 3, 4, 5]
lista2 = [i**2 for i in lista1]
lista3 = [i for i in lista1 if i % 2 != 0]

print("Usando list comprehension")
print(lista1)
print(lista2)
print(lista3)
