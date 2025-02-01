import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Точка: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

p1 = Point(float(input()), float(input()))
p2 = Point(float(input()), float(input()))

p1.show()
p2.show()

print(p1.dist(p2))

p1.move(float(input()), float(input()))

p1.show()
