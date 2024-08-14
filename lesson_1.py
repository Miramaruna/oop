"""Обьектно ориентирование программирование """
# # def my_car():
# #     pass
# class Car:   #"Шаблоны или чертеж"
#     "Атрибут класса"
#     # marka = 'mercedes'
#     # model = 'cls'
#     # color = 'black'
#     def __init__(self, marka, model, color):  #  __int__ - Конструктор
#         "Атрибут обьекта"
#         self.marka = marka
#         self.model = model
#         self.color = color
#         self.bak = 10
#         self.is_start = False
#     def info(self):
#         print(f"Mарка машины-{self.marka},Модель-{self.model},Цвет-{self.color}")
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f"Mарка машины-{self.marka},Модель-{self.model},Машина заведена")
#         else:
#             print(f"Mарка машины-{self.marka},Модель-{self.model},Машина не заведена")
#     def drive(self, city):
#         if self.is_start == True:
#             print(f"Mарка машины-{self.marka},Модель-{self.model},едет в {city}")
# toyota = Car('Toyota','camry','white')
# toyota.info()
# toyota.start()
# toyota.drive("Караганду")
"""Пример"""
# class Book:
#     def __init__(self, avtor, book_name, year):
#         self.avtor = avtor
#         self.book_name = book_name
#         self.year = year

#     def info(self):
#         print(f"Автор-{self.avtor}, Название книги-{self.book_name}, Год создания-{self.year}")

# book = Book('kto-to', 'Day_d', 1943)


# book.info()

class Fruits:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def info(self):
        print(f"Название фрукта-{self.name}, Цвет фрукта-{self.color}, Вес фрукта-{self.weight}грамм")
        
fruit = Fruits('Яблоко','Красное',130)
fruit.info()

class Book:
    def __init__(self, title, author, pages):
        title = 'Day_D'
        author = 'Stiven E.Ambrosa'
        pages = 103
        self.title = title
        self.author = author
        self.pages = pages

    def chek_pages(self):
        if self.pages < 100:
            print('Книга тонка')
        elif self.pages < 300:
            print('Книга среднего размера')
        elif self.pages > 300:
            print('Книга толстая')
            
boke = Book('Day_D', 'Stiven E.Ambrosa', 103)
boke.chek_pages()