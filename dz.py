class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        married_status = "да" if self.is_married else "нет"
        print(f"Полное имя: {self.fullname}")
        print(f"Возраст: {self.age}")
        print(f"Замужем/женат: {married_status}")


class Teacher(Person):
    salary = 0  

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus = (self.experience // 3) * 3000
        self.salary += bonus

    def introduce_myself(self):
        super().introduce_myself()
        print(f"Опыт работы: {self.experience} лет")
        print(f"Зарплата: {self.salary}")


teacher = Teacher("Ислам Ахмедов", 35, False, 9)
teacher.calculate_salary()
teacher.introduce_myself()
