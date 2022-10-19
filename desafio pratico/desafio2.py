'''
# Atividade 1
num = input("Digite um número: ")

try:
    num = int(num)
    if (num % 2) == 0:
        print(f"{num} É par")
    else:
        print(f"{num} É ímpar")

except:
    print("Isso não é um numero inteiro")
'''

'''
# Atividade 2
horas = input("Digite as horas: ")

try:
    horas = int(horas)
    if horas <= 11:
        print("bom dia!")
    elif horas <= 17:
        print("boa tarde!")
    elif horas <= 23:
        print("boa noite!")
    else:
        print("Horário deve estar entre 0 e 23")

except:
    print("Por favor,digite um horário entre o e 23")
'''
'''
# Atividade 3

nome = input("Digite seu nome: ")

try:
    tamanho = len(nome)
    if tamanho <= 4:
        print("seu nome é curto")
    elif tamanho <= 6:
        print("seu nome é normal")
    else:
        print("seu nome é muito grande")

except:
    print("Isso não é um numero inteiro")
'''