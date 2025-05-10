#task(class):

class Rectangle:
    def __init__(self, height, breadth):
        self.height = height
        self.breadth = breadth

    def area(self):
        return self.height * self.breadth    
    


rec1 = Rectangle(10, 15)
print("area of rec1: ", rec1.area())