class Person:

    def __init__(self, full_name, age, is_married):
        self.name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"имя - {self.name}, лет - {self.age}, женат - {self.is_married}")

class Teacher(Person):
    salary = 0

    def __init__(self, full_name, age, is_married, salary, years):
        Person.__init__(self, full_name, age, is_married)
        self.salary = salary
        self.years = years

    def salary_month(self):
        bonus = (self.years // 3) * 3000
        self.salary += bonus

    def info(self):
        print(f"имя - {self.name}, Возраст - {self.age}, женат - {self.is_married}, стаж - {self.years}")
        print(f'зарплата - {self.salary}')

# persona = Person("mira", 12, False)
# persona.introduce_myself()

teacher = Teacher('Islam', 'i dont know', False, 3000, 6)
teacher.salary_month()
teacher.info()

        


