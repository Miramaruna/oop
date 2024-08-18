import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30) NOT NULL,
        age INT DEFAULT NULL,
        grade TEXT NOT NULL,
        enrollment_date DATE
    )
""")

cursor_2 = conn.cursor()

cursor_2.execute("""
    CREATE TABLE IF NOT EXISTS subject(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL,
        teacher_name TEST NOT NULL
    )         
""")

def register():
    full_name = input("Введите свое имя: ")
    age = int(input("Введите свой возраст: "))
    grade = input("Введите свой класс: ")
    enrollment_date = input("Введите свою дату рождения: ")

    cursor.execute(""" INSERT INTO student
                   (full_name, age, grade, enrollment_date)
                   VALUES (?, ?, ?, ?)""", (full_name, age, grade, enrollment_date))
    conn.commit()

# register()
    
def register_subject():
    subject_name = input("Введите название предмета: ")
    teacher_name = input("Введите имя преподователя этого предмета: ")

    cursor_2.execute(""" INSERT INTO subject 
                   (subject_name, teacher_name)
                   VALUES (?, ?)""", (subject_name, teacher_name))
    conn.commit()   

# register_subject()
         

def get_students():
    cursor.execute(""" SELECT * FROM student """)
    students = cursor.fetchall()
    print(students)

# get_students()

def get_subject():
    cursor_2.execute(""" SELECT * FROM subject """)
    subjects = cursor_2.fetchall()
    print(subjects)

# get_subject()

def get_strudents_by_grade(grade):
    cursor.execute(" SELECT * FROM student WHERE grade = ?", (grade,))
    students_2 = cursor.fetchall()
    for i in students_2:
        print(i)

# get_strudents_by_grade(7)

def update_student_age(student_id, new_age):
    cursor.execute("""CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT)""", )
    conn.commit()

# input_student_id = int(input("Введите ID студента для обновления возраста:: "))
# input_new_age = int(input("Введите новый возраст: "))

# update_student_age(input_student_id, input_new_age)

def delet_student(student_id):
    cursor.execute("DELETE FROM students WHERE id")

# delet_student() не понял

# cursor.close()
# cursor_2.close()
# conn.close()