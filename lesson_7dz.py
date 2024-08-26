import sqlite3
c = sqlite3.connect("xx.db") 
cur = c.cursor()

class BankAccount: 
    def __init__(self):
        self.balance = 0
    
    def deposit(self, popol):
        self.balance += popol
        

    def withdraw(self, minus):
        if self.balance >= minus: 
             self.balance -= minus
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.balance
    
account = BankAccount()

    
    

choice = input("Выберите действие (1-получение средств, 2-вывод средств): ").strip().lower()
print(f"Ваш выбор: {choice}")

if choice == "1":
    ckok = float(input("На какую сумму вы хотите пополнить свой баланс: "))
    account.deposit(ckok)

elif choice == "2":
    minus = float(input("Какую сумму вы хотите снять со счета: "))
    account.withdraw(minus)

else:
    print("Неизвестная ошибка")

print(f"Текущий баланс: {account.get_balance()}")


    

class Student:
    cur.execute("""CREATE TABLE IF NOT EXISTS students(      
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    age INTEGER,
    spisok_kurs TEXT
)
""")
    
def pip():
    full_name = input("Введите своё ФИО: ")
    age = int(input("Введите свой возраст: "))
    spisok_kurs = float(input("Введите свой курс: "))

    cur.execute("""INSERT INTO students
                      (full_name, age, spisok_kurs)
                      VALUES (?, ?, ?)""", (full_name, age, spisok_kurs))
c.commit()

pip()


class Course:
    def pik(self):
        kredins = int(input("Введите количество кредитов: "))
        school_class = input("Введите cвой класс: ")

        cur.execute("""INSERT INTO student
                      (kredins, school_class)
                      VALUES (?, ?)""", (kredins, school_class))
    c.commit()


    cur.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kredins INTEGER,
    school_class TEXT NOT NULL
)
""")
    
course = Course()
course.pik()

cur.execute("SELECT * FROM student")
students = cur.fetchall()

for student in students:
    print(f"ID: {student[0]}, school_class: {student[1]}, kredins: {student[2]}")

c.close()



class Database: 
    def __init__(self, db_name='library.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY,
                name TEXT,
                birth_year INTEGER
            )
            """)
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author_id INTEGER,
                publication_year INTEGER,
                FOREIGN KEY (author_id) REFERENCES authors(id)
            )
            """)

    def add_author(self, name, birth_year):
        with self.conn:
            self.conn.execute(
                'INSERT INTO authors (name, birth_year) VALUES (?, ?)',
                (name, birth_year)
            )

    def get_author(self, name):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, birth_year FROM authors WHERE name = ?", (name,))
        return cursor.fetchone()

    def add_book(self, title, author_id, publication_year):
        with self.conn:
            self.conn.execute(
                'INSERT INTO books (title, author_id, publication_year) VALUES (?, ?, ?)',
                (title, author_id, publication_year)
            )

    def remove_book(self, title):
        with self.conn:
            self.conn.execute('DELETE FROM books WHERE title = ?', (title,))

    def find_book_by_author(self, author_name):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT books.title, authors.name, books.publication_year
            FROM books
            JOIN authors ON books.author_id = authors.id
            WHERE authors.name = ?
        ''', (author_name,))
        return cursor.fetchall()
    


    def list_books(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT books.title, authors.name, books.publication_year
            FROM books
            JOIN authors ON books.author_id = authors.id
        ''')
        return cursor.fetchall()


class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return f"{self.name} (born {self.birth_year})"

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.publication_year})"

class Library:
    def __init__(self, db: Database):
        self.db = db

    def add_author(self, author):
        if not self.db.get_author(author.name):
            self.db.add_author(author.name, author.birth_year)

    def add_book(self, book):
        author = self.db.get_author(book.author.name)
        if author is None:
            self.add_author(book.author)
            author = self.db.get_author(book.author.name)

        self.db.add_book(book.title, author[0], book.publication_year)

    def remove_book(self, title):
        self.db.remove_book(title)

    def find_books_by_author(self, author_name):
        rows = self.db.find_books_by_author(author_name)
        return [Book(title=row[0], author=Author(name=row[1], birth_year=None), publication_year=row[2]) for row in rows]

    def list_books(self):
        rows = self.db.list_books()
        return [Book(title=row[0], author=Author(name=row[1], birth_year=None), publication_year=row[2]) for row in rows]


db = Database()

library = Library(db)

author1 = Author('Фёдор Достоевский', 1821)
author2 = Author('Антон Чехов', 1860)


book1 = Book('Толстый и худой', author2, 1883)
book2 = Book('Преступление и наказание', author1, 1866)
book3 = Book('Белые ночи', author1, 1848)


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print("Все книги:")
for book in library.list_books():
    print(book)

name_boo = 'Сюды назв книги'
books = library.remove_book(name_boo)

if books:
    print(f"\nНайдена книга: {books}")
else:
    print(f"\nКнига с названием '{name_boo}' не найдена.")


import math

class Shape:
    def cvad(number):
        return number ** 2

    result = cvad(5)
    print(result)  

class Circle(Shape):
    import math

def circle_area(radius):
    return math.pi * radius ** 2

result = circle_area(5)
print(result) 

class Rectangle(Shape):
    def triangle_area(base, height):
        return 0.5 * base * height


    result = triangle_area(10, 5)
    print(result)  


"""Создайте класс Car, который будет представлять автомобиль с маркой, моделью и годом выпуска.
Создайте класс Garage, который будет управлять коллекцией автомобилей.
Реализуйте методы для добавления автомобилей в гараж, удаления автомобиля по марке и модели, и вывода списка всех автомобилей в гараже.
Напишите код, который создаст несколько объектов Car, добавит их в гараж, удалит один автомобиль, и выведет оставшиеся автомобили.
"""

class Car:
    def vop(self):
        self.marka = input("Введите марку авто: ")
        self.model = input("Введиет модель авто: ")
        self.gods = input("Введите год выпуска: ")
    

class Garage(Car):

    def __init__(self, gg_name='car.db'):
        self.con = sqlite3.connect(gg_name)
        

    
        self.con.execute("""
                    CREATE TABLE IF NOT EXISTS carr(
                         id INTEGER PRIMARY KEY, 
                         marka TEXT, 
                         model TEXT, 
                         gods TEXT)""")
        
    def save_car(self):
        cur = self.con.cursor()
        cur.execute("INSERT INTO carr(marka, model, gods) VALUES (?, ?, ?)",
                    (self.marka, self.model, self.gods))
        self.con.commit()
        print(f"Автомобиль {self.marka} {self.model} {self.gods} сохранен в базе данных.")
        
garage = Garage()
garage.vop()       
garage.save_car()