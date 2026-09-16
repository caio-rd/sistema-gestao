Sistema de Gestão de Clientes e Serviços

Sistema web desenvolvido em Flask e SQLite para gestão de clientes e serviços, com autenticação de usuários e dashboard de estatísticas. Projeto criado como forma de aplicar na prática conhecimentos de Python e desenvolvimento web.

Funcionalidades
Autenticação de usuários: login com sessões protegidas, controle de acesso por usuário (multi-tenant)
CRUD de Clientes: cadastro, edição, listagem e exclusão de clientes
CRUD de Serviços: gestão de serviços vinculados a cada cliente
Dashboard: estatísticas gerais via consultas SQL (COUNT, SUM)
Tecnologias utilizadas
Back-end: Python, Flask
Banco de dados: SQLite
Front-end: HTML, CSS
Como executar o projeto
Clone o repositório:
   git clone https://github.com/caio-rd/sistema-gestao.git
   cd sistema-gestao
Crie e ative um ambiente virtual:
   python -m venv venv
   venv\Scripts\Activate.ps1   # Windows (PowerShell)
Instale as dependências:
   pip install -r requirements.txt
Execute a aplicação:
   python app.py
Acesse no navegador:
   http://localhost:5000
Estrutura do projeto
sistema-gestao/
├── app.py                 # Arquivo principal da aplicação
├── banco.db                # Banco de dados SQLite
├── requirements.txt         # Dependências do projeto
├── routes/                  # Rotas da aplicação (auth, clientes, dashboard, serviços)
├── static/                  # Arquivos estáticos (CSS)
└── templates/                # Templates HTML (login, dashboard, clientes, serviços)
Autor

Desenvolvido por Caio Rodrigues.
