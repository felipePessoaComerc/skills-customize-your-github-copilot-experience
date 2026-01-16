# 📘 Assignment: Construindo APIs REST com FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a construir APIs RESTful usando o framework FastAPI em Python. Você criará endpoints para gerenciar uma coleção de livros, implementando operações CRUD (Create, Read, Update, Delete) e trabalhando com validação de dados, tipos de resposta e documentação automática.

## 📝 Tasks

### 🛠️	Criar API Básica com Endpoints GET

#### Description
Crie uma aplicação FastAPI básica com endpoints para listar todos os livros e buscar um livro específico por ID. Use dados em memória (uma lista de dicionários) para armazenar as informações dos livros.

#### Requirements
Completed program should:

- Importar e instanciar a classe FastAPI
- Criar um endpoint GET `/books` que retorna uma lista de todos os livros
- Criar um endpoint GET `/books/{book_id}` que retorna um livro específico por ID
- Retornar erro 404 quando um livro não for encontrado
- Incluir pelo menos 3 livros de exemplo com campos: id, title, author, year


### 🛠️	Implementar Operações POST e PUT

#### Description
Expanda sua API para permitir a criação de novos livros e atualização de livros existentes. Use modelos Pydantic para validar os dados de entrada.

#### Requirements
Completed program should:

- Criar um modelo Pydantic `Book` com campos apropriados e validações
- Implementar endpoint POST `/books` para adicionar novos livros
- Implementar endpoint PUT `/books/{book_id}` para atualizar livros existentes
- Validar que os campos obrigatórios estejam presentes
- Retornar status code 201 para criação e 200 para atualização bem-sucedida


### 🛠️	Adicionar Operação DELETE e Melhorias

#### Description
Complete as operações CRUD adicionando a funcionalidade de deletar livros. Adicione também tratamento de erros apropriado, tipos de resposta e customize a documentação automática da API.

#### Requirements
Completed program should:

- Implementar endpoint DELETE `/books/{book_id}` para remover livros
- Retornar mensagens de erro apropriadas com status codes corretos
- Adicionar metadados à API (título, descrição, versão)
- Incluir response_model nos endpoints para documentação clara
- Testar todos os endpoints usando a interface Swagger UI automática (`/docs`)
