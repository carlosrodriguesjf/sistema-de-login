# PROJETO 6 - SISTEMA DE LOGIN
import os

lista = []

# Funções
def cadastrar_usuario():
    nome = input('Nome para novo usuário: ')
    senha = input('Senha para o novo usuário: ')
    with open('cadastro.txt','a',encoding='utf-8',newline='') as arquivo:
        arquivo.write(f'{nome},{senha}'+ os.linesep)
    return nome

def consultar_usuario(usuario,senha):
    with open('cadastro.txt','r',encoding='utf-8',newline='') as arquivo:
        for linha in arquivo:
            lista.append(linha)
    for i in range(0,len(lista)):
        usuarios = lista[i].split(',')
        nome_usuario = usuarios[0]
        senha_previa = usuarios[1].split('\r')
        senha_usuario = senha_previa[0]
        if usuario == nome_usuario and senha == senha_usuario:
            resultado = 'certo'
        else:
            resultado = 'erro'
    return resultado


# Criação de menu principal
while True:
    print('BEM-VINDO A ESTE SISTEMA\nEscolha uma opção: \n[1] - Fazer login\n[2] - Cadastrar novo usuário')
    opcao = input('Digite a sua opção: ')
    if opcao == "1":
        usuario = input('Digite o seu usuário: ')
        senha = input('Digite a sua senha: ')
        logon = consultar_usuario(usuario,senha)
        
        if logon == 'certo':
            print(f'Bem-vindo {usuario}! Login efetuado com sucesso!') 
            print('')
            break
        else:
            print('Usuário ou senha incorreta!')
            print('')
        
    if opcao == '2':
        nome = cadastrar_usuario()
        print(f'Usuário {nome} criado com sucesso!')
        print('')
        break


