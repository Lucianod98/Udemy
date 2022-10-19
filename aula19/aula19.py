'''
FOR / ELSE em Python
'''

variavel = ["Gabriel otavio","Luciano duarte","Maria fernandes"]

#for valor in variavel:
#     if valor.startswith("l"):
#         print("começa com L", valor)
#     else:
#         print("não começa com L", valor)

# comeca_com_j = False
# for valor in variavel:
#     if valor.lower().startswith("l"):
#         comeca_com_j = True
#
# if comeca_com_j:
#     print("Existe uma palavra que começa com L.")
# else:
#     print("NÃO existe uma palavra que começa com L.")


for valor in variavel:
    if valor.lower().startswith("l"):
        continue
    print(valor)





