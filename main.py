from library import Library

def main():
    library = Library()
    while True:
        print("\n--- Kütüphane Menüsü ---")
        print("1. Kitap Ekle (ISBN ile)")
        print("2. Kitap Sil")
        print("3. Kitapları Listele")
        print("4. Kitap Ara")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            isbn = input("Kitabın ISBN numarasını girin: ")
            library.add_book(isbn)

        elif choice == "2":
            isbn = input("Silinecek kitabın ISBN: ")
            if not library.remove_book(isbn):
                print(f"ISBN {isbn} ile kitap bulunamadı.")

        elif choice == "3":
            books = library.list_books()
            if not books:
                print("Kütüphane boş.")
            for book in books:
                print(book)

        elif choice == "4":
            isbn = input("Aranacak kitabın ISBN: ")
            book = library.find_book(isbn)
            if book:
                print(book)
            else:
                print(f"ISBN {isbn} ile kitap bulunamadı.")

        elif choice == "5":
            print("Programdan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, tekrar deneyin.")

if __name__ == "__main__":
    main()
