# -*- coding: utf-8 -*-

# # Leitura
# arquivo = open("arquivo.txt")

# linhas = arquivo.readlines()

# for linha in linhas:
#     print(linha)

# texto_completo = arquivo.read()
# print(texto_completo)
# arquivo.close()

# Escrita
arquivo2 = open("arquivo2.txt", "w")
arquivo2.write("Este é o meu outro arquivo\n")
arquivo2.close()
arquivo2 = open("arquivo2.txt", "a")
arquivo2.write("Estou escrevendo uma nova linha\n")
arquivo2.close()
