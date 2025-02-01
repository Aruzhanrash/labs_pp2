class Shape:
    def __init__(self):
        self.area = 0  

    def print_area(self):
        print(f"Shape area: {self.area}")

class Rectangle(Shape):
    def __init__(self):
        super().__init__()  
        self.length = float(input("Введите длину прямоугольника: "))  
        self.width = float(input("Введите ширину прямоугольника: "))  
        self.area = self.length * self.width  

    def print_area(self):
        print(f"Rectangle area: {self.area}")

myrectangle = Rectangle()
myrectangle.print_area()

myshape = Shape()
myshape.print_area()
