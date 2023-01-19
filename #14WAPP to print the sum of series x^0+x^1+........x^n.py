#WAPP to print the sum of series x^0+x^1+........x^n
n=int(input("enter the number (x):"))
n=int(input("enter the value of n:"))
sum=0
for i in range(n+1):
    sum=sum+x**i
    print("sum of series =",sum)
