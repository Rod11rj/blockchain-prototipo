import valida_login
import cria_blockchain

if __name__ == '__main__':
    print('Login')
    usuario_login = input('Usuario: ').upper()
    senha_login = input('Senha: ')

    if valida_login.valida_login(usuario_login,senha_login):
        print('Login Bem-Sucedido')
        cria_blockchain.define_blockchain(usuario_login)
    else:
        print('Usuario/senha incorretos.')
