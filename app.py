# PROJETO 6 - SISTEMA DE LOGIN
import os

lista = []

# Funções
def cadastrar_usuario():
    nome = input('Nome para novo usuário: ')
    senha = input('Senha par o novo usuário: ')
    with open('cadastro.txt','a',encoding='utf-8',newline='') as arquivo:
        arquivo.write(f'{nome},{senha}'+ os.linesep)
    return nome

def consultar_usuario(usuario,senha):
    with open('cadastro.txt','r',encoding='utf-8',newline='') as arquivo:
        for linha in arquivo:
            lista.append(linha)
    return lista




# Criação de menu principal

print('BEM-VINDO A ESTE SISTEMA\nEscolha uma opção: \n[1] - Fazer login\n[2] - Cadastrar novo usuário')
opcao = input('Digite a sua opção: ')
if opcao == "1":
    usuario = input('Digite o seu usuário: ')
    senha = input('Digite a sua senha: ')
    lista = consultar_usuario(usuario,senha)
    print(lista)
    
if opcao == '2':
    nome = cadastrar_usuario()
    print(f'Usuário {nome} criado com sucesso!')



