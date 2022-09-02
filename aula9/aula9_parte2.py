'''
num_1 = 2
num_2 = 2

var_1 = "Luiz"
var_2 = "otávio"

expressao = (var_1 == var_2)
print(expressao)
'''

nome = input("qual o seu nome? ")
idade = input("qual sua idade? ")

idade = int(idade)

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f"{nome} pode pegar o empréstimo")
else:
    print(f"{nome} não pode pegar o empréstimo!")