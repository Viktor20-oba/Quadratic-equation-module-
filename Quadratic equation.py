# This is a module that solves quadratic equation
import math
a = float(input("what is a"))
b = float(input("what is b"))
c = float(input("what is c"))
f1 = math.sqrt (pow (b,2)-(4*a*c))
x1 = (-b-f1)/(2*a)
x2 = (-b+f1)/(2*a)
print(f"your answers are  x¹={x1} and x²={x2} ")