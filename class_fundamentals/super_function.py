class Rectangle:
    pass

class Square(Rectangle):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.length

square = Square(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())