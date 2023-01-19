#WAPP to calculate and print the roots of  any equation in the form ax**2+bx+c(a should not be 0)
from math import sqrt
a=int(input("enter the coefficient of x**2:"))
b=int(input("enter the middle term:"))
c=int(input("enter the constant term:"))
D=b**2-4*a*c
if D<0:
    print("roots are imaginary")
elif D>=0:
    x= (-b+ sqrt(D))/(2*a)
    y=(-b- sqrt(D))/(2*a)
    print("roots of the equation are:",x,"and",y)
