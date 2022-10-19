'''
Estrutura de repetição em Python
'''

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         break
#     print(x)
#     x = x + 1
# print("Acabou!")

# x = 0
#
# while x < 10:
#     y = 0
#     while y < 5:
#         print(f"({x},{y})")
#         y += 1
#     x += 1
#
# print("acabou!")

while True:
    print()
    num_1 = input("Digite um Número: ")
    num_2 = input("Digite um outro Número: ")
    operador = input("Digite um operador: ")
    sair = input("Deseja sair? [s]sim ou [n]não:")

    if sair == "s":
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("você precisa digitar um número.")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == "+":
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == "*":
        print(num_1 * num_2)
    elif operador == "/":
        print(num_1 / num_2)
    else:
        print("operador invalido")