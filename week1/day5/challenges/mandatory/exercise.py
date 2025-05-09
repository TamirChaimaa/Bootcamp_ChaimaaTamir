import math
import turtle

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius:
            self.radius = radius
        else:
            self.radius = diameter / 2
    
    def area(self):
        a = round(math.pi * (self.radius ** 2), 3)
        return a

    def __str__(self):
        return f"The radius of the circle is {self.radius}, its diameter is {self.radius * 2}, and the area is {self.area()}"
    
    def __add__(self, other):
        return (self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius
    

list_circle = [Circle(2), Circle(4), Circle(3), Circle(5), Circle(6)]
list_sorted = sorted(list_circle)
for i in list_sorted:
    turtle.circle(i.radius * 10)

circle = Circle(2)
circle2 = Circle(3)
print(circle.area())
print(circle.__add__(circle2))
print(circle.__gt__(circle2))
print(circle.__eq__(circle2)) 
