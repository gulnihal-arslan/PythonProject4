from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library import Library  # Aşama 1 ve 2'de oluşturduğun sınıf

app = FastAPI(title="Kütüphane API", version="1.0")
library = Library()

# Pydantic modelleri
class ISBNRequest(BaseModel):
    isbn: str

class BookResponse(BaseModel):
    title: str
    author: str
    isbn: str
    borrowed: bool

# GET /books
@app.get("/books", response_model=list[BookResponse])
def list_books():
    return [
        BookResponse(
            title=b.title,
            author=b.author,
            isbn=b.isbn,
            borrowed=b.is_borrowed
        )
        for b in library.books
    ]

# POST /books
@app.post("/books", response_model=BookResponse)
def add_book(isbn_request: ISBNRequest):
    before_count = len(library.books)
    library.add_book(isbn_request.isbn)
    after_count = len(library.books)

    if before_count == after_count:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")

    added_book = library.books[-1]
    return BookResponse(
        title=added_book.title,
        author=added_book.author,
        isbn=added_book.isbn,
        borrowed=added_book.is_borrowed
    )

# DELETE /books/{isbn}
@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    for book in library.books:
        if book.isbn == isbn:
            library.books.remove(book)
            return {"message": f"ISBN {isbn} kitap silindi."}
    raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
