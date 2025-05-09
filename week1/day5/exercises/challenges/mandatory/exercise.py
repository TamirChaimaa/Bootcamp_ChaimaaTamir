import math

class Circle:
    def __init__(self, *, radius=None, diameter=None):
        # Initialize the circle using either the radius or the diameter.
        # If neither is provided, raise a ValueError.
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be specified.")

    @property
    def diameter(self):
        # Compute the diameter based on the radius.
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        # Allow setting the diameter, which updates the radius.
        self.radius = value / 2

    @property
    def area(self):
        # Calculate and return the area of the circle.
        return math.pi * self.radius ** 2

    def __str__(self):
        # Return a user-friendly string representation of the circle.
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __add__(self, other):
        # Define how two circles can be added by summing their radii.
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __lt__(self, other):
        # Define less-than comparison based on the radius.
        return self.radius < other.radius

    def __eq__(self, other):
        # Define equality comparison based on the radius.
        return isinstance(other, Circle) and self.radius == other.radius

    def __gt__(self, other):
        # Define greater-than comparison based on the radius.
        return self.radius > other.radius


# Example usage:
if __name__ == "__main__":
    c1 = Circle(radius=500)
    c2 = Circle(diameter=200)
    c3 = Circle(radius=100)

    print("C1:", c1)
    print("C2:", c2)
    print("C3:", c3)

    # Add two circles
    c4 = c1 + c2
    print("C1 + C2:", c4)

    # Compare circles
    print("C1 == C3:", c1 == c3)
    print("C1 > C2:", c1 > c2)

    # Sort the circles based on radius
    circles = [c1, c2, c3, c4]
    circles.sort()
    print("\nCircles sorted by radius:")
    for c in circles:
        print(c)

    # BONUS: Draw the sorted circles using Turtle (optional)
    try:
        import turtle

        turtle.speed(0)  # Fastest drawing speed
        turtle.bgcolor("white")

        for circle in circles:
            turtle.penup()
            turtle.goto(0, -circle.radius)  # Move to the appropriate position
            turtle.pendown()
            turtle.circle(circle.radius)    # Draw the circle

        turtle.done()
    except ImportError:
        print("Turtle module not installed or not available.")
