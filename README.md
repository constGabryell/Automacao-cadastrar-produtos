# Automa-o-cadastrar-produtos
# Automação de Cadastro de Produtos

Projeto desenvolvido em Python para automatizar o cadastro de produtos em um formulário web.

A automação lê os dados de um arquivo CSV utilizando a biblioteca Pandas e preenche automaticamente os campos do formulário com PyAutoGUI.

## Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas
- CSV

## Como funciona

1. O programa lê os produtos armazenados no arquivo `produtos.csv`.
2. Abre o navegador automaticamente.
3. Acessa a página de cadastro.
4. Realiza o login.
5. Percorre os produtos da tabela.
6. Preenche os campos do formulário automaticamente.
7. Envia cada produto para o sistema.

## Exemplo de dados

O arquivo CSV possui informações como:

- Código do produto
- Marca
- Tipo
- Categoria
- Preço
- Custo
- Observação

## Como executar

Instale as dependências:

```bash
pip install pandas pyautogui
```
Depois execute:
```
python main.py
