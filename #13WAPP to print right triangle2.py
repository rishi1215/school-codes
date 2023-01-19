#WAPP to print right triangle2
n=int(input("enter the numb er of rows:"))
for i in range(1,n+1):
    for k in range(n-i):
        print(end= "  ")
    for k in range(i):
         print("*",end=" ")
    print()
