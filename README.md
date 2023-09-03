# Desafio Backend Fábrica de Software

## Após a semana de treinamento, ao foi proposto um desafio com alguns requisitos:
- Funcionamento das operações (get, post, put e delete)
- Conexão com a sgbd a escolha (não podia usar o sqlite3)
- Mínimo 2 entedidades e relacionamento entre elas
- Criar um requirements.txt

## Alguns diferencias(opcional):
- Usar funções do DjangoRestFramework que não foram vista durante o treinamento.

#### O que eu usei durante o desenvolvimento:
- [x] python 3.11.5
- [x] django 4.2
- [x] DjangoRestFramework 3.14
- [x] Xampp Control Panel to ru MySQL

### Sobre o projeto:
- Desenvolvi uma aplicação para Cadastro de Alunos de uma Academia. Nela contém alguns campos de preenchimento como nome, idade, cpf.
- Nessa academia os alunos podiam fazer consultas com uma Nutricionista. Guardando alguns dados como peso, altura, imc e também podendo agendar um retorno.

#### Rodando o projeto:
- Clonar o repositório do git
- Entrar no ambiente virtual (venv) no terminal
- Instalar os requerimentos dando o comando: pip install -r requeriments.txt
- Abrir o Xampp e ativar o APACHE e MYSQL
- Usar o comando: python .\manage.py migrate
- Usar o comando: python .\manage.py runserver
- e abrir no navegador: http://127.0.0.1:8000/
