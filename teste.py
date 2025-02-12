import json
import os

# Nome do arquivo onde os dados dos usuários serão armazenados
USUARIOS_ARQUIVO = 'usuarios.json'

def carregar_usuarios():
    if os.path.exists(USUARIOS_ARQUIVO):
        with open(USUARIOS_ARQUIVO, 'r') as arquivo:
            return json.load(arquivo)
    return {}

def salvar_usuarios(usuarios):
    with open(USUARIOS_ARQUIVO, 'w') as arquivo:
        json.dump(usuarios, arquivo)

def cadastrar_usuario(username, senha):
    usuarios = carregar_usuarios()
    if username in usuarios:
        return False
    usuarios[username] = senha
    salvar_usuarios(usuarios)
    return True

def autenticar_usuario(username, senha):
    usuarios = carregar_usuarios()
    if username in usuarios and usuarios[username] == senha:
        return True
    return False

def main():
    while True:
        print("\nMenu:")
        print("1. Cadastrar usuário")
        print("2. Fazer login")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            username = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            if cadastrar_usuario(username, senha):
                print("Usuário cadastrado com sucesso!")
            else:
                print("Erro: Nome de usuário já existe.")
        
        if escolha == '2':
            username = input("Digite o nome de usuário: ")
            senha = input("Digite a senha: ")
            if autenticar_usuario(username, senha):
                print("Login bem-sucedido!")
            else:
                print("Erro: Nome de usuário ou senha incorretos.")

        if escolha == '3':
            print("Saindo...")
            break

if __name__ == "__main__":
    main()