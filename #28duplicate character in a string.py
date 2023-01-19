#WAPP to find all the duplicate characters in a string
str=input("Enter the string: ")
l=[]
for i in str:
    z=str.find(i)
    x=str.find(i,z+1,len(str))
    if x>z and i not in l:
        l.append(i)
for i in l:
    print(i,"is duplicate")
