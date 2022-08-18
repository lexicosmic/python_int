# -*- coding: utf-8 -*-

# Dicionários
meu_dicionario = {"carro": "Fiat Palio", "cor": "Roxo", "placa": "HRK-7C78"}
print(meu_dicionario)

print(meu_dicionario["cor"])

for chave in meu_dicionario:
    print(chave)

for chave in meu_dicionario:
    print(chave + ": " + meu_dicionario[chave])

for item in meu_dicionario.items():
    print(item)

for valor in meu_dicionario.values():
    print(valor)
