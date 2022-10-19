'''
Split, Join e Enumerate em Python
'''

#SPLIT

# string = "O Brasil é o o o país do futebol, o Brasil é penta."
# lista_1 = string.split(" ")
# lista_2 = string.split(",")
# #print(lista_2)
#
# for cada in lista_2:
#     print(cada.strip( ).capitalize())
# palavra =""
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
# # print(f"A palavra {valor} apareceu {lista_1.count(valor)}x na frase.")
# print(f"a palavra que apareceu mais vezes é {palavra} ({contagem}x)")

#JOIN

# string = "o brasil é penta"
# lista = string.split(" ")
# string2 = " ".join(lista)
#
# print(string)
# print(lista)
# print(string2)

#ENUMERATE

# string = "o brasil é penta"
# lista = string.split(" ")
#
# for indice,valor in enumerate(lista):
#     print(indice,valor,lista[indice])

# lista = [
#     [0,"luiz"],
#     [1,"joao"],
#     [2,"maria"],
# ]
#
# for indice,nome in lista:
#     print(indice,nome)

lista = ["luiz","joao","maria"]

n1,n2,n3 = lista

print(n2)

for indice,nome in enumerate(lista):
    print(indice,nome)