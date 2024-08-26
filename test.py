class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.__age = age
    def info(self):
        print(f"Имя = {self.name}, Фамилия = {self._surname}, Возраст = ")

    def __get_age(self):
        return self.__age
    
    def set_age(self):
        return self.__get_age() 
     
    def bd(self):

        import sqlite3 

        connect = sqlite3.connect("geeks.db")
        cursor = connect.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS person(
        name VARCHAR(30) NOT NULL,
        surname VARCHAR(40) NOT NULL,
        age INTEGER NOT NULL
        )
        """)

        name = self.name
        surname = self._surname
        age = self.__age

        cursor.execute(""" INSERT INTO goko
                   (name, surname, age)
                   VALUES (?, ?, ?)""", (name, surname, age))
        connect.commit()
        
surn = Person('Mar', 'Mir', 13)

surn.info()
print(surn.set_age())        
  
# class Math:
#     def __init__(self, num2, num3):
#         self.num2 = num2
#         self.num3 = num3

#     def __add__(self):
#         print(self.num2 + self.num3)
    
#     def __sub__(self):
#         print(self.num3 - self.num2)
    
# sif = Math(1, 1)
# sif.__add__()
# sif.__sub__()
    
