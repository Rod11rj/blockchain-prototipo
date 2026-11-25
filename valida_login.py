import hashlib

def valida_login(usuario, senha):

    with open('usuarios.txt', 'r') as arquivo_de_usuarios:

        for linha in arquivo_de_usuarios:
            usr,passwd = linha.strip().split(':')

            hash_senha = hashlib.sha256(senha.encode()).hexdigest()

            if usuario == usr and hash_senha == passwd:
                return True
    return False
