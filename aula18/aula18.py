'''
Listas em Python
'''
#         0   1   2   3   4   5
# lista = ["A","B","C","D","E",10.5]
#
# print(lista[::-1])

# l1 = [1,2,3]
# l2 = [4,5,6]
# print(l2)
# l1.extend("a")
# l2.append("b")
# l2.insert(0,"banana")
# print(l2)
# l2.pop()
# print(l2)

#     0 1 2 3 4 5 6 7 8
# l2 = [1,2,3,4,5,6,7,8,9]
# print(l2)
# l2.insert(0,"banana")
# print(l2)
# del(l2[0])
# print(l2)
# print(max(l2))
# print(min(l2))

# l2 = [0,1,2,3,4,5,6,7,8,9]
#
# soma = 0
# for valor in l2:
#     soma = soma + valor
# print(soma)

# l2 = ["string", True , 10, -20.5]
#
# for elem in l2:
#     print(f"o tipo de elem é {type(elem)} e seu valor é {elem}")

secreto = "perfume"
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print("suas tentativas acabaram, você perdeu!!")
        break


    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("isso não vale, digite apenas uma letra!")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f"UHUULLL, a letra '{letra}' existe na palavra secreta.")
    else:
        print(f" poxaa, a letra '{letra}' não existe na palavra secreta, você ainda tem {chances} tentativas! ")
        digitadas.pop()

    secreto_teporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_teporario += letra_secreta
        else:
            secreto_teporario += "*"

    if secreto_teporario == secreto:
        print(f"que legal você ganhou o jogo!! a palavra era {secreto_teporario}!")
        break
    else:
        print(f"a palavra secreta está assim: {secreto_teporario}")

    if letra not in secreto:
        chances -= 1