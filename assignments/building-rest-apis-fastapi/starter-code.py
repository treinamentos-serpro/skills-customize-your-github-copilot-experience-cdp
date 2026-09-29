from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="API de Livros")


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


class BookInput(BaseModel):
    title: str
    author: str
    year: int


books = [
    Book(id=1, title="O Jardim Secreto", author="Frances Hodgson Burnett", year=1911),
    Book(id=2, title="A Ilha do Tesouro", author="Robert Louis Stevenson", year=1883),
]


@app.get("/books", response_model=list[Book])
def list_books():
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: encontre o livro pelo identificador e responda 404 se ele nao existir.
    raise NotImplementedError


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput):
    # TODO: crie um identificador, adicione o livro a colecao e retorne o novo livro.
    raise NotImplementedError


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    # TODO: atualize os dados do livro ou responda 404 se ele nao existir.
    raise NotImplementedError


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: remova o livro ou responda 404 se ele nao existir.
    raise NotImplementedError


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
