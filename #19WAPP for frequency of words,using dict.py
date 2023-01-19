#WAPP to print frequency of a word in a string ,using dictionary
st=input("Enter the string:").split()
d={}
for i in st:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
