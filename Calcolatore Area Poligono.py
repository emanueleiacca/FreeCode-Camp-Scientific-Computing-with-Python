class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
#This is the constructor method for the Rectangle class
    def set_width(self, width):
        self.width = width
#set the width of a rettangle after it has been created
    def set_height(self, height):
        self.height = height
#set the height of a rettangle after it has been created

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
#this method calculate and return the area, perimeter and diagonal of a rectangle
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
#This method returns a string representation of the shape using lines of "*" for a max of 50 "*"
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())
#number of times a given shape can fit inside the current shape.
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
#string representation of a Rectangle object.

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"
#calls the constructor of the Rectangle class with the side length as both the width and height in the Square class

# Usage example
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
