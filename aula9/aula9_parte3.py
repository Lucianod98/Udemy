'''
a = 2
b = 3


a = 'asdwdads'
b = 0


if b > a:
if not b > a:
    print('B é maior que A.')
else:
    print('A é maior que B.')

if not b:
    print('Por favor, preencha o valor de B')

nome = "Luiz Otávio"

if "vio" not in nome:
    print("Existe.")
else:
    print("não existe o texto.")
'''

usuario = input("nome de usuário: ")
senha = input("senha do usuário: ")

usuario_bd = "luiz"
senha_bd = "123456"

if usuario_bd == usuario and senha_bd == senha:
    print("você está logado no sistema")
else:
    print("Usuário ou senha inválidos")