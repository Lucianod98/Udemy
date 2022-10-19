'''
Índices e fatiamento de strings em Python
'''
# positivos   [0123456789]
texto       = "Python_s2"
# negativos  -[987654321]
print(texto[8])

url = "www.google.com.br/"
print(url[:-1])

nova_string = texto[-9:-3]
nova_string2 = texto[0::2]
print(len(texto),nova_string,nova_string2)


