#WAPP to multiply the even number by 2 in a list and dividean odd number by 2 in a list
l=[]
n=int(input("enter the length of the list: "))
for i in range(n):
    v=int(input("Enter the value: "))
    l.append(v)
print("Original list:  ",l)
for i in range(len(l)):
    if l[i]%2==0:
        l[i]*=2
    else:
        l[i]/=2
print("Updated list: ",l)
