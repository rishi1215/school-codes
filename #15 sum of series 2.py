#WAPP to print sum 0f +1x/1!+x^2/2!+x^3/!.......+x^n/n!
x=int(input("enter the value of x:"))
n=int(input("Enter the value of n:"))
res=0
for i in range(n+1):
    num=i
    res=1
    while num>1:
        res*=num
        num=1
        res+=(x**n)/res
print("sum of  the series is : ",res)
