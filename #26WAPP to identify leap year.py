l=[]
n=int(input("Enter the  number of years to be checked"))
for i in range(n):
    t=int(input("enter the year"))
    l.append(t)
print(l)
for i in range(len(l)):
    if l[i]%4==0 and n%100!=0 or n%400==0:
        print("This is a leap year")
    else:
        print("This is not a leap year")
