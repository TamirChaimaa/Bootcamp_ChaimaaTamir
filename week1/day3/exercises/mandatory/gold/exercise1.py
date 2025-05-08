#Exercise 1 : Geometry
#Instructions
#Write a class called Circle that receives a radius as an argument (default is 1.0).
#Write two instance methods to compute perimeter and area.
#Write a method that prints the geometrical definition of a circle.
import math

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def definition(self):
        """Print the geometrical definition of a circle."""
        print("A circle is a two-dimensional shape consisting of all the points in a plane that are a given distance from a given point, the center.")


c = Circle(5)
print("Perimeter:", c.perimeter())
print("Area:", c.area())
c.definition()
c1= Circle()
print("Perimeter:", c1.perimeter())
print("Area:", c1.area())
c1.definition()


