#WAPP to print reverse of any given number
n=int(input("enter the number:"))
sum=0
for i in range(len(str(n))):
    rem=n%10
    sum=sum*10+rem
    n=n//10
print("reverse of the number is:",sum)
