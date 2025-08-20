class Book:
    """Kütüphanedeki tek bir kitabı temsil eder."""

    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False  # Kitap ödünç verilmiş mi?

    def borrow_book(self):
        """Kitabı ödünç alındı olarak işaretler."""
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            raise ValueError(f"'{self.title}' zaten ödünç verilmiş.")

    def return_book(self):
        """Kitabı iade edildi olarak işaretler."""
        if self.is_borrowed:
            self.is_borrowed = False
        else:
            raise ValueError(f"'{self.title}' ödünç alınmamıştı.")

    def __repr__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
