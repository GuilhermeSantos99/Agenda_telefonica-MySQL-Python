# Agenda telefônica (MySQL/Python)

> Status: Em desenvolvimento.

## Projeto de agenda telefônica
O código, escrito em Python, utiliza o banco de dados MySQL para armazenar os dados informados.
Utiliza-se a biblioteca "mysql-connector-python" na sua versão 8.0.27 para realizar a conexão entre o script e o banco de dados.
Na construção da sua GUI, utiliza-se a biblioteca "Tkinter".

### Funcionalidades
+ Salvar nome e número telefônico.
+ Limpar campos através de um botão.

> Futuras funções:
> Deletar contatos.
> Consultar contatos salvos.
> Modificar informações.

### Requisitos
+ Python3 instalado na máquina.
+ Uma IDE ou outra ferramenta semelhante para executar o código.
+ Banco de dados MySQL instalado e configurado na máquina.
+ Adicionar a biblioteca "mysql-connector-python" com o comando "pip install mysql-connector-python"

### Modo de uso:
+ Crie o banco de dados, utilizando o código do arquivo "banco_de_dados.sql".
+ Insira o seu user(linha 7) e password(linha 8).
+ Rode o código.
+ Insira o nome no primeiro entry e o telefone no segundo.
Após isso os dados são adicionados ao banco.