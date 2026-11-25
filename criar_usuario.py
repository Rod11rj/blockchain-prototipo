import hashlib

def criar_ususario():

    usuario = input('Informe o nome desejado para o usuario: ').upper()
    senha = input('Informe a senha desejada: ')

    hash_senha = hashlib.sha256(senha.encode()).hexdigest()

    with open('usuarios.txt', 'a') as arquivo_de_usuarios:
        arquivo_de_usuarios.write(f'{usuario}:{hash_senha}\n')

    print('Usuario Criado!')

criar_ususario()
