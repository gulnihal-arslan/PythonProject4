import httpx
from book import Book

class Library:
    """Kütüphane işlemlerini yönetir."""

    def __init__(self):
        self.books = []

    def add_book(self, isbn: str):
        """ISBN ile Open Library'den kitap çekip ekler."""
        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url)
            response.raise_for_status()
            data = response.json()

            title = data.get('title', 'Başlık bulunamadı')
            authors_data = data.get('authors', [])
            authors = []

            for author in authors_data:
                author_url = f"https://openlibrary.org{author['key']}.json"
                author_resp = httpx.get(author_url)
                author_resp.raise_for_status()
                author_info = author_resp.json()
                authors.append(author_info.get('name', 'Yazar bilgisi yok'))

            book = Book(title=title, author=", ".join(authors), isbn=isbn)
            self.books.append(book)
            print(f"Kitap eklendi: {book}")

        except httpx.HTTPStatusError:
            print("Kitap bulunamadı. Geçersiz ISBN veya API hatası.")
        except httpx.RequestError:
            print("API isteği sırasında bir hata oluştu. İnternet bağlantınızı kontrol edin.")

    def remove_book(self, isbn: str):
        """ISBN'e göre kitabı siler."""
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            print(f"'{book.title}' kütüphaneden silindi.")
            return True
        return False

    def list_books(self):
        """Kütüphanedeki tüm kitapları listeler."""
        return self.books

    def find_book(self, isbn: str):
        """ISBN ile kitap bulur."""
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
