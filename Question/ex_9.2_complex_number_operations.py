#  Create a class Complex with real and imaginary part as data member. Write member functions to read the complex number, Add  two complex numbers and display the complex number in python.

class Complex:
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def readComplex(self):
        self.real = float(input("Real part: "))
        self.imaginary = float(input("Imaginary part: "))

    def addComplex(self, other):
        result = Complex()
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result

    def displayComplex(self):
        print(f"{self.real} + {self.imaginary}i")


complex1 = Complex()
complex2 = Complex()

print("Complex Number 1")
complex1.readComplex()

print("Complex Number 2")
complex2.readComplex()

result = complex1.addComplex(complex2)

print("Sum of Complex Numbers is")
result.displayComplex()
