#WAPP to check whether the number is armstrong or not
n=int(input("enter the number:"))
temp=n
sum=0
for i in range(len(str(n))):
    rem=temp%10
    sum=sum+rem**len(str(n))
    temp=temp//10
if sum==n:
    print(n," is armstrong")
else:
    print(n,"is not armstrong")
