import tkinter as tk
import valida_login
import datetime

blockchain = []

def fazer_login():
    usuario = entry_usuario.get().upper()
    senha = entry_senha.get()

    if valida_login.valida_login(usuario, senha):
        janela_login.destroy()
        abrir_executavel(usuario)
    else:
        mensagem_login.config(text='Usuario/senha incorretos.')

def abrir_executavel(usuario):
    janela_executavel = tk.Tk()
    janela_executavel.title('CBB')
    janela_executavel.geometry('500x500')

    texto_saida = tk.Text(janela_executavel, height=10, width=10, wrap=tk.WORD)
    texto_saida.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(texto_saida)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    texto_saida.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=texto_saida.yview)

    caixa_texto = tk.Entry(janela_executavel)
    caixa_texto.pack(fill=tk.X)

    def processa_texto():
        texto = caixa_texto.get()
        if texto.lower() == 'ler':
            exibir_blockchain(texto_saida)
        else:
            atualizar_blockchain(usuario,texto)
            exibir_blockchain(texto_saida)
            caixa_texto.delete(0, tk.END)

    botao_processar = tk.Button(janela_executavel, text='Enviar', command=processa_texto)
    botao_processar.pack()

    caixa_texto.bind('<Return>', lambda event=None: processa_texto())

    janela_executavel.mainloop()

def exibir_blockchain(text_widget):
    text_widget.delete('1.0', tk.END)
    for bloco in blockchain:
        text_widget.insert(tk.END, bloco + '\n')

def atualizar_blockchain(usuario, texto):
    indice = len(blockchain) + 1
    timestamp = datetime.datetime.now()
    novo_bloco = f"Índice: {indice}\nTimestamp: {timestamp}\nRemetente: {usuario}\nMensagem: {texto}\n"
    blockchain.append(novo_bloco)

janela_login = tk.Tk()
janela_login.geometry("500x150")
janela_login.title("Login - Comunicacao Baseada em Blockchain")

label_usuario = tk.Label(janela_login, text="Usuario:")
label_usuario.pack()
entry_usuario = tk.Entry(janela_login)
entry_usuario.pack()

label_senha = tk.Label(janela_login, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(janela_login, show="*")
entry_senha.pack()


botao_login = tk.Button(janela_login, text="Login", command=fazer_login)
botao_login.pack()


mensagem_login = tk.Label(janela_login, text="")
mensagem_login.pack()


janela_login.mainloop()
