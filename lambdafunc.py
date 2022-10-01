#Lambda function anonymous
#Addition of two numbers
#cube of a number
#number which are even or odd

frank = lambda a,b : a+b
print(frank(34,44))
f= lambda  x: x**3
print(f(4))
x= lambda  x:   "number is even" if x%2==0 else "number is odd"
print(x(81))
print(x(50))