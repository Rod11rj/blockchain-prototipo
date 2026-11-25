# Comunicação Baseada em Blockchain (C3I)

DOI 10.5281/zenodo.24537055

Protótipo de chat em Python no qual cada mensagem trocada é um bloco de uma blockchain, como camada adicional de segurança para sistemas de Comando, Controle, Comunicações e Inteligência (C3I). Inclui versão em terminal e versão com interface gráfica (Tkinter). Código desenvolvido no Trabalho de Conclusão de Curso *"Aplicabilidade da Tecnologia do Blockchain na Marinha do Brasil"* (CIAA, 2023).

## Conteúdo

|Arquivo|Descrição|
|-|-|
|`blockchain.py`|Classes `Bloco` e `Blockchain` (Apêndice C)|
|`criar\_usuario.py`|Cria usuário e grava o hash SHA-256 da senha em `usuarios.txt` (Apêndice D)|
|`valida\_login.py`|Valida usuário/senha comparando o hash da senha informada (Apêndice E)|
|`cria\_blockchain.py`|Mensagens de instrução e laço do chat sobre a blockchain (Apêndice F)|
|`executavel.py`|Ponto de entrada da versão em terminal (Apêndice G)|
|`terminal\_grafico.py`|Versão com interface gráfica em Tkinter (Apêndice H)|

## Premissas

* Usuários e senhas são criados apenas por uma Organização Militar (OM) específica, com `criar\_usuario.py`; apenas o hash da senha é armazenado.
* Cada usuário é identificado por um trigrama por missão.
* Cada mensagem enviada corresponde a um bloco da blockchain.
* Comandos no chat: `ler` (lê a conversa), `status` (verifica a validade da blockchain), `sair` (encerra o chat).

## Requisitos e execução

* Python 3 (biblioteca padrão; a interface gráfica usa `tkinter`, que acompanha a maioria das instalações do Python – no Linux pode ser necessário instalar o pacote `python3-tk`).
1. Crie um usuário (gera `usuarios.txt`):

```bash
   python criar\_usuario.py
   ```

2. Versão em terminal:

```bash
   python executavel.py
   ```

3. Versão gráfica:

```bash
   python terminal\_grafico.py
   ```

O arquivo `usuarios.txt` está no `.gitignore` para que hashes de senhas não sejam publicados.

> Protótipo acadêmico/didático: a blockchain é mantida em memória em um único processo. Não use em produção sem as devidas adaptações.

## 

## Como citar

Veja `CITATION.cff` (o GitHub mostra o botão *Cite this repository*). Trabalho de origem:

ALMEIDA, Rodrigo Antonio Ribeiro de. **Aplicabilidade da tecnologia do blockchain na Marinha do Brasil**. 2023. Trabalho de Conclusão de Curso (Curso de Aperfeiçoamento Avançado em Segurança da Informação e Comunicações) – Centro de Instrução Almirante Alexandrino (CIAA), Marinha do Brasil, Rio de Janeiro, 2023. Orientadores: Prof. Dr. Carlos Vinicio Rodriguez; Capitão-Tenente Warlley Paulo Freire.

## Licença

MIT – veja `LICENSE`.

