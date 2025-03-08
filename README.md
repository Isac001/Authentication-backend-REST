# Authentication-backend-REST

Este repositório demonstra como criar uma API capaz de realizar autenticação de usuários utilizando Django REST Framework.

## Sumário

- [Introdução](#introdução)
- [Primeiros Passos](#primeiros-passos)
  - [Configurações do Ambiente](#configurações-do-ambiente)
    - [Pré-requisitos](#pré-requisitos)
    - [Instalação](#instalação)
- [Uso](#uso)

## Introdução

A autenticação de usuários é um aspecto essencial para sistemas seguros. Este projeto visa fornecer um exemplo simples de como implementar autenticação de usuários em uma API REST utilizando Django REST Framework.

## Primeiros Passos

### Configurações do Ambiente

#### Pré-requisitos

Antes de iniciar, certifique-se de que possui os seguintes requisitos instalados:

| Requisitos | Recomendações |
| --- |---|
| Sistema Operacional | Windows, macOS ou Linux |
| Python | Versão 3.11 ou superior |
| Banco de Dados | PostgreSQL |
| Git | Para controle de versão |

#### Instalação

Clone o repositório e navegue até a pasta do projeto:

```bash
git clone https://github.com/SeuUsuario/Autentica-o-Simples-com-Django-REST.git
cd Autentica-o-Simples-com-Django-REST
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv env
source env/bin/activate  # No Windows use: env\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Configuração do Banco de Dados

Inicie o PostgreSQL e configure o banco de dados:

```bash
sudo service postgresql start
sudo -u postgres psql
```

No prompt do PostgreSQL, crie o banco de dados e o usuário:

```sql
CREATE DATABASE auth;
CREATE USER auth WITH PASSWORD 'root';
GRANT ALL PRIVILEGES ON DATABASE auth TO auth;
```

Saia do prompt do PostgreSQL com `\q`.

Caso seja necessário, conceda permissões adicionais:

```bash
sudo -u postgres psql -d auth
```

```sql
GRANT ALL PRIVILEGES ON SCHEMA public TO auth;
```

Para sair, digite `\q`.

## Uso

### Inicialização do Servidor

Com o ambiente configurado, ative a venv e aplique as migrações:

```bash
source env/bin/activate  # No Windows use: env\Scripts\activate
python3 manage.py migrate
```

Caso queira popular o banco de dados com dados iniciais:

```bash
python3 manage.py loaddata fixtures.json
```

Inicie o servidor:

```bash
python3 manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

Agora sua API de autenticação está pronta para uso!

