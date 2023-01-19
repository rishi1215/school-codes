#WAPP to swap elements from even to odd
l=[]
n=int(input("Enter  the max length of the list:"))
for i in range(n):
    val=int(input("Enter the element:"))
    l.append(val)
print("orginal list : ",l)
z=len(l)
if z!=0:
    z-=1
for i in range(0,z,2):
    l[i],l[i+1]=l[i+1],l[i]
print("Updated list: ",l)
