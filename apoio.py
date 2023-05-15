import os

lista = []


def consultar_usuario(usuario,senha):
    with open('cadastro.txt','r',encoding='utf-8',newline='') as arquivo:
        for linha in arquivo:
            lista.append(linha)
    return lista




# Criação de menu principal



usuario = 'ca'
senha = '232'
lista = consultar_usuario(usuario,senha)



i = 0
print(lista)
for i in range(0, len(lista)-1):
    nome = lista[i].split(',')
    print(nome[i])






