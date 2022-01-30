import math


class Circle():
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * (self.__radius ** 2) 

    def perimeter(self):
        return 2 * math.pi * self.__radius
        
    def properties_menu(self):
        print("""(P)erimeter
(A)rea
(M)enu
""")
        option = input("->> ")
        return option


class Triangle():
    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def area(self):
        s = self.perimeter() / 2
        a = self.__side1
        b = self.__side2
        c = self.__side3
        _area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return _area
    
    def perimeter(self):
        return self.__side1 + self.__side2 + self.__side3
    
    def is_possible(self):
        largest = max(self.__side1, self.__side2, self.__side3, )
        others = self.__side1 + self.__side2 + self.__side3 - largest
        if largest < others:
            return True
        return False

    def properties_menu(self):
        print("""(P)erimeter
(A)rea
(M)enu
""")
        option = input("->> ")
        return option


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
