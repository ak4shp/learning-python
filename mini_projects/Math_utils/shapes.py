from math import pi


class Circle():
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * (self.__radius ** 2) 

    def perimeter(self):
        return 2 * pi * self.__radius


class Triangle():
    def __init__(self, base, side1, side2, height):
        self.__base = base
        self.__side1 = side1
        self.__side2 = side2
        self.__height = height

    def area(self):
        return 0.5 * self.__base * self.__height
    
    def perimeter(self):
        return self.__base + self.__side1 + self.__side2


class Rectangle():
    pass


class Cone():
    pass


class Cylinder():
    pass


class Sphere():
    pass


# c = Circle()
# c.area()

# s = Sphere()
# s.area()
