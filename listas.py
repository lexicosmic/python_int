# -*- coding: utf-8 -*-

minha_lista = ["Mamão", "Melancia", "Açaí"]
minha_lista2 = [1, 4, 2, 6, 3]
minha_lista3 = ["Ana", 78, "Banana", 87.7]
minha_lista4 = []

print(len(minha_lista))

for item in minha_lista2:
    print(item, end=" ")
print()

minha_lista.append("Banana")
print(minha_lista)

if 78 in minha_lista3:
    print("Minha lista 2 possui o número 78")

del (minha_lista2[2:4])
print(minha_lista2)

minha_lista4.append(57)
print(minha_lista4)
