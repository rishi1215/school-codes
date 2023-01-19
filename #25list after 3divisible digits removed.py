l=[]
n=int(input("Enter the mex length of the list: "))
for i in range(n):
    x=int(input("Enter the value: "))
    l.append(x)
print(l)
index=0
while index<len(l):
    if l[index]%3==0:
       l.pop(index)
       index-=1
    index+=1
print("Updated list: ",l)
