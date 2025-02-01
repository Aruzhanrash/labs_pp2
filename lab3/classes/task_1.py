class StringManipulator:
    def getString(self):
        self.input_string = input("Введите строку: ")

    def printString(self):
        print(self.input_string.upper())

string_manipulator = StringManipulator()
string_manipulator.getString()
string_manipulator.printString()
