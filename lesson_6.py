# "BD - База данных"
# "СУБД - Системв управления базы данных"
# "CRUD - Create, Reade, Update, Delete"

import sqlite3 

connect = sqlite3.connect("geeks.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTs geeks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30) NOT NULL,
        age INT DEFAULT NULL,
        direction TEXT,
        is_have BOOLEAN NOT NULL DEFAULT FALSE,
        rating DOUBLE(4, 2) DEFAULT (0.0),
        birth_date DATE
    )
""")

def register():
    full_name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    direction = input("Введите направление: ")
    is_have = bool(input("Наличие ноутбука: "))
    rating = float(input("Введите свой рейтинг: "))
    birth_date = (input("Введите свою дату рождения: "))

    # cursor.execute(f"""INSERT INTO geeks
    #                (full_name, age, direction, is_have, rating, birth_date)
    #                VALUES ('{full_name}', {age}, '{direction}', {is_have}, {rating}, '{birth_date}') """)
    
    # connect.commit()

    cursor.execute(""" INSERT INTO geeks
                   (full_name, age, direction, is_have, rating, birth_date)
                   VALUES (?, ?, ?, ?, ?, ?)""", (full_name, age, direction, is_have, rating, birth_date))
    connect.commit()

# register()

def all_students():
    cursor.execute(""" SELECT * FROM geeks """)
    students = cursor.fetchall()
    print(students)

# all_students()


