class Shape:
    def __init__(self):
        self.area = 0  

    def set_a(self, a):
        self.area = a  

    def print_area(self):
        print(f"Shape area: {self.area}")


class Square(Shape):
    def __init__(self):
        super().__init__() 
        self.length = float(input("Введите длину стороны квадрата: "))  
        self.area = self.length ** 2 

    def print_area(self):
        print(f"Square area: {self.area}")
mysquare = Square()
mysquare.print_area()  
myshape = Shape()
myshape.print_area() 
