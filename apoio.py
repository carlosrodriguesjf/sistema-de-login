import os

lista = []


def consultar_usuario(usuario,senha):
    with open('cadastro.txt','r',encoding='utf-8',newline='') as arquivo:
        for linha in arquivo:
            lista.append(linha)
    return lista


# Criação de menu principal

lista = consultar_usuario(usuario,senha)


for i in range(0,len(lista)):
    usuarios = lista[i].split(',')
    nome_usuario = usuarios[0]
    senha_previa = usuarios[1].split('\r')
    senha_usuario = senha_previa[0]
    if usuario == nome_usuario and senha == senha_usuario:
        print('Login Efetuado com sucesso')
        break
    else:
        print('Login ou senha incorreta')
    









