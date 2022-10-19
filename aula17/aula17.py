'''
For in - Estrutura de repetição em Python
'''

texto = "python"
nova_string = ""
#
# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# for n, letra in enumerate(texto):
#     print(n,letra)

# for n in range(0,100,8):
#     print(n)
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)

for letra in texto:
    if letra == "t":
        nova_string = nova_string + letra.upper()
    elif letra == "h":
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)
