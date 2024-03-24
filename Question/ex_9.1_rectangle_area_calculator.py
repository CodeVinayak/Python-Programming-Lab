# Write a program to print the area of a rectangle by creating a class named 'Area' having two functions. First function named as 'setDim' takes the length and breadth of the rectangle as parameters and the second function named as 'getArea' returns the area of the rectangle. Length and breadth of the rectangle are entered through keyboard. in python

class Area:
    def setDim(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth

length = float(input("Enter Length of Rectangle:"))
breadth = float(input("Enter Breadth of Rectangle: "))

rectangle = Area()
rectangle.setDim(length, breadth)

area = rectangle.getArea()
print("The area of the rectangle is:", area)