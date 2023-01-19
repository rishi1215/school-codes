#WAPP to count the frequency of elemets in the list using dictionary
l=[]
d={}
n=int(input("Enter the number of elements in the lsit:"))
for i in range(n):
    val=int(input("Enter the element:"))
    l.append(val)
for j in l:
    if  j in d:
        d[j]+=1
    else:
        d[j]=1
print(d)



    
