"Инкапсуляция"

# class Phone:

#     def __init__(self, brand, model, memory):

#         self.brand = brand # публичный
#         self._model = model # Защищенный
#         self.__memory = memory # Приватный

#     def info(self):
#         print(f"Бренд телефона - {self.brand}\nМодель - {self._model}\nПамять - {self.__memory}")

#     def __private(self):
#         print('Private info')

# phone = Phone('Iphone', 'Pro', '1tb')

# phone.info()

# class Ximi:
    
#     def __init__(self, brand, model, proc, memory, battery, camera):
#         self.brand = brand
#         self.model = model
#         self.proc = proc
#         self.memory = memory
#         self.battery = battery
#         self.camera = camera

#     def info(self):
#         print(f"Брэнд и модель - {self.brand}{self.model}\nПроц - {self.proc}\nПамять - {self.memory}\nБатарея - {self.battery}\nКамера - {self.camera}")

# xami = Ximi('Xaomi', '14T', 'Snap8gen3', '1TB', '5000mah', '50mp')

# xami.info()

# class PublicExample:
#     def __init__(self, value):
#         self.value = value # Публичный атрибут
#     def info(self):
#         return self.value #Публичный метод
    
# public = PublicExample(1488)

# print(public.info()) #Вызов публичного метода

# print(public.value) #Доступ к публичному артибуту

# #Зашишенный
# class ProtectExample:
#     def __init__ (self, value):
#         self._value = value #Защищенный атрибут

#     def _info(self):
#         return self._value #Защищенный метод
    
# protector = ProtectExample(52)

# print(protector._info())

# # Приват

# class PrivateExample:
#     def __init__(self, value):
#         self.__value = value #приват артибут

#     def __info(self):
#         return self.__value
    
#     def acces_private(self):
#         return self.__info() #Публичный метод где мы получаем доступ к приватному атрибуту
     
# prvate = PrivateExample(51)

# # Прямой вызов приватного атрибута вызовет ошибку

# # Доступ через публичный метод

# print(prvate.acces_private())

# # Доступ к приватному атрибуту через name mangling
# print(prvate._PrivateExample__value)

# class Example(PrivateExample):
#     def __init__(self, value, current):
#         super().__init__(value)
#         self._current = current # Зашишенный атрибут

#     def public(self):
#         print(f"Приватный - {self.acces_private()}, Зашишенный артибут - {self._current}")

# exemple = Example(3, 4)
# print(exemple.public())

# import datetime

# class Car:
#     def __init__(self, make, model, year, mileage):
#         self.make = make
#         self.model = model
#         self._year = year
#         self.__mileage = mileage

#     def display_info(self):
#         print(f"марка - {self.make}\nМодель - {self.model}")

#     def _calculate_age(self):
#         current = datetime.datetime.now().year
#         return current - self._year
    
#     def __update_mileage(self):
#         print(self.__mileage)

#     def set_mileage(self):
#         return self.__update_mileage()
    
# car = Car('Mazda', 'RX8', '2008', 1488234)



class Pc:
    def __init__(self, memory, cpu, snak, num1, num2, otvet):
        self.memory = memory
        self.cpu = cpu
        self.num1 = num1
        self.num2 = num2
        self.snak = snak
        self.otvet = otvet

    def make_computations(self):
        if snak == '+':
            self.otvet = num1 + num2
            print(f"ответ - {self.otvet}")

        elif snak == '-':
            self.otvet = num1 - num2
            print(f"ответ - {self.otvet}")

        elif snak == '*':
            self.otvet = num1 * num2
            print(f"ответ - {self.otvet}")

        elif snak == '/':
            self.otvet = num1 / num2
            print(f"ответ - {self.otvet}")

    def info(self):
        print(f"Память - {self.memory}\nПроцессор - {self.cpu}")

# print("Введите число")
# num1 = int(input(": "))

# print("Введите второе число")
# num2 = int(input(": "))

# print("Введите знак")
# snak = input(": ")   

lil = Pc('1TB', 'intel i14800k', snak, num1, num2, 0)
# lil.make_computations()

class Laptop(Pc):
    def __init__(self, memory, cpu, snak, num1, num2, otvet, memory_card):
        Laptop.__init__(memory, cpu, snak, num1, num2, otvet, memory_card)
        self.__memory_card = memory_card
    
    def __get_memory_card(self):
        return self.__memory_card
    
    def set_memory_card(self):
        return self.__get_memory_card
    
    # def info(self):
    #     print(f"Карта памяти - ")
lol = Laptop('1TB', 'intel i14800k', snak, num1, num2, 0, '1000gb')

print(lol.set_memory_card())




