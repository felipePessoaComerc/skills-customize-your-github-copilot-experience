# FastAPI REST API - Starter Code
# Assignment: Construindo APIs REST com FastAPI

# TODO: Importe as bibliotecas necessárias
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List, Optional

# TODO: Crie uma instância da aplicação FastAPI
# app = FastAPI(
#     title="Books API",
#     description="Uma API simples para gerenciar uma coleção de livros",
#     version="1.0.0"
# )

# TODO: Defina o modelo Pydantic para Book
# class Book(BaseModel):
#     id: int
#     title: str
#     author: str
#     year: int

# TODO: Crie uma lista em memória para armazenar os livros
# Dica: Comece com alguns livros de exemplo
books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 2, "title": "O Senhor dos Anéis", "author": "J.R.R. Tolkien", "year": 1954},
    {"id": 3, "title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899}
]

# TODO: Task 1 - Implemente os endpoints GET
# @app.get("/books")
# async def get_all_books():
#     """Retorna todos os livros"""
#     pass

# @app.get("/books/{book_id}")
# async def get_book(book_id: int):
#     """Retorna um livro específico por ID"""
#     pass

# TODO: Task 2 - Implemente os endpoints POST e PUT
# @app.post("/books", status_code=201)
# async def create_book(book: Book):
#     """Cria um novo livro"""
#     pass

# @app.put("/books/{book_id}")
# async def update_book(book_id: int, book: Book):
#     """Atualiza um livro existente"""
#     pass

# TODO: Task 3 - Implemente o endpoint DELETE
# @app.delete("/books/{book_id}")
# async def delete_book(book_id: int):
#     """Deleta um livro"""
#     pass

# Para executar a aplicação, use o comando:
# uvicorn starter-code:app --reload
# Acesse a documentação automática em: http://localhost:8000/docs
