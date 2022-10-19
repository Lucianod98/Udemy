'''
Iterando strings com while em Python
'''

#       Índices
#       01234567890.......................33

frase ="o rato roeu a roupa do rei de roma " # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ""
input_do_usuario = input("Qual letra deseja colocar maiúscula: ")

# Iteração <- Iterar
while contador < tamanho_frase:
    #print(frase[contador], contador)
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    #nova_string += frase[contador]
    contador += 1
print(nova_string)
