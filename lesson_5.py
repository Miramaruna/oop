# Абстракция

# class Shape:
#     def area(self):
#         pass

#     def perimetr(self):
#         pass

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side 

#     def area(self):
#         return self.side * 2
    
#     def perimetr(self):
#         return 4 * self.side
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     def perimetr(self):
#         return 2 * 3.14 * self.radius
    
# square = Square(4)
# print(f'Площадь квадрата - {square.area()}')
# print(f'Периметр квадрата - {square.perimetr()}')

# circle = Circle(3)
# print(f'Площадь круга - {circle.area()}')
# print(f'Периметр круга - {circle.perimetr()}')

# class Vehicle:
#     def start_engine(self):
#         pass

#     def stop_engine(self):
#         pass

#     def drive(self):
#         pass

# class Car(Vehicle):
#     def start_engine(self):
#         return "Двигатель заведен"
    
#     def stop_engine(self):
#         return "Двигатель остановлен"
    
#     def drive(self):
#         return "Автомобиль едет"
    
# class Bicycle(Vehicle):
#     def start_engine(self):
#         return "У велосипеда нет двигателя"
    
#     def stop_engine(self):
#         return "У велосипеда нет двигателя"
     
#     def drive(self):
#         return "Велосипед едет"
    
# car = Car()

# print(car.start_engine())
# print(car.stop_engine())
# print(car.drive())

# bicycle = Bicycle()

# print(bicycle.start_engine())
# print(bicycle.stop_engine())
# print(bicycle.drive())


###################################


