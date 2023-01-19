#WAPP to write fibonacci series upto 20 elements
n=int(input("Enter the  limit:"))
x=0
y=1
if n==0:
    print("series :",x)
elif n>=0:
    print(x)
    for i in range(n-1):
       z=x+y
       x=y
       y=z
       print(x)
 
