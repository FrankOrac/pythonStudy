# create a python  module to solve a quadratic equation
import cmath


def calc():




    a = (input("Enter the value of a"))
    b = (input("Enter the value of b"))
    c = (input("Enter the value of c"))
    if not a.isdigit() or b.isdigit() or c.isdigit():
        print("Please try again")
    a = (input("Enter the value of a"))
    b = (input("Enter the value of b"))
    c = (input("Enter the value of c"))



    fr = (b ** 2) - (4 * a * c)
    a1 = 2 * a
    x1 = ((cmath.sqrt(fr)) / (a1))
    x2 = ((cmath.sqrt(fr)) / (a1))
    b1 = (-b) - x1
    b2 = (-b) + x2
    if fr == 0:
        print("Invalid input")
    else:
        print("The first value is", b1)
        print("The second value is", b2)
