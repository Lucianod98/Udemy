"""
usuario = input("digite seu usuário: ")
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print("você precisa digitar pelo menos 6 caracteres")
else:
    print("você foi cadastrado no sistema")
"""
'''''
string1 = input("digite alguma coisa: ")
string2 = input("digite outra coisa: ")

print(f"A quantidade total de caracteres digitados foi {len(string1) + len(string2)}")
print(f"A quantidade total de caracteres digitados foi {(string1.__len__()) + (string2.__len__())}")
'''
