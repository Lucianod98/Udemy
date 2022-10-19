nome = "Luciano"
idade = 24
altura = 1.69
peso = 80.0
ano = 2022
nasc = ano - idade
imc = peso / altura ** 2

print(f"{nome} tem {ano-nasc} anos e {altura} de altura e pesa {peso}Kg.")
print(f"O IMC de {nome} é {imc:.2f}.")
print(f"{nome} nasceu em {nasc}.")
