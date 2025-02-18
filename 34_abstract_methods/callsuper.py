from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        print("Default drawing behavior in Shape")

class Circle(Shape):
    def draw(self):
        super().draw()  # Calls the default implementation
        print("Drawing a Circle")

class Square(Shape):
    def draw(self):
        super().draw()

circle = Circle()
circle.draw()
# Output:
# Default drawing behavior in Shape
# Drawing a Circle

square = Square()
square.draw()
# Output:
# Default drawing behavior in Shape

