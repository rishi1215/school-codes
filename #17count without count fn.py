#WAPP to input a list from a user  and count the occurance of an element in given list
L=[]
L1=int(input("enter the number of  elements :"))
for i in range(L1):
    n=int(input("enter the  elements"))
    L.append(n)
print(L)
y=int(input("the element to be checked in the list:"))
count=0
for x in L:
  if x==y:
    count+=1
print(count)
