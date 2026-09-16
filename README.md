# Sistema de Gestão de Clientes e Serviços

Sistema web desenvolvido em Flask e SQLite para gestão de clientes e serviços, com autenticação de usuários e dashboard de estatísticas. Projeto criado como forma de aplicar na prática conhecimentos de Python e desenvolvimento web.

## Funcionalidades

- **Autenticação de usuários**: login com sessões protegidas, controle de acesso por usuário (multi-tenant)
- **CRUD de Clientes**: cadastro, edição, listagem e exclusão de clientes
- **CRUD de Serviços**: gestão de serviços vinculados a cada cliente
- **Dashboard**: estatísticas gerais via consultas SQL (COUNT, SUM)

## Tecnologias utilizadas

- **Back-end**: Python, Flask
- **Banco de dados**: SQLite
- **Front-end**: HTML, CSS

## Como executar o projeto

1. Clone o repositório:

git clone https://github.com/caio-rd/sistema-gestao.git
cd sistema-gestao


2. Crie e ative um ambiente virtual:

python -m venv venv
venv\Scripts\Activate.ps1


3. Instale as dependências:

pip install -r requirements.txt


4. Execute a aplicação:

python app.py


5. Acesse no navegador:

http://localhost:5000


## Estrutura do projeto

sistema-gestao/
├── app.py
├── banco.db
├── requirements.txt
├── routes/
├── static/
└── templates/


## Autor

Desenvolvido por Caio Rodrigues.
