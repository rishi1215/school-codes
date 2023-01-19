#WAPP to check whether the number is pallindrome or not
n=int(input("enter the number:"))
temp=n
sum=0
for i in range(len(str(n))):
    rem=temp%10
    sum=sum*10+rem
    temp=temp//10
if sum==n:
    print(n," is pallindrome")
else:
    print(n,"is not pallindrome")
