import math

class Shape:

    def get_perimeter(self):
        pass

    def get_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2
    
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        return self.a + self.b + self.c

    def get_area(self):
        poluPerimetr = get_perimeter(self) / 2
        return math.sqrt(poluPerimetr) * (poluPerimetr - self.a) * (poluPerimetr - self.b) * (poluPerimetr - self.c)
    

if __name__ == '__main__':
    