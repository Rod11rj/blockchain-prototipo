import blockchain

def estrutura_chat():
    print('\n ===================== \n')
    print('    Acesso liberado')
    print('\n ===================== \n')
    print("    Instrucoes:")
    print("    Para ler as mensagens digite 'ler'")
    print("    Para consultar validade da blockchain digite 'status'")
    print("    Para sair do chat digite 'sair'")
    print('\n ===================== \n')

def estrutura_conversa():
    print('\n ===================== \n')
    print('      CONVERSA')

def define_blockchain(usuario_login):
    comunicacao_baseada_em_blockchain = blockchain.Blockchain(usuario_login)

    estrutura_chat()

    while True:
        msg = input('Mensagem: ')

        if msg == 'sair':
            print('Chat Encerrado!')
            break

        if msg == 'status':
            status = comunicacao_baseada_em_blockchain.verifica_validade_bloco()
            if status == True:
                print('blockchain VALIDA')
            else:
                print('blockchain INVALIDA')

        elif msg == 'ler':
            estrutura_conversa()
            for bloco in comunicacao_baseada_em_blockchain.corrente:
                print(f"Data-Hora: {bloco.datahora}")
                print(f"Remetente: {bloco.usuario}")
                print(f"Mensagem: {bloco.msg}")
                print("\n")

        comunicacao_baseada_em_blockchain.adiciona_bloco(msg)

if __name__ == '__main__':
    pass
