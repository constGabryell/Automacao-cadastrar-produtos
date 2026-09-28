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
4. Realiza o login em um ambiente de treinamento.
5. Percorre os produtos da tabela.
6. Preenche os campos do formulário automaticamente.
7. Envia cada produto para o sistema.

## Estrutura do projeto

- `main.py`: executa a automação principal.
- `auxiliar.py`: auxilia na identificação das coordenadas do mouse.
- `produtos.csv`: contém os dados dos produtos.
- `requirements.txt`: contém as dependências do projeto.

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
pip install -r requirements.txt
```

Depois execute:

```bash
python main.py
```

## Observações

A automação utiliza coordenadas da tela para realizar alguns cliques. Por isso, pode ser necessário ajustar as coordenadas dependendo da resolução ou configuração do computador.

As credenciais utilizadas no projeto pertencem a um ambiente de treinamento e são usadas apenas para simulação.

## Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar Python e aplicar conceitos de automação, manipulação de dados e controle de mouse e teclado.
