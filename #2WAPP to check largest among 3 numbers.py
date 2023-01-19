#WAPP to enter 3 numbers and print the largest number
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number"))
if  a>=b and a>=c:
    print(a,"is largest")
elif b>=a and b>=c:
    print(b,"is largest")
elif c>=a and c>=b:
    print(c,"is largest")
