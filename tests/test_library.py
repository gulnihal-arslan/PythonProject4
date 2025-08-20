import pytest
from fastapi.testclient import TestClient
from api import app
from library import Library
from book import Book

client = TestClient(app)

def test_add_valid_book(monkeypatch):
    lib = Library()
    class DummyResponse:
        def raise_for_status(self): pass
        def json(self):
            return {"title": "Dummy Kitap", "authors": [{"key": "/authors/OL1A"}]}
    class DummyAuthorResponse:
        def raise_for_status(self): pass
        def json(self): return {"name": "Dummy Yazar"}
    import httpx
    def fake_get(url):
        if "authors" in url: return DummyAuthorResponse()
        return DummyResponse()
    monkeypatch.setattr(httpx, "get", fake_get)
    lib.add_book("1234567890")
    assert lib.books[0].title == "Dummy Kitap"
    assert "Dummy Yazar" in lib.books[0].author

def test_invalid_isbn(monkeypatch):
    lib = Library()
    class DummyResponse:
        def raise_for_status(self):
            from httpx import HTTPStatusError, Response
            raise HTTPStatusError("Not Found", request=None, response=Response(status_code=404))
        def json(self): return {}
    import httpx
    monkeypatch.setattr(httpx, "get", lambda url: DummyResponse())
    lib.add_book("invalidisbn")
    assert len(lib.books) == 0

def test_api_endpoints(monkeypatch):
    # POST book
    def fake_add_book(self, isbn):
        self.books.append(Book("Fake Kitap", "Fake Yazar", isbn))
    monkeypatch.setattr(Library, "add_book", fake_add_book)

    resp = client.post("/books", json={"isbn": "123"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["title"] == "Fake Kitap"

    # GET books
    resp = client.get("/books")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

    # DELETE book
    resp = client.delete("/books/123")
    assert resp.status_code == 200
