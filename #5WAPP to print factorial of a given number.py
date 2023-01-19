#WAPP to print factorial of a given number
n=int(input("enter the number:"))
prod = 1
for i in range(1,n+1):
    n=n*i
    prod=n
print("factorial of the number is :",prod)
