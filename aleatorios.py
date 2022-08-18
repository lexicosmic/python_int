import random

numero = random.randint(0, 10)
print(numero)

lista = [1, 7, 4, -6, 3]
numero = random.choice(lista)
print(numero)

random.seed(1)
numero = random.randint(0, 10)
print(numero)
