#WAPP to search element in the list
l=[]
n=int(input("enter the max length "))
for i in range(n):
    z= int(input("enter the value:"))
    l.append(z)
print(l)   
z1=int(input("enter the value to search:"))
for i in range(len(l)):
    if z1==l[i]:
        
        print("position of the element is:",i+1)
        break
   
