class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        self.length = length
        super().__init__(length, length)


# class Cube(Square):
#     def __init__(self, length):
#         self.length = length
#         super().__init__(length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length
# In this example, you are setting Square as the subclass argument to super(), instead of Cube.
# This causes super() to start searching for a matching method (in this case, .area()) at one level above Square in the instance hierarchy, in this case Rectangle.


sq = Square(4)
print(sq.area())
print(sq.perimeter())

cube = Cube(3)
print(cube.area())
print(cube.perimeter())




# https://realpython.com/python-super/