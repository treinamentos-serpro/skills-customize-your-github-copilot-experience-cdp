from copy import deepcopy

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

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


INITIAL_BOOKS = [
    Book(id=1, title="O Jardim Secreto", author="Frances Hodgson Burnett", year=1911),
    Book(id=2, title="A Ilha do Tesouro", author="Robert Louis Stevenson", year=1883),
]
books = deepcopy(INITIAL_BOOKS)


@app.get("/books", response_model=list[Book])
def list_books():
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Livro nao encontrado")


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput):
    next_id = max((book.id for book in books), default=0) + 1
    book = Book(id=next_id, title=book_input.title, author=book_input.author, year=book_input.year)
    books.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    for index, book in enumerate(books):
        if book.id == book_id:
            updated_book = Book(
                id=book_id,
                title=book_input.title,
                author=book_input.author,
                year=book_input.year,
            )
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Livro nao encontrado")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Livro nao encontrado")
