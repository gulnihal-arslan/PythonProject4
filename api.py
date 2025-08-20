from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library import Library

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
def get_books():
    return [
        BookResponse(
            title=b.title,
            author=b.author,
            isbn=b.isbn,
            borrowed=b.is_borrowed
        ) for b in library.list_books()
    ]

# POST /books
@app.post("/books", response_model=BookResponse)
def post_book(request: ISBNRequest):
    before_count = len(library.books)
    library.add_book(request.isbn)
    after_count = len(library.books)

    if before_count == after_count:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")

    book = library.books[-1]
    return BookResponse(
        title=book.title,
        author=book.author,
        isbn=book.isbn,
        borrowed=book.is_borrowed
    )

# DELETE /books/{isbn}
@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    if library.remove_book(isbn):
        return {"message": f"ISBN {isbn} kitap silindi."}
    raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
