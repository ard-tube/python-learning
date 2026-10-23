"""
Library Database System — Learning OOP + SQLite
Author: Gökhan Arda Borulu
Topic: OOP, SQLite3, CRUD Operations, Database Management

A full library management system using classes and SQLite:
- Add books to the database
- List all books
- Search for a book by name
- Delete a book
- Update edition numbers

Demonstrates combining OOP with persistent database storage.
"""

import sqlite3


class Book:
    """Represents a book with its metadata."""

    def __init__(self, name: str, author: str, publisher: str, genre: str, edition: int):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.edition = edition

    def __str__(self) -> str:
        return (
            f"  📖 Kitap: {self.name}\n"
            f"  ✍️ Yazar: {self.author}\n"
            f"  🏢 Yayınevi: {self.publisher}\n"
            f"  📚 Tür: {self.genre}\n"
            f"  🔢 Baskı: {self.edition}"
        )


class Library:
    """Library management system backed by SQLite database."""

    def __init__(self, db_name: str = "library.db"):
        self.db_name = db_name
        self._connect()

    def _connect(self) -> None:
        """Create database connection and ensure table exists."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                name TEXT,
                author TEXT,
                publisher TEXT,
                genre TEXT,
                edition INTEGER
            )
        """)
        self.connection.commit()

    def close(self) -> None:
        """Close the database connection."""
        self.connection.close()

    def list_books(self) -> None:
        """Display all books in the library."""
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()

        if not books:
            print("📚 Kütüphanede kitap bulunmuyor...")
        else:
            print(f"\n📚 Kütüphanede {len(books)} kitap var:\n")
            for i, row in enumerate(books, start=1):
                book = Book(*row)
                print(f"{'─' * 35}")
                print(f"  #{i}")
                print(book)
            print(f"{'─' * 35}")

    def search_book(self, name: str) -> None:
        """Search for a book by name."""
        self.cursor.execute("SELECT * FROM books WHERE name = ?", (name,))
        results = self.cursor.fetchall()

        if not results:
            print(f"❌ '{name}' adında bir kitap bulunamadı.")
        else:
            book = Book(*results[0])
            print(f"\n✅ Kitap bulundu:\n{book}")

    def add_book(self, book: Book) -> None:
        """Add a book to the library."""
        self.cursor.execute(
            "INSERT INTO books VALUES (?, ?, ?, ?, ?)",
            (book.name, book.author, book.publisher, book.genre, book.edition),
        )
        self.connection.commit()
        print(f"✅ '{book.name}' kütüphaneye eklendi!")

    def delete_book(self, name: str) -> None:
        """Delete a book by name."""
        self.cursor.execute("DELETE FROM books WHERE name = ?", (name,))
        self.connection.commit()
        print(f"🗑️ '{name}' kütüphaneden silindi.")

    def increment_edition(self, name: str) -> None:
        """Increment the edition number of a book."""
        self.cursor.execute("SELECT * FROM books WHERE name = ?", (name,))
        results = self.cursor.fetchall()

        if not results:
            print(f"❌ '{name}' adında bir kitap bulunamadı.")
        else:
            new_edition = results[0][4] + 1
            self.cursor.execute(
                "UPDATE books SET edition = ? WHERE name = ?", (new_edition, name)
            )
            self.connection.commit()
            print(f"✅ '{name}' baskı numarası güncellendi: {new_edition}")


if __name__ == "__main__":
    library = Library()

    # Demo: Add some books
    library.add_book(Book("Python Crash Course", "Eric Matthes", "No Starch Press", "Programming", 3))
    library.add_book(Book("Clean Code", "Robert C. Martin", "Prentice Hall", "Software Engineering", 1))

    # List all books
    library.list_books()

    # Search for a book
    library.search_book("Clean Code")

    library.close()
