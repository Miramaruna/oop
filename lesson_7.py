from  database import Database

class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return f'Автор: {self.name}, дата рождения: {self.birth_year}'

author = Author("Пушкин", "1488")
print(author)

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f'Название книги: {self.title}, Автор: {self.author}, Год пулбикации: {self.publication_year}'

book = Book('Niger', 'skibidi dop', '1488')
print(book)

class library:
    def __init__(self, db: Database):
        self.db = db

    def add_author(self):
        if not self.db.get_author(author.name):
            self.db.add_authors(author.name, author.birth_year)

    def add_book(self, book):
        author = self.db.get_author(book.name)
        if author in None:
            self.add_author(book.author)
            author = self.db.get_author(book.author.name)

        self.db.add_book(book.title, author[0], book.publication.year)

    def remove_book(self, title):
        self.db.remove_book(title)

    def find_books_by_author(self, author_name):
        rows = self.db.find_book_by_author(author_name) 
        return [Book(title=row[0], author=Author(name=row[1], birth_year=None), publication_year=row[2]) for row in rows]
    
    # row = [('asd', 'pyshka', 1799), ()]