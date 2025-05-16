class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        return f"📘 '{self.title}' от {self.author}, {self.year} г."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("📚 Книги в библиотеке:")
        for book in self.books:
            print(book.display())

b1 = Book("Война и мир", "Толстой", 1869)
b2 = Book("1984", "Оруэлл", 1949)
b3 = Book("Маленький принц", "Экзюпери", 1943)

library = Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.show_books()
